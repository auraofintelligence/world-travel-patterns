"""Add currency and the RBA exchange rate to money-and-cost.

Reads data/sources/currencies-wikidata.json (a signal) and the latest data/sources/rba-f11-*.json (Reserve Bank of
Australia daily rates). Fills currency where a record has none, and sets rate_and_date wherever the RBA publishes a
rate for the place's currency. Never guesses a rate the RBA doesn't publish.

    python scripts/money_rates.py
"""
import pathlib
import sys
from datetime import date

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402


def main():
    D = today().isoformat()
    places = load_places()
    cur = read(ROOT / "data/sources/currencies-wikidata.json")
    rba = read(sorted((ROOT / "data/sources").glob("rba-f11-*.json"))[-1])
    on = date.fromisoformat(rba["date"])
    when = f"{on.day} {on.strftime('%B %Y')}"
    rba_src = dict(rba["source"], checked=D, supports=f"A$ exchange rates on {when}")
    cur_src = dict(cur["source"], checked=D, supports="currencies in use")
    new = rated = 0
    for pid, codes in cur["countries"].items():
        if pid not in places or pid == "au":
            continue
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].get("money-and-cost")
        if body is None:
            body = rec["patterns"]["money-and-cost"] = {"status": "noted", "checked": D, "evidence": "signal", "sources": [cur_src]}
            new += 1
        if not body.get("currency"):
            body["currency"] = ", ".join(f"{name} ({code})" for code, name in codes)
            if cur_src["url"] not in {s["url"] for s in body.get("sources", [])}:
                body.setdefault("sources", []).append(cur_src)
        parts = []
        for code, name in codes:
            if code == "AUD":
                parts.append("Australian dollar: no exchange needed")
            elif code in rba["aud_to"]:
                parts.append(f"A$1 = {rba['aud_to'][code]:,} {code}")
        if parts:
            dated = any(not x.startswith("Australian dollar") for x in parts)
            body["rate_and_date"] = "; ".join(parts) + (f" (Reserve Bank of Australia, {when})" if dated else "")
            if rba_src["url"] not in {s["url"] for s in body.get("sources", [])}:
                body.setdefault("sources", []).append(rba_src)
            rated += 1
        body["checked"] = D
        write(path, rec)
    print(f"money: {new} new records, {rated} with an A$ rate")


if __name__ == "__main__":
    main()
