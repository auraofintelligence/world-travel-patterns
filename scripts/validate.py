"""Validate patterns, the place tree and vetting records. Exits non-zero on any problem. Stdlib only."""
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, VETTING, applies, load_patterns, load_places, parse_date, read, today  # noqa: E402

KINDS = {"country", "territory", "associated", "jurisdiction", "state", "district", "electorate", "region",
         "island", "island-group", "nation", "zone", "city", "site"}
PATTERN_KEYS = {"id", "name", "layer", "method", "question", "applies_to", "inherit", "baseline_days", "sources", "statuses", "rules", "version"}
FORBIDDEN_KEYS = re.compile(r"passport_?(no|number)|booking|card_number|phone|email|password|home_address|live_location", re.I)
problems = []


def check(condition, message):
    if not condition:
        problems.append(message)


def main():
    patterns = load_patterns()
    for pid, p in patterns.items():
        check(PATTERN_KEYS <= set(p), f"pattern {pid}: missing {sorted(PATTERN_KEYS - set(p))}")
        check(p.get("inherit") in {"nearest", "stack", "none"}, f"pattern {pid}: bad inherit mode")
        check(p.get("method") in {"machine", "agent", "mixed"}, f"pattern {pid}: bad method")
        check(set(p.get("applies_to", [])) <= KINDS, f"pattern {pid}: unknown kind in applies_to")
        check("unknown" in p.get("statuses", []), f"pattern {pid}: statuses must include unknown")

    places = load_places()
    for pid, place in places.items():
        check(place["kind"] in KINDS, f"place {pid}: unknown kind {place['kind']}")
        if "/" in pid:
            check(pid.split("/")[0] in places, f"place {pid}: id prefix is not a spine place")
            check(place.get("parent"), f"place {pid}: sub-place without parent")

    on = today()
    for path in VETTING.glob("*.json"):
        record = read(path)
        pid = record["place"]
        check(pid in places, f"{path.name}: unknown place {pid}")
        for pattern_id, body in record["patterns"].items():
            where = f"{pid}#{pattern_id}"
            pattern = patterns.get(pattern_id)
            check(pattern, f"{where}: unknown pattern")
            if not pattern or pid not in places:
                continue
            check(applies(pattern, places[pid]) or not pattern.get("only_tagged"), f"{where}: pattern does not apply to this kind")
            check(body.get("status") in pattern["statuses"] + ["imported"], f"{where}: status {body.get('status')} not in pattern")
            checked = body.get("checked")
            check(checked and re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked), f"{where}: checked must be YYYY-MM-DD")
            if checked:
                check(parse_date(checked) <= on, f"{where}: checked date is in the future")
            text = json.dumps(body, ensure_ascii=False)
            for key in re.findall(r'"([a-z_]+)":', text):
                check(not FORBIDDEN_KEYS.search(key), f"{where}: private field {key} is not allowed")
            for url in re.findall(r'"url": "([^"]+)"', text):
                check(url.startswith("https://") or url.startswith("http://"), f"{where}: bad url {url}")
            if body.get("provenance", {}).get("repo") is None:
                check(chr(0x2014) not in text, f"{where}: em dash in new text")

    try:
        tracked = subprocess.check_output(["git", "ls-files", "private"], cwd=ROOT, encoding="utf-8", stderr=subprocess.DEVNULL).split()
        check(set(tracked) <= {"private/README.md"}, f"private files are tracked by git: {tracked}")
    except (OSError, subprocess.CalledProcessError):
        pass

    if problems:
        print(f"{len(problems)} problems:")
        for problem in problems[:80]:
            print(" -", problem)
        sys.exit(1)
    vetted = len(list(VETTING.glob("*.json")))
    print(f"OK: {len(patterns)} patterns, {len(places)} places, {vetted} places with vetting records")


if __name__ == "__main__":
    main()
