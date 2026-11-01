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
