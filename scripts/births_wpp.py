"""Write the "births" area of births-and-family-support from UN World Population Prospects 2024.

Births per woman (total fertility rate) and the average age of mothers at birth, in 1975, 2000 and 2023
(the latest estimate year), and the number of births in 2023. Pass the downloaded demographic indicators file:
https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/CSV_FILES/WPP2024_Demographic_Indicators_Medium.csv.gz

    python scripts/births_wpp.py --csv PATH/WPP2024_Demographic_Indicators_Medium.csv.gz [--skip-region "Middle East"]

Replaces earlier items written by this script (marked "by": "births_wpp"); leaves every other item alone.
"""
import argparse
import csv
import gzip
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import load_places, read, today, vetting_path, write  # noqa: E402

URL = "https://population.un.org/wpp/"
YEARS = ("1975", "2000", "2023")


def births_text(n):
    """Births in thousands, as a rounded plain number."""
    n = float(n) * 1000
    if n >= 1_000_000:
        return f"about {n / 1_000_000:.1f} million"
    if n >= 10_000:
        return f"about {round(n, -3):,.0f}"
    if n >= 1_000:
        return f"about {round(n, -2):,.0f}"
    return f"about {round(n, -1):,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--skip-region", action="append", default=[])
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    rows = {}
    with gzip.open(args.csv, "rt", encoding="utf-8-sig", errors="replace") as f:
        for r in csv.DictReader(f):
            iso = (r.get("ISO2_code") or "").lower()
            if iso and r["Time"] in YEARS:
                rows.setdefault(iso, {})[r["Time"]] = r
    src = {"title": "World Population Prospects 2024", "authority": "United Nations, Department of Economic and Social Affairs, Population Division",
           "url": URL, "checked": D, "supports": "births per woman, births and mothers' average age, 1975 to 2023"}
    written = 0
    for iso, by_year in sorted(rows.items()):
        pid = "xk" if iso == "xk" else iso
        p = places.get(pid)
        if not p or p.get("region") in args.skip_region or not all(y in by_year for y in YEARS):
            continue
        tfr = [f"{float(by_year[y]['TFR']):.1f} in {y}" for y in YEARS]
        mac = [f"{float(by_year[y]['MAC']):.1f} in {y}" for y in (YEARS[0], YEARS[-1])]
        items = [
            {"area": "births", "kind": "figure", "changing": True, "text": f"Births per woman: {', '.join(tfr)}.", "source": URL, "checked": D, "by": "births_wpp"},
            {"area": "births", "kind": "figure", "changing": True, "text": f"Average age of mothers at birth: {', '.join(mac)}.", "source": URL, "checked": D, "by": "births_wpp"},
            {"area": "births", "kind": "figure", "text": f"Births in 2023: {births_text(by_year['2023']['Births'])}.", "source": URL, "checked": D, "by": "births_wpp"},
        ]
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].setdefault("births-and-family-support", {"status": "partly-mapped", "evidence": "official", "items": [], "sources": [],
                                                                        "notes": "UN estimates; the national statistics office may publish newer figures."})
        body["items"] = items + [i for i in body.get("items", []) if i.get("by") != "births_wpp"]
        if not any(s["url"] == URL for s in body["sources"]):
            body["sources"].append(src)
        body["checked"] = D
        write(path, rec)
        written += 1
    print(f"births: {written} places")


if __name__ == "__main__":
    main()
