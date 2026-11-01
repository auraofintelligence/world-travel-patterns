# Activity log

Dated handover notes for whoever works on this repo next (Claude, Codex, Grok). Newest entry at the bottom. Times are Brisbane time (AEST, UTC+10).

## Standing notes from Luke (1 November 2026)

- **What this repo is.** A dataset only: accurate, sourced records that a separate oracle (built elsewhere) will draw on for Luke's own spontaneous overseas travel. This repo is not the oracle. Focus purely on accurate, cited data.
- **Australia is out of scope here.** Skip all Australian domestic data work (councils, wards, electorates, Minjerribah and other Australian places); it's covered by Luke's separate p4a.xyz repo. Prioritise overseas sources and facts.

## 2026-11-01 15:40 AEST, Grok: batch 1, dead sources

**What changed.** Rechecked the 92 sources that `data/source-status.json` marked as error, 403, 500 or soft-404, using curl with a browser user agent from a different network. Most (46) now answer 200; about 38 still return 403 or time out, which looks like bot blocking or geo-blocking, not dead pages. Those were left alone: a blocked fetch is not a dead source. Real 404s and soft-404s were fixed where an official replacement could be verified:

- `data/vetting/nl.json`: IND self-employed page moved to https://ind.nl/en/residence-permits/work/residence-permit-self-employed-person (200, checked 2026-11-01).
- `data/vetting/in.json`: MHA "Details of visas granted by India" 2018 PDF is gone; replaced with the August 2020 edition https://www.mha.gov.in/files/documents/AnnexIIIDetailsofVisas20082020.pdf (200, PDF, covers business, employment and other visa types).
- `data/vetting/ae.json`: UAE embassy Canberra FAQ now redirects to a 404 page (both letter cases). Replaced with GDRFA Dubai's visa-on-arrival list https://gdrfad.gov.ae/en/node/69, which lists Australia. That page blocked direct fetches from here (403, timeout); its content was read via a search index snapshot. **Conflict flagged:** the old FAQ said 30 days, Emirates airline (operational) lists Australia for 90 days. The `route` text in ae.json still says 30 days. Confirm with an official UAE source (ICP or GDRFA) and update.

**Left undone.**
- `in.json`: MHA "Work-related visa FAQs" PDF (`.../2022-07/ForeigD-work_visa_faq.pdf`) is 404. The search engine lists `https://www.mha.gov.in/sites/default/files/ForeigD-work_visa_faq.pdf` but it also 404s from here. Not replaced. Try the MHA Foreigners Division FAQ page in a browser.
- Still blocked from this network (not dead, recheck from a browser): france-visas.gouv.fr, travel.state.gov, mofa.go.jp and Japanese embassies, mfa.gr, inclusion.gob.es, gea.gov.sa, ble.dole.gov.ph, intgovforum.org; timeouts on kln.gov.my, aima.gov.pt, indianvisaonline.gov.in, portal.www.gov.qa, customs.gov.qa, mohre.gov.ae, evisa.gov.vn, fam.state.gov.

## 2026-11-01 15:55 AEST, Grok: batch 2, soft-404 detector

**What changed.** `scripts/source_watch.py` now has `soft_404()`: a 200 response that redirected to a 404-style URL (for example `mofa.gov.ae/404?item=...`) or whose `<title>` says not found is recorded as status `soft-404` and counted with the dead sources (`dead_since`). Ordinary redirects still pass. New `tests/test_source_watch.py` (5 cases, stdlib unittest); `.github/workflows/validate.yml` now also runs `python -m unittest discover tests`.

**Next steps.** Add tests for `lib.py`, `due.py` and the permit-zone lead-time maths in `brief.py`. The weekly Action will mark any remaining soft-404s on its next run.

## 2026-11-01 16:10 AEST, Grok: batch 3, stale facts

