"""Visitor brief: everything that applies at a place, stacked across every level, with the gaps shown.

  python scripts/brief.py cl/rapa-nui --start 2027-03-01 --end 2027-04-15 --activities tourism,filming
  python scripts/brief.py au/minjerribah --out private/briefs/minjerribah.md

The special permit zone scan walks up to the country and down into any flagged zone inside the
place, so a national visa is never mistaken for permission to enter a zone. Each zone layer's
lead time is counted back from the start date to give a latest safe start.
Unvetted is not permitted: a level with no record is listed as not yet checked.
"""
import argparse
import datetime
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import (ROOT, applies, descendants, event_span, events_for, load_feeds, load_patterns,  # noqa: E402
                 load_places, parse_date, read, resolve, today)

ORDER = ["advisory", "entry", "activities", "health-entry", "zone-requirements", "local-law",
         "culture-and-protocol", "affection-and-relationships", "culture-cycles", "seasons-and-flow", "year-ahead", "consular", "money-and-cost", "works-and-purpose"]


def age(record, on):
    checked = parse_date(record.get("checked")) if record else None
    return f"checked {record['checked']} ({(on - checked).days} days ago)" if checked else "date missing"


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def window_months(start, end):
    if not start:
        return set()
    end = end or start
    months, d = set(), start.replace(day=1)
    while d <= end:
        months.add(d.month)
        d = (d + datetime.timedelta(days=32)).replace(day=1)
    return months


