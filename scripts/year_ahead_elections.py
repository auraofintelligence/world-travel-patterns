"""Write national elections and referendums into year-ahead, from data/sources/electionguide-upcoming.json (a signal).

Each election becomes an event on the country's year-ahead record. Elections already past are skipped.
Replaces earlier events written by this script (marked "by": "elections"); leaves every other event alone.

    python scripts/year_ahead_elections.py
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402

NAMES = {"Gambia, The": "gm", "Virgin Islands, U.S.": "vi", "Micronesia, Federated States of": "fm", "Northern Cyprus": "cy",
         "United States of America": "us", "Cabo Verde": "cv"}


def norm(s):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())


def main():
    D = today().isoformat()
    places = load_places()
    by = {norm(p["name"]): pid for pid, p in places.items() if "/" not in pid}
    for pid, p in places.items():
        if "/" not in pid:
            for a in p.get("aliases", []):
                by.setdefault(norm(a), pid)
    src = read(ROOT / "data/sources/electionguide-upcoming.json")
    source = dict(src["source"], checked=D, supports="election dates")
    events = {}
    for country, what, start, end, confirmed in src["elections"]:
        if end < D:
            continue
        pid = NAMES.get(country) or by.get(norm(country))
        if not pid:
            print("no place for", country)
            continue
        ev = {"date": start, "what": what + ("" if confirmed else " (date not yet confirmed)"), "effect": "National election",
              "url": source["url"], "by": "elections"}
        if end != start:
            ev["end"] = end
        events.setdefault(pid, []).append(ev)
    for pid, evs in events.items():
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].setdefault("year-ahead", {"status": "mapped", "evidence": "signal", "events": [], "sources": []})
        body["events"] = sorted([e for e in body.get("events", []) if e.get("by") != "elections"] + evs, key=lambda e: e["date"])
        if not any(s["url"] == source["url"] for s in body["sources"]):
            body["sources"].append(source)
        body["checked"] = D
        write(path, rec)
    print(f"elections: {sum(len(v) for v in events.values())} events for {len(events)} places")


if __name__ == "__main__":
    main()
