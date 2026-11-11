"""Validate patterns, the place tree and vetting records. Exits non-zero on any problem. Stdlib only."""
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from third_country import third_country  # noqa: E402
from lib import ROOT, VETTING, applies, load_patterns, load_places, parse_date, read, today  # noqa: E402
from law_repositories import problems_in as law_repo_problems  # noqa: E402

KINDS = {"country", "territory", "associated", "jurisdiction", "state", "district", "electorate", "region",
         "island", "island-group", "nation", "zone", "city", "site"}
PATTERN_KEYS = {"id", "name", "layer", "method", "question", "applies_to", "inherit", "baseline_days", "sources", "statuses", "rules", "version"}
FORBIDDEN_KEYS = re.compile(r"passport_?(no|number)|booking|card_number|phone|email|password|home_address|live_location", re.I)
problems = []

CONFLICT_START = "<" * 7
CONFLICT_END = ">" * 7
BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".bmp", ".tif", ".tiff",
    ".pdf", ".zip", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".woff", ".woff2",
    ".ttf", ".otf", ".eot", ".mp3", ".mp4", ".mov", ".avi", ".wav", ".sqlite",
    ".bin", ".exe", ".dylib", ".so",
}


def conflict_marker_lines(text):
    """Return 1-based line numbers whose stripped text starts with a git conflict marker."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith(CONFLICT_START) or stripped.startswith(CONFLICT_END):
            hits.append(i)
    return hits


def check_tracked_conflict_markers():
    """Fail if any tracked text, JSON or markdown file contains a git conflict marker."""
    try:
        raw = subprocess.check_output(
            ["git", "ls-files", "-z"], cwd=ROOT, stderr=subprocess.DEVNULL
        )
    except (OSError, subprocess.CalledProcessError):
        return
    nul = bytes([0])
    for rel in raw.split(nul):
        if not rel:
            continue
        path = ROOT / rel.decode("utf-8", "surrogateescape")
        if path.suffix.lower() in BINARY_SUFFIXES:
            continue
        try:
            data = path.read_bytes()
        except OSError as exc:
            problems.append(f"{path.relative_to(ROOT)}: could not read file ({exc})")
            continue
        if bytes([0]) in data[:8192]:
            continue
        text = data.decode("utf-8", "replace")
        rel_s = path.relative_to(ROOT).as_posix()
        for i in conflict_marker_lines(text):
            problems.append(f"{rel_s}:{i}: git conflict marker must not be committed")




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
    for t in patterns.get("ancient-sites-and-mysteries", {}).get("themes", []):
        check(t["lore"].startswith("Lore:") and all(x in places for x in t["places"]), f"theme {t['id']}: lore line must start 'Lore:' and link known places")
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
            for url in re.findall(r'"(?:url|source)": "(https?://[^"]+)"', text):
                check(not third_country(pid, url), f"{where}: another country's travel advice is not a source ({url}); use the place's own official source, then Smartraveller")
            for url in re.findall(r'"url": "([^"]+)"', text):
                check(url.startswith("https://") or url.startswith("http://"), f"{where}: bad url {url}")
            if pattern_id == "year-ahead":
                cats = set(pattern.get("event_categories", []))
                for ev in body.get("events", []):
                    if "category" in ev:
                        check(ev["category"] in cats, f"{where}: unknown event category {ev['category']}")
                    if ev.get("by") == "official-events":
                        check(re.fullmatch(r"\d{4}-\d{2}-\d{2}", ev.get("date", "")) and ev.get("url"), f"{where}: official event needs date and url")
            if pattern_id == "ancient-sites-and-mysteries":
                for st in body.get("sites", []):
                    tag = f"{where}: site {st.get('name')}"
                    check(st.get("name") and st.get("place") in places, f"{tag}: needs a name and a known place")
                    check(st.get("sources") and all(x.get("url") for x in st["sources"]), f"{tag}: facts need official sources")
                    tids = {t["id"] for t in pattern.get("themes", [])}
                    check(set(st.get("themes", [])) <= tids, f"{tag}: unknown theme")
                    lore = st.get("lore") or {}
                    if lore.get("text"):
                        check(lore.get("source") or lore.get("label") == "popular lore, not an official source", f"{tag}: unsourced lore must carry the popular-lore label")
                        check(re.match(r"(Popular theories claim|Local legend|Popular lore)", lore["text"]), f"{tag}: lore must be framed as claims")
                    if st.get("kind") == "underwater-site":
                        check(isinstance(st.get("underwater"), dict) and st["underwater"].get("diving"), f"{tag}: underwater site needs diving access")
            if body.get("provenance", {}).get("repo") is None:
                check(chr(0x2014) not in text, f"{where}: em dash in new text")

    repos = read(ROOT / "data/law-repositories.json", {})
    problems.extend(law_repo_problems(repos, places, today=on))

    try:
        tracked = subprocess.check_output(["git", "ls-files", "private"], cwd=ROOT, encoding="utf-8", stderr=subprocess.DEVNULL).split()
        check(set(tracked) <= {"private/README.md"}, f"private files are tracked by git: {tracked}")
    except (OSError, subprocess.CalledProcessError):
        pass

    check_tracked_conflict_markers()

    if problems:
        print(f"{len(problems)} problems:")
        for problem in problems[:80]:
            print(" -", problem)
        sys.exit(1)
    vetted = len(list(VETTING.glob("*.json")))
    print(f"OK: {len(patterns)} patterns, {len(places)} places, {vetted} places with vetting records")


if __name__ == "__main__":
    main()
