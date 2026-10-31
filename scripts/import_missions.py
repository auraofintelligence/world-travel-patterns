"""Import the foreign missions and consulates in Australia, from the reviewed DFAT Protocol snapshot in aura-horn-torus.

These are the offices you'd contact to apply for a visa or to confirm a rule in writing before you go.
Source: ../aura-horn-torus/data/missions-australia.json (DFAT Protocol public directory, reviewed there).
Writes data/missions/in-australia.json, grouped by place id. Institutional offices only: no staff,
phone or email fields are copied. Map positions are left in the source repo (ODbL there).
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_places import ALIASES, norm  # noqa: E402
from lib import ROOT, load_places, write  # noqa: E402

SOURCE = ROOT.parent / "aura-horn-torus" / "data" / "missions-australia.json"
# DFAT Protocol country labels that don't normalise to a place name or alias.
EXTRA = {"Korea, Republic of": "kr", "Korea (Republic of)": "kr", "Republic of Korea": "kr", "Taiwan (Taipei Economic and Cultural Office)": "tw",
         "Korea - Republic of Korea": "kr", "Korea - Democratic People's Republic of Korea": "kp", "Gambia, The": "gm",
         "Naoero": "nr", "Slovak Republic": "sk", "Holy See": "va", "Palestine": "ps"}
# Not places in the tree: noted, not imported.
SKIP = {"European Union", "Sovereign Military Order of Malta"}


def main():
    src = json.loads(SOURCE.read_text(encoding="utf-8"))
    places = load_places()
    by_name = {}
    for pid, p in places.items():
        if "/" in pid:
            continue
        by_name[norm(p["name"])] = pid
        for alias in ALIASES.get(pid.upper(), []):
            by_name[norm(alias)] = pid
    out, unmatched = {}, set()
    for r in src["records"]:
        label = r["country"]
        if label in SKIP:
            continue
        pid = EXTRA[label] if label in EXTRA else by_name.get(norm(label))
        if not pid:
            unmatched.add(label)
            continue
        office = {"name": r["officialName"], "type": r["type"], "honorary": r.get("honorary", False),
                  "city": r.get("city") or None, "state": r.get("stateCode") or None, "address": r.get("address") or None,
                  "website": r.get("website") or None, "source": r["sourceUrl"], "checked": r["checkedAt"]}
        notice = r.get("operationNotice") or ""
        if notice:
            office["notice"] = notice
        out.setdefault(pid, []).append(office)
    order = {"Embassy": 0, "High Commission": 0, "Diplomatic mission": 1, "Consulate-General": 2, "Consulate": 3}
    for offices in out.values():
        offices.sort(key=lambda o: (order.get(o["type"], 4), o["honorary"], o["state"] or "", o["name"]))
    write(ROOT / "data/missions/in-australia.json", {
        "what": "Each place's own embassies, high commissions and consulates in Australia: where to apply for a visa or confirm a rule in writing.",
        "source": src["sourceLabel"], "source_urls": src["sourceIndexUrls"], "checked": src["checkedAt"],
        "via": "auraofintelligence/aura-horn-torus data/missions-australia.json (reviewed snapshot)",
        "rule": "Institutional offices only. A checked date is when the directory was read, not a promise the office is open.",
        "places": dict(sorted(out.items())),
        "unmatched": sorted(unmatched),
    })
    print(f"{sum(map(len, out.values()))} offices for {len(out)} places; unmatched labels: {sorted(unmatched)}")

    # Australian posts abroad: which country each post's city is in, so consular.py can tell
    # "Australian Embassy, Athens" on Bulgaria's page is a post next door.
    layer = ROOT.parent / "aura-horn-torus" / "data" / "layers" / "australian-missions-abroad.js"
    rows = json.loads(layer.read_text(encoding="utf-8").split("=", 2)[2].rstrip().rstrip(";"))
    cities, missed = {}, set()
    for label, _lat, _lng, country, kind, *_ in rows:
        country = country.split(" · ")[0]
        pid = by_name.get(norm(country)) or {"Korea, Republic of (South)": "kr", "Palestinian Authority": "ps", "Laos": "la", "Russia": "ru"}.get(country)
        if not pid:
            missed.add(country)
            continue
        city = label.split(" · ")[0]
        cities[city] = {"place": {"Hong Kong": "hk"}.get(city, pid), "type": kind}
    write(ROOT / "data/missions/post-cities.json", {
        "what": "The city of each Australian post abroad and the place it sits in.",
        "via": "auraofintelligence/aura-horn-torus data/layers/australian-missions-abroad.js (from Australian-world-travel abroad.html)",
        "rule": "Used only to place a post. Smartraveller pages remain the source for which post helps where.",
        "cities": dict(sorted(cities.items())),
    })
    print(f"{len(cities)} post cities; unmatched countries: {sorted(missed)}")


if __name__ == "__main__":
    main()
