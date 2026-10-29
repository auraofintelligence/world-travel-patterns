# World Travel Patterns

🤝🔷 **A Luke × Claude build.** Created by Luke Nathan Hayes (`auraofintelligence`) and Claude (Opus 5.5) on 30 October 2026. Not a Codex build.

Every place an Australian passport holder might visit, vetted with the same simple, repeatable patterns: so local laws aren't broken by accident, and local culture is met on its own terms.

## What's in it

- **A place tree that keeps growing.** 248 countries, territories and separately travelled jurisdictions form the spine. Underneath sit Australia's 2,088 states, councils, wards and electorates (from [P4A](https://auraofintelligence.github.io/p4a-xyz-cinema/)), the 50 US states and DC, plus islands, island groups, nations and permit zones such as Rapa Nui, Bougainville, the Torres Strait Islands and the APY Lands. That's 2,409 places today, with no upper limit. Each country gets its own folder, so a country broken down to council level is just a bigger folder.
- **Thirteen patterns.** Each is one question asked the same way everywhere: advice level, entry, activities, special permit zones, health entry, local law, culture and protocol, culture cycles, seasons and visitor flow, the year ahead, consular reach, money, and works and purpose. See [patterns/README.md](patterns/README.md). Adding a pattern is one file.
- **Laws and protocols that stack.** A visitor is bound by every level at once. A brief for Minjerribah shows Australia, then Queensland, then Redland City, then the island, each with its own laws and protocols, or "not yet checked".
- **A special permit zone scan.** It walks down into any flagged zone and up to the country, so a national visa is never mistaken for permission to enter a zone. Each permit's lead time is counted back from the travel date to give a latest safe start.
- **Feedstock from your other work.** [GAJRA Earth Ahead](https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html)'s upcoming AI governance events and open doors (62 entries, 31 doors on 30 October 2026) are mapped onto the tree daily. Briefs and the window watch show which fall before or during a trip. See [data/feeds/README.md](data/feeds/README.md).
- **Honest ages.** Records carried from the earlier [Visa and Activity Atlas](https://auraofintelligence.github.io/Australian-visa-activity-atlas/) keep their original dates, so the queue knows exactly what's stale.

## How it runs

Two modes. **Baseline** runs all year and maps each place's laws, seasons, culture cycles and year. **Window** mode tightens everything for declared trips.

| Job | Runs | Where | What it does |
| --- | --- | --- | --- |
| Daily advisories | 06:00 every day | GitHub Actions | Smartraveller levels for every destination; opens an issue when one changes |
| Weekly source watch | Monday 05:00 | GitHub Actions | Checks every cited page is still there and whether its text changed |
| Daily feeds | 08:45 every day | GitHub Actions | GAJRA Earth Ahead events and open doors, mapped to places |
| Monthly calendars | 1st of the month | GitHub Actions | Public holidays for this year and next, for the 204 places the dataset covers |
| Weekly place passes | Weekly | Claude routine | Vets the next seven places from official sources |
| Monthly cycles | Monthly | Claude routine | Seasons, moving calendars, festivals, protocols and dated events for 25 places |
| Window watch | Daily, exits fast when no trip is near | Claude routine, this machine | Tightens vetting and refreshes the private visitor brief as a trip approaches |

All times are Brisbane time.

Window phases, from `config/cadence.json`:

| Phase | Starts | Age limit for any record |
| --- | --- | --- |
| Approach | 90 days out, or earlier when a permit's lead time needs it | 30 days |
| Countdown | 30 days out | 7 days |
| Imminent | 7 days out | 2 days |
| In place | During the trip | 1 day (law, zones, calendars, advice) |
| Debrief | Up to 14 days after | Record what was learned |

The Actions treat every place the same, so the public history never shows where a trip is heading. Travel windows live in `private/`, which git ignores.

## Where it stands

As at 30 October 2026, 201 places carry records from the earlier atlas: 36 with deep activity guides, the rest with first-pass entry notes from August 2025. The queue holds 279 place passes and 2,913 pattern checks, with dead sources and the Thailand rule change first. At seven places a week, the first full pass takes about 40 weeks. Window mode jumps any trip's places to the front.

## Use it

```text
python scripts/brief.py cl/rapa-nui --start 2027-03-01 --activities tourism,filming
python scripts/due.py
python scripts/validate.py
```

To declare a trip, copy `examples/windows.example.json` to `private/windows.json`. To add a place, see [data/places/README.md](data/places/README.md).

Everything is Python standard library: no installs.

## Licence

[Strange But True Public Source Licence](LICENCE.md). Non-commercial use is welcome with credit; commercial rights are reserved.

---

🤝🔷 Luke × Claude · world-travel-patterns
