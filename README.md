# World Travel Patterns

🤝🔷 **A Luke × Claude, Codex and Grok build.** Created by Luke Nathan Hayes (`auraofintelligence`) with Claude (Opus 5.5) on 30 October 2026, and built on from November 2026 with Codex and Grok, each in the lanes Luke directs.

A growing, source-linked research system for Australian passport holders: not just where to travel, but how to arrive lawfully, respect local culture, participate in activities, stay longer, establish enterprises and develop meaningful connections with places around the world.

The same repeatable questions are asked at the level where the answer belongs. Unchecked information stays visibly unknown. National permission does not override local law or community consent.

**README reviewed 25 November 2026. Coverage snapshot: 24 November 2026.**

## Explore the website

[Open World Travel Patterns](https://auraofintelligence.github.io/world-travel-patterns/)

| Page | What it does |
| --- | --- |
| [Home](https://auraofintelligence.github.io/world-travel-patterns/) | Search places, explore the research layers and see advisory summaries and recent changes |
| [Places](https://auraofintelligence.github.io/world-travel-patterns/places.html) | Browse and search the worldwide place tree |
| [Place pages](https://auraofintelligence.github.io/world-travel-patterns/place.html?id=fj) | Individual dossiers, applicable levels, dated sources, permits, law repositories, consular contacts and related places |
| [Patterns](https://auraofintelligence.github.io/world-travel-patterns/patterns.html) | Explore the research questions, inheritance, evidence and coverage |
| [Upcoming](https://auraofintelligence.github.io/world-travel-patterns/upcoming.html) | Dated events, elections, consultations and other opportunities mapped to places |
| [Advisories](https://auraofintelligence.github.io/world-travel-patterns/advisories.html) | Smartraveller advice levels, changes and last successful check |
| [Queue](https://auraofintelligence.github.io/world-travel-patterns/queue.html) | Research priorities, stale records, watched rules, source issues and run notes |
| [How it works](https://auraofintelligence.github.io/world-travel-patterns/how.html) | Evidence principles, inheritance, permits, data structures and research method |
| [Your view](https://auraofintelligence.github.io/world-travel-patterns/view.html) | Browser-local preferences for patterns, individual topics, relationship relevance, drone photography and ancient-site lore |
| [Site map](https://auraofintelligence.github.io/world-travel-patterns/site-map.html) | Country links, related projects and photograph credits |

The website is a static GitHub Pages application with nine main navigation pages and one reusable place-page template. It reads structured data from the repository. Every place has a stable address, for example [Minjerribah](https://auraofintelligence.github.io/world-travel-patterns/place.html?id=au%2Fminjerribah) or [Rapa Nui](https://auraofintelligence.github.io/world-travel-patterns/place.html?id=cl%2Frapa-nui).

Your view changes presentation, not the underlying research. Preferences are stored in the browser, not a public profile. Hiding a topic does not remove a legal obligation. Drone-specific material is collected even when its display is switched off.

## The worldwide place tree

The 24 November 2026 generated report records:

| Measure | Current snapshot |
| --- | ---: |
| Countries, territories and separately travelled jurisdictions | 248 |
| States, provinces and regions | 3,597 |
| Other places, including councils, wards, electorates, islands, nations, permit zones and sites | 2,123 |
| **Total places** | **5,968** |
| Places with at least one record | 1,658 |
| Research patterns | 29 |
| Pattern records | 8,704 |
| Individual rules, layers, events, sites and checks | 18,459 |

The place tree is extensible, not limited to a country list. ISO 3166-2 regions, Australian governance geography, the US states and DC, and individually researched islands, Indigenous nations, permit zones and heritage sites coexist in the same structure. Country folders contain their own subdivisions; overlapping governance geography is explicitly represented where appropriate.

See [the place data](data/places/) and [adding a place](data/places/README.md). The generated status report is the authoritative count; older explanatory documents may retain historical figures.

## The 29 research patterns

Each pattern defines its question, scope, fields, evidence rules, inheritance and recheck age. The JSON definitions in [patterns/](patterns/) are the machine-readable source of truth.

| Research family | Patterns |
| --- | --- |
| Travel advice | Safety advice level |
| Permission and preparation | Entry, visa preparation, activity permission, health entry, special permit zones |
| Law | Local law for visitors, Australian law that travels with you, drone pilot and legal footage pathways |
| Culture and language | Culture and protocol, languages, culture cycles |
| Relationships and family | Affection and relationships, births and family support |
| Substances | Psychoactive substances, including alcohol, tobacco, vaping, medical and ceremonial contexts |
| Time and seasons | Seasons and visitor flow, year ahead |
| History and exploration | Ancient sites and mysteries |
| Practical needs | Consular reach, money and cost |
| Long-term stay and enterprise | Digital residency, physical residency, citizenship, enterprise establishment, collective ownership, financial infrastructure, intellectual property, research and enterprise opportunities |
| Personal project alignment | Works and purpose fit |

### Residency, citizenship and enterprise

The eight country-first patterns added on 24 November extend the system beyond ordinary travel and visa permission.

| Pattern | What is researched | Country/territory coverage, excluding Australia |
| --- | --- | ---: |
| Digital residency | E-residency, digital identity, electronic signatures and renewal | 243/247 |
| Physical residency | Temporary and permanent residence, presence requirements and cost signals | 243/247 |
| Citizenship | Naturalisation, descent, dual citizenship and restrictions | 243/247 |
| Enterprise establishment | Companies, subsidiaries, foreign ownership and official registries | 245/247 |
| Collective ownership | Cooperatives, mutuals, charities, foundations and associations | 244/247 |
| Financial infrastructure | Banking, tax, investment and cross-border transfers | 244/247 |
| Intellectual property | Patents, trademarks, licensing and official IP offices | 246/247 |
| Research and enterprise opportunities | Universities, special economic zones, grants and industry strengths | 245/247 |

These are official-agency research records and practical starting points, not claims that a country offers every route or that an Australian automatically qualifies. Digital residency is not physical residency or citizenship. Financial and enterprise rules can depend on residence, activity, ownership and jurisdiction.

The patterns inherit the nearest relevant record. A state or region uses its country's record unless that level has a distinct rule, such as company formation at US state level or Swiss cantonal taxation. Research and enterprise opportunities are general-purpose information, separate from Works and purpose fit, which concerns Luke's own projects.

### Ancient sites, mysteries and lawful exploration

Research includes ancient temples, megaliths, lost cities, underground settlements, submerged ruins and other heritage sites. Records distinguish documented history and official access conditions from popular lore and speculative theories.

The pattern covers opening, tickets, permits, guides, closures, photography, diving and cultural heritage protection. Underwater sites can include the applicable heritage law and UNESCO 2001 Convention context. Legends are labelled as claims, not historical discoveries. Unchecked access details remain unchecked.

### Drone photography and legal footage

The drone pathway researches official operator registers, licence requirements, foreign-operator restrictions, local permits and lawful access to existing aerial footage. It supports hiring a registered local pilot where appropriate, rather than assuming a visitor can fly. National aviation rules, state or regional permits, and local/site restrictions can all apply.

## Law, permissions and evidence

- **Stack:** local law, culture and protocol, permit zones and other applicable layers accumulate from the country to the destination. A visitor on Minjerribah can be subject to Australian, Queensland, Redland City and island-specific rules at once.
- **Nearest:** entry, many activity rules, seasons, residency and enterprise patterns use the closest applicable record rather than copying national text into every subdivision.
- **Place only:** dated events and personal works are attached to the place they concern.
- **Australian law abroad:** Commonwealth law and official guidance that applies to Australians overseas is held once on Australia's record and shown as its own layer, covering departure and return, consular limits, extraterritorial law, tax residency, health cover and voting.

Each record belongs at the level that owns the rule. Place pages link to applicable higher-level records instead of duplicating them. The permit-zone scan walks down into flagged zones as well as up the tree, accounting for land council permissions, community consent, visitor limits, guides, fees, closures and lead times.

### Finding the official law itself

The law-source map is now a separate, substantial research layer. It links legislation portals, official gazettes, parliamentary collections, regional authorities and other official repositories, with verification and access notes.

| State and regional law-source status | Places |
| --- | ---: |
| At least one verified official source | 1,402 |
| Listed source not yet confirmed | 1,097 |
| No regional law-making body; follows national law | 949 |

At country and territory level, 241 of 248 have a law-source URL; seven are marked as having no official online source found.

See [law repositories](data/law-repositories.json), [state law research notes](docs/STATE-LAW-AMERICAS-AFRICA.md) and the generated [status report](docs/STATUS.md). A verified portal is not a completed review of every law inside it. A missing link is not evidence that a law or authority does not exist.

Official sources, community guidance, signals, operational evidence and legacy baselines are distinguished. Original dates survive imports from earlier projects. Failed fetches, conflicting official sources and expired recheck ages remain visible rather than being replaced by guesses. This is a planning aid, not legal, immigration, financial or safety advice.

## Coverage and outstanding work

Selected figures from [docs/STATUS.md](docs/STATUS.md), generated 24 November 2026:

| Pattern | Country/territory records | Direct state/region records where applicable |
| --- | ---: | ---: |
| Entry permission | 246/247 | Nearest |
| Activity permission | 247/247 | Nearest |
| Visa preparation | 247/247 | Nearest |
| Health entry | 240/247 | Nearest |
| Local law for visitors | 244/247 | 749/3,597 |
| Culture and protocol | 241/247 | 108/3,597 |
| Languages | 244/247 | 747/3,597 |
| Culture cycles | 242/247 | 471/3,597 |
| Affection and relationships | 236/247 | 17/3,597 |
| Births and family support | 236/247 | 0/3,597 |
| Psychoactive substances | 231/247 | 176/3,597 |
| Seasons and visitor flow | 241/247 | Nearest |
| Year ahead | 217/247 | 105/3,594 |
| Special permit zones | 41/247 | 251/3,597 |
| Ancient sites and mysteries | 156/241 | 158/3,594 |
| Drone pilot and footage pathways | 87/241 | 1/3,587 |
| Consular reach | 240/247 | Nearest |
| Money and cost | 247/247 | Nearest |
| Works and purpose fit | 0/26 tagged places | 0/2 |

Denominators vary according to pattern applicability. A record means research exists, not that every individual topic is resolved. Australian law abroad is Australia-specific and is not measured against the foreign-country denominator.

Of 3,705 activity checks across 247 places, 242 still say confirm in writing, 28 say confirm and 15 are unknown. The generated status reports 7% requiring confirmation (including both confirm categories), down substantially from earlier passes. Permission for activities such as remote work, research, volunteering, filming, speaking and enterprise must still be checked against the actual visa and purpose.

Regional/local laws, specific permit conditions, ancient-site access, drone pathways, cultural detail, future events and Works and purpose fit remain substantial areas of further research. The [status report](docs/STATUS.md) contains the full generated table, known gaps and source limitations; its hand-written historical notes may be older than the generated section.

## Calendars, consular help and the wider project ecosystem

- **Culture cycles:** public holidays for this year and next, festivals, religious calendars, seasonal closures and source-backed regional holiday differences. Projected or unconfirmed dates are not presented as official.
- **Seasons:** climate normals, monthly temperatures and rainfall, hazard and visitor-flow signals; not a live weather forecast.
- **Consular help both ways:** Smartraveller's Australian mission and partner contacts for 179 destinations in [australian-abroad.json](data/missions/australian-abroad.json), plus the reviewed DFAT Protocol directory snapshot for 168 places' missions in Australia in [in-australia.json](data/missions/in-australia.json). Check current opening and contact information before relying on the snapshot.
- **Preparation:** generic readiness checklist in [data/preparation/checklist.json](data/preparation/checklist.json), alongside country-specific visa preparation. Imported baseline items retain their original dates and recheck flags. Personal document details do not belong in public data.
- **GAJRA Earth Ahead:** daily feed of AI governance events and open doors, including consultations, hearings and submission opportunities. The 24 November feed contains 59 entries. Events are mapped to place, parent, region or bloc and included in dated briefs when relevant. An event is not permission to participate.

Related projects are linked rather than merged into a single application:

| Project | Relationship |
| --- | --- |
| [Australian World Travel](https://auraofintelligence.github.io/Australian-world-travel/) | Country cards, missions, travel documents and logistics |
| [Australian Visa and Activity Atlas](https://auraofintelligence.github.io/Australian-visa-activity-atlas/) | Earlier entry, activity and preparation baseline; original evidence dates retained |
| [Global Founder Atlas](https://auraofintelligence.github.io/global-founder-atlas/) | Funding, startup visas, residencies, research placements and pilots |
| [Strange But True Travel Oracle](https://auraofintelligence.github.io/strange-but-true-travel-oracle/) | Personal navigation, dossiers and strategy builders |
| [GAJRA Earth Ahead](https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html) | Dated event and opportunity feed |
| [UNGA81 contribution](https://auraofintelligence.github.io/UNGA81-Luke-Hayes/) | Locally rooted, connective rather than assimilative approach to culture |
| [Mutual Futures](https://auraofintelligence.github.io/mutual-futures/) | Mutual enterprise, Try Everything Once and Intermittent Retirement |
| [Aura Tourism](https://auraofintelligence.github.io/aura-tourism/) | Welcoming visitors, from Minjerribah towards Brisbane 2032 |

The [site map](https://auraofintelligence.github.io/world-travel-patterns/site-map.html) and [related project data](site/data/related.json) contain the wider collection, including the Desire Atlas, Event Search QLD and Minjerribah projects.

## Photographs and cultural authority

Main research pages use credited photography. Individual places show an image of that place, a labelled image of somewhere inside it, or none. They do not use a substitute from somewhere unrelated.

The generated status records 313 places with photographs, one awaiting Luke's review. [Photo review notes](docs/PHOTO-REVIEW.md) document the earlier visual review, rejected choices, replacements and the no-drone image selection rule. Communities with their own cultural authority over imagery do not receive automatic photographs. Credits and image-specific licences remain separate from the project's licence.

## Research cadence and automation

Two modes: **Baseline** maps places year-round; **Window** tightens rechecks for a declared trip, its applicable parent levels and relevant permit zones.

| Job | Configured schedule (Brisbane time) | Function |
| --- | --- | --- |
| [Daily advisories](.github/workflows/daily-advisories.yml) | Daily, 06:00 | Fetch Smartraveller export, rebuild queue/index, report level changes; preserve old advice on failed fetch |
| [Daily feeds](.github/workflows/daily-feeds.yml) | Daily, 08:45 | Refresh GAJRA Earth Ahead and rebuild |
| [Weekly source watch](.github/workflows/weekly-sources.yml) | Monday, 05:00 | Check cited URLs for missing or changed pages and report issues |
| [Monthly calendars](.github/workflows/monthly-calendars.yml) | 1st at 19:00 UTC, which is 2nd at 05:00 Brisbane | Refresh holidays, place photos and consular reach |
| [Validation](.github/workflows/validate.yml) | Push and pull request | Validate data, exercise a dated queue and run Python unit tests |
| Round 1 research | Manual agent sessions | Luke directs Claude, Codex and Grok through official-source research passes |

These are configured trigger times, not promises of execution or successful fetches. In particular, the advisory data file at the time of this review reports a last successful check of 29 October 2026 despite later daily workflow commits. The site should be read with its displayed last-check date; verify current advice directly with [Smartraveller](https://www.smartraveller.gov.au/).

The original Claude scheduled place passes, monthly cycles and window watch were switched off on 4 November 2026. Their routine definitions remain in [routines/](routines/) for manual or future authorised use. The [automation checklist](docs/AUTOMATION-CHECKLIST.md) and [machine-readable recheck plan](config/recheck-plan.json) describe suggested future checks, not additional active schedules.

Window phases are defined in [config/cadence.json](config/cadence.json):

| Phase | Starts | Age limit |
| --- | --- | --- |
| Approach | 90 days before travel, or earlier for a permit lead time plus buffer | 30 days |
| Countdown | 30 days before | 7 days |
| Imminent | 7 days before | 2 days |
| In place | During travel | 1 day for advice, local law, permit zones and calendars |
| Debrief | Up to 14 days after | Record findings |

The public Actions treat places independently of personal travel windows. Private trip dates, readiness, briefs and unpublished findings live in gitignored `private/`. Do not commit personal itineraries, passport details, bookings or private records.

## Run it locally

Python standard library only; no package installation is required. GitHub Actions uses Python 3.12.

```sh
git clone https://github.com/auraofintelligence/world-travel-patterns.git
cd world-travel-patterns
python -m http.server
```

Open http://localhost:8000/ in a browser.

Useful commands:

```sh
python scripts/brief.py cl/rapa-nui --start 2027-03-01 --activities tourism,filming
python scripts/due.py
python scripts/validate.py
python -m unittest discover tests
python scripts/status_report.py
python scripts/build_site.py
```

To declare a private travel window, copy [examples/windows.example.json](examples/windows.example.json) to `private/windows.json`. See [private/README.md](private/README.md).

### Repository layout

| Path | Purpose |
| --- | --- |
| [patterns/](patterns/) | Research schema, source rules, inheritance and applicability |
| [data/places/](data/places/) | Hierarchical place registry |
| [data/vetting/](data/vetting/) | Dated research records, one JSON file per vetted place |
| [data/](data/) | Advisory, law-source, preparation, calendar, consular, feed and source-health data |
| [site/](site/) | Browser JavaScript, CSS, imagery and generated website indices |
| [scripts/](scripts/) | Importers, builders, dated briefs, validators, queue and source checks |
| [config/](config/) | Cadence and generated recheck plan |
| [tests/](tests/) | Unit tests for inheritance, evidence conflicts, visa preparation, law repositories, residency/enterprise and related logic |
| [docs/](docs/) | Coverage, run notes, photo decisions and handovers |

The generated website index and law stacks support the browser interface. `scripts/build_site.py` also regenerates the sitemap and AI-readable site guide. See [patterns/README.md](patterns/README.md) for extending existing patterns or adding another. [docs/ACTIVITY-LOG.md](docs/ACTIVITY-LOG.md) records dated handovers between research agents.

## Search discovery

[`robots.txt`](robots.txt) documents scoped search and training preferences: search crawlers including OAI-SearchBot and Claude-SearchBot are allowed, while training crawlers GPTBot, ClaudeBot and Google-Extended are disallowed. [`sitemap.xml`](sitemap.xml) lists the main pages and country/territory or checked place pages. [`llms.txt`](llms.txt) is a voluntary guide.

GitHub project Pages cannot set the origin-root crawler policy. [`.github/robots-root-snippet.txt`](.github/robots-root-snippet.txt) provides the scoped account-root addition, previously merged into that policy on 1 November 2026. Discovery does not grant additional reuse or AI-training rights.

## Licence

[Strange But True Public Source Licence](LICENCE.md). Non-commercial use is welcome with credit, subject to the full licence. Commercial rights are reserved. This is public source, not an open-source licence. Third-party data, photographs and other material retain their own rights.

---

🤝🔷 Luke × Claude, Codex and Grok · world-travel-patterns
