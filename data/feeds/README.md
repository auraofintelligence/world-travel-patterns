# Feeds

Dated leads from Luke's other projects, mapped onto the place tree. Every feed file has the same shape: `feed`, `name`, `source`, `checked_on`, `evidence` and `events`. Each event carries `title`, `kind` (event or door), `starts`, `ends`, `closes`, `where`, `place` (a place id, or null for online and global), optional `bloc` and `members`, `keywords` and `source_url`.

| Feed | From | Refreshed |
| --- | --- | --- |
| `gajra-ahead.json` | [GAJRA Earth Ahead](https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html): upcoming AI governance events and open doors (consultations, hearings, calls for submissions) | Daily, 08:45 Brisbane, after the Ahead routine publishes |

Feeds are signals. An event is never a permission: taking part still runs through the entry, activities and zone checks. The source project owns its content and its exclusions.

Briefs show every upcoming event at the place, its parents, anything inside it, or its bloc (for example the EU). The window watch lists events and open doors that fall before or during a trip.

To add a feed, write a `scripts/feed_<name>.py` that outputs this shape, then add it to `.github/workflows/daily-feeds.yml`.
