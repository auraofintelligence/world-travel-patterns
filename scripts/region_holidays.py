"""Write regional public holidays (the next twelve months) onto each region's culture-cycles record.

Reads data/calendar/holidays-*.json (Nager.Date, a signal), where a holiday that applies only in some regions
lists their ISO 3166-2 codes. Region places are matched by iso_3166_2, or by name through
data/sources/iso-3166-2-first-level.json.

    python scripts/region_holidays.py
"""
import pathlib
import re
import sys
import unicodedata
from datetime import date, timedelta

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402


def norm(s):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())


def main():
    on = today()
    D, until = on.isoformat(), (on + timedelta(days=365)).isoformat()
    places = load_places()
    code_to_place = {p["iso_3166_2"]: pid for pid, p in places.items() if p.get("iso_3166_2")}
    names = {(pid.split("/")[0], norm(p["name"])): pid for pid, p in places.items() if "/" in pid and p.get("kind") in ("state", "region")}
    for r in read(ROOT / "data/sources/iso-3166-2-first-level.json")["regions"]:
        code_to_place.setdefault(r["iso_3166_2"], names.get((r["country"], norm(r["name"]))))
    found, unmatched = {}, set()
    for f in sorted((ROOT / "data/calendar").glob("holidays-*.json")):
        for cc, rows in read(f)["places"].items():
            for h in rows:
                if not h.get("regions") or not (D <= h["date"] <= until):
                    continue
                for code in h["regions"]:
                    pid = code_to_place.get(code)
                    if not pid:
                        unmatched.add(code)
                        continue
                    local = f" ({h['local_name']})" if h.get("local_name") and h["local_name"] != h["name"] else ""
                    found.setdefault(pid, []).append((h["date"], f"{h['name']}{local}"))
    src = {"title": "Public holidays (Nager.Date)", "authority": "Signal: machine holiday data", "url": "https://date.nager.at/", "checked": D,
           "supports": "regional public holidays in the next twelve months"}
    for pid, rows in found.items():
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].setdefault("culture-cycles", {"status": "partly-mapped", "evidence": "signal", "festivals": [], "closures": [],
                                                             "moving_calendars": [], "protocol_notes": [], "sources": []})
        body["public_holidays"] = [f"{d}: {what} (regional holiday)" for d, what in sorted(set(rows))]
        if src["url"] not in {s["url"] for s in body["sources"]}:
            body["sources"].append(src)
        body["checked"] = D
        write(path, rec)
    print(f"regional holidays: {sum(len(v) for v in found.values())} for {len(found)} regions; unmatched codes: {sorted(unmatched)}")


if __name__ == "__main__":
    main()
