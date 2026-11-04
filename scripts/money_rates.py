"""Add currency and the RBA exchange rate to money-and-cost.

Reads data/sources/currencies-wikidata.json (a signal) and the latest data/sources/rba-f11-*.json (Reserve Bank of
Australia daily rates). Fills currency where a record has none, and sets rate_and_date wherever the RBA publishes a
rate for the place's currency. Where the RBA has no rate, falls back to the destination central bank's own published
rate in data/sources/central-bank-rates.json (cited, dated, marked approximate). Never guesses a rate.

    python scripts/money_rates.py
"""
import pathlib
import sys
from datetime import date

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402


def fallback_rate(code, cb, rba):
    """A$1 in `code` from a central bank rate, crossed via the RBA USD or EUR rate when needed."""
    e = cb.get("rates", {}).get(code)
    if not e:
        return None
    if e["base"] == "AUD":
        return e["rate"]
    if e["base"] in rba["aud_to"]:
        return round(e["rate"] * rba["aud_to"][e["base"]], 4)
    return None


def main():
    D = today().isoformat()
    places = load_places()
    cur = read(ROOT / "data/sources/currencies-wikidata.json")
    rba = read(sorted((ROOT / "data/sources").glob("rba-f11-*.json"))[-1])
    on = date.fromisoformat(rba["date"])
    when = f"{on.day} {on.strftime('%B %Y')}"
    rba_src = dict(rba["source"], checked=D, supports=f"A$ exchange rates on {when}")
    cur_src = dict(cur["source"], checked=D, supports="currencies in use")
    cb_path = ROOT / "data/sources/central-bank-rates.json"
    cb = read(cb_path) if cb_path.exists() else {"rates": {}}
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
        parts, cb_used = [], []
        for code, name in codes:
            if code == "AUD":
                parts.append("Australian dollar: no exchange needed")
            elif code in rba["aud_to"]:
                parts.append(f"A$1 = {rba['aud_to'][code]:,} {code}")
            elif fallback_rate(code, cb, rba):
                e = cb["rates"][code]
                d = date.fromisoformat(e["date"])
                via = "" if e["base"] == "AUD" else f", crossed via the RBA {e['base']} rate of {when}"
                parts.append(f"A$1 = about {fallback_rate(code, cb, rba):,} {code} ({e['source']['authority']}, "
                             f"{d.day} {d.strftime('%B %Y')}{via}; no RBA rate for {code})")
                cb_used.append(e)
        if parts:
            dated = any(not x.startswith("Australian dollar") and "about" not in x for x in parts)
            body["rate_and_date"] = "; ".join(parts) + (f" (Reserve Bank of Australia, {when})" if dated else "")
            have = {s["url"] for s in body.get("sources", [])}
            if (dated or any(e["base"] != "AUD" for e in cb_used)) and rba_src["url"] not in have:
                body.setdefault("sources", []).append(rba_src)
            for e in cb_used:
                if e["source"]["url"] not in {s["url"] for s in body.get("sources", [])}:
                    body.setdefault("sources", []).append(dict(e["source"], checked=D, supports=f"{e['source']['authority']} rate on {e['date']}"))
            rated += 1
        body["checked"] = D
        write(path, rec)
    print(f"money: {new} new records, {rated} with an A$ rate")


if __name__ == "__main__":
    main()
