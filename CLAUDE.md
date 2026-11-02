# Working rules for world-travel-patterns

These rules bind every agent and routine working in this repo.

## Purpose

Vet every place an Australian passport holder might visit, with the same simple, repeatable patterns, so that local laws aren't broken by accident and local culture is respected. The place list is open: the ISO spine is a starting layer, and islands, regions, nations, zones and governance units grow underneath it.

## Voice

- Australian English. No em dashes. Plain words; gloss technical terms.
- The smaller true claim beats the bigger vague one. No absolutes, no exaggeration.
- Describe; don't moralise. No ranking of places or cultures.
- Costs in AUD with the conversion rate and its date.

## Evidence

- A rule comes from the government, authority or community that owns it. Everything else is a signal and is labelled as one.
- Evidence levels: `official`, `community` (a community's own published process), `operational` (transport or venue operator), `signal`, `legacy-baseline` (carried from an earlier atlas, recheck it).
- Only date what was actually rechecked. A failed fetch is not a change.
- **Unvetted is not permitted.** A missing record means "not yet checked", never "no rules".
- Advice levels are information for the traveller, never an automatic exclusion.

## Culture

The GAJRA Earth register: connective, not assimilative; each place interpreted locally.

- Record each place's own guidance in its own terms, and its own names first.
- Cultural authority over information stays with the community. Where nothing is published, use `ask-locally` and say who to ask.
- Never write cultural rules for a community, and never presume the outcome of a consent process.

## Privacy

- `private/` is gitignored apart from its README. Travel windows, window findings and briefs live there.
- Never store passport numbers, bookings, card details, phone numbers, emails, home addresses or live location. The validator rejects those field names.
- Public commits must not reveal where the traveller is heading. Window-driven vetting goes to `private/findings/` unless the window says `"share": true`.

## The three inheritance modes

| Mode | Meaning | Patterns |
| --- | --- | --- |
| nearest | The place's own record, else the closest ancestor's | entry, activities, health, consular, money, seasons |
| stack | Every level at once, country down to the place | local law, culture and protocol, culture cycles, zone requirements |
| none | The place's own record only | year ahead, works and purpose |

Inheritance decides what applies, not what is printed. The website shows each record once, on the page of the level that holds it. A deeper page shows its own records in full, one line per level above listing what still applies with links up, and one line naming what isn't checked at its own level. Never copy a parent's text into a child's record, and never render a parent's record on a child's page.

Home obligations (`home-obligations`, `home_only`) belong to the home base and the levels above it (`config/home-base.json`). They show on those pages only. A country page outside Australia gets one line linking to Australia's page for the laws that follow a traveller overseas.

## Record format

One file per place in `data/vetting/`, named by place id with `/` replaced by `__`.

```json
{
 "place": "cl__rapa-nui is the filename; the id inside is cl/rapa-nui",
 "patterns": {
  "zone-requirements": {
   "status": "requirements-found",
   "checked": "2026-11-02",
   "evidence": "official",
   "layers": [
    {"type": "entry-permit", "authority": "who issues it", "process": "what to do, in plain words",
     "lead_time_days": 30, "activities": ["all"], "url": "https://...", "checked": "2026-11-02"}
   ],
   "sources": [{"title": "...", "authority": "...", "url": "https://...", "checked": "2026-11-02"}]
  },
  "local-law": {
   "status": "partly-mapped", "checked": "2026-11-02", "evidence": "official",
   "laws": [{"topic": "filming", "rule": "plain statement of the rule", "penalty_signal": "fine range if published",
             "source": "https://...", "checked": "2026-11-02"}]
  }
 }
}
```

- `status` must be one of the pattern's statuses (`imported` is allowed for records carried from the earlier atlas, until they're rechecked).
- `checked` is `YYYY-MM-DD`, Brisbane date, never in the future.
- Activities keep a checked date per activity, under `activities.activities.<id>`.

## Website

