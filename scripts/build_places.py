"""Build data/places/spine.json: every ISO country, territory and separately travelled jurisdiction.

The spine is the root layer only. Islands, regions, nations, zones and governance units
live in country shards (data/places/<iso2>/*.json) whose parents point back here.

Inputs (all read-only):
  data/sources/iso-regions.json          ISO 3166 alpha-2 names (from Node's Intl.DisplayNames)
  data/advisories.json                   Smartraveller destinations, if already fetched
  ../Australian-visa-activity-atlas      world baseline and deep guide names, if present

Place ids are the lower-case ISO code (au, th). They are stable keys used by every vetting record.
"""
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
ATLAS = ROOT.parent / "Australian-visa-activity-atlas"

# ISO codes that are not separate travel destinations (groupings, placeholders, parts of another entry).
SKIP = {"EU", "EZ", "UN", "QO", "XA", "XB", "ZZ", "AC", "TA", "DG", "CP", "EA", "IC", "UM", "BV", "HM",
        # Legacy and alternate codes that duplicate a current place (UK = GB, FX = FR, SU = RU, YU = RS ...)
        "AN", "BU", "CS", "DD", "DY", "FX", "HV", "NH", "RH", "SU", "TP", "UK", "VD", "YD", "YU", "ZR"}

TERRITORIES = set(
    "AS AI AQ AW AX BL BM BQ CC CW CX FK FO GF GG GI GL GP GS GU HK IM IO JE KY MF MO MP MQ MS "
    "NC NF PF PM PN PR RE SH SJ SX TC TF TK VG VI WF YT".split()
)
ASSOCIATED = {"CK", "NU"}
# Travelled separately; kind carries no position on status.
JURISDICTIONS = {"TW", "PS", "XK", "EH"}

DISPLAY = {
    "MM": "Myanmar", "CI": "Côte d'Ivoire", "CD": "Democratic Republic of the Congo",
    "CG": "Republic of the Congo", "HK": "Hong Kong", "MO": "Macau", "PS": "Palestine",
    "KN": "Saint Kitts and Nevis", "LC": "Saint Lucia", "VC": "Saint Vincent and the Grenadines",
    "PM": "Saint Pierre and Miquelon", "BL": "Saint Barthélemy", "MF": "Saint Martin",
    "SH": "Saint Helena, Ascension and Tristan da Cunha", "AG": "Antigua and Barbuda",
    "BA": "Bosnia and Herzegovina", "TT": "Trinidad and Tobago", "ST": "São Tomé and Príncipe",
    "TC": "Turks and Caicos Islands", "WF": "Wallis and Futuna", "HM": "Heard and McDonald Islands",
    "GS": "South Georgia and the South Sandwich Islands", "SJ": "Svalbard and Jan Mayen",
    "PN": "Pitcairn Islands", "VG": "British Virgin Islands", "VI": "United States Virgin Islands",
    "FM": "Federated States of Micronesia", "KP": "North Korea", "KR": "South Korea",
    "VA": "Vatican City", "CZ": "Czechia", "US": "United States", "GB": "United Kingdom",
    "BQ": "Caribbean Netherlands", "CW": "Curaçao", "AX": "Åland Islands",
    "IO": "British Indian Ocean Territory", "TF": "French Southern Territories",
}

