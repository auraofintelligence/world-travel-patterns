---
name: travel-monthly-cycles
description: Monthly mapping of seasons, visitor flow, culture cycles, protocols and the year ahead for 25 places in world-travel-patterns
---

Monthly cycles pass for world-travel-patterns: how the year moves in each place.
Run start to finish on your own. Do not ask the user anything.
Repo: C:\Users\sbt41\githublocal\world-travel-patterns. Read its CLAUDE.md first; it is binding.

SCOPE · AUSTRALIA LIGHT PASS (rule from 2 November 2026)
International work is the priority. Australia gets a light pass only: state, territory and notable-region
level (Aboriginal land permits, major events in the user's categories, culture and respecting Country).
No council or ward depth (p4a.xyz covers that); don't duplicate p4a. Visa and work patterns don't apply
to an Australian citizen in Australia (they are skipped for au via skip_home); never invent data for them.

STEP 0 · STAMP THE CLOCK
Run exactly the clock command in routines/weekly-place-passes.md, Step 0. DATE is today.

STEP 1 · SYNC AND CHOOSE
    git pull --rebase
    python scripts/due.py
From queue/due.json, take the first 25 places that have any of these patterns due:
seasons-and-flow, culture-cycles, culture-and-protocol, year-ahead. Keep queue order.
Also take any place listed under not_covered in data/calendar/holidays-<this year>.json that has
no culture-cycles record yet, up to 10 more.

STEP 2 · MAP THE CYCLES
- seasons-and-flow: twelve months, each with season, hazard window (cyclone, monsoon, fire, snow)
  and visitor flow (peak, shoulder, quiet). National meteorological service and tourism statistics first.
- culture-cycles: the public holidays are already in data/calendar (a signal). Add the moving
  calendars for the next twelve months with real dates (lunar, Islamic, Hindu, Buddhist, Christian
  and others as they apply), major festivals, and community-declared closures from the community's
  own channel. Fill missing public holidays for not_covered places from official calendars.
- culture-and-protocol: the place's own names first, greetings, welcome and acknowledgement,
  sacred or restricted places, photography and story permissions, reciprocity, dress, who holds
  cultural authority. Optional GAJRA Earth thread: local words for joyful, responsible and abundance,
  and ideas that don't translate. Record what the place publishes, in its terms.
- year-ahead: dated elections, major events and scheduled rule changes for the next twelve months.
  A date must come from a source. Start from data/feeds (GAJRA Earth Ahead lists AI governance
  events and open doors by place), confirm each at its own source, then search for the rest.
Same evidence rules as the weekly routine: primary sources, today's DATE only on what you rechecked,
unknown when you can't establish it.

STEP 3 · LOOK FOR IMPROVEMENTS
Once a month, note in the run file: patterns that need a new field or topic, places the tree is
missing (islands, regions, nations with their own processes), sources that would make a pattern
machine-checkable, and wording that has aged. Add a new pattern file only when the same question
has come up in three or more places; otherwise propose it in the run note.

STEP 4 · CHECK AND COMMIT
    python scripts/validate.py
    python scripts/due.py
    python scripts/build_site.py
Write docs/runs/<DATE>-monthly.md, then commit and push as in the weekly routine.

STEP 5 · REPORT
One short paragraph: places mapped, notable cycles in the next three months (big festivals, wet
seasons, elections), proposed improvements.
