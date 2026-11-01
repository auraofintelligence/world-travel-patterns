"""Add monthly climate to seasons-and-flow from the World Bank Climate Change Knowledge Portal (1991-2020 averages).

Reads data/sources/cckp-climatology-1991-2020.json. Each month gets temp_c and rain_mm; the record gets a one-line
climate summary (wettest, driest, hottest, coolest months). Season names, hazards and visitor flow already recorded
are left as they are.

    python scripts/climate_seasons.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402

M = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def months_text(idx):
    return " and ".join(M[i] for i in sorted(idx)) if len(idx) <= 2 else ", ".join(M[i] for i in sorted(idx)[:-1]) + " and " + M[sorted(idx)[-1]]


def summary(t, r):
    by_r = sorted(range(12), key=lambda i: r[i])
    by_t = sorted(range(12), key=lambda i: t[i])
    return (f"Wettest: {months_text(by_r[-3:])}. Driest: {months_text(by_r[:3])}. "
            f"Hottest: {M[by_t[-1]]} ({t[by_t[-1]]}°C average). Coolest: {M[by_t[0]]} ({t[by_t[0]]}°C average). "
            "Country-wide averages for 1991 to 2020; coasts, mountains and the far north or south can differ a lot.")


def main():
    D = today().isoformat()
    places = load_places()
    src = read(ROOT / "data/sources/cckp-climatology-1991-2020.json")
    source = dict(src["source"], checked=D, supports="monthly average temperature and rainfall, 1991 to 2020")
    added = updated = 0
    for pid, c in sorted(src["countries"].items()):
        if pid not in places:
            continue
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].get("seasons-and-flow")
        if body is None:
            body = rec["patterns"]["seasons-and-flow"] = {"status": "partly-mapped", "checked": D, "evidence": "official", "months": [], "sources": []}
            added += 1
        else:
            updated += 1
        months = {m["month"]: m for m in body.get("months", [])}
        for i in range(12):
            m = months.setdefault(i + 1, {"month": i + 1})
            m["temp_c"], m["rain_mm"] = c["temp_c"][i], c["rain_mm"][i]
        body["months"] = [months[k] for k in sorted(months)]
        body["climate"] = summary(c["temp_c"], c["rain_mm"])
        if not any(s["url"] == source["url"] for s in body.get("sources", [])):
            body.setdefault("sources", []).append(source)
        body["checked"] = D
        write(path, rec)
    print(f"climate: {added} new seasons records, {updated} existing ones given climate")


if __name__ == "__main__":
    main()
