"""Find a photograph OF each place for its page hero, from Wikidata's main image (P18).

Rule: a place page shows a photo of that place, or of somewhere inside it (labelled as such),
or no photo. Never a stand-in from somewhere else.

Covers ISO countries and territories (P297), Australian and US states (P300), and any place in the
tree that carries a "wikidata" id.

Places that belong to a nation or community with its own cultural authority (tagged first-nations
and of kind nation, zone, site or island-group) get no automatic photo: how they are pictured is chosen
with their community. Keeps only
openly licensed, landscape-shaped photographs, with full credit from Wikimedia Commons.
Curated photos in site/heroes/place-photos-curated.json always win. Every automatic pick is
marked "review": "pending" until Luke has looked at it.
Writes site/data/place-photos.json. Images are linked from Wikimedia, not stored here.
"""
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, write  # noqa: E402

UA = {"User-Agent": "world-travel-patterns/1.0 (https://github.com/auraofintelligence; place photos)"}
SPARQL = "https://query.wikidata.org/sparql"
COMMONS = "https://commons.wikimedia.org/w/api.php"
OPEN = re.compile(r"^(public domain.*|pd.*|cc0.*|cc[ -]by(-sa)? \d(\.\d)?.*|attribution.*)$", re.I)
FROM_ORBIT = re.compile(r"\bISS\d|\bSTS-?\d|satellite|sentinel-?2|modis|landsat|copernicus|cloud-free|view of .* from space|bushfires", re.I)
NOT_A_PLACE_PHOTO = re.compile(r"flag|map|coat of arms|arms of|emblem|locator|seal of|logo|dannebrog|banner of|location", re.I)
QUERY = """
SELECT ?code ?label ?img ?banner WHERE {
  { ?p wdt:P297 ?code . } UNION { ?p wdt:P300 ?code . FILTER(STRSTARTS(?code, "AU-") || STRSTARTS(?code, "US-")) }
  OPTIONAL { ?p wdt:P18 ?img . }
  OPTIONAL { ?p wdt:P948 ?banner . }
  FILTER(BOUND(?img) || BOUND(?banner))
  ?p rdfs:label ?label . FILTER(LANG(?label) = "en")
}"""


def get(url, params=None):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={**UA, "Accept": "application/json"}), timeout=90) as r:
                return json.load(r)
        except OSError:
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


def clean(html_text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html_text or "")).strip()


