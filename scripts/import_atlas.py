"""Seed vetting records from the Australian Visa and Activity Atlas (read-only, one-off or on demand).

Carries each claim with its ORIGINAL checked date and claim id, so ages stay true.
Never overwrites a record that is newer than the atlas claim.
Needs Node (to evaluate the atlas's data.js) and ../Australian-visa-activity-atlas.
"""
import datetime
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, load_vetting, vetting_path, write  # noqa: E402
from build_places import norm  # noqa: E402

ATLAS = ROOT.parent / "Australian-visa-activity-atlas"
DUMP = """
const fs=require('fs'),vm=require('vm');const s={window:{}};vm.createContext(s);
for(const f of ['assets/data.js','assets/world-baseline.js'])vm.runInContext(fs.readFileSync(process.argv[1]+'/'+f,'utf8'),s);
process.stdout.write(JSON.stringify({atlas:s.window.ATLAS_DATA,baseline:s.window.WORLD_BASELINE}));
"""


def iso(value):
    return datetime.datetime.strptime(value.strip(), "%d %B %Y").date().isoformat() if value else None


def keep(existing, record):
    return not existing or (existing.get("checked") or "") < record["checked"]


def main():
    data = json.loads(subprocess.check_output(["node", "-e", DUMP, str(ATLAS)], encoding="utf-8"))
    places = load_places()
    lookup = {}
    for p in places.values():
        if p["kind"] in ("country", "territory", "associated", "jurisdiction"):
            for label in [p["name"], *p.get("aliases", []), p.get("atlas_name", "")]:
                if label:
                    lookup[norm(label)] = p["id"]
    provenance = "Australian-visa-activity-atlas"
    written = deep = 0

    deep_ids = set()
    for country in data["atlas"]["countries"]:
        pid = lookup.get(norm(country["name"]))
        if not pid:
            print("No place for", country["name"]); continue
        deep_ids.add(pid)
        checks = country["claimChecks"]
        sources = [{"title": s["title"], "authority": s.get("authority"), "url": s["url"], "checked": iso(s.get("checked")),
                    "supports": s.get("supports")} for s in country.get("sources", [])]
        vet = load_vetting(pid)
        entry = {"status": "imported", "summary": country.get("entrySnapshot"),
                 "pre_arrival": country.get("launch", {}).get("beforeDeparture"),
                 "max_stay": country.get("launch", {}).get("usefulStay"),
                 "checked": iso(checks["entrySnapshot"]["checked"]), "evidence": "official",
                 "sources": sources, "provenance": {"repo": provenance, "claim_id": checks["entrySnapshot"]["id"]}}
        if keep(vet["patterns"].get("entry"), entry):
            vet["patterns"]["entry"] = entry
        acts = vet["patterns"].get("activities", {"activities": {}})
        for activity, path in country.get("pathways", {}).items():
            claim = checks["pathways"][activity]["status"]
            record = {"status": path.get("status"), "route": path.get("route"), "detail": path.get("detail"),
                      "next": path.get("next"), "checked": iso(claim["checked"]),
                      "provenance": {"repo": provenance, "claim_id": claim["id"]}}
            if keep(acts["activities"].get(activity), record):
                acts["activities"][activity] = record
        dates = [a["checked"] for a in acts["activities"].values()]
        acts.update({"status": "imported", "checked": min(dates), "evidence": "official", "sources": sources,
                     "note": "checked is the oldest activity date; each activity keeps its own."})
        vet["patterns"]["activities"] = acts
        write(vetting_path(pid), vet); written += 1; deep += 1

    for record in data["baseline"]:
        pid = lookup.get(norm(record["name"]))
        if not pid or pid in deep_ids:
            continue
        vet = load_vetting(pid)
        entry = {"status": "imported", "summary": record.get("entrySummary"), "checked": iso(record.get("baselineVisaReviewed")),
                 "evidence": "legacy-baseline", "provenance": {"repo": provenance, "claim_id": record.get("entryClaimId")},
                 "note": "First-pass triage carried from Australian World Travel; recheck against the official source."}
        if record.get("entrySourceUrl"):
            entry["sources"] = [{"title": record.get("entrySourceTitle"), "url": record["entrySourceUrl"], "checked": entry["checked"]}]
        cost = {"status": "noted", "daily_cost_aud": None, "visa_cost_signal": record.get("estimatedCostAud"),
                "checked": iso(record.get("costReviewed")), "evidence": "legacy-baseline",
                "provenance": {"repo": provenance, "claim_id": record.get("costClaimId")}}
        if keep(vet["patterns"].get("entry"), entry):
            vet["patterns"]["entry"] = entry
        if keep(vet["patterns"].get("money-and-cost"), cost):
            vet["patterns"]["money-and-cost"] = cost
        write(vetting_path(pid), vet); written += 1
    print(f"{written} places seeded ({deep} with deep activity guides)")


if __name__ == "__main__":
    main()