def public_holidays(spine, places, start, end, on):
    """Machine public holidays (Nager.Date, a signal) for the trip window, or the next 90 days."""
    first, last = (start, end or start) if start else (on, on + datetime.timedelta(days=90))
    found = []
    for year in sorted({first.year, last.year}):
        cal = read(ROOT / f"data/calendar/holidays-{year}.json", {"places": {}})
        for h in cal["places"].get(spine, []):
            d = parse_date(h["date"])
            if first <= d <= last:
                found.append(h)
    label = "during the window" if start else "in the next 90 days"
    out = [f"### Public holidays {label} ({places[spine]['name']})", "",
           "_Machine data from Nager.Date, a signal: confirm closures locally._", ""]
    out += [f"- {h['date']}: {h['name']}" + (f" ({h['local_name']})" if h.get("local_name") and h["local_name"] != h["name"] else "")
            + (f", regions {', '.join(h['regions'])}" if h.get("regions") else "") for h in found] or ["- None found in the holiday data."]
    return out + [""]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("place")
    parser.add_argument("--start")
    parser.add_argument("--end")
    parser.add_argument("--activities", default="")
    parser.add_argument("--out")
    args = parser.parse_args()
    on = today()
    places, patterns = load_places(), load_patterns()
    place = places[args.place]
    activities = [a for a in args.activities.split(",") if a]
    start = parse_date(args.start) if args.start else None
    advisories = read(ROOT / "data/advisories.json", {"destinations": {}})
    watch = read(ROOT / "data/watch.json")["items"]
    cache = {}
    names = lambda pid: places[pid]["name"]  # noqa: E731
    lines = [f"# Visitor brief: {place['name']}", "",
             f"Generated {on.isoformat()} (Brisbane). A planning aid, not legal advice. "
             "A level marked *not yet checked* has unknown rules, not no rules.", ""]
    if start:
        lines += [f"Window starts {start.isoformat()} ({(start - on).days} days away).", ""]

    gaps = 0
    chain_patterns = [p for p in ORDER if p in patterns] + sorted(set(patterns) - set(ORDER))
    for pid in chain_patterns:
        pattern = patterns[pid]
        if pid == "zone-requirements" or (pattern.get("only_tagged") and not place.get("tags")):
            continue
        if pid == "advisory":
            spine = args.place.split("/")[0]
            key = places[spine].get("smartraveller")
            rec = advisories["destinations"].get(key) if key else None
            lines += ["## Safety advice level", ""]
            lines.append(f"- {names(spine)}: **{rec['level']}** (Smartraveller, fetched {advisories['checked_on']}) {rec['url']}"
                         if rec else f"- {names(spine)}: no separate Smartraveller page; check the neighbouring or parent advice.")
            lines.append("")
            continue
        levels = resolve(places, patterns, args.place, pid, cache)
        levels = [(lp, rec) for lp, rec in levels if applies(pattern, places[lp]) or rec]
        if not levels:
            continue
        lines += [f"## {pattern['name']}", "", f"_{pattern['question']}_", ""]
        for lp, rec in levels:
            if not rec:
                lines.append(f"- {names(lp)}: *not yet checked*"); gaps += 1
                continue
            if pid == "activities":
                lines.append(f"- {names(lp)}: {len(rec.get('activities', {}))} activities vetted, oldest {age(rec, on)}")
                if not activities:
                    lines.append("  - pass --activities to list the ones you plan")
            else:
                text = f"{rec['summary']} " if rec.get("summary") else ""
                lines.append(f"- {names(lp)}: {text}[{rec.get('status')}, {age(rec, on)}]")
            if pid == "activities":
                for act in activities:
                    a = rec.get("activities", {}).get(act)
                    lines.append(f"  - {act}: " + (f"**{a['status']}**: {a.get('route')} ({age(a, on)})" if a else "*not yet checked*"))
                    gaps += 0 if a else 1
            for law in rec.get("laws", []):
                lines.append(f"  - {law['topic']}: {law['rule']} ({law.get('source', 'no source')})")
            for item in rec.get("items", []):
                lines.append(f"  - {item['area']} ({item['kind']}{', signal' if item.get('evidence') == 'signal' else ''}): {item['text']} ({item.get('source', 'no source')})")
            if pid == "seasons-and-flow" and rec.get("months"):
                # Only the trip's months when a window is given, else the whole year.
                wanted = window_months(start, parse_date(args.end) if args.end else None)
                for m in rec["months"]:
                    if wanted and m["month"] not in wanted:
                        continue
                    bits = [b for b in (m.get("season"), m.get("hazard") and f"hazard: {m['hazard']}", m.get("visitor_flow") and f"visitors: {m['visitor_flow']}") if b]
                    lines.append(f"  - {MONTHS[m['month'] - 1]}: {'; '.join(bits) or 'not yet mapped'}")
            for key in ("festivals", "closures", "moving_calendars", "protocol_notes"):
                for item in rec.get(key) or []:
                    lines.append(f"  - {key.replace('_', ' ')}: {item if isinstance(item, str) else item.get('what')}")
        lines.append("")
        if pid == "culture-cycles":
            lines += public_holidays(args.place.split("/")[0], places, start, parse_date(args.end) if args.end else None, on)

    zones = [args.place] + [z for z in descendants(places, args.place) if places[z].get("zone_scan")]
    lines += ["## Special permit zone scan", ""]
    for zid in zones:
        levels = resolve(places, patterns, zid, "zone-requirements", cache)
        for lp, rec in levels:
            if lp != zid and lp in zones:
                continue
            if not rec:
                flagged = places[lp].get("zone_scan")
                lines.append(f"- {names(lp)}: *not yet checked*" + (" (flagged)" if flagged else "")); gaps += 1
                continue
            lines.append(f"- {names(lp)}: {rec.get('status')} ({age(rec, on)})")
            for layer in rec.get("layers", []):
                if activities and layer.get("activities") and not set(layer["activities"]) & set(activities + ["all"]):
                    continue
                lead = layer.get("lead_time_days")
                safe = f"; latest safe start {(start - datetime.timedelta(days=lead)).isoformat()}" if start and lead else ""
                lines.append(f"  - {layer['type']}: {layer.get('process')} ({layer.get('authority')}){safe} {layer.get('url', '')}")
    lines.append("")

    end = parse_date(args.end) if args.end else None
    upcoming = []
    for event in events_for(places, args.place, load_feeds()):
        first, last = event_span(event)
        if not first or (last or first) < on:
            continue
        during = bool(start and end and first <= end and (last or first) >= start)
        upcoming.append((first, during, event))
    if upcoming:
        lines += ["## Upcoming from the feeds", "",
                  "_Dated leads, not permissions: taking part still runs through entry, activities and zone checks._", ""]
        for first, during, e in sorted(upcoming, key=lambda item: item[0]):
            door = f"**Open door, closes {e['closes']}** · " if e["kind"] == "door" and e.get("closes") else ""
            flag = "**During the window** · " if during else ""
            lines.append(f"- {flag}{door}{e.get('when_text') or e['starts']}: {e['title']}. {e['where']} "
                         f"({e['feed_name']}) {e.get('source_url') or ''}".rstrip())
        lines.append("")

    active = [w for w in watch if w["status"] != "resolved" and set(w["places"]) & {args.place.split('/')[0], args.place}]
    if active:
        lines += ["## Rule changes being watched", ""]
        lines += [f"- {w['what']} Status: {w['status']}. Effective: {w.get('effective') or 'not settled'}. {w['next']}" for w in active]
        lines.append("")
    lines += [f"**{gaps} gaps** still to check before relying on this brief.", ""]

    text = "\n".join(lines)
    if args.out:
        out = ROOT / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"Wrote {out} ({gaps} gaps)")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)


if __name__ == "__main__":
    main()