**What changed.**
- `data/vetting/ve.json` (money): currency now "Venezuelan bolívar (VES; redenominated 1 October 2021)". Source: ISO 4217 Amendment 170, https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/dl_currency_iso_amendment_170.pdf. Smartraveller's cash notes kept as read, with a note that they name the outdated VEF. bcv.org.ve timed out from here.
- `data/vetting/ca.json` (psychoactive substances): psilocybin and MDMA re-read against the Controlled Substances Regulations SOR/2025-242, https://laws-lois.justice.gc.ca/eng/regulations/SOR-2025-242/FullText.html (s. 239 in force 1 October 2026; s. 6 restricted-drug possession, including a person who got the drug for their own use from a practitioner named in a letter of authorization; both drugs in Schedule 4). The 2022 class-exemption source is still listed for the history.
- `docs/STATUS.md` "Known source problems" updated.

**Not resolved.**
- WHO vaccination list: the newest WHO yellow fever list found is still November 2022, so there's nothing newer to cite. Health-entry records left as they were.
- Fiji 2027 holidays: no revised Fiji Government list found, only third-party calendars, so `fj.json` stays "confirm on the gazetted list". Next: check the Ministry of Employment, Productivity and Workplace Relations site and the Fiji Government Gazette.
- UAE visa-on-arrival length (30 vs 90 days) still needs an official source (see batch 1).

## 2026-11-01 16:20 AEST, Grok: batch 4, README numbers

**What changed.** `README.md` "Where it stands" now takes its numbers from the generated table in `docs/STATUS.md` (1 November 2026) instead of the hand-written 31 October counts, which had drifted (for example local law 179 vs 177, culture 93 vs 92, "25 permit zones" vs 6 countries plus 4 regions). It links STATUS.md and this log.

**Next step.** Have `scripts/status_report.py` also rewrite the README table between markers, so they can't drift again.

## 2026-11-01 16:35 AEST, Grok: Luke's other travel repos (survey only, nothing imported)

Public repos under github.com/auraofintelligence that hold travel reference data (read-only shallow clones, 1 November 2026):

