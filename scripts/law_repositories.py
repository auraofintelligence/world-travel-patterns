"""Law-source map helpers: official places to look for statutes, gazettes and ordinances.

The records live in data/law-repositories.json. New source fields (kind, language,
searchable, source) are optional so earlier records stay valid until they are revisited.
"""
import re

SOURCE_KINDS = ("statutes", "gazette", "regulations", "municipal", "court")
SOURCE_ORIGINS = ("read directly", "search snapshot", "unverified")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
HTTP = re.compile(r"^https?://")

KIND_LABEL = {
    "statutes": "Statutes and codes",
    "gazette": "Official gazette",
    "regulations": "Regulations and ordinances",
    "municipal": "Municipal and city codes",
    "court": "Court decisions",
}


def is_first_level(place):
    return place.get("source_kind") == "first-level" or place.get("kind") == "state"


def first_level_ids(places):
    return [pid for pid, place in places.items() if is_first_level(place)]


def is_verified(source):
    """A source counts as verified when the official page was read directly.

    Legacy records have no source label; a check value of 'loaded' is treated as
    verified until that record is revisited. Search snapshots and failed fetches
    are not verified.
    """
    if not isinstance(source, dict) or not source.get("url"):
        return False
    origin = source.get("source")
    if origin == "unverified" or origin == "search snapshot":
        return False
    if origin == "read directly":
        return True
    if origin is None and source.get("check") == "loaded":
        return True
    return False


def coverage(repos, places):
    """Coverage of the state-level law-source map.

    repos is the top-level law-repositories object (or just its places map).
    """
    records = repos.get("places", repos) if isinstance(repos, dict) else {}
    first = first_level_ids(places)
    have = [pid for pid in first if records.get(pid)]
    verified = [pid for pid in have if any(is_verified(src) for src in records[pid])]
    listed = [pid for pid in have if pid not in verified]
    spine = [pid for pid in places if "/" not in pid]
    none = repos.get("no_online_source") or {}
    spine_with_url = [pid for pid in spine if records.get(pid)]
    return {
        "first_level": len(first),
        "with_any_source": len(have),
        "verified": len(verified),
        "listed_unverified": len(listed),
        "spine": len(spine),
        "spine_with_url": len(spine_with_url),
        "spine_with_record": len(set(spine_with_url) | set(none)),
        "no_online_source": len(none),
    }


def problems_in(repos, places, today=None):
    """Return a list of validation problems in a law-repositories document."""
    problems = []

    def check(condition, message):
        if not condition:
            problems.append(message)

    if not isinstance(repos, dict):
        return ["law-repositories.json must be an object"]
    records = repos.get("places")
    check(isinstance(records, dict), "law-repositories: places must be an object")
    if not isinstance(records, dict):
        return problems
    for pid, sources in records.items():
        where = f"law-repositories {pid}"
        check(pid in places, f"{where}: unknown place")
        check(isinstance(sources, list) and sources, f"{where}: sources must be a non-empty list")
        if not isinstance(sources, list):
            continue
        for i, src in enumerate(sources):
            tag = f"{where}[{i}]"
            if not isinstance(src, dict):
                problems.append(f"{tag}: source must be an object")
                continue
            for key in ("name", "publisher", "url", "check", "checked"):
                check(src.get(key), f"{tag}: missing {key}")
            url = src.get("url") or ""
            check(not url or HTTP.match(url), f"{tag}: bad url {url}")
            checked = src.get("checked")
            check(not checked or DATE.fullmatch(str(checked)), f"{tag}: checked must be YYYY-MM-DD")
            if today and checked and DATE.fullmatch(str(checked)):
                check(checked <= today.isoformat(), f"{tag}: checked date is in the future")
            if "kind" in src:
                check(src["kind"] in SOURCE_KINDS, f"{tag}: unknown kind {src.get('kind')}")
            if "source" in src:
                check(src["source"] in SOURCE_ORIGINS, f"{tag}: source must be one of {', '.join(SOURCE_ORIGINS)}")
            if "searchable" in src:
                check(isinstance(src["searchable"], bool), f"{tag}: searchable must be true or false")
            language = src.get("language")
            if language is not None:
                if isinstance(language, list):
                    check(language and all(isinstance(x, str) and x.strip() for x in language), f"{tag}: language list must be non-empty strings")
                else:
                    check(isinstance(language, str) and language.strip(), f"{tag}: language must be a non-empty string")
            if src.get("discovery_source"):
                check(HTTP.match(src["discovery_source"]), f"{tag}: discovery_source must be a URL")
            text = " ".join(str(src.get(k) or "") for k in ("name", "publisher", "check", "note"))
            check("\u2014" not in text, f"{tag}: em dash in text")
    for group in repos.get("groups") or []:
        tag = f"law-repositories group {group.get('id')}"
        check(group.get("id") and group.get("name"), f"{tag}: needs id and name")
        for mid in group.get("members") or []:
            check(mid in places, f"{tag}: unknown member {mid}")
        check(isinstance(group.get("repositories"), list) and group["repositories"], f"{tag}: repositories must be a non-empty list")
    for pid in repos.get("not_yet_found") or []:
        check(pid in places, f"law-repositories not_yet_found: unknown place {pid}")
    for pid, note in (repos.get("no_online_source") or {}).items():
        check(pid in places, f"law-repositories no_online_source: unknown place {pid}")
        check(isinstance(note, str) and note.strip(), f"law-repositories no_online_source {pid}: needs a note")
    return problems
