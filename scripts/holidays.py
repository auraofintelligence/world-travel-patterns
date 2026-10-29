"""Machine layer of the culture-cycles pattern: public holidays for this year and next.

Source: Nager.Date (https://date.nager.at), an open community dataset. It is a signal, not an
authority: national gazettes and community calendars still decide. Places it doesn't cover are
listed so the monthly routine can fill them from official calendars.
Writes data/calendar/holidays-<year>.json. Stdlib only.
"""
import json
import pathlib
import sys
import time
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, today, write  # noqa: E402

API = "https://date.nager.at/api/v3"
UA = {"User-Agent": "Mozilla/5.0 (compatible; world-travel-patterns/1.0; +https://github.com/auraofintelligence)"}


def get(url, tries=4):
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as response:
                body = response.read()
                return json.loads(body) if response.status == 200 and body else None
        except OSError:
            if attempt == tries - 1:
                raise
            time.sleep(5 * (attempt + 1))


def main():
    on = today()
    places = load_places()
    spine = {p["iso2"]: pid for pid, p in places.items() if p.get("iso2")}
    covered = {c["countryCode"] for c in get(f"{API}/AvailableCountries")}
    for year in (on.year, on.year + 1):
        holidays, missing, failed = {}, [], []
        for code, pid in sorted(spine.items()):
            if code not in covered:
                missing.append(pid)
                continue
            try:
                rows = get(f"{API}/PublicHolidays/{year}/{code}") or []
            except OSError:
                failed.append(pid)
                continue
            holidays[pid] = [{"date": r["date"], "name": r["name"], "local_name": r["localName"],
                              "regions": r.get("counties"), "types": r.get("types")} for r in rows]
            time.sleep(0.5)
        write(ROOT / f"data/calendar/holidays-{year}.json", {
            "source": "Nager.Date public holiday API", "evidence": "signal", "checked_on": on.isoformat(),
            "year": year, "places": holidays, "not_covered": missing, "fetch_failed": failed,
            "rule": "A signal for planning. Moving and community calendars come from the culture-cycles routine."})
        print(f"{year}: {len(holidays)} places, {len(missing)} not covered, {len(failed)} failed")


if __name__ == "__main__":
    main()
