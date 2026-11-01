# Patterns

A pattern is one repeatable question asked of every place it applies to. Every pattern has the same shape, so a new one is one file.

| Pattern | Question in short | Method | Inherits | Recheck within |
| --- | --- | --- | --- | --- |
| advisory | Australian Government advice level | machine, daily | nearest | 1 day |
| entry | Can an Australian passport holder enter, and how? | agent | nearest | 90 days |
| visa-preparation | Steps, documents, lead time and visa cost signal to prepare before entry (baseline imports carry `needs_recheck`) | agent | nearest | 90 days |
| activities | Does that status allow the planned activity? (15 activities) | agent | nearest | 120 days |
| zone-requirements | Extra permits, consents, caps, guides, fees, lead times | agent | stack | 120 days |
| health-entry | Vaccination or health certificates required to enter | agent | nearest | 180 days |
| local-law | Laws a visitor could break without knowing (14 topics) | agent | stack | 180 days |
| culture-and-protocol | How the place asks visitors to arrive and behave, in its own words | agent | stack | 365 days |
| languages | Official and national languages, English speaking capacity and English hotspots | agent | stack | 365 days |
| affection-and-relationships | Affection in public, couples in private, marriage and partnership, what's changing (law or custom) | agent | stack | 365 days |
| births-and-family-support | Births per woman over time and what governments offer families (connected to affection-and-relationships) | agent | stack | 365 days |
| psychoactive-substances | Alcohol, tobacco and vaping, cannabis, MDMA, psilocybin, ayahuasca and more: law, medical and ceremonial access, penalties, change | agent | stack | 180 days |
| culture-cycles | Holidays, moving calendars, festivals, closures | mixed | stack | 365 days |
| seasons-and-flow | Twelve months of season, hazard and visitor flow | agent | nearest | 365 days |
| year-ahead | Dated elections, events and rule changes | agent | none | 90 days |
| consular | Nearest Australian mission or partner | agent | nearest | 365 days |
| money-and-cost | Currency, cash and card, daily cost in AUD | agent | nearest | 180 days |
| works-and-purpose | Where this place meets Luke's works (tagged places only) | agent | none | 365 days |

## Adding a pattern

1. Copy the closest existing file and give it a new `id`.
2. Fill in `question`, `applies_to` (place kinds), `inherit` (nearest, stack or none), `baseline_days`, `sources`, `statuses` (always include `unknown`) and `rules`.
3. Run `python scripts/validate.py` and `python scripts/due.py`.

Every place the pattern applies to now shows it as never checked, and the routines start vetting it in queue order. Nothing else needs to change.

## Extending a pattern

- **activities** and **local-law** carry open lists (`activities`, `topics`). Add an item and every place shows it as not yet checked.
- **zone-requirements** carries `requirement_types`. Add a type when a new kind of layer keeps turning up.

Bump `version` when a change alters what a record means.
