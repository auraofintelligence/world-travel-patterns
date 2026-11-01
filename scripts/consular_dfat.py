"""Consular records for places without a Smartraveller page, from DFAT's A to Z list of missions.

Reads data/sources/dfat-missions-az.json. "Place (Australian Mission - City)" means a mission in the place; "- see X"
means X's mission covers it; a Canadian mission means the Canada-Australia consular sharing arrangement.
Only writes places that have no consular record yet.

    python scripts/consular_dfat.py
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402

ALIASES = {"cg": ["Congo, Republic of the"], "cv": ["Cabo Verde"], "kn": ["Saint Kitts & Nevis"], "vc": ["Saint Vincent & The Grenadines"],
           "va": ["Holy See"], "st": ["Sao Tome & Principe"], "bq": ["Bonaire"], "tc": ["Turks & Caicos Islands"], "wf": ["Wallis & Futuna"],
           "mp": ["Northern Mariana Islands, Commonwealth of"], "gw": ["Guinea Bissau"], "vi": ["Virgin Islands (USA)"], "pn": ["Pitcairn Island"],
           "re": ["Reunion"], "ag": ["Antigua and Barbuda"], "vg": ["Virgin Islands (British)"]}
# Covering places whose post DFAT lists under another name.
POSTS = {"us/hawaii": ("Australian Consulate-General, Honolulu", "Honolulu")}
SEE = {"trinidad & tobago": "tt", "trinidad and tobago": "tt", "lisbon": "pt", "hawaii": "us/hawaii", "usa, new york": "us",
       "united states of america": "us", "usa": "us", "united kingdom": "gb", "new caledonia": "nc", "samoa": "ws", "zimbabwe": "zw"}


def norm(s):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())


def main():
    D = today().isoformat()
    places = load_places()
    src = read(ROOT / "data/sources/dfat-missions-az.json")
    source = dict(src["source"], checked=D, supports="which mission covers this place")
    by_name = {norm(p["name"]): pid for pid, p in places.items() if "/" not in pid}
    written = 0
    for pid, p in places.items():
        if "/" in pid or pid == "au":
            continue
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        if "consular" in rec["patterns"]:
            continue
        names = [p["name"]] + ALIASES.get(pid, [])
        hits = [e.lstrip("* ").strip() for e in src["entries"] if any(e.lstrip("* ").lower().startswith(n.lower()) for n in names)]
        if not hits:
            continue
        e = hits[0]
        mission = re.search(r"\((Australian|Canadian) ([^)]+?) [-–] ([^)]+)\)", e)
        see = re.search(r" - see (?:also )?(.+)$", e)
        cover = None
        if see:
            target = see.group(1).strip()
            cover = SEE.get(target.lower()) or by_name.get(norm(target))
        body = {"checked": D, "evidence": "official", "sources": [source]}
        if mission and mission.group(1) == "Canadian":
            body.update(status="partner-arrangement", mission=f"Canadian {mission.group(2)}, {mission.group(3)}", city=mission.group(3),
                        notes="Canada gives consular help to Australians here under the Canada-Australia consular sharing arrangement.")
        elif mission and not see:
            body.update(status="in-place", mission=f"Australian {mission.group(2)}, {mission.group(3)}", city=mission.group(3), covers_from=pid,
                        notes=f"For consular help, contact the Australian {mission.group(2)} in {mission.group(3)}.")
        elif cover:
            covering = dict(read(vetting_path(cover), {"patterns": {}})["patterns"].get("consular", {}))
            if not covering.get("mission") and cover in POSTS:
                covering = {"mission": POSTS[cover][0], "city": POSTS[cover][1]}
            if not covering.get("mission"):
                own = [x for x in src["entries"] if norm(x.lstrip("* ").split(" (")[0]) == norm(places[cover]["name"])]
                m2 = own and re.search(r"\(Australian ([^)]+?) [-–] ([^)]+)\)", own[0])
                if m2:
                    covering = {"mission": f"Australian {m2.group(1)}, {m2.group(2)}", "city": m2.group(2)}
            if covering.get("mission"):
                covering["mission"] = covering["mission"].split("; ")[0]
            local = f" There's also an Australian {mission.group(2)} in {mission.group(3)}." if mission else ""
            body.update(status="neighbour", covers_from=cover, mission=covering.get("mission"), city=covering.get("city"),
                        notes=f"Covered by the Australian mission responsible for {places[cover]['name']}.{local}")
        else:
            continue
        if len(hits) > 1:
            body["notes"] += " DFAT also lists: " + "; ".join(hits[1:]) + "."
        rec["patterns"]["consular"] = {k: v for k, v in body.items() if v is not None}
        write(path, rec)
        written += 1
    print(f"consular: {written} places from DFAT's list")


if __name__ == "__main__":
    main()