- **[Australian-visa-activity-atlas](https://github.com/auraofintelligence/Australian-visa-activity-atlas)** (last commit 2026-11-01). `assets/world-baseline.js` holds 201 countries, each with `entrySummary`, `estimatedCostAud` (visa cost signal, such as "Free", "~ $125", "Variable"; 7 blank or "Variable"), `costReviewed` (mostly 16 August 2025), `advisoryLevel` and `distanceFromBrisbaneKm`, each with claim ids (for example `WORLD-ALGERIA-COST`). `assets/data.js` holds the deeper activity pathways (speaking, performing, filming and so on). This repo already imports it through `scripts/import_atlas.py` (needs Node and a sibling checkout); 30 vetting records already cite `WORLD-*-COST` claims as `legacy-baseline` money. **Possible next import:** add `estimatedCostAud` as a visa cost field in the entry pattern for all 201 countries, evidence `legacy-baseline`, keep the claim id and the original `costReviewed` date, then recheck each against the country's official fee page. Cite the atlas as the source of the baseline, never as the authority.
- **[Australian-world-travel](https://github.com/auraofintelligence/Australian-world-travel)** (last commit 2026-09-07). The upstream of that baseline: `index.html` carries per-country `cost` strings (for example "~ $110 + fee") and simplicity ratings that `world-baseline.js` was generated from. `data/missions-reviewed.js` is the DFAT Protocol directory of foreign missions in Australia (checked 2026-09-06), already covered here via aura-horn-torus in `data/missions/`. Import from the atlas, not from here, to avoid duplicates.
- **[global-founder-atlas](https://github.com/auraofintelligence/global-founder-atlas)** (last commit 2026-11-01). `data/opportunities.json` has 62 dated, sourced opportunities (funding, startup visas, residencies, pilots) with `source_url`, `status`, `opens`/`closes`. Overseas ones (Canada, Chile, Estonia, France, Netherlands, Portugal, Qatar, Saudi Arabia, Singapore, Switzerland, UAE, NZ and others) could feed the `activities` (startup and founder routes) and `year-ahead` (deadlines) patterns as signals, each confirmed at its official source. Skip the Australia-only entries.
- Not travel data: aura-horn-torus (already the source of `data/missions/in-australia.json`), lifetime-memory-map (personal history; privacy rules apply), australian-sire-story-forge (fiction).

Australian domestic data is out of scope here (see standing notes); don't import it from any of these.

## 2026-11-01 16:55 AEST, Grok: visa preparation carried over (local commits, not pushed)

Luke asked for the visa preparation steps and documents from his earlier repos to be carried over, with room to improve and update them.

**What changed.**
- New pattern `patterns/visa-preparation.json` (inherit nearest, 90-day recheck, overseas only, `skip_home`). Fields: `steps`, `before_departure`, `documents`, `fastest_entry`, `useful_stay`, `host_unlock`, `open_questions`, `cost_aud_baseline`, `needs_recheck`, `last_reviewed`, `provenance`. Statuses: `steps-found`, `baseline-only`, `confirm-in-writing`, `unknown` (plus `imported`). Listed in `patterns/README.md`; README now says eighteen patterns.
- New `scripts/import_visa_prep.py` (read-only, needs Node and a sibling `../Australian-visa-activity-atlas` checkout; re-runnable; never overwrites a record with `needs_recheck: false` or a newer date).
- Ran it at atlas commit 60f4fbc: **36 countries** now carry steps, pre-departure tasks, document packets, open questions, sources and claim ids (`status: imported`, dates 20 to 21 August 2026). **165 more** carry only the entry summary and AUD visa cost signal (`status: baseline-only`, mostly 16 August 2025). All 201 have `evidence: legacy-baseline` and `needs_recheck: true`. Australia is excluded.
- New `data/preparation/checklist.json`: 49 readiness items by horizon (from the atlas's `assets/prepare.js`) and 22 business-visa document items (from Australian-world-travel `documents.html`, commit 22746ae, file last changed 2026-09-07), each with `needs_recheck: true`.
- New `tests/test_visa_preparation.py`: no Australian records; baselines carry needs_recheck, legacy-baseline evidence and provenance; rechecked records need sources; checklist ids are unique and dated.

**How to improve a record.** Open the destination's official visa or e-visa page, reread each step, document and fee, replace the text in that place's own terms, add the source with today's date, then set `needs_recheck: false`, `status: steps-found`, `evidence: official` and redate `checked`. Keep `provenance` for history. Start with the 36 deep countries; their atlas notes flag pending changes (for example Thailand's 60-day vs 30-day exemption).

**Left out on purpose.**
- The atlas's per-activity pathways (speaking, performing and so on): already carried into the `activities` pattern by `scripts/import_atlas.py`.
- The atlas's `ageNote` text: it's personal (age), not destination data.
- global-founder-atlas: it holds funding and residency opportunities, not visa preparation steps. Overseas ones could later feed `activities` and `year-ahead` as signals (see the earlier survey entry).
- Australian-world-travel's mission directory: Australian domestic data, already covered via aura-horn-torus.

**Next steps.**
1. The website doesn't show the new pattern yet: `site/site.js` lists patterns by hand (line ~32 group list and line ~643 `ORDER`). Add `visa-preparation` to the Permission group and render `steps`, `documents` and a "needs recheck" badge.
2. Recheck the 36 deep countries at official sources (the queue lists them once they pass 90 days; 157 baseline-only records are already over budget).
3. Turn `cost_aud_baseline` strings such as "~ $125" into a number, currency and rate date once each fee is reread at an official source.

## 2026-11-01 17:10 AEST, Grok: site shows visa preparation

**What changed.** `site/site.js` now lists `visa-preparation` in the Permission group (after Entry) and in `ORDER`. A place page shows entry summary, fastest entry, before departure, stay, host route, numbered steps, documents, structured fees (or the baseline cost signal), open questions and a recheck note. Any record with `needs_recheck: true` (any pattern) shows a gold "needs recheck" chip. Asset version bumped to `v=20261101k` in every page. The pattern gained `fees` and `recheck_note` fields. Checked in headless Chrome on `place.html?id=th`.
