"""Draft psychoactive-substances records from UK FCDO travel advice, for places with no Smartraveller page.

Reads the GOV.UK content API safety-and-security and health parts, splits them by subheading and sorts
sentences by substance with the same rules as smartraveller_substances.py. FCDO advice is official (UK
Government) but written for British travellers, so each record says so. Never overwrites an existing
psychoactive-substances record unless --force.

    python scripts/fcdo_substances.py ad bb lu
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fcdo_local_law import ALIASES, API, get, text  # noqa: E402
from lib import load_places, read, today, vetting_path, write  # noqa: E402
from smartraveller_substances import items_from  # noqa: E402


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
        if rec["patterns"].get("psychoactive-substances") and not args.force:
            print(f"{pid}: exists, skipped")
            continue
        page = get(f"{API}/{slug}")
        secs, used = [], []
        for part in page["details"]["parts"]:
            if part["slug"] not in ("safety-and-security", "health"):
                continue
            bits = re.split(r"<h[23][^>]*>(.*?)</h[23]>", part["body"])
            n = len(secs)
            secs += [(text(bits[i]), [text(bits[i + 1])]) for i in range(1, len(bits), 2)]
            if len(secs) > n:
                used.append(part["slug"])
        url = f"https://www.gov.uk/foreign-travel-advice/{slug}/safety-and-security"
        items = items_from(secs, url, D)
        for it in items:
            it["by"] = "fcdo_substances"
        if not items:
            print(f"{pid}: nothing found")
            continue
        updated = page.get("public_updated_at", "")[:10]
        rec["patterns"]["psychoactive-substances"] = {
            "status": "partly-mapped", "checked": D, "evidence": "official", "items": items,
            "notes": "From UK Government (FCDO) travel advice, written for British travellers; Smartraveller has no advice page for this place. Confirm with the place's own law.",
            "sources": [{"title": f"{page['title']} (updated {updated})", "authority": "Foreign, Commonwealth and Development Office, UK Government",
                         "url": url, "checked": D, "supports": "drugs, alcohol, vaping and health notes (" + ", ".join(used) + ") as read on " + D}]}
        write(path, rec)
        print(f"{pid}: {len(items)} items")


if __name__ == "__main__":
    main()
