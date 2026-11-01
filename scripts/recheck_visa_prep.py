"""Apply hand-verified visa-preparation rechecks (data in scripts/visa_prep_rechecks.py). Stdlib only.

Each verified entry replaces the baseline text with what an official page said on the check date,
keeps the atlas provenance for history, moves unverified atlas extras under baseline_unverified,
and sets needs_recheck false. Entries marked flag=True keep needs_recheck true with a recheck_note.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import load_vetting, vetting_path, write  # noqa: E402
from visa_prep_rechecks import CHECKED, RECHECKS, SR  # noqa: E402


def apply(pid, spec):
    vet = load_vetting(pid)
    rec = vet["patterns"].get("visa-preparation", {})
    if spec.get("flag"):
        rec["recheck_note"] = spec["note"]
        rec["needs_recheck"] = True
        vet["patterns"]["visa-preparation"] = rec
        write(vetting_path(pid), vet)
        return "flagged"
    extras = {k: rec.pop(k) for k in ("host_unlock", "fastest_entry", "before_departure", "useful_stay", "documents", "steps") if k in rec}
    sources = [{"title": "Smartraveller travel advice: entry and exit", "authority": "Smartraveller, Australian Government",
                "url": SR[pid], "checked": CHECKED, "supports": "visa status, pre-arrival forms and border documents as read"}]
    sources += [{**s, "checked": CHECKED} for s in spec.get("sources", [])]
    rec.update({
        "status": "steps-found", "checked": CHECKED, "last_reviewed": CHECKED, "evidence": "official", "needs_recheck": False,
        "fastest_entry": spec["fastest_entry"], "before_departure": spec.get("before_departure"),
        "useful_stay": spec.get("useful_stay"), "steps": spec["steps"], "documents": spec["documents"],
        "fees": [{**f, "checked": CHECKED} for f in spec["fees"]], "sources": sources,
    })
    if "baseline_unverified" not in rec:
        rec["baseline_unverified"] = {"from": "Australian-visa-activity-atlas (see provenance); not reread at recheck", **extras}
    if spec.get("note"):
        rec["recheck_note"] = spec["note"]
    else:
        rec.pop("recheck_note", None)
    rec = {k: v for k, v in rec.items() if v is not None}
    vet["patterns"]["visa-preparation"] = rec
    write(vetting_path(pid), vet)
    return "verified"


def main(only=None):
    out = {}
    for pid, spec in RECHECKS.items():
        if only and pid not in only:
            continue
        out.setdefault(apply(pid, spec), []).append(pid)
    for k, v in out.items():
        print(f"{k}: {len(v)} ({', '.join(v)})")


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
