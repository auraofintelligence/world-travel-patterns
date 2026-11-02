"""Shared loaders for the place tree, patterns, vetting records and cadence. Stdlib only."""
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PLACES = ROOT / "data/places"
VETTING = ROOT / "data/vetting"
PRIVATE = ROOT / "private"


def read(path, default=None):
    path = pathlib.Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path, data):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def today():
    """Brisbane date (UTC+10 all year, no daylight saving)."""
    now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=10)
    return now.date()


def parse_date(value):
    return datetime.date.fromisoformat(value[:10]) if value else None


def load_places():
    """Spine plus every country shard. Returns {id: place} with children lists attached."""
    places = {p["id"]: dict(p) for p in read(PLACES / "spine.json", {"places": []})["places"]}
    for shard in sorted(PLACES.glob("*/*.json")):
        for p in read(shard)["places"]:
            if p["id"] in places:
                raise ValueError(f"Duplicate place id {p['id']} in {shard}")
            places[p["id"]] = dict(p, shard=str(shard.relative_to(ROOT)).replace("\\", "/"))
    for pid, extra in read(PLACES / "annotations.json", {"places": {}})["places"].items():
        place = places[pid]
        place["tags"] = sorted(set(place.get("tags", [])) | set(extra.get("tags", [])))
        place.update({k: v for k, v in extra.items() if k != "tags"})
    for p in places.values():
        p["children"] = []
    for p in places.values():
        parent = p.get("parent")
        if parent:
            if parent not in places:
                raise ValueError(f"{p['id']} names missing parent {parent}")
            places[parent]["children"].append(p["id"])
    return places


def ancestors(places, place_id):
    chain, current = [], places[place_id].get("parent")
    while current:
        chain.append(current)
        current = places[current].get("parent")
    return chain


def descendants(places, place_id):
    out, stack = [], list(places[place_id]["children"])
    while stack:
        current = stack.pop()
        out.append(current)
        stack.extend(places[current]["children"])
    return out


def load_patterns():
    return {p["id"]: p for p in (read(f) for f in sorted((ROOT / "patterns").glob("*.json")))}


def vetting_path(place_id):
    return VETTING / (place_id.replace("/", "__") + ".json")


def load_vetting(place_id):
    return read(vetting_path(place_id), {"place": place_id, "patterns": {}})


def resolve(places, patterns, place_id, pattern_id, cache=None):
    """Return [(place_id, record or None)] for a pattern, following its inherit mode.

    nearest: the place's own record, else the closest ancestor's (entry rules, seasons).
    stack:   every level from the country down, own level last (laws, protocols, zone layers).
    none:    the place's own record only (dated events, works).
    A None record means that level has not been vetted: unvetted is never read as "no rules".
    """
    cache = {} if cache is None else cache
    mode = patterns[pattern_id]["inherit"]

    def own(pid):
        if pid not in cache:
            cache[pid] = load_vetting(pid)["patterns"]
        return cache[pid].get(pattern_id)

    if mode == "none":
        return [(place_id, own(place_id))]
    chain = [place_id] + ancestors(places, place_id)
    if mode == "nearest":
        for pid in chain:
            if own(pid):
                return [(pid, own(pid))]
        gap = next((pid for pid in chain if applies(patterns[pattern_id], places[pid])), place_id)
        return [(gap, None)]
    levels = [pid for pid in reversed(chain) if applies(patterns[pattern_id], places[pid])]
    return [(pid, own(pid)) for pid in levels]


_HOME = {}


def home_chain():
    """The home base (config/home-base.json) and every level above it, country first."""
    if "chain" not in _HOME:
        home = read(ROOT / "config/home-base.json", {}).get("place")
        places = load_places()
        _HOME["place"] = home
        _HOME["chain"] = list(reversed([home] + ancestors(places, home))) if home in places else []
    return _HOME["chain"]


def applies(pattern, place):
    if pattern.get("home_only") and place["id"] not in home_chain():
        return False
    if place["kind"] not in pattern["applies_to"]:
        return False
    if pattern.get("only_tagged") and not place.get("tags"):
        return False
    return True


def load_feeds():
    """Every event from data/feeds/*.json, each tagged with its feed id."""
    events = []
    for path in sorted((ROOT / "data/feeds").glob("*.json")):
        feed = read(path)
        events += [dict(e, feed=feed["feed"], feed_name=feed["name"]) for e in feed["events"]]
    return events


def event_span(event):
    """(first day, last day) of an event; a month-only date covers the whole month."""
    def bound(value, last):
        if not value:
            return None
        if len(value) == 7:
            year, month = map(int, value.split("-"))
            if not last:
                return datetime.date(year, month, 1)
            nxt = datetime.date(year + month // 12, month % 12 + 1, 1)
            return nxt - datetime.timedelta(days=1)
        return parse_date(value)
    first = bound(event.get("starts"), False)
    last = bound(event.get("closes") or event.get("ends") or event.get("starts"), True)
    return first, max(filter(None, [last, first]), default=None)


def events_for(places, place_id, events):
    """Events at the place, its ancestors, anything inside it, or a bloc its country belongs to."""
    chain = {place_id, *ancestors(places, place_id), *descendants(places, place_id)}
    spine = place_id.split("/")[0]
    return [e for e in events if e.get("place") in chain or spine in e.get("members", [])]


def is_active(place):
    """Sub-places are dormant until tagged, flagged for a zone scan, or named in a travel window."""
    return place["kind"] in ("country", "territory", "associated", "jurisdiction") or bool(
        place.get("tags") or place.get("zone_scan") or place.get("active"))
