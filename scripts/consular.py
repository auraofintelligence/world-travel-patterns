"""Consular reach for every Smartraveller destination, read from each page's "Consular contacts" section.

Writes the consular record into data/vetting/<id>.json for each spine place (status in-place,
neighbour or partner-arrangement), and data/missions/australian-abroad.json listing the Australian
offices each page names. Institutional offices only: names, cities and websites, no phone numbers or emails.
A page that can't be fetched or parsed keeps its old record and date: a failed fetch is not a change.

    python scripts/consular.py              # fetch each page with curl (Smartraveller refuses urllib)
    python scripts/consular.py --dir PAGES  # read <key>.html files already fetched
"""
import argparse
import html
import json
import pathlib
import re
import subprocess
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
OFFICE = re.compile(r"^((?:The )?Australian (?:Embassy|High Commission|Consulate(?:-General)?|Office|Representative Office|Mission)[^\n]*|Embassy of Australia[^\n]*|Canadian [^\n]*|Embassy of Canada[^\n]*)$")
CONTACT = re.compile(r"^(Phone|Tel|Telephone|Fax|Email|E-mail|Facebook|X|Twitter|Instagram|LinkedIn|YouTube)\s*:", re.I)


def page_text(raw):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|<footer.*?</footer>", "", raw, flags=re.S)
    t = re.sub(r"<(h[1-4])[^>]*>", "\n## ", t)
    t = re.sub(r"<li[^>]*>", "\n- ", t)
    t = re.sub(r"<(p|br|div)[^>]*>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    return [re.sub(r"\s+", " ", line).strip() for line in t.split("\n") if line.strip()]


POSTS = read(ROOT / "data/missions/post-cities.json", {"cities": {}})["cities"]
PLACE_NAMES = {}  # filled in main(); a post named for its own place (Hong Kong, Macau) is in it


def parse(lines, others=(), pid=None):
    heads = [i for i, l in enumerate(lines) if l in ("## Consular contacts", "## Consular services", "## Consular help", "## Consular assistance")]
    if not heads:
        return None
    start = heads[-1]
    section = []
    for line in lines[start + 1:]:
        if line.startswith("## 24-hour") or line.startswith("## Travelling to") or line.startswith("## Sign up"):
            break
        section.append(line)
    lead = []
    for l in section:
        if l.startswith("## "):
            break
        lead.append(l)
    # Sentences only: no addresses, phone numbers or emails in a public record.
    intro = " ".join(l for l in lead if "Consular Services Charter" not in l and not CONTACT.match(l) and "@" not in l
                     and not re.search(r"\+?\d[\d ()-]{6,}", l) and len(l.split()) > 4)
    offices, current = [], None
    for line in section:
        head = line[3:].strip() if line.startswith("## ") else None
        if head and OFFICE.match(head):
            current = {"name": head, "lines": []}
            offices.append(current)
        elif head:
            current = None
        elif current is not None:
            current["lines"].append(line)
    out = []
    for o in offices:
        name = o["name"]
        city = name.split(",", 1)[1].strip() if "," in name else None
        website = next((re.sub(r"^(Website|Web)\s*:\s*", "", l, flags=re.I) for l in o["lines"] if re.match(r"^(Website|Web)\s*:", l, re.I)), None)
        out.append({"name": name, "city": city, "website": website.strip() if website else None,
                    # An office heading that names another country is based there.
                    "elsewhere": any(name.rsplit(",", 1)[-1].strip() == other or re.search(rf"(?:Embassy|Commission|Consulate)(?: in)? {re.escape(other)}$", name)
                                     for other in others) or bool(city and pid and city != PLACE_NAMES.get(pid) and POSTS.get(city.split(",")[0].strip(), {}).get("place", pid) != pid),
                    "canadian": name.startswith("Canadian") or "Canada" in name})
    return {"intro": intro, "offices": out}


def fetch(url):
    for attempt in range(3):
        r = subprocess.run(["curl", "-sL", "-m", "60", "-A", UA, url], capture_output=True)
        if r.returncode == 0 and len(r.stdout) > 50000:
            return r.stdout.decode("utf-8", errors="replace")
        time.sleep(3 * (attempt + 1))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir")
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    adv = read(ROOT / "data/advisories.json", {"destinations": {}})["destinations"]
    by_key = {p["smartraveller"]: pid for pid, p in places.items() if p.get("smartraveller")}
    abroad = read(ROOT / "data/missions/australian-abroad.json", {"places": {}})
    listed = abroad.get("places", {})
    done, failed, unparsed = 0, [], []
    # Country names an office heading might carry ("Australian Embassy, Warsaw, Poland"). Not "Australia": every heading says Australian.
    PLACE_NAMES.update({i: p["name"] for i, p in places.items()})
    names = {p["name"] for i, p in places.items() if "/" not in i and len(p["name"]) > 3 and i != "au"} | {"Russia", "Türkiye", "Turkiye", "Ukraine"}
    for key, dest in sorted(adv.items()):
        pid = by_key.get(key)
        if not pid:
            continue
        if args.dir:
            f = pathlib.Path(args.dir) / f"{key}.html"
            raw = f.read_text(encoding="utf-8", errors="replace") if f.exists() and f.stat().st_size > 50000 else None
        else:
            raw = fetch(dest["url"])
            time.sleep(1)
        if not raw:
            failed.append(pid)
            continue
        found = parse(page_text(raw), names - {places[pid]["name"]}, pid)
        if not found or (not found["offices"] and not found["intro"]):
            unparsed.append(pid)
            continue
        offices = found["offices"]
        intro = found["intro"]
        if not offices:
            m = re.search(r"contact the (Australian (?:Embassy|High Commission|Consulate(?:-General)?|Office)) in ([A-Z][\w'-]+(?: [A-Z][\w'-]+)*)", intro)
            if m:
                offices = [{"name": f"{m.group(1)}, {m.group(2)}", "city": m.group(2), "website": None, "canadian": False, "elsewhere": False}]
        if "Canad" in intro or any(o["canadian"] for o in offices):
            status = "partner-arrangement"
        elif re.search(r"(?:doesn.t|does not|don.t) have an? (?:embassy|high commission|consulate|diplomatic)|(?:embassy|consulate)[^.]* is closed|based in", intro, re.I):
            status = "neighbour"
        elif any(not o["elsewhere"] and re.search(r"Embassy|High Commission|Consulate-General|Consulate General|Office|Representative", o["name"]) for o in offices):
            status = "in-place"
        elif offices:
            # Only an honorary consulate here (limited help); full help comes from a post next door.
            status = "neighbour"
        else:
            status = "unknown"
        first = offices[0] if offices else None
        source = {"title": f"{dest['title']} travel advice: consular contacts", "authority": "Smartraveller, Australian Government",
                  "url": dest["url"], "checked": D, "supports": "the Australian offices that give consular help"}
        record = {"status": status, "mission": "; ".join(o["name"] for o in offices) or None,
                  "city": first["city"] if first else None,
                  "covers_from": pid if status == "in-place" else next(
                      (POSTS[o["city"]]["place"] for o in offices if not o["canadian"] and o["city"] in POSTS and POSTS[o["city"]]["place"] != pid), None),
                  "notes": intro[:400] or None, "checked": D, "evidence": "official", "sources": [source]}
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        rec["patterns"]["consular"] = record
        write(path, rec)
        listed[pid] = [{k: o[k] for k in ("name", "city", "website")} | {"source": dest["url"], "checked": D} for o in offices]
        done += 1
    write(ROOT / "data/missions/australian-abroad.json", {
        "what": "Australian embassies, high commissions and consulates that Smartraveller names for each destination's consular help.",
        "source": "Smartraveller destination pages, Consular contacts section", "authority": "Australian Government",
        "rule": "Institutional offices only. Names, cities and websites; no phone numbers or emails.",
        "places": dict(sorted(listed.items())),
    })
    print(f"consular: {done} places written, {len(failed)} fetch failures {failed[:20]}, {len(unparsed)} unparsed {unparsed[:20]}")


if __name__ == "__main__":
    main()
