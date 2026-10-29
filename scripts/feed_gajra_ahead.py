"""Feed: upcoming AI governance events and open doors from GAJRA Earth's Ahead page.

Reads ../gajra-earth-claude-build/ahead.html when it is next to this repo, otherwise the
published page. Each entry is mapped to the most specific place in the tree that its
"where" line names. Online and global entries stay in the feed with no place.
The Ahead routine owns the content, including its defence exclusion; this only reads it.
Writes data/feeds/gajra-ahead.json. Stdlib only.
"""
import html
import os
import pathlib
import re
import sys
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_places import norm  # noqa: E402
from lib import ROOT, load_places, today, write  # noqa: E402

LOCAL = ROOT.parent / "gajra-earth-claude-build" / "ahead.html"
PAGE = "https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html"
MATCH_KINDS = {"country", "territory", "associated", "jurisdiction", "state", "region", "island", "island-group", "nation", "zone"}
BLOCS = {"europeanunion": ("eu", "at be bg hr cy cz dk ee fi fr de gr hu ie it lv lt lu mt nl pl pt ro sk si es se".split())}


def text(fragment):
    fragment = re.sub(r"<span class=\"chip[^\"]*\">.*?</span>", "", fragment, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def place_index(places):
    exact, contains = {}, []
    for pid, p in places.items():
        if p["kind"] not in MATCH_KINDS or p.get("overlay"):
            continue
        for label in [p["name"], *p.get("aliases", [])]:
            key = norm(label)
            if len(key) >= 4:
                exact.setdefault(key, pid)
                contains.append((key, pid))
    # Longer names first, so "South Australia" wins over "Australia".
    return exact, sorted(contains, key=lambda item: -len(item[0]))


def locate(where, index, places):
    """Anchor on the country named exactly (the last such part wins), then the deepest place inside it."""
    exact, contains = index
    parts = [norm(part) for part in re.split(r",| through | for the | in | after ", where) if part.strip()]
    spine = [exact[p] for p in parts if p in exact and "/" not in exact[p]]
    if not spine:
        for part in parts:
            hit = next((pid for key, pid in contains if "/" not in pid and len(key) >= 6 and key in part), None)
            if hit:
                spine.append(hit)
    if not spine:
        return None
    country = spine[-1]
    # Whole-part matches first ("Ohio"); substrings ("Delaware County") only when no part matches whole.
    inside = {exact[p] for p in parts if p in exact and exact[p].startswith(country + "/")}
    if not inside:
        for part in parts:
            for key, pid in contains:
                if pid.startswith(country + "/") and len(key) >= 6 and key in part:
                    inside.add(pid)
                    break
    # Several separate places inside one country (a multi-state entry) stay at country level.
    leaves = {p for p in inside if not any(q != p and q.startswith(p + "/") for q in inside)}
    return leaves.pop() if len(leaves) == 1 else country


def main():
    use_local = LOCAL.exists() and os.environ.get("FEED_SOURCE") != "web"
    source = LOCAL.read_text(encoding="utf-8") if use_local else urllib.request.urlopen(
        urllib.request.Request(PAGE, headers={"User-Agent": "Mozilla/5.0 (compatible; world-travel-patterns/1.0)"}), timeout=60
    ).read().decode("utf-8")
    places = load_places()
    index = place_index(places)
    events, unplaced = [], 0
    for attrs, body in re.findall(r'<article class="ev"([^>]*)>(.*?)</article>', source, flags=re.S):
        get = lambda name: (re.search(rf'data-{name}="([^"]*)"', attrs) or [None, None])[1]  # noqa: E731
        title = text(re.search(r"<h3>(.*?)</h3>", body, flags=re.S).group(1))
        where_match = re.search(r'<p class="ev-where">(.*?)</p>', body, flags=re.S)
        where = text(where_match.group(1)) if where_match else ""
        when_match = re.search(r'<p class="ev-date">(.*?)</p>', body, flags=re.S)
        link = re.search(r'<p class="src"><a href="([^"]+)"', body)
        place = None if re.match(r"(?i)online|global", where) else locate(where, index, places)
        bloc = next((b for key, b in BLOCS.items() if key in norm(where)), None) if place is None else None
        unplaced += place is None and bloc is None
        events.append({
            "title": title,
            "kind": "door" if 'chip door' in body else "event",
            "starts": get("when"), "ends": get("ends"), "closes": get("closes"),
            "days": [d for d in (get("days") or "").split(",") if d],
            "when_text": text(when_match.group(1)) if when_match else None,
            "where": where, "place": place,
            **({"bloc": bloc[0], "members": bloc[1]} if bloc else {}),
            "keywords": (get("k") or "").split(),
            "source_url": link.group(1) if link else None,
        })
    write(ROOT / "data/feeds/gajra-ahead.json", {
        "feed": "gajra-ahead",
        "name": "GAJRA Earth Ahead: AI governance events and open doors",
        "source": PAGE,
        "checked_on": today().isoformat(),
        "evidence": "signal",
        "rule": "Dated leads for planning and the works-and-purpose layer. An event is not a permission: visiting to speak or take part still runs through entry, activities and zone checks.",
        "events": events,
    })
    doors = sum(e["kind"] == "door" for e in events)
    print(f"{len(events)} entries ({doors} open doors), {len(events) - unplaced} placed (place or bloc), {unplaced} online or global")


if __name__ == "__main__":
    main()
