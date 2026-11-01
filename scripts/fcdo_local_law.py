"""Draft local-law records from UK FCDO foreign travel advice, for places with no Smartraveller page.

Reads the GOV.UK content API (https://www.gov.uk/api/content/foreign-travel-advice/<slug>), takes the
"Laws and cultural differences" section of the Safety and security part, and writes one law per
subheading. FCDO advice is written for British travellers; it is official (UK Government) but not
Australian, so each record says so. Never overwrites an existing local-law record unless --force.

    python scripts/fcdo_local_law.py ai bm ky       # place ids
"""
import argparse
import html
import json
import pathlib
import re
import sys
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import load_places, read, today, vetting_path, write  # noqa: E402
from smartraveller_draft import CONTACTS, topic_for, trim  # noqa: E402

API = "https://www.gov.uk/api/content/foreign-travel-advice"
ALIASES = {"United States": "USA", "Vatican City": "Vatican City", "Cabo Verde": "Cape Verde", "Congo - Brazzaville": "Congo",
           "Republic of the Congo": "Congo", "São Tomé & Príncipe": "Sao Tome & Príncipe", "São Tomé and Príncipe": "Sao Tome & Príncipe", "Sao Tome and Principe": "Sao Tome & Príncipe",
           "St Kitts and Nevis": "St Kitts and Nevis", "Saint Kitts and Nevis": "St Kitts and Nevis", "Saint Lucia": "St Lucia",
           "Saint Vincent and the Grenadines": "St Vincent and the Grenadines", "British Virgin Islands": "British Virgin Islands",
           "Turks and Caicos Islands": "Turks and Caicos Islands", "Falkland Islands": "Falkland Islands", "Saint Helena": "St Helena, Ascension and Tristan da Cunha",
           "Saint Helena, Ascension and Tristan da Cunha": "St Helena, Ascension and Tristan da Cunha"}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "world-travel-patterns (dataset)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def text(fragment):
    t = re.sub(r"</(p|li|h\d)>", "\n", fragment)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = " ".join(re.sub(r"\s+", " ", l).strip() for l in t.split("\n") if l.strip())
    return CONTACTS.sub("[see source]", t).strip()


def laws_from(body):
    m = re.search(r"<h2[^>]*>\s*Laws and cultural differences\s*</h2>", body)
    if not m:
        return []
    rest = body[m.end():]
    end = re.search(r"<h2", rest)
    seg = rest[:end.start()] if end else rest
    parts = re.split(r"<h3[^>]*>(.*?)</h3>", seg)
    out = []
    for i in range(1, len(parts), 2):
        title, body_txt = text(parts[i]), text(parts[i + 1])
        if body_txt:
            out.append((title, body_txt))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("places", nargs="+")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    index = {re.sub(r" \(.*?\)| travel advice$", "", c["title"]): c["base_path"].split("/")[-1] for c in get(API)["links"]["children"]}
    for pid in args.places:
        name = places[pid]["name"]
        slug = index.get(ALIASES.get(name, name)) or next((s for t, s in index.items() if t.lower() == name.lower()), None)
        if not slug:
            print(f"{pid}: no FCDO page for {name}")
            continue
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        if rec["patterns"].get("local-law") and not args.force:
            print(f"{pid}: local-law exists, skipped")
            continue
        page = get(f"{API}/{slug}")
        body = next((p["body"] for p in page["details"]["parts"] if p["slug"] == "safety-and-security"), "")
        found = laws_from(body)
        if not found:
            print(f"{pid}: no laws section")
            continue
        url = f"https://www.gov.uk/foreign-travel-advice/{slug}/safety-and-security"
        laws = [{"topic": topic_for(t, b), "rule": trim(b, 700), "level": "country", "source": url, "checked": D, "heading": t} for t, b in found]
        updated = page.get("public_updated_at", "")[:10]
        rec["patterns"]["local-law"] = {
            "status": "partly-mapped", "checked": D, "evidence": "official", "laws": laws,
            "note": "From UK Government (FCDO) travel advice, written for British travellers; Smartraveller has no advice page for this place. Confirm with the place's own authorities.",
            "sources": [{"title": f"{page['title']} (updated {updated})", "authority": "Foreign, Commonwealth and Development Office, UK Government",
                         "url": url, "checked": D, "supports": "laws and cultural differences as read on " + D}]}
        write(path, rec)
        print(f"{pid}: local-law ({len(laws)})")


if __name__ == "__main__":
    main()
