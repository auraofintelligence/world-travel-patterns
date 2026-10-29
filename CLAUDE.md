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
   "laws": [{"topic": "filming-and-drones", "rule": "plain statement of the rule", "penalty_signal": "fine range if published",
             "source": "https://...", "checked": "2026-11-02"}]
  }
 }
}
```

- `status` must be one of the pattern's statuses (`imported` is allowed for records carried from the earlier atlas, until they're rechecked).
- `checked` is `YYYY-MM-DD`, Brisbane date, never in the future.
- Activities keep a checked date per activity, under `activities.activities.<id>`.

## Before committing

```text
python scripts/validate.py
python scripts/due.py
```

Commit only when validation passes. End commit messages with the Claude co-author line.
