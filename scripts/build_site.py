"""Build site/data/index.json, the compact index the website reads.

The website reads vetting records, feeds and advisories straight from data/, and uses this index
for the place tree, freshness, pattern coverage and the run list. It never reads private/.
Run after due.py: python scripts/build_site.py
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, VETTING, applies, is_active, load_patterns, load_places, read, today  # noqa: E402


def main():
    places, patterns = load_places(), load_patterns()
    queue = read(ROOT / "queue/due.json", {"summary": {}, "queue": []})
    due = {entry["place"]: entry["due"] for entry in queue["queue"]}
    vetted = {read(p)["place"]: read(p)["patterns"] for p in VETTING.glob("*.json")}
    agent = [p for p in patterns.values() if p["method"] != "machine"]

    rows = []
    for pid, p in places.items():
        own = vetted.get(pid, {})
        applicable = [pat["id"] for pat in agent if applies(pat, p) and not (pat.get("skip_home") and pid == "au")]
        due_here = {d["pattern"]: d["reason"] for d in due.get(pid, [])}
        fresh = [x for x in applicable if x in own and x not in due_here]
        row = {
            "id": pid, "name": p["name"], "kind": p["kind"], "parent": p.get("parent"),
            "tags": p.get("tags", []), "zone": bool(p.get("zone_scan")), "overlay": bool(p.get("overlay")),
            "region": p.get("region"), "aliases": p.get("aliases", [])[:4], "children": len(p["children"]),
            "active": is_active(p), "smartraveller": p.get("smartraveller"), "p4a": (p.get("p4a_url") or "").replace("https://auraofintelligence.github.io/p4a-xyz-cinema/", "") or None,
            "applicable": len(applicable), "records": len([x for x in applicable if x in own]),
            "fresh": len(fresh), "due": due_here, "vetted": pid in vetted, "sk": p.get("source_kind"),
        }
        rows.append({k: v for k, v in row.items() if v not in (None, [], {}, False) or k in ("records", "fresh")})

    coverage = {}
    for pat in agent:
        targets = [r for r in rows if r.get("active") and applies(pat, places[r["id"]])]
        coverage[pat["id"]] = {"active_places": len(targets),
                               "with_record": sum(1 for r in targets if pat["id"] in vetted.get(r["id"], {})),
                               "fresh": sum(1 for r in targets if pat["id"] in vetted.get(r["id"], {}) and pat["id"] not in r.get("due", {}))}

    runs = sorted((p.name for p in (ROOT / "docs/runs").glob("*.md")), reverse=True)
    out = ROOT / "site/data/index.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "built_on": today().isoformat(),
        "counts": {"places": len(rows), "spine": sum(1 for r in rows if "/" not in r["id"]),
                   "active": sum(1 for r in rows if r.get("active")), "patterns": len(patterns),
                   "with_records": len(vetted)},
        "queue_summary": queue.get("summary", {}),
        "next": [{"place": e["place"], "name": e["name"], "due": len(e["due"]),
                  "reasons": sorted({d["reason"] for d in e["due"]})} for e in queue["queue"][:24]],
        "watch_checks": queue.get("watch_checks", []),
        "patterns": [dict(p, coverage=coverage.get(p["id"])) for p in patterns.values()],
        "places": rows,
        "runs": runs,
        "has_change_log": (ROOT / "data/logs/advisory-changes.jsonl").exists(),
    }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"site index: {len(rows)} places, {len(runs)} run notes")


if __name__ == "__main__":
    main()
