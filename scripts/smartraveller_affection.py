"""Draft affection-and-relationships records from Smartraveller destination pages.

Reads the full advice (safety, local laws, local customs and LGBTQIA+ sections) sentence by sentence and sorts what it
finds into four areas: in public, in private, marriage and partnership, and changing. Each item
says whether it is law or custom. A first draft for a place pass: check every item against the page.

    python scripts/smartraveller_affection.py --dir PAGES fj id ws     # read <key>.html already fetched
    python scripts/smartraveller_affection.py --all --dir PAGES        # every place with a Smartraveller page
    python scripts/smartraveller_affection.py --all --dir PAGES

Writes affection-and-relationships into data/vetting/<id>.json, dated today, evidence "official"
(Australian Government advice), unless that pattern was already checked today.
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from consular import fetch, page_text  # noqa: E402
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402
from smartraveller_draft import clean, sections  # noqa: E402

NOT_HEADS = re.compile(r"assault|crime|scam|fraud|kidnap|terror|health|medic|drink|dating|social media|insurance|hiv|disease|emergenc|contacts?$", re.I)
AREAS = [
    ("changing", re.compile(r"decriminali[sz]|legali[sz]ed|recogni[sz]ed .*since|since (19|20)\d\d|in (19|20)\d\d|new law|recently (passed|introduced|changed)", re.I)),
    ("in-public", re.compile(r"affection|kiss|holding hands|hold hands|intimate|embrac|hugging", re.I)),
    ("in-private", re.compile(r"unmarried|cohabit|live together|living together|share a (hotel )?room|sex outside|extramarital|adultery|"
                              r"sexual (relations|activity|acts)|same-sex (relationships|relations|acts|sexual|activity)|homosexual|consensual", re.I)),
    ("marriage-and-partnership", re.compile(r"marri|surrogacy|civil union|civil partnership|de facto|spouse|wedding|polygam|dowry", re.I)),
]
ABOUT = re.compile(r"same-sex|lgbt|homosexual|marri|relationship|partner|affection|cohabit|sexual|sex outside|adultery|civil union", re.I)
LAW = re.compile(r"authorities|illegal|\blegal|\blaws?\b|arrest|penalt|prison|jail|\bfines?\b|criminal|prosecut|death penalty|corporal|offence|banned|"
                 r"prohibit|recogni[sz]|decriminali[sz]|legali[sz]", re.I)
SKIP = re.compile(r"legal advice|reputable organisation|research prospective|be aware of all legal and other risks|smartraveller|"
                  r"consular|Australian Government|more information|advice for LGBTQIA|see source|contact the|^See ", re.I)


def items_from(secs, url, on):
    found, seen = [], set()
    for title, body in secs:
        if NOT_HEADS.search(title):
            continue
        text = clean(body)
        for sentence in re.split(r"(?<=[.!?])\s+(?=[A-Z])|(?<=[a-z])\s+(?=(?:The|Same-sex|Public|If|Avoid|You|Homosexual|Unmarried) )", text):
            s = sentence.strip()
            s = re.sub(r"\s{2,}", " ", s)
            if len(s) < 25 or SKIP.search(s) or s in seen:
                continue
            area = next((a for a, rx in AREAS if rx.search(s) and (a != "changing" or ABOUT.search(s))), None)
            if not area:
                continue
            if area == "in-public" and not re.search(r"affection|kiss|hand|intimate|embrac|hug", s, re.I):
                continue
            seen.add(s)
            found.append({"area": area, "kind": "law" if LAW.search(s) else "custom", "text": s[:320], "source": url, "checked": on})
    per = {}
    keep = []
    for it in found:
        per[it["area"]] = per.get(it["area"], 0) + 1
        if per[it["area"]] <= 4:
            keep.append(it)
    return keep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("places", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--skip-region", action="append", default=[])
    ap.add_argument("--dir")
    ap.add_argument("--force", action="store_true", help="redraft records already checked today")
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    adv = read(ROOT / "data/advisories.json", {"destinations": {}})["destinations"]
    todo = args.places or [pid for pid, p in places.items() if args.all and p.get("smartraveller") and p.get("region") not in args.skip_region]
    counts = {"written": 0, "nothing": 0}
    for pid in todo:
        key = places[pid].get("smartraveller")
        dest = adv.get(key)
        if not dest:
            continue
        page = pathlib.Path(args.dir) / f"{key}.html" if args.dir else None
        raw = page.read_text(encoding="utf-8", errors="replace") if page and page.exists() else fetch(dest["url"])
        if not raw:
            print(f"{pid}: fetch failed, nothing written")
            continue
        lines = page_text(raw)
        secs = sections(lines)
        full = next((i for i, (t, _) in enumerate(secs) if t == "Full advice"), 0)
        stop = next((i for i in range(full + 1, len(secs)) if secs[i][0] in ("Travel", "Local contacts")), len(secs))
        scope = secs[full + 1:stop]
        items = items_from(scope, dest["url"], D)
        updated = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("Updated:")), "")
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        if not items:
            counts["nothing"] += 1
            continue
        if not args.force and rec["patterns"].get("affection-and-relationships", {}).get("checked") == D:
            continue
        old = rec["patterns"].get("affection-and-relationships", {})
        kept = [i for i in old.get("items", []) if i.get("by")]
        kept_sources = [s for s in old.get("sources", []) if s["url"] != dest["url"] and any(i.get("source") == s["url"] for i in kept)]
        rec["patterns"]["affection-and-relationships"] = {
            "status": "partly-mapped", "checked": D, "evidence": "official", "items": items + kept,
            "notes": "Read from the Australian Government's travel advice. Custom differs between communities and places; ask locally.",
            "sources": [{"title": f"{dest['title']} travel advice (updated {updated})", "authority": "Smartraveller, Australian Government",
                         "url": dest["url"], "checked": D, "supports": "local laws, local customs and LGBTQIA+ sections as read on " + D}] + kept_sources}
        write(path, rec)
        counts["written"] += 1
        print(f"{pid}: {len(items)} items ({', '.join(sorted({i['area'] for i in items}))})")
    print(counts)


if __name__ == "__main__":
    main()