def main():
    places = load_places()
    by_iso = {p["iso2"]: pid for pid, p in places.items() if p.get("iso2")}
    au_states = {"AU-" + pid.split("/")[1].upper(): pid for pid, p in places.items() if p["kind"] == "state" and pid.startswith("au/")}
    us_states = {re.sub(r"[^a-z]", "", p["name"].lower()): pid for pid, p in places.items() if p["kind"] == "state" and pid.startswith("us/")}

    rows = get(SPARQL, {"query": QUERY, "format": "json"})["results"]["bindings"]
    by_qid = {p["wikidata"]: pid for pid, p in places.items() if p.get("wikidata")}
    if by_qid:
        values = " ".join("wd:" + q for q in by_qid)
        extra = get(SPARQL, {"format": "json", "query": f"""SELECT ?item ?img ?banner WHERE {{ VALUES ?item {{ {values} }}
            OPTIONAL {{ ?item wdt:P18 ?img . }} OPTIONAL {{ ?item wdt:P948 ?banner . }} }}"""})["results"]["bindings"]
        for row in extra:
            row["code"] = {"value": "QID:" + row["item"]["value"].rsplit("/", 1)[1]}
            row["label"] = {"value": ""}
        rows += [r for r in extra if "img" in r or "banner" in r]
    candidates = {}
    for row in rows:
        code, label = row["code"]["value"], row["label"]["value"]
        if code.startswith("QID:"):
            pid = by_qid.get(code[4:])
        elif code.startswith("AU-"):
            pid = au_states.get(code)
        elif code.startswith("US-"):
            pid = us_states.get(re.sub(r"[^a-z]", "", label.lower()))
        else:
            pid = by_iso.get(code)
        if not pid:
            continue
        for key, kind in (("img", "photo"), ("banner", "banner")):
            if key in row:
                name = urllib.parse.unquote(row[key]["value"].rsplit("/", 1)[1]).replace("_", " ")
                if (name, kind) not in candidates.setdefault(pid, []):
                    candidates[pid].append((name, kind))

    titles = sorted({t for names in candidates.values() for t, _ in names})
    info = {}
    for i in range(0, len(titles), 40):
        batch = titles[i:i + 40]
        data = get(COMMONS, {"action": "query", "titles": "|".join("File:" + t for t in batch), "prop": "imageinfo",
                             "iiprop": "url|size|extmetadata|mime", "iiurlwidth": 1920, "format": "json"})
        normal = {n["to"]: n["from"] for n in data["query"].get("normalized", [])}
        for page in data["query"]["pages"].values():
            if "imageinfo" not in page:
                continue
            ii = page["imageinfo"][0]
            meta = ii.get("extmetadata", {})
            title = normal.get(page["title"], page["title"])[5:]
            info[title] = {
                # Wikimedia serves standard thumbnail widths only; 1920 suits a hero. Drop tracking parameters.
                "url": (ii.get("thumburl") or ii["url"]).split("?")[0], "width": ii["width"], "height": ii["height"], "mime": ii.get("mime"),
                "licence": clean(meta.get("LicenseShortName", {}).get("value")), "licence_url": clean(meta.get("LicenseUrl", {}).get("value")),
                "artist": clean(meta.get("Artist", {}).get("value"))[:120], "source": ii["descriptionurl"],
                "description": clean(meta.get("ImageDescription", {}).get("value")).replace(chr(0x2014), ", ").replace(chr(0x2013), "-")[:160],
            }
        time.sleep(1)

    choices = read(ROOT / "site/heroes/place-photo-choices.json", {"choices": {}})["choices"]
    photos, skipped = {}, []
    for pid, names in sorted(candidates.items()):
        pick = None
        use = choices.get(pid, {}).get("use")
        place = places[pid]
        if "first-nations" in place.get("tags", []) and place["kind"] in ("nation", "zone", "site", "island-group"):
            skipped.append(pid)
            continue
        if use == "none":
            skipped.append(pid)
            continue
        # Ground photo first (a full hero), then the Wikivoyage banner (a wide band), then a view from orbit.
        def rank(n):
            name, kind = n
            if use == "banner":
                return 0 if kind == "banner" else 2
            if use == "main":
                return 0 if kind == "photo" else 2
            return 0 if kind == "photo" and not FROM_ORBIT.search(name) else 1 if kind == "banner" else 2
        allowed = {"banner": {"banner"}, "main": {"photo"}}.get(use, {"photo", "banner"})
        for name, kind in sorted((n for n in names if n[1] in allowed), key=rank):
            meta = info.get(name)
            if not meta or meta["mime"] not in ("image/jpeg", "image/png", "image/webp") or NOT_A_PLACE_PHOTO.search(name):
                continue
            ratio = meta["width"] / meta["height"]
            # No drone imagery on this site (Luke, 1 November 2026).
            if re.search(r"drone|\bUAV\b|quadcopter", " ".join((name, meta["description"], meta["artist"])), re.I):
                continue
            if not OPEN.match(meta["licence"]) or meta["width"] < 1600:
                continue
            if (kind == "photo" and ratio < 1.25) or (kind == "banner" and ratio < 3):
                continue
            pick = (name, meta, kind)
            break
        if not pick:
            skipped.append(pid)
            continue
        name, meta, kind = pick
        photos[pid] = {"src": meta["url"], "shape": "banner" if kind == "banner" else "hero", "alt": f"{places[pid]['name']}: {meta['description'] or name.rsplit('.', 1)[0]}",
                       "title": name, "artist": meta["artist"] or "Unknown", "licence": meta["licence"],
                       "licence_url": meta["licence_url"], "source": meta["source"], "via": "Wikivoyage page banner" if kind == "banner" else "Wikidata main image",
                       "review": "pending"}

    curated = read(ROOT / "site/heroes/place-photos-curated.json", {"photos": {}})["photos"]
    photos.update(curated)
    # Review verdicts (approved / rejected) recorded in place-photo-choices.json apply only to the exact file judged.
    for pid, ph in photos.items():
        c = choices.get(pid, {})
        if c.get("review") == "approved" and c.get("title") == ph["title"]:
            ph["review"] = "approved"
            ph["review_note"] = c.get("why", "")
    write(ROOT / "site/data/place-photos.json", {
        "built_on": today().isoformat(),
        "rule": "A photo of the place, or of somewhere inside it (labelled), or none. Never a stand-in from elsewhere.",
        "photos": photos,
        "no_suitable_photo": sorted(set(skipped) - set(photos)),
    })
    print(f"{len(photos)} places with a photo ({len(curated)} curated), {len(skipped)} with no suitable open landscape photo")


if __name__ == "__main__":
    main()
