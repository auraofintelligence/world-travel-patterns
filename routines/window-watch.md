---
name: travel-window-watch
description: Daily self-gating watch for declared travel windows in world-travel-patterns; tightens vetting and refreshes the private visitor brief as a window approaches and while travelling
---

Daily travel window watch for world-travel-patterns.
Run start to finish on your own. Do not ask the user anything.
Repo: C:\Users\sbt41\githublocal\world-travel-patterns. Read its CLAUDE.md first; it is binding.

SCOPE · AUSTRALIA LIGHT PASS (rule from 2 November 2026)
International work is the priority. Australia gets a light pass only: state, territory and notable-region
level (Aboriginal land permits, major events in the user's categories, culture and respecting Country).
No council or ward depth (p4a.xyz covers that); don't duplicate p4a. Visa and work patterns don't apply
to an Australian citizen in Australia (they are skipped for au via skip_home); never invent data for them.
This routine runs on the local machine because it reads private/windows.json, which is never committed.

STEP 0 · STAMP THE CLOCK
Run exactly the clock command in routines/weekly-place-passes.md, Step 0. DATE is today.

STEP 1 · GATE
    git pull --rebase
    python scripts/due.py --private
Read private/queue.json. If no queue entry has a window field and no window ended in the last
14 days, stop here and report one line: "No travel window in range." That is a normal, cheap run.

STEP 2 · WORK BY PHASE
The phase sets the age limit, so the queue already holds only what is due. Phases:
- approach (from 90 days out, earlier when a permit lead time needs it): vet everything due on
  the window's places, their parents (laws stack) and any flagged zones inside them.
- countdown (30 days out) and imminent (7 days out): the same, with tighter age limits.
  Recheck every watch item touching these places.
- in-place (during the window): advisory, local law, zone requirements, culture cycles and the
  year ahead only. Look for anything published in the last few days.
- debrief (up to 14 days after): note what the brief got right, what it missed, and which places
  or patterns should be added. Mark findings ready to share.
Vet with the same rules as the weekly routine, but write results to private/findings/<window id>/
as vetting-format JSON, not to data/vetting, unless the window has "share": true. Public commits
must not show where the traveller is heading.

STEP 3 · SPECIAL PERMIT ZONE SCAN AND BRIEF
For each place in the window:
    python scripts/brief.py <place> --start <window start> --activities <window activities> --out private/briefs/<window id>-<place slug>.md
Read each brief's zone scan. For every zone layer with a lead time, check the latest safe start.
If a latest safe start is within 14 days, or already passed, put it first in the report.
Where a flagged zone shows not yet checked, vet zone-requirements for it today.
Read window_events in private/queue.json: feed events and open doors at the window's places.
An open door closing before or during the trip, and any event during it, go in the report, with
the activities check it would need (attending, speaking, filming) and whether that check is done.

STEP 4 · CHECK
    python scripts/validate.py
If the window shares, commit and push the public vetting as in the weekly routine. Otherwise commit
nothing: private/ is gitignored.

STEP 5 · REPORT
Lead with deadlines: any permit whose latest safe start is near or past, then open doors closing soon. Then the phase, the places
vetted, the gaps that remain, and any advice level or rule change touching the window.
