"""Import Australia's governance tree from p4a-xyz-cinema into data/places/au/p4a-governance.json.

Reads ../p4a-xyz-cinema/content/places/route-registry.json (read-only) and keeps p4a's own ids,
prefixed "au/", so a place here and its P4A page always line up.

Travel inheritance runs country -> state -> council -> ward. Electorates overlap that chain,
so they hang off their state as overlays: they carry election and works patterns, never
permission inheritance.
"""
import hashlib
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, write  # noqa: E402

SOURCE = ROOT.parent / "p4a-xyz-cinema" / "content" / "places" / "route-registry.json"
P4A_SITE = "https://auraofintelligence.github.io/p4a-xyz-cinema/"
STATES = {"act": "Australian Capital Territory", "nsw": "New South Wales", "nt": "Northern Territory",
          "qld": "Queensland", "sa": "South Australia", "tas": "Tasmania", "vic": "Victoria", "wa": "Western Australia"}
KINDS = {"council": "district", "ward": "district", "unincorporated-area": "district", "special-local-body": "district",
         "federal-division": "electorate", "state-district": "electorate", "state-region": "electorate",
         "senate-area": "electorate", "statewide-upper-house": "electorate"}


def main():
    raw = SOURCE.read_bytes()
    registry = json.loads(raw.decode("utf-8-sig"))
    places = [{"id": f"au/{code}", "name": name, "kind": "state", "parent": "au", "tags": ["p4a-xyz"],
               "p4a_url": f"{P4A_SITE}states/{code}/index.html"} for code, name in STATES.items()]
    for record in registry["places"]:
        kind = KINDS[record["kind"]]
        parent = f"au/{record['parentId']}" if record.get("parentId") else f"au/{record['jurisdiction']}"
        place = {"id": f"au/{record['id']}", "name": record["name"], "kind": kind, "parent": parent,
                 "source_kind": record["kind"], "p4a_url": P4A_SITE + record["url"]}
        if kind == "electorate":
            place["overlay"] = True
        places.append(place)
    write(ROOT / "data/places/au/p4a-governance.json", {
        "generated_by": "scripts/import_p4a_au.py",
        "source": "p4a-xyz-cinema/content/places/route-registry.json",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "source_updated": registry.get("implementationUpdated"),
        "rule": "Generated. Re-run the importer instead of hand-editing. Hand additions go in data/places/au/extra.json.",
        "places": places,
    })
    print(f"{len(places)} Australian governance places from p4a ({registry.get('implementationUpdated')})")


if __name__ == "__main__":
    main()
