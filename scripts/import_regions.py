"""Add every country's first-level regions (states, provinces, regions) to the place tree.

Reads data/sources/iso-3166-2-first-level.json (from Wikidata: each country's first-level divisions that carry an
ISO 3166-2 code) and writes data/places/<country>/regions.json. A region already in the tree, matched by Wikidata
ID or by name within its country, is left where it is.

    python scripts/import_regions.py
"""
import json
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import PLACES, ROOT, read  # noqa: E402

WHY = "First-level region: its own laws, languages and seasons can differ from the country's."


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]", "", s)


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def main():
    src = read(ROOT / "data/sources/iso-3166-2-first-level.json")
    spine = {p["id"] for p in read(PLACES / "spine.json")["places"]}
    existing, taken = {}, set()
    for shard in sorted(PLACES.glob("*/*.json")):
        if shard.name == "regions.json":
            continue
        for p in read(shard)["places"]:
            cc = p["id"].split("/")[0]
            taken.add(p["id"])
            existing.setdefault(cc, set()).add(norm(p["name"]))
            if p.get("wikidata"):
                existing[cc].add(p["wikidata"])
    by_cc = {}
    for r in src["regions"]:
        cc = r["country"]
        if cc not in spine:
            continue
        known = existing.get(cc, set())
        bare = re.sub(r"\b(prefecture|province|region|state|district|county|governorate|department|oblast|municipality)\b", "", r["name"], flags=re.I)
        if r["wikidata"] in known or norm(r["name"]) in known or norm(bare) in known:
            continue
        pid = f"{cc}/{slug(r['name'])}"
        if pid in taken:
            pid = f"{cc}/{slug(r['name'])}-{r['iso_3166_2'].split('-')[-1].lower()}"
        taken.add(pid)
        by_cc.setdefault(cc, []).append({"id": pid, "name": r["name"], "kind": "region", "source_kind": "first-level", "parent": cc,
                                         "iso_3166_2": r["iso_3166_2"], "wikidata": r["wikidata"], "why": WHY})
    total = 0
    for cc, rows in sorted(by_cc.items()):
        rows.sort(key=lambda p: p["name"])
        (PLACES / cc).mkdir(exist_ok=True)
        (PLACES / cc / "regions.json").write_text(json.dumps({
            "rule": "First-level regions from ISO 3166-2 (via Wikidata). Rerun scripts/import_regions.py to refresh; hand additions go in extra.json.",
            "places": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        total += len(rows)
    print(f"regions: {total} added across {len(by_cc)} countries")


if __name__ == "__main__":
    main()
