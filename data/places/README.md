# Place tree

`spine.json` holds every ISO country, territory and separately travelled jurisdiction (264 today). It is the root layer, not a limit.

Everything below it lives in a country folder, named by the lower-case ISO code:

- `au/governance.json`: Australia's states, councils, wards and electorates, generated from the route registry kept in the neighbouring p4a-xyz-cinema repo. Re-run `scripts/import_au_governance.py`; don't hand-edit it.
- `<iso>/extra.json`: hand or agent additions, such as islands, island groups, regions, nations, permit zones, cities and sites.

## Adding a place

Add one object to the right `extra.json`:

```json
{ "id": "cl/rapa-nui", "name": "Rapa Nui", "kind": "island", "parent": "cl",
  "aliases": ["Easter Island"], "tags": ["oceania"], "zone_scan": true,
  "why": "Flagged for a zone scan: island-level visitor process to vet." }
```

- `id` is `<parent country>/<slug>`, stable forever.
- `parent` is the place it sits inside for inheritance. Electorates and other overlapping layers set `"overlay": true`.
- `kind` is one of: state, district, electorate, region, island, island-group, nation, zone, city, site.
- `tags` group places, for example home, oceania, first-nations. A tagged place becomes active and joins the vetting queue.
- `zone_scan: true` asks the zone pattern to look for extra permits, consents, caps and lead times.
- `why` says why the place was added. It's a reason to vet, never a finding.

Sub-places stay dormant (they inherit from their parents and aren't queued) until they're tagged, flagged for a zone scan, or named in a travel window.
