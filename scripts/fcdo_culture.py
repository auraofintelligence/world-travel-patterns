"""Draft culture-and-protocol records from UK FCDO foreign travel advice ("Laws and cultural differences").

Only subheadings about customs (dress, religion, Ramadan, cultural sensitivities, behaviour) are used; laws
stay in local-law. FCDO advice is written for British travellers; each record says so. Places with no
customs subheading get status ask-locally with the named authority. Never overwrites an existing
culture-and-protocol record. Stdlib only.

    python scripts/fcdo_culture.py [--dry] ai bm ky
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fcdo_local_law import ALIASES, API, get, laws_from  # noqa: E402
from lib import load_places, read, today, vetting_path, write  # noqa: E402
from smartraveller_draft import trim  # noqa: E402

DRESS = re.compile(r"dress|cloth|swimwear|topless|beachwear|nudi|behaviour|decency|custom|cultur|etiquette|respect|tradition", re.I)
SKIP = re.compile(r"camouflage|military|trading|drug|LGBT|personal id|money|alcohol", re.I)
SACRED = re.compile(r"relig|sacred|church|mosque|temple|ramadan|holy|worship|shrine|chief|village|kava|sunday|sabbath", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("places", nargs="+")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    index = {re.sub(r" \(.*?\)| travel advice$", "", c["title"]): c["base_path"].split("/")[-1] for c in get(API)["links"]["children"]}
    for pid in args.places:
        name = places[pid]["name"]
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        if rec["patterns"].get("culture-and-protocol"):
            print(f"{pid}: exists, skipped")
            continue
        slug = index.get(ALIASES.get(name, name)) or next((s for t, s in index.items() if t.lower() == name.lower()), None)
        if not slug:
            print(f"{pid}: NO-FCDO {name}")
            continue
        page = get(f"{API}/{slug}")
        body = next((p["body"] for p in page["details"]["parts"] if p["slug"] == "safety-and-security"), "")
        found = [(t, b) for t, b in laws_from(body) if not SKIP.search(t)]
        dress = [f"{t}: {trim(b, 450)}" for t, b in found if SACRED.search(t) is None and DRESS.search(t)]
        sacred = [f"{t}: {trim(b, 450)}" for t, b in found if SACRED.search(t)]
        url = f"https://www.gov.uk/foreign-travel-advice/{slug}/safety-and-security"
        updated = page.get("public_updated_at", "")[:10]
        src = [{"title": f"{page['title']} (updated {updated})", "authority": "Foreign, Commonwealth and Development Office, UK Government",
                "url": url, "checked": D, "supports": "laws and cultural differences section as read on " + D}]
        if dress or sacred:
            out = {"status": "partly-mapped", "checked": D, "evidence": "official"}
            if dress:
                out["dress_and_conduct"] = " ".join(dress)
            if sacred:
                out["sacred_or_restricted_places"] = " ".join(sacred)
            out["cultural_authority"] = f"Government of {name}; local community and religious leaders."
            out["note"] = "From UK Government (FCDO) travel advice, written for British travellers. Confirm locally."
        else:
            out = {"status": "ask-locally", "checked": D, "evidence": "official",
                   "dress_and_conduct": f"FCDO's laws and cultural differences section for {name} has no customs or etiquette guidance. A national etiquette page has not been searched for yet. Ask locally.",
                   "cultural_authority": f"Government of {name} and its tourism office; local community leaders.",
                   "note": "FCDO page checked (written for British travellers); it has no customs guidance. National tourism or government etiquette pages not yet searched."}
        out["sources"] = src
        print(f"{pid}: {out['status']} {[x.split(':')[0] for x in dress + sacred]}")
        if not args.dry:
            rec["patterns"]["culture-and-protocol"] = out
            write(path, rec)


if __name__ == "__main__":
    main()
