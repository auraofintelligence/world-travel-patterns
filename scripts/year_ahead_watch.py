"""Copy dated rule changes from data/watch.json into each affected place's year-ahead record.

Every unresolved watch item with an effective date in the next twelve months becomes an event, with its sources.
Replaces earlier events written by this script (marked "by": "watch").

    python scripts/year_ahead_watch.py
"""
import pathlib
import sys
from datetime import timedelta

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402


def main():
    on = today()
    D, until = on.isoformat(), (on + timedelta(days=365)).isoformat()
    places = load_places()
    watch = read(ROOT / "data/watch.json")
    items = watch.get("items", watch) if isinstance(watch, dict) else watch
    events = {}
    for w in items:
        eff = w.get("effective")
        if w.get("status") == "resolved" or not eff or not (D <= eff <= until):
            continue
        for pid in w["places"]:
            if pid in places:
                events.setdefault(pid, []).append((w, eff))
    for pid, rows in events.items():
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].setdefault("year-ahead", {"status": "mapped", "evidence": "official", "events": [], "sources": []})
        body["events"] = [e for e in body.get("events", []) if e.get("by") != "watch"]
        urls = {s["url"] for s in body["sources"]}
        for w, eff in rows:
            body["events"].append({"date": eff, "what": w["what"], "effect": "Rule change: check entry before booking",
                                   "url": (w.get("sources") or [""])[0], "by": "watch"})
            for u in w.get("sources") or []:
                if u not in urls:
                    body["sources"].append({"title": "Rule change watched", "authority": "Smartraveller, Australian Government" if "smartraveller" in u else "Official source",
                                            "url": u, "checked": D, "supports": w["what"]})
                    urls.add(u)
        body["events"].sort(key=lambda e: e["date"])
        body["checked"] = D
        write(path, rec)
    print(f"watch: {sum(len(v) for v in events.values())} rule-change events for {len(events)} places")


if __name__ == "__main__":
    main()
