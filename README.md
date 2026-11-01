# World Travel Patterns

🤝🔷 **A Luke × Claude build.** Created by Luke Nathan Hayes (`auraofintelligence`) and Claude (Opus 5.5) on 30 October 2026. Not a Codex build.

Every place an Australian passport holder might visit, vetted with the same simple, repeatable patterns: so local laws aren't broken by accident, and local culture is met on its own terms.

## The website

Nine pages on GitHub Pages: home, places, a page for every place, patterns, upcoming, advisories, queue, how it works and a site map linking the related projects. Each page leads with a large, openly licensed photograph (credits on the site map). A place page shows a photograph of that place, or of somewhere inside it with a label saying so, or none: 316 places have one so far, all awaiting review. Places whose imagery belongs to a community's own cultural authority get no automatic photo. The site reads the same data the scripts and routines write, so it updates with every commit. Preview locally with `python -m http.server` in this folder, then open `index.html`.

## What's in it

- **A place tree that keeps growing.** 248 countries, territories and separately travelled jurisdictions form the spine. Underneath sit Australia's 2,088 states, councils, wards and electorates, the 50 US states and DC, plus islands, island groups, nations and permit zones such as Rapa Nui, Bougainville, the Torres Strait Islands and the APY Lands. That's 2,409 places today, with no upper limit. Each country gets its own folder, so a country broken down to council level is just a bigger folder.
- **Fifteen patterns.** Each is one question asked the same way everywhere: advice level, entry, activities, special permit zones, health entry, local law, culture and protocol, affection and relationships, psychoactive substances, culture cycles, seasons and visitor flow, the year ahead, consular reach, money, and works and purpose. See [patterns/README.md](patterns/README.md). Adding a pattern is one file.
- **Laws and protocols that stack.** A visitor is bound by every level at once. A brief for Minjerribah shows Australia, then Queensland, then Redland City, then the island, each with its own laws and protocols, or "not yet checked".
- **A special permit zone scan.** It walks down into any flagged zone and up to the country, so a national visa is never mistaken for permission to enter a zone. Each permit's lead time is counted back from the travel date to give a latest safe start.
- **Feedstock from your other work.** [GAJRA Earth Ahead](https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html)'s upcoming AI governance events and open doors (62 entries, 31 doors on 30 October 2026) are mapped onto the tree daily. Briefs and the window watch show which fall before or during a trip. See [data/feeds/README.md](data/feeds/README.md).
- **Embassies both ways.** Consular reach for all 179 Smartraveller destinations is read from each page's consular contacts: 87 with an Australian post in place, 74 served from a neighbour (sometimes with an honorary consul in place), and 18 through Canada's partner arrangement. Each country's own embassies and consulates in Australia (520 offices for 168 places, from the reviewed DFAT Protocol directory in [aura-horn-torus](https://github.com/auraofintelligence/aura-horn-torus)) show on its page as where to apply for a visa or ask for a rule in writing. See `data/missions/`.
- **Honest ages.** Records carried from the earlier [Visa and Activity Atlas](https://auraofintelligence.github.io/Australian-visa-activity-atlas/) keep their original dates, so the queue knows exactly what's stale.

## How it runs

Two modes. **Baseline** runs all year and maps each place's laws, seasons, culture cycles and year. **Window** mode tightens everything for declared trips.

| Job | Runs | Where | What it does |
| --- | --- | --- | --- |
| Daily advisories | 06:00 every day | GitHub Actions | Smartraveller levels for every destination; opens an issue when one changes |
| Weekly source watch | Monday 05:00 | GitHub Actions | Checks every cited page is still there and whether its text changed |
| Daily feeds | 08:45 every day | GitHub Actions | GAJRA Earth Ahead events and open doors, mapped to places |
| Monthly calendars | 1st of the month | GitHub Actions | Public holidays for this year and next, for the 204 places the dataset covers; place photos; consular reach for every destination |
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

On 31 October 2026, 267 places had records checked that day:

| Pattern | Places checked 31 October 2026 |
| --- | --- |
| Entry | 247 (every spine place but home): 99 visa-free, 28 visa on arrival, 21 e-visa, 14 travel authorisation, 29 visa required, 56 confirm in writing |
| Local law | 179 |
| Consular reach | 179 |
| Money | 173 |
| Culture and protocol | 93 |
| Health entry | 74 (yellow fever) |
| Special permit zones | 25, including Minjerribah, the Torres Strait, the APY Lands, NT and WA Aboriginal land, Gwaii Haanas, Tokelau and Pitcairn |

"Confirm in writing" means no official page could be read that day; each record names who to ask. The queue holds 280 place passes and 1,980 pattern checks, none of them for dead sources. Activities, seasons, culture cycles and the year ahead are the next layers. Run notes are in [docs/runs/](docs/runs/). At seven places a week, the first full pass takes about 40 weeks. Window mode jumps any trip's places to the front.

## Use it

```text
python scripts/brief.py cl/rapa-nui --start 2027-03-01 --activities tourism,filming
python scripts/due.py
python scripts/validate.py
```

To declare a trip, copy `examples/windows.example.json` to `private/windows.json`. To add a place, see [data/places/README.md](data/places/README.md).

Everything is Python standard library: no installs.

## Search discovery

`robots.txt` documents scoped search and training preferences: search crawlers (including OAI-SearchBot and Claude-SearchBot) are allowed; training crawlers (GPTBot, ClaudeBot, Google-Extended) are not. `sitemap.xml` lists the real public pages, including a page per country, territory and checked place, and `llms.txt` is a voluntary guide; `scripts/build_site.py` rewrites both. GitHub project Pages can't set the origin-root crawler policy, so `.github/robots-root-snippet.txt` is a scoped addition for the account-root `robots.txt` when authorised. The snippet was merged into the account-root policy on 1 November 2026. Discovery grants no additional reuse or AI-training rights.

## Licence

[Strange But True Public Source Licence](LICENCE.md). Non-commercial use is welcome with credit; commercial rights are reserved.

---

🤝🔷 Luke × Claude · world-travel-patterns