# Names used by other sources that don't normalise to the ISO display name.
ALIASES = {
    "BN": ["Brunei Darussalam", "Brunei"], "CZ": ["Czech Republic"], "KG": ["Kyrgyz Republic"],
    "US": ["United States of America", "USA"], "BS": ["The Bahamas", "Bahamas"],
    "GM": ["The Gambia", "Gambia"], "TR": ["Turkiye", "Turkey"], "CV": ["Cabo Verde", "Cape Verde"],
    "SZ": ["Swaziland"], "MK": ["Macedonia"], "TL": ["East Timor"], "LA": ["Lao PDR"],
    "CD": ["Congo, Dem. Rep.", "DR Congo"], "CG": ["Congo, Rep.", "Congo"],
    "KR": ["South Korea (Republic of Korea)", "Korea, South"],
    "KP": ["North Korea (Democratic People's Republic of Korea)", "Korea, North"],
    "CI": ["Cote d'Ivoire", "Ivory Coast", "Côte d'Ivoire (Ivory Coast)"],
    "FM": ["Micronesia"], "VA": ["Holy See", "Vatican"], "PS": ["State of Palestine", "Palestinian Territories"],
    "MO": ["Macao", "Macao SAR"], "HK": ["Hong Kong SAR"], "RU": ["Russian Federation"], "SY": ["Syrian Arab Republic"],
    "VN": ["Viet Nam"], "IR": ["Iran, Islamic Republic of"], "MM": ["Burma"],
    "ST": ["Sao Tome and Principe"], "KN": ["St Kitts and Nevis", "St. Kitts and Nevis"],
    "LC": ["St Lucia", "St. Lucia"], "VC": ["St Vincent and the Grenadines", "St. Vincent and the Grenadines"],
}


def norm(name):
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    name = name.replace("&#039;", "'").replace("&", "and").lower()
    return re.sub(r"[^a-z0-9]+", "", name)


def slug(name):
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", name.replace("'", "")).strip("-")


def load_json(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def atlas_baseline():
    path = ATLAS / "assets" / "world-baseline.js"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    return json.loads(text[text.index("["):text.rindex("]") + 1])


def atlas_guides():
    folder = ATLAS / "countries"
    return {p.stem for p in folder.glob("*.html")} if folder.exists() else set()


def main():
    iso = load_json(ROOT / "data/sources/iso-regions.json", {})
    previous = {p["iso2"]: p for p in load_json(ROOT / "data/places/spine.json", {"places": []})["places"]}
    advisories = load_json(ROOT / "data/advisories.json", {"destinations": {}})["destinations"]
    baseline = atlas_baseline()
    guides = atlas_guides()

    places = []
    for code, iso_name in sorted(iso.items()):
        if code in SKIP or not re.fullmatch(r"[A-Z]{2}", code):
            continue
        name = DISPLAY.get(code, iso_name.replace(" & ", " and ").replace("St. ", "Saint "))
        kind = ("territory" if code in TERRITORIES else "associated" if code in ASSOCIATED
                else "jurisdiction" if code in JURISDICTIONS else "country")
        place = previous.get(code, {})
        place.update({
            "id": code.lower(),
            "slug": slug(name),
            "iso2": code,
            "name": name,
            "kind": kind,
            "aliases": sorted({iso_name, *ALIASES.get(code, [])} - {name}),
        })
        places.append(place)

    lookup = {}
    for place in places:
        for label in [place["name"], *place["aliases"]]:
            lookup[norm(label)] = place

    unmatched = {"advisories": [], "baseline": []}
    for key, record in advisories.items():
        place = lookup.get(norm(record["title"])) or lookup.get(norm(key.replace("-", " ")))
        if place:
            place["smartraveller"] = key
            place["region"] = record.get("region") or place.get("region")
        else:
            unmatched["advisories"].append(record["title"])
    for record in baseline:
        place = lookup.get(norm(record["name"]))
        if place:
            place["atlas_name"] = record["name"]
        else:
            unmatched["baseline"].append(record["name"])
    for place in places:
        guide = slug(place.get("atlas_name", place["name"]))
        if guide in guides:
            place["atlas_guide"] = guide

    out = {
        "note": "Every place stays selectable. Kind is a travel-planning label, not a position on status. The spine is a starting layer, not a limit: shards add any island, region, nation or zone.",
        "count": len(places),
        "places": places,
        "unmatched": unmatched,
    }
    (ROOT / "data/places").mkdir(parents=True, exist_ok=True)
    (ROOT / "data/places/spine.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    kinds = {}
    for p in places:
        kinds[p["kind"]] = kinds.get(p["kind"], 0) + 1
    print(f"{len(places)} places {kinds}; unmatched {unmatched}")


if __name__ == "__main__":
    main()