The site (root `*.html`, `site/`) reads the repo's data directly; `scripts/build_site.py` writes its index. It never reads `private/`. Hero photographs are openly licensed from Wikimedia Commons and credited in `site/heroes/credits.json`; Luke doesn't want SVG art.

Place pages show a photo of that place, or of somewhere inside it (labelled), or none: never a stand-in from elsewhere. `scripts/place_photos.py` picks from Wikidata and Wikivoyage; hand decisions and their reasons live in `site/heroes/place-photo-choices.json`, and chosen photos in `site/heroes/place-photos-curated.json`. Places belonging to a nation or community with its own cultural authority get no automatic photo. Every automatic pick stays `review: pending` until Luke has looked.

`view.html` (Your view) lets each viewer switch any pattern off, switch off its parts one by one (the pattern file's own list: activities, topics, substances, areas, event categories or requirement types), and choose who they are and who they love; choices stay in that browser's storage. What a viewer hides is never mentioned anywhere except Your view: no "hidden" notes on other pages. The default is Luke's: a man who loves women, so same-sex relationship content is hidden. The filter is display-only (`viewText` in `site/site.js` drops same-sex sentences and reads "opposite or same-sex couples" as "couples"); records keep their full source text. Run any new text field on a place page through `viewText`.

These photo rules describe how Claude picks photos automatically. They don't bind Luke's directions: he asks Codex, Grok or anyone else for images, generated or not, wherever he judges them worthwhile.

Search discovery follows Luke's pattern across his sites: hand-kept `robots.txt` and `.github/robots-root-snippet.txt` (search crawlers allowed, training crawlers disallowed), `sitemap.xml` and `llms.txt` written by `build_site.py`, and `index,follow`, canonical and Open Graph tags in each page head. The account-root robots policy lives in the auraofintelligence.github.io repo; the snippet was merged there on 1 November 2026 with his OK; keep the two in step if the rules change.

## Feeds

`data/feeds/` holds dated leads from Luke's other projects (GAJRA Earth Ahead today). They are signals: confirm a date at its source before recording it, and never read an event as permission to attend, speak or film.

## Before committing

```text
python scripts/validate.py
python scripts/due.py
python scripts/build_site.py
python scripts/status_report.py   # refreshes the coverage table in docs/STATUS.md
```

Commit only when validation passes. End commit messages with the Claude co-author line.

## Handover for Claude: GitHub About metadata (1 November 2026)

At Luke's request, Codex updated the repository's GitHub About fields to match the established Aura of Intelligence repository navigation and search pattern. The original Luke × Claude build credit in the README and this project's licence remain unchanged.

**Description:** A Luke × Claude travel research project for Australian passport holders, using repeatable, source-linked checks of entry, local laws, cultural protocols, permit zones, seasons, consular reach and events, with dated records and private trip windows.

**Website:** https://auraofintelligence.github.io/world-travel-patterns/

**Topics:**

```text
auraofintelligence-world-travel-patterns
built-2026-10-31
consular-services
cultural-protocols
github-pages
local-laws
permit-zones
privacy-first
public-source
source-provenance
travel-advisories
travel-planning
visa-requirements
world-travel-patterns
```

The `built-2026-10-31` tag records GitHub repository creation: `2026-10-31T12:56:30Z`, which is 22:56:30 on 31 October 2026 in Australia/Brisbane. It does not replace the README's 30 October project build date, or any source-check date.

For future About maintenance, retain the lower-case repository slug, the complete `auraofintelligence-<slug>` search topic when it fits GitHub's 50-character topic limit, the actual repository-creation date in Brisbane time, `github-pages` for a published Pages site, and a few accurate subject topics. Preserve useful existing topics and stay within GitHub's 20-topic limit. The combined identifier lets people search for the project from link-free comments.

The description names the research workflow and its subjects without claiming that every place and pattern has already been checked. Keep source-check dates and coverage claims tied to their records. Keep private travel windows and visitor briefs out of public commits.

This maintenance changed only the GitHub About metadata and this handover note. It did not change travel records, routines, website content, photographs, deployment settings or licence terms.
