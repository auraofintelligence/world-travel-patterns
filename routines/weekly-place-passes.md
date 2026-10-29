---
name: travel-weekly-place-passes
description: Weekly vetting of the next seven places in the world-travel-patterns queue, from official sources, committed with a dated run note
---

Weekly place passes for world-travel-patterns.
Run start to finish on your own. Do not ask the user anything.
Repo: C:\Users\sbt41\githublocal\world-travel-patterns. Read its CLAUDE.md first; it is binding.

STEP 0 · STAMP THE CLOCK
Run exactly this, nothing else (it is allowlisted; other forms have stalled unattended runs):

    python -c "from datetime import datetime,timezone,timedelta; u=datetime.now(timezone.utc); b=u+timedelta(hours=10); print('UTC:',u.strftime('%Y-%m-%d %H:%M')); print('Brisbane:',b.strftime('%A %d %B %Y %H:%M')); print('DATE:',b.strftime('%Y-%m-%d')); print('STAMP:',b.strftime('%H:%M')+' Brisbane (UTC+10)')"

The DATE line is today for every checked field in this run.

STEP 1 · SYNC AND QUEUE
    git pull --rebase
    python scripts/due.py
Read queue/due.json. Take watch_checks first, then the first 7 place passes in queue order.
The queue order already puts dead or changed sources, watched rule changes, home and tagged
places first. Do not reorder it by advice level: advice is information, never exclusion.

STEP 2 · VET EACH PLACE PASS
For each place, work through every pattern listed as due:
- Read the pattern file in patterns/ for its question, fields, statuses and rules.
- Answer from primary sources: the government, authority or community that owns the rule.
  Organiser, airline, blog and aggregator pages are signals: label them, never cite them as the rule.
- Write the result into data/vetting/<id>.json (id with "/" replaced by "__"), using the record
  format in CLAUDE.md. Give every record today's DATE as checked, its sources, and the evidence level.
- Only date what you actually rechecked. For activities, each activity keeps its own checked date.
- If a source can't be reached, keep the old record and its old date. A failed fetch is not a change.
- If you can't establish the answer, write status unknown or confirm-in-writing and say who confirms.
  Never fill a gap with a guess. Unvetted is not permitted.
- Local law and culture stack: vet the level you were given, and don't copy a parent's laws down.
- Culture and protocol: record the place's own published guidance and its own names, in its terms.
  Where nothing is published, the status is ask-locally, with who to ask. Describe; don't lecture.
- year-ahead and works-and-purpose: read data/feeds for events at the place. A feed entry is a lead;
  confirm the date at its source before writing it as a year-ahead event, and keep the feed name in sources.
- Watch items: if the effective date has passed and an official source confirms the new rule,
  update the affected claims and set the item to resolved. Otherwise update its checked date and next step.

STEP 3 · GROW THE TREE WHERE THE WORK SHOWS IT
If vetting finds a zone, island or community inside the place with its own process (a permit,
a land council, a restricted area), add it to data/places/<iso>/extra.json with zone_scan true and a
why. That is how the tree grows. Don't add places without a reason.

STEP 4 · CHECK AND COMMIT
    python scripts/validate.py
    python scripts/due.py
    python scripts/build_site.py
Write docs/runs/<DATE>-weekly.md: the places done, every status that changed (old to new) at the top,
sources that moved, gaps left, and any improvement worth surfacing (a new source, a pattern topic
that keeps coming up, a better word). Then:
    git add -A data docs queue patterns site/data
    git commit -m "Weekly place passes <DATE>"
    git push
Commit only when validate passes. Never commit anything under private/.

STEP 5 · REPORT
One short paragraph in the app: places vetted, status changes, gaps, and the next places in the queue.
