"""Work out what needs vetting next.

  python scripts/due.py            public queue -> queue/due.json (never reads travel windows)
  python scripts/due.py --private  window-aware queue -> private/queue.json (reads private/windows.json)

The unit of work is a place pass: one place with every pattern that is due there, because
the same official sources usually answer several patterns at once.
"""
import argparse
import datetime
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import (ROOT, PRIVATE, ancestors, applies, descendants, event_span, events_for, is_active,  # noqa: E402
                 load_feeds, load_patterns, load_places, load_vetting, parse_date, read, today, write)

SPINE = ("country", "territory", "associated", "jurisdiction")


def window_phases(windows, cadence, places, vetting, on):
    """Map place id -> (phase, window id) for every place a window touches."""
    phases = {p["id"]: p for p in cadence["phases"]}
    touched = {}
    for window in windows:
        start, end = parse_date(window["start"]), parse_date(window["end"])
        lead = 0
        for pid in window["places"]:
            for zid in [pid] + descendants(places, pid):
                zone = vetting(zid).get("zone-requirements") or {}
                lead = max([lead] + [layer.get("lead_time_days") or 0 for layer in zone.get("layers", [])])
        approach = max(phases["approach"]["starts_days_before"], lead + cadence["lead_time_buffer_days"])
        days_out = (start - on).days
        if start <= on <= end:
            phase = "in-place"
        elif 0 < days_out <= phases["imminent"]["starts_days_before"]:
            phase = "imminent"
        elif 0 < days_out <= phases["countdown"]["starts_days_before"]:
            phase = "countdown"
        elif 0 < days_out <= approach:
            phase = "approach"
        elif end < on <= end + datetime.timedelta(days=phases["debrief"]["ends_days_after"]):
            phase = "debrief"
        else:
            continue
        for pid in window["places"]:
            zones = [z for z in descendants(places, pid) if places[z].get("zone_scan")]
            for member in [pid] + ancestors(places, pid) + zones:
                touched[member] = (phase, window["id"], approach)
    return touched


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--private", action="store_true")
    parser.add_argument("--date", help="override today (YYYY-MM-DD) for testing")
    args = parser.parse_args()
    on = parse_date(args.date) if args.date else today()

    places, patterns = load_places(), load_patterns()
    cadence = read(ROOT / "config/cadence.json")
    watch = read(ROOT / "data/watch.json")["items"]
    cache = {}
    flagged_sources = {}
    for url, src in read(ROOT / "data/source-status.json", {"sources": {}})["sources"].items():
        for where in src.get("used_by", []):
            if src.get("dead_since"):
                flagged_sources.setdefault(where, set()).add("source-dead")
            elif src.get("changed_on"):
                flagged_sources.setdefault(where, {"changed_on": src["changed_on"]})

    def vetting(pid):
        if pid not in cache:
            cache[pid] = load_vetting(pid)["patterns"]
        return cache[pid]

    windows = read(PRIVATE / "windows.json", {"windows": []})["windows"] if args.private else []
    touched = window_phases(windows, cadence, places, vetting, on)
    phase_caps = {p["id"]: p for p in cadence["phases"]}
    rank = {"in-place": 0, "imminent": 0, "countdown": 1, "approach": 2, "debrief": 3}

    passes = []
    for pid, place in places.items():
        in_window = pid in touched
        if not (is_active(place) or in_window):
            continue
        phase = touched.get(pid, (None,))[0]
        phase_rule = phase_caps.get(phase, {})
        due = []
        for pattern in patterns.values():
            if pattern["method"] == "machine" or not applies(pattern, place):
                continue
            if pattern.get("skip_home") and pid == "au":
                continue
            if phase_rule.get("patterns") and pattern["id"] not in phase_rule["patterns"]:
                continue
            record = vetting(pid).get(pattern["id"])
            checked = parse_date(record.get("checked")) if record else None
            age = (on - checked).days if checked else None
            budget = pattern["baseline_days"]
            if phase_rule.get("age_cap_days"):
                budget = min(budget, phase_rule["age_cap_days"])
            watched = [w["id"] for w in watch if pid in w["places"] and pattern["id"] in w["patterns"]
                       and w["status"] != "resolved" and w.get("effective") and parse_date(w["effective"]) <= on]
            flag = flagged_sources.get(f"{pid}#{pattern['id']}")
            source_changed = isinstance(flag, dict) and checked and parse_date(flag["changed_on"]) > checked
            if watched:
                reason = "watch"
            elif isinstance(flag, set):
                reason = "source-dead"
            elif source_changed:
                reason = "source-changed"
            elif checked is None:
                reason = "never-checked"
            elif record.get("status") == "imported":
                reason = "imported" if age > budget else None
            elif age > budget:
                reason = "over-budget"
            else:
                reason = None
            if reason:
                due.append({"pattern": pattern["id"], "reason": reason, "age_days": age, "budget_days": budget,
                            **({"watch": watched} if watched else {})})
        if not due:
            continue
        tags = place.get("tags", [])
        order = (rank.get(phase, 9),
                 0 if any(d["reason"] in ("watch", "source-dead", "source-changed") for d in due) else 1,
                 0 if "home" in tags else 1 if tags else 2,
                 0 if place["kind"] in SPINE else 1,
                 -max((d["age_days"] or 0) - d["budget_days"] for d in due),
                 place["name"])
        entry = {"place": pid, "name": place["name"], "kind": place["kind"], "tags": tags, "due": due}
        if phase:
            entry["window"] = {"phase": phase, "id": touched[pid][1], "approach_days": touched[pid][2]}
        passes.append((order, entry))

    passes.sort(key=lambda item: item[0])
    queue = [entry for _, entry in passes]
    summary = {
        "generated_on": on.isoformat(),
        "mode": "private" if args.private else "public",
        "place_passes": len(queue),
        "pattern_items": sum(len(e["due"]) for e in queue),
        "by_reason": {},
    }
    for entry in queue:
        for d in entry["due"]:
            summary["by_reason"][d["reason"]] = summary["by_reason"].get(d["reason"], 0) + 1
    watch_checks = []
    for w in watch:
        last = parse_date(w.get("checked"))
        if w["status"] != "resolved" and (not last or (on - last).days >= w.get("check_every_days", 14)):
            watch_checks.append({"id": w["id"], "what": w["what"], "status": w["status"], "last_checked": w.get("checked")})
    summary["watch_checks"] = len(watch_checks)
    window_events = []
    if windows:
        feeds = load_feeds()
        for window in windows:
            start, end = parse_date(window["start"]), parse_date(window["end"])
            for pid in window["places"]:
                for e in events_for(places, pid, feeds):
                    first, last = event_span(e)
                    if first and first <= end and (last or first) >= on:
                        window_events.append({"window": window["id"], "place": pid, "title": e["title"], "kind": e["kind"],
                                              "starts": e["starts"], "closes": e.get("closes"), "feed": e["feed"],
                                              "during": (last or first) >= start, "url": e.get("source_url")})
        summary["window_events"] = len(window_events)
    target = PRIVATE / "queue.json" if args.private else ROOT / "queue/due.json"
    body = {"summary": summary, "watch_checks": watch_checks, "queue": queue}
    if args.private:
        body["window_events"] = window_events
    write(target, body)
    print(summary)


if __name__ == "__main__":
    main()
