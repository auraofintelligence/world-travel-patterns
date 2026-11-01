"""Carry visa preparation steps and visa cost signals from Luke's Australian-visa-activity-atlas (read-only).

Writes the visa-preparation pattern for overseas places only. Every record is a baseline to recheck:
status imported (deep countries) or baseline-only (cost signal only), evidence legacy-baseline,
needs_recheck true, the atlas's ORIGINAL dates, and provenance (repo, commit, claim ids).
Never overwrites a record that has been rechecked (needs_recheck false) or is newer.
Needs Node and a sibling checkout: ../Australian-visa-activity-atlas.
Run: python scripts/import_visa_prep.py
"""
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, load_vetting, vetting_path, write  # noqa: E402
from build_places import norm  # noqa: E402
from import_atlas import iso  # noqa: E402

ATLAS = ROOT.parent / "Australian-visa-activity-atlas"
REPO = "https://github.com/auraofintelligence/Australian-visa-activity-atlas"
DUMP = """
const fs=require('fs'),vm=require('vm');const s={window:{}};vm.createContext(s);
for(const f of ['assets/data.js','assets/world-baseline.js'])vm.runInContext(fs.readFileSync(process.argv[1]+'/'+f,'utf8'),s);
process.stdout.write(JSON.stringify({atlas:s.window.ATLAS_DATA,baseline:s.window.WORLD_BASELINE}));
"""
HOME = "au"


def keep(existing, record):
    if not existing:
        return True
    if existing.get("needs_recheck") is False:
        return False
    return (existing.get("checked") or "") <= record["checked"]


def deep_record(country, commit):
    checks, launch = country["claimChecks"], country.get("launch", {})
    lc = checks.get("launch", {})
    claim = lambda node: {"id": node["id"], "checked": iso(node["checked"])} if node else None  # noqa: E731
    return {
        "status": "imported",
        "checked": iso(checks["steps"]["checked"]),
        "last_reviewed": iso(country["reviewed"]),
        "evidence": "legacy-baseline",
        "needs_recheck": True,
        "fastest_entry": launch.get("fastestEntry"),
        "before_departure": launch.get("beforeDeparture"),
        "useful_stay": launch.get("usefulStay"),
        "host_unlock": launch.get("hostUnlock"),
        "documents": launch.get("quickPacket", []),
        "steps": country.get("steps", []),
        "open_questions": country.get("cautions", []),
        "sources": [{"title": s["title"], "authority": s.get("authority"), "url": s["url"],
                     "checked": iso(s.get("checked")), "supports": s.get("supports")} for s in country.get("sources", [])],
        "provenance": {"repo": REPO, "commit": commit, "file": "assets/data.js", "country_id": country["id"],
                       "claims": {"steps": claim(checks.get("steps")), "open_questions": claim(checks.get("cautions")),
                                  **{k: claim(lc.get(v)) for k, v in [("fastest_entry", "fastestEntry"),
                                     ("before_departure", "beforeDeparture"), ("useful_stay", "usefulStay"),
                                     ("host_unlock", "hostUnlock"), ("documents", "quickPacket")]}}},
    }


def main():
    data = json.loads(subprocess.check_output(["node", "-e", DUMP, str(ATLAS)], encoding="utf-8"))
    commit = subprocess.check_output(["git", "-C", str(ATLAS), "rev-parse", "HEAD"], encoding="utf-8").strip()
    places = load_places()
    lookup = {}
    for p in places.values():
        if p["kind"] in ("country", "territory", "associated", "jurisdiction"):
            for label in [p["name"], *p.get("aliases", []), p.get("atlas_name", "")]:
                if label:
                    lookup[norm(label)] = p["id"]
    costs = {}
    for b in data["baseline"]:
        pid = lookup.get(norm(b["name"]))
        if pid and pid != HOME:
            costs[pid] = b
    deep = cost_only = skipped = 0
    missing = []
    done = set()
    for country in data["atlas"]["countries"]:
        pid = lookup.get(norm(country["name"]))
        if not pid:
            missing.append(country["name"]); continue
        if pid == HOME:
            continue
        record = deep_record(country, commit)
        b = costs.get(pid)
        if b:
            record["cost_aud_baseline"] = {"value": b.get("estimatedCostAud"), "checked": iso(b.get("costReviewed")),
                                           "claim_id": b.get("costClaimId")}
        vet = load_vetting(pid)
        if keep(vet["patterns"].get("visa-preparation"), record):
            vet["patterns"]["visa-preparation"] = record
            write(vetting_path(pid), vet); deep += 1
        else:
            skipped += 1
        done.add(pid)
    for pid, b in costs.items():
        if pid in done or not b.get("costReviewed"):
            continue
        record = {"status": "baseline-only", "checked": iso(b["costReviewed"]), "last_reviewed": iso(b["costReviewed"]),
                  "evidence": "legacy-baseline", "needs_recheck": True,
                  "entry_summary": b.get("entrySummary"),
                  "cost_aud_baseline": {"value": b.get("estimatedCostAud"), "checked": iso(b["costReviewed"]),
                                        "claim_id": b.get("costClaimId")},
                  "steps": [], "documents": [],
                  "provenance": {"repo": REPO, "commit": commit, "file": "assets/world-baseline.js",
                                 "claims": {"entry_summary": b.get("entryClaimId"), "cost": b.get("costClaimId")},
                                 "upstream": "https://github.com/auraofintelligence/Australian-world-travel"}}
        vet = load_vetting(pid)
        if keep(vet["patterns"].get("visa-preparation"), record):
            vet["patterns"]["visa-preparation"] = record
            write(vetting_path(pid), vet); cost_only += 1
        else:
            skipped += 1
    print(f"visa-preparation: {deep} with steps, {cost_only} cost-only baselines, {skipped} kept (newer or rechecked).")
    unmatched = [b["name"] for b in data["baseline"] if not lookup.get(norm(b["name"]))]
    if missing or unmatched:
        print("No place for:", ", ".join(missing + unmatched))


if __name__ == "__main__":
    main()
