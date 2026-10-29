"""Machine pattern: refresh Smartraveller advice levels for every destination.

Reads the official export at https://www.smartraveller.gov.au/destinations-export,
writes data/advisories.json and appends each level change to data/logs/advisory-changes.jsonl.
Prints a markdown summary of changes (used as the GitHub issue body). Stdlib only.
"""
import datetime
import html
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPORT = "https://www.smartraveller.gov.au/destinations-export"
OUT = ROOT / "data/advisories.json"
LOG = ROOT / "data/logs/advisory-changes.jsonl"


def fetch(source=None):
    if source:
        return json.loads(pathlib.Path(source).read_text(encoding="utf-8", errors="replace"))
    request = urllib.request.Request(EXPORT, headers={"User-Agent": "Mozilla/5.0 (compatible; world-travel-patterns/1.0; +https://github.com/auraofintelligence)"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def parse_changed(value):
    # Export format: "Fri, 2026-10-16 05:25" (Canberra time, as published)
    try:
        return datetime.datetime.strptime(value.split(", ", 1)[1], "%Y-%m-%d %H:%M").strftime("%Y-%m-%dT%H:%M")
    except (IndexError, ValueError):
        return value


def main():
    # Brisbane date (UTC+10, no daylight saving), matching every other checked date in the repo.
    today = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=10)).strftime("%Y-%m-%d")
    raw = fetch(sys.argv[1] if len(sys.argv) > 1 else None)
    previous = json.loads(OUT.read_text(encoding="utf-8"))["destinations"] if OUT.exists() else {}
    destinations = {}
    for record in raw:
        url = record.get("field_url") or ""
        if "/destinations/" not in url:
            continue  # page-type entries such as "Crisis alert"
        key = url.rstrip("/").rsplit("/", 1)[1]
        destinations[key] = {
            "title": html.unescape(record["title"]).strip(),
            "level": record["field_overall_advice_level"].strip(),
            "region": record.get("field_region") or None,
            "published_change": parse_changed(record.get("changed", "")),
            "url": url,
        }

    changes = []
    for key, now in sorted(destinations.items()):
        before = previous.get(key)
        if before and before["level"] != now["level"]:
            changes.append({"date": today, "destination": key, "from": before["level"], "to": now["level"], "url": now["url"]})
    for key in sorted(previous.keys() - destinations.keys()):
        changes.append({"date": today, "destination": key, "from": previous[key]["level"], "to": "no longer listed", "url": previous[key]["url"]})

    OUT.write_text(json.dumps({
        "source": EXPORT,
        "authority": "Australian Government, Smartraveller",
        "checked_on": today,
        "rule": "Advice level is information for the traveller, never an automatic exclusion.",
        "destinations": destinations,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if changes and previous:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as log:
            for change in changes:
                log.write(json.dumps(change, ensure_ascii=False) + "\n")
        print(f"## Smartraveller level changes, {today}\n")
        for c in changes:
            print(f"- **{destinations.get(c['destination'], {}).get('title', c['destination'])}**: {c['from']} → {c['to']} ([advice]({c['url']}))")
    print(f"{len(destinations)} destinations, {len(changes) if previous else 0} level changes", file=sys.stderr)


if __name__ == "__main__":
    main()
