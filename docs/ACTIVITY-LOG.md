# Activity log

Dated handover notes for whoever works on this repo next (Claude, Codex, Grok). Newest entry at the bottom. Times are Brisbane time (AEST, UTC+10).

## Handoff for Claude (updated 2026-11-01 evening AEST, Grok)

**State today.** Every country and territory outside Australia has entry, activities and culture records. 637 of 3,705 activity checks (17%) still say "confirm in writing"; 317 of those are outside the Do-not-travel places (remote work 62, volunteering 51, book launches 38, research 37, unpaid speaking 25, mixed missions 23, filming 12, entrepreneur 2, others 67).

**Later passes (e802e79 to 08304a9).** Volunteering for 32 places (ca, ie, mx, th, Nordics, Baltics, central Europe, is, co, rw, tr, Pacific, Caribbean); remote work for 12 (Armenia allowed for a foreign employer; Dominica WIN visa; US and territories not addressed); research for 9 (US B-1, Namibia NCRST permit 4 months ahead); book launches for 7 (Armenia, Serbia, Kazakhstan); filming for 9 (ca, jp, za, ie, br, co, cl, hk, uz). Corrections: the Canada volunteering source was a mirror (migova.ca), replaced with canada.ca in 078680c; a Vietnam research draft based on a misread Taiwan page was reverted before commit.

**Latest (f77a2c7, 3edb052).** Entrepreneur for 12 places: tw, mu, sc, mn, am, az, vu, ws, pw, rw, jm, tt.

**Run of 1 to 2 November (1fbff79 to 4950548).** Entrepreneur for 15 more places (rs, kg, uz, tj, la, bt, mo, pf, tn, co, kz, pk, mg, cm, sr); filming for 11 (pk, uy, tn, sn, mx, qa, rs, rw, pg, sb, ar); Kyrgyz Digital Nomad status; volunteering at, ch, si, kr, tr; research sg, th, ar; book launches na, mn (plus unpaid speaking), ro. Switzerland and Türkiye volunteering stay confirm-in-writing with detail (official pages don't settle it).

**Latest (eb8b663 to 1fe906d).** Entrepreneur ao, sn, na (new Investor Permit from 1 September 2026), sz, ki, ck; filming la, gy, cm; research hk, sa, vn. Remote work searches found few official routes (Azerbaijan's planned nomad visa seen only in news, not recorded).

**Latest (dbe7dca to f65a627).** Mixed missions for 28 places derived from each record's already-cited paid-work source (strictest element decides); dbe7dca overwrote deliberate detail, fixed in 523b376 (cu, dk, se restored to confirm-in-writing). Book launch or unpaid speaking reused sibling sources for am, sc, to, mu, gy, cu. Entrepreneur ci, lc, vc, dz, dm, nc (Saint Lucia escape fix 60a77c0). Filming dz, mg, ci.

**2 November (3ba2b5c to 947ea86).** Reviewed Claude's 26d61c3 (kept): fixed the Central Land Council permit link and labelled the Minjerribah festival news source as a signal. Australia light pass: 2027 writers' and arts festivals for NSW (Sydney, Byron), VIC (Melbourne), SA (Adelaide Writers' Week) and WA (Perth Festival). Scope rule added to the three routines. Entrepreneur gy, kn.

**Next.** Entrepreneur (2) and filming (12), then remaining remote work, volunteering, research, book launches; Do-not-travel work rules last; then ask-locally culture and 2027 events.

**Today's work (3bf3434 to d0191a2).**
- Work rules filled for about 90 places.
- Do-not-travel culture searched in full.
- Then focused passes on four activities:
  - **Remote work:** digital nomad visas in 22 places, with income thresholds from official pages. Estonia's two official figures conflict and are flagged. Norway's UDI says remote work as a visitor is not allowed (recorded as not-fit).
  - **Book launches:** lecture and artist exemptions across Europe. Slovenia names literature; Poland allows 30 days a year of occasional lectures since 1 December 2025; the US has no author category.
  - **Research:** sg, ie, mx, kr, br, th, tr, ke, za, ph, ae.
  - **Volunteering:** de, nl, in, ch, fr, cn, at, es, it, pt, be, jp, ar, gr, ph.

**Corrections to know about.**
- ab9a95d was an accidental test push titled "x" with 9 records. Fixed forward in 720cad7.
- af, bf, cd and cf culture entries in 897e1c1 were marked "none found" without fresh searches. They were redone in c9cb164.
- li activity rules in 94c0948 cited a generic EU page and an unverified "8 days in 90" rule. Corrected from the Liechtenstein Ausländer- und Passamt in daa1922.

**Top next priorities.**
1. Volunteering (83 left): mostly smaller states, the Pacific, the Caribbean and Africa.
2. Remote work (65 left): EU states without a nomad route (sk, lu, lt, dk, se); Pacific and US territories; Africa.
3. Research (52) and book launches (50): Latin America, Africa and the Pacific.
4. Entrepreneur and filming (81 together): not yet started as a focused pass.
5. Do-not-travel work rules last (23 places, all 14 activities).
6. Year ahead is still only 90 of 247 countries, mostly signal.
7. Pending Luke: the Uluru photo (do not touch). The five repos stay separate: no cross-repo links or imports.

**Rules in force.**
- Official sources only, never invent figures, Australian English, no em dashes.
- Batches of 10 to 15 vetting records (smaller only when finishing a category).
- Run validate, tests, build_site, due and status_report before each commit.
- `git pull --rebase`, fast-forward push only, clear descriptive commit messages, a dated AEST entry here per batch.
- When a page doesn't name the activity, leave "confirm in writing" and record what it does say.

## Standing notes from Luke (1 November 2026)

- **What this repo is.** A dataset only: accurate, sourced records that a separate oracle (built elsewhere) will draw on for Luke's own spontaneous overseas travel. This repo is not the oracle. Focus purely on accurate, cited data.
- **Australia: light pass only (rule changed 2 November 2026).** Australia is no longer fully excluded. Do state, territory and notable-region work only (Aboriginal land permits, major events in Luke's categories, culture and respecting Country). No council or ward depth, which Luke's separate p4a.xyz repo covers; don't duplicate it. Visa and work patterns are skipped for Australia (skip_home), not filled. International work is the priority.

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

Australia gets a light pass only (see standing notes); don't import council or ward data from any of these.

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

## 2026-11-01 17:40 AEST, Grok: visa-preparation recheck, batch 1 (10 countries)

**Verified at official sources on 2026-11-01** (`needs_recheck: false`, `status: steps-found`, `evidence: official`, structured `fees`): th, gb, us, ca, in, vn, ke, br, id, sg. Each record cites Smartraveller's entry section (read the same day) plus the destination's own page for portals and fees: GOV.UK ETA £20; USAGov ESTA US$40.27; Canada IRPR s. 294.1 eTA CAD 7; Indian Visa Online fee table (US$25/10/40/200); Vietnam immigration portal US$25/50; ETA Kenya US$30 plus eCitizen insurance up to US$44; Brazil Miami consulate e-Visa US$80.90; Indonesia e-VOA IDR 500,000 and Bali levy IDR 150,000 (Smartraveller figures); Thailand and Singapore free (visa exemption plus free arrival cards). The atlas's unverified extras (host routes, old steps) moved under `baseline_unverified` in each record. Thailand's atlas text (60 days) was outdated: 30 days from 15 September 2026.

**Notes left in records (`recheck_note`):** us (live ESTA page may show US$40.62), in (business and medical e-Visa fees not reread), ke (reported court suspension of the insurance mandate), br (Canberra embassy page 404).

**Tooling.** `scripts/visa_prep_rechecks.py` holds the verified data; `scripts/recheck_visa_prep.py [ids]` applies it (re-runnable). Add the next countries to `RECHECKS` the same way.

## 2026-11-01 17:55 AEST, Grok: visa-preparation recheck, batch 2 (10 countries)

**Verified 2026-11-01:** jp, kr, nz, ph, cn, ie, ar, uy, tr, za. All visa-free or waiver entries for Australian ordinary passports, so the recorded fee is 0 in local currency (source: Smartraveller entry section read that day). Arrival-form portals cited where they loaded: Visit Japan Web, Korea e-Arrival, NZTD, Philippines eTravel; Irish immigration border page. **Expiry notes:** kr K-ETA exemption and cn visa waiver both end 31 December 2026 unless extended: recheck in December.

## 2026-11-01 18:10 AEST, Grok: visa-preparation recheck, batch 3 (Schengen 10, 6 flagged)

**Verified 2026-11-01:** at, be, ch, de, es, fr, gr, it, nl, pt (Schengen short stays, EES registration at the border, free; ETIAS not started; country-specific notes from each Smartraveller page, including the Austrian and German bilateral agreements to check with their embassies).

**Still flagged (`needs_recheck: true`, reason in `recheck_note`):** ae (stay length 30 vs 90 days, fee), qa (stay length, fee), sa (e-visa fee not readable on the official portal), pw (portal down, arrival fee), my (fee not stated), mx (FMM cost not stated). Next: read ICP/GDRFA (UAE), Hukoomi or MOI (Qatar), visa.visitsaudi.com in a browser, Palau BCBP, imi.gov.my and INM (Mexico).

**Totals now:** 30 of 36 detailed countries verified, 6 flagged. The 165 `baseline-only` cost signals remain unverified.

## 2026-11-01 18:30 AEST, Grok: baseline-only recheck, batch A (Asia-Pacific, 25 countries)

**Verified 2026-11-01 (12):** fj, nu, hk, mo, tw, mn, mv, lk, sb, kh, np, bt. Fees: Solomon Islands Tourist Visa US$100 (now applied for before travel, grace period for visas on arrival); Cambodia e-Visa T US$30 / E US$35; Nepal visa on arrival US$30/50/125 (15/30/90 days); Bhutan visa US$40 plus SDF US$100 a night (discount to 31 August 2027); Sri Lanka tourist ETA free (30 days, no longer on arrival); the rest visa-free or free on arrival. The Cambodia, Nepal and Bhutan pages blocked direct fetches from the box, so they were read via search-index snapshots (noted in each source).

**Flagged (13), reason in `recheck_note`:** ws, ck, vu, fm, mh, tl (on-arrival permits with no fee stated), to (no visa details on Smartraveller), pg, la, mm, bd, bn, pk (visa needed, fee not confirmed on an official page). ki, nr, tv have no Smartraveller page in their entry records and weren't touched.

**Method note.** Smartraveller entry sections for all 141 baseline countries with a Smartraveller URL were fetched to `/tmp/sr2` on the box (scratch, not committed). Specs use helpers `visa()`, `fee()`, `src()`, `flag()` in `scripts/visa_prep_rechecks.py`.

## 2026-11-01 18:45 AEST, Grok: baseline-only recheck, batch B (Europe, 31 countries)

**Verified 2026-11-01 (29):** cy, al, ba, me, mk, rs, xk, md, am, ge, ua, by (visa-free; ua and by under "do not travel" advice, by only via listed airports and only to 31 December 2026), and the Schengen members ro, bg, hr, is, no, dk, se, fi, ee, lv, lt, pl, cz, sk, hu, si, mt (EES at the border, free). Notable: Georgia allows 12 months visa-free; Armenia 180 days a year; Latvia requires health insurance; Montenegro requires address registration within 24 hours.

**Flagged (2):** ru (visa required, fee not confirmed), az (e-visa fee not confirmed).

**Not reached:** ad, sm, mc, va, li, lu have no Smartraveller page in their entry records.

## 2026-11-01 19:05 AEST, Grok: baseline-only recheck, batch C (65 countries, alphabetical)

**Principle from Luke (1 November 2026):** don't prioritise by region. Any country not under Smartraveller "Do not travel" is equally plausible for a spontaneous trip, so work through them alphabetically (or whatever is efficient) and leave "Do not travel" countries until last.

**Verified 2026-11-01 (28):** ao, bo, bs, bw, cl, co, cr, ec, eh (via Smartraveller's Morocco page), gy, hn, jm, kg, kz, ls, ma, mu, om, pe, py, rw, sz, tj, tn, uz, zm (all visa-free or free on arrival), tt (e-Visa TTD 800), mg (under 15 days free plus EUR 10 administration fee). **Notable correction:** Chile dropped its visa requirement for Australians (announced 17 September 2026), so the baseline cost signal is outdated.

**Flagged (37):** bh, bi, bj, bz, ci, cm, cu, dj, do, dz, eg, er, et, ga, gh, gm, gn, gt, ni, sv, il, jo, kw, lr, mr, mw, mz, na, ng, sc, sl, sn, tz, ug, zw, pa, tm. Each `recheck_note` says what Smartraveller confirmed and that the fee wasn't stated; next step is each government's own visa or e-visa fee page.

## 2026-11-01 19:15 AEST, Grok: leftovers and what's next

- **UAE entry (`ae.json` entry note):** still unresolved. No official UAE page lists Australia's on-arrival stay; Emirates (operational) says 90 days, multiple entry; the Ministry of Economy and Tourism says 30 or 90 days by nationality. Note added to the entry record; visa-preparation stays flagged.
- **Fiji 2027 holidays (`fj.json`):** the Fiji Government page still shows 2026 dates; Cabinet reportedly endorsed 11 holidays on 1 October 2026 (third-party report). No Gazette notice found; note added.
- **India work-visa FAQ:** not found at any MHA URL; left as is.
- **"Do not travel" countries left until last, untouched:** af, bf, cd, cf, ht, iq, ir, kp, lb, ly, ml, ne, ps, sd, so, ss, sy, td, ve, ye (still `baseline-only`, `needs_recheck: true`).
- **No Smartraveller page in entry records, untouched:** ad, ag, bb, cg, cv, dm, gd, gq, gw, ki, km, kn, lc, li, lu, mc, nr, sm, sr, st, tg, tv, va, vc. Next: find each Smartraveller page (most exist) and add it to the entry sources, then recheck.
- **Flagged records** (about 60 across all batches): each `recheck_note` names what's missing, usually an official fee page.

## 2026-11-01 16:30 AEST, Grok: batch D1, no-Smartraveller countries (Europe and Caribbean, 13 records)

Smartraveller only has stub pages (no advice) for these 24 countries, so there's no Smartraveller link to add. Instead, `recheck_visa_prep.py` now accepts a `primary` source in a spec: the destination government's page, or Smartraveller's Schengen page for Schengen members and the microstates reached through them. `ofc()` in `visa_prep_rechecks.py` sets it up.

**Verified (13):**
- Europe: lu, li, mc, sm, va (Schengen 90/180, through the Smartraveller Schengen page plus the European Commission), ad (Govern d'Andorra, read via a search snapshot).
- Caribbean: ag (Immigration Department exempt list, 6 months), bb (Foreign Affairs list revised 9 May 2025, 6 months, online form), dm (Commonwealth citizens 6 months), gd (no visa; stay length not stated), kn (Australia not on the visa-required list), vc (not on the visa-required list, read via a snapshot), lc (see below).

The entry records for ag, bb, dm, gd, kn, lc and vc were upgraded from `confirm-in-writing`/`signal` to official, and the aggregator sources were removed.

**Notable correction:** Saint Lucia **requires a visa** for Australians. Immigration Act Schedule 1 (revised 2023) lists Australia; fees are EC$125 single entry and EC$190 multiple entry, through the police visa office. The entry record had assumed the Commonwealth Caribbean norm (visa-free).

## 2026-11-01 16:50 AEST, Grok: batch D2, no-Smartraveller countries (Africa, Pacific, Suriname, 11 records)

**Verified (3):**
- nr: Justice and Border Control visa fees are AUD 50, 150 or 250 for 1, 2 or 3 months, and a sponsor letter is needed.
- ki: Visa Exemption Order 2023, 90 days in 12 months (read via a snapshot).
- tg: voyage.gouv.tg e-visa, XOF 25,000 to 65,000, at least 5 days ahead, visa on arrival suspended.

The ki and tg entry records were upgraded to official.

**Flagged (8)**, with the reasons in each `recheck_note`:
- cv: needs a visa (not on the gov.cv exempt list) plus a CVE 3,400 airport security fee; the visa fee wasn't found.
- st, gw, km, cg, gq: no official page found.
- tv: the regulations PDF wouldn't load to check whether Australians are exempt from the AUD 100 fee.
- sr: the VFS portal blocked fetches.

**Correction:** Cabo Verde is not visa-free for Australians; Australia is absent from the official exempt list.

## 2026-11-01 17:10 AEST, Grok: batch F1, fee pages for flagged records (12 verified)

All 12 now cite the destination government's fee page. Pages that blocked fetches were read via search snapshots (marked SNAP).

| Country | Fee |
|---|---|
| eg | USD 30 (raised from USD 25 on 1 March 2026) |
| il | ETA-IL NIS 25 |
| tz | Ordinary visa USD 50 (Immigration guidelines PDF, September 2026, read directly); the NIC/ZIC insurance cost is still unconfirmed |
| ug | USD 50 (read directly) |
| sc | Travel Authorisation EUR 12.06 |
| et | USD 62 for 30 days |
| jo | JOD 40 |
| zw | USD 30 |
| mw | USD 50 |
| na | N$1,600 |
| kw | KWD 3 (may vary by nationality) |
| bh | BHD 13 single entry or BHD 29 multiple entry |

The Egypt increase is a correction to older baseline figures.

## 2026-11-01 17:30 AEST, Grok: batch F2, fee pages for flagged records (9 verified)

| Country | Finding |
|---|---|
| qa | Ministry of Interior: free 30-day multiple-entry visa, extendable |
| cm | MINREX (read directly): XAF 100,000 ordinary or 150,000 express |
| bj | CatIS: XOF 32,798 single or 49,197 multiple entry, 30 days |
| dj | USD 23 |
| pg | Tourist visa free, plus a US$50 online lodgement fee |
| la | USD 50 (varies by nationality) |
| bd | VOA USD 50 plus processing |
| tl | VOA US$30 cash |
| az | ASAN USD 29 |

Most were read via search snapshots of official pages (marked SNAP).

**Still flagged:** ae, sa, pw, my, mx, ws, ck, vu, fm, mh, to, mm, bn, pk, ru, bi, bz, ci, cu, do, dz, er, ga, gh, gm, gn, gt, ni, sv, lr, mr, mz, ng, sl, sn, pa, tm, plus the 8 no-Smartraveller flags.
- Ghana: the USD 260 e-visa figure came only from non-government reports.
- Saudi Arabia: SAR 535 (non-official site).
- Mozambique: about USD 190 (news report).
None of these were used.

## 2026-11-01 17:45 AEST, Grok: batch F3, fee pages (4 verified)

- my: entry free; the MDAC is free (Immigration Department FAQ, which warns about fake paid sites).
- pk: USD 60 single entry, USD 90 multiple entry (DGI&P fee table).
- vu: visa-exempt for up to 120 days (Vanuatu Immigration).
- cu: tourist card AUD 69 blank or AUD 76 completed (Cuban Embassy in Australia tariff, October 2026).

All four were read via search snapshots.

**Correction to the plan:** Russia (ru) is under Smartraveller "Do not travel", so it moves to the conflict-zones-last list.

**Not done:** mx (the FMM cost isn't on an official page), sa (fee only on non-official sites), ae.

## 2026-11-01 16:40 AEST, Grok: part 3 starts, culture-and-protocol batch 1 (13 records)

`smartraveller_draft.py` changes:
- New `--only culture|local-law|money` option, so it can write one pattern without touching the others.
- The "Local customs" capture now includes its subheadings (Ramadan, Dress and behaviour, ...); before, it stopped at the first one.

Of the 87 places with no culture record and a Smartraveller page, only 23 have a "Local customs" section. The rest (France, Japan, the US and others) have none, so there's nothing official to record yet. For those, own-community sources are the next step.

**Written from Smartraveller's local customs (status ask-locally, evidence official):** ae, bd, dz, eh, gm, id, ke, kg, kz, mh, mo, mr, mv.

## 2026-11-01 17:00 AEST, Grok: culture-and-protocol batch 2 (13 new), and a correction to batch 1

**Correction:** the batch 1 commit (f57bbb0) actually wrote only ae, bd, dz, gm and id. Some Smartraveller pages title the section "Local Laws" (capital L), and `block()` matched headings case-sensitively, so ke, kg, kz, mh, mo, mr and mv were silently skipped. eh has no Smartraveller key of its own (it reads Morocco's page). Heading matching is now case-insensitive. The same bug may have left other pages' local-law drafts empty; that's worth a re-run with `--only local-law` on pages titled "Local Laws".

**This batch:**
- New: ke, kg, kz, mh, mo, mr, mv, mz, pw, tm, tn, uy, xk.
- Refreshed: ma (now includes its Religious festivals subsection).
- ae, bd, dz, gm and id were re-cut at sentence ends with the new `trim()`.

That's 18 new culture records in all. "Do not travel" places with customs sections (af, ml, so, ye) are left until last.

## 2026-11-01 17:20 AEST, Grok: local-law for places without Smartraveller pages, batch 1 (11 records, plus mr)

New `scripts/fcdo_local_law.py`:
- Reads UK FCDO travel advice through the GOV.UK content API and takes the "Laws and cultural differences" section, one law per subheading. Topics come from `smartraveller_draft.topic_for`.
- FCDO is an official government source written for British travellers; each record notes that.
- It never overwrites an existing local-law record (`--force` to override).

**Written:** ad, ag, bb, dm, gd, kn, lc, li, lu, mc, sm. Highlights: camouflage clothing is illegal in ag, bb, dm, gd, kn and lc; smoking in public places is illegal in ag; Monaco fines swimsuits, bare chests and bare feet away from beaches.

**Not written:**
- va: no FCDO page for Vatican City.
- vc: the FCDO page has no laws section.

**Also:** mr's local-law was drafted from Smartraveller with `--only local-law` (2 laws). It was missing because of the case-sensitivity bug.

## 2026-11-01 17:35 AEST, Grok: local-law from FCDO, batches 2 and 3

**Batch 2 (11 countries):** cg, cv, gq, gw, ki, km, nr, sr, st, tg, tv. Notable: same-sex acts are illegal in Kiribati (up to 14 years) and Comoros (up to 5 years); Comoros requires dress covering shoulders to knees and bans public drinking.

**Batch 3 (8 British Overseas Territories):** ai, bm, ky, ms, tc, vg, gi, fk. Notable: Bermuda bans going topless in public and drinking outside licensed premises.

**Not written:** sh (FCDO's St Helena page title didn't match; alias needed).

FCDO sections sometimes include non-law items (money, stray dogs, internet); they are kept with the heading so readers can tell.

## 2026-11-01 18:00 AEST, Grok: states and regions, substances batch 1 (8 records), plus aw and cw local-law

Cannabis rules from state and provincial regulators and statutes:

| Place | Age | Public carry limit | Other |
|---|---|---|---|
| us/california | 21+ | 28.5 g (8 g concentrate) | |
| us/nevada | 21+ | 2.5 oz (raised from 1 oz on 1 January 2024) | no public use; lounges allowed |
| us/new-york | 21+ | 3 oz (24 g concentrate) | use allowed in most places tobacco is |
| us/washington | 21+ | 1 oz | no public use |
| us/michigan | 21+ | 2.5 oz (15 g concentrate) | |
| ca/british-columbia | 19+ | 30 g | |
| ca/ontario | 19+ | 30 g | |
| ca/quebec | **21+** | 30 g | public-use ban |

**Skipped (couldn't confirm on an official page):**
- Illinois: a snapshot claimed a new 30 g non-resident limit from June 2026; the statute page wouldn't load.
- Massachusetts: a snapshot claimed a 2 oz limit from April 2026; the statute page wouldn't load.

**Also:** FCDO local-law records for Aruba (aw) and Curaçao (cw). FCDO has no laws section for the French overseas departments (gf, gp, mq, re, yt) or for io.

**Year-ahead:** the K-ETA (kr) and China waiver (cn) expiries on 31 December 2026 are already in year-ahead through `data/watch.json`. ETIAS has no official start date: the EU site says it is "not in operation" and the date will be announced months ahead. So there's no dated event; recheck in early 2027.

## 2026-11-01 18:15 AEST, Grok: states and regions, local-law (id/bali)

id/bali local-law comes from Governor's Circular 4/2023 on how foreign tourists must behave. Prohibitions 2f to 2h were read directly from the PDF (abuse or aggression including online, working without documents, trading in illegal goods, artefacts or drugs). The dos and don'ts summary (temple main areas, sacred trees, modest dress, licensed guides and money changers, paying in rupiah) came from a Bali Tourism Office snapshot.

**Where to resume:**
- States and regions: more US states (Massachusetts and Illinois need direct statute reads), Phuket, Goa, Hawaii local-law.
- Culture: places with no Smartraveller "Local customs" section need own-community sources.
- Leftovers: re-run FCDO for sh (title alias) and va.
- "Do not travel" places stay last.

## 2026-11-01 18:40 AEST, Grok: St Helena, Vatican, and regions batch 2 (7 places, 8 records)

**St Helena (sh):**
- FCDO title alias added to `fcdo_local_law.py`.
- local-law written (2 laws).

**Vatican City (va):**
- local-law (2) and culture-and-protocol written.
- Source: St Peter's Basilica's own rules (basilicasanpietro.va, the Fabbrica di San Pietro).
- Rules: shoulders covered; long trousers or below-knee skirts; no sleeveless tops, short clothing or hats; no phones, smoking or food inside.

**Cannabis (psychoactive-substances):**

| Place | Status | Limit or penalty | Notes |
|---|---|---|---|
| us/hawaii | No adult use | 3 g or less is a US$130 violation | International visitors can't use the out-of-state medical route |
| us/arizona | 21+ | 1 oz (5 g concentrate) | Smoking in public is a petty offence |
| us/new-jersey | 21+ | 6 oz | Consumption lounges allowed |
| us/florida | No adult use | 20 g or less is a misdemeanour; more is a felony | |

**in/goa local-law:** the Goa Tourism do's and don'ts PDF says drinking, drugs and smoking are banned on all beaches (fine, jail or both), and beaches close at sunset. The fine amounts (INR 2,000 per person, 10,000 per group) are noted as news-reported only.

**Still skipped:** Illinois (the official sources conflict: an IDFPR PDF says 15 g; snapshots claim 30 g from June 2026).

## 2026-11-01 19:00 AEST, Grok: culture-and-protocol from countries' own guidance (9 records)

These countries have no Smartraveller "Local customs" section, so the records come from each government's or national tourism body's own visitor guidance (status community-published; all read via search snapshots):
- jp: JNTO manners, onsen and tipping guides.
- nz: the Tiaki Promise (Tourism NZ).
- is: the Icelandic Pledge (Visit Iceland, Icelandic Tourist Board).
- kr: Korea.net and VisitKorea etiquette.
- pe: Machu Picchu code of conduct (Ministry of Culture).
- ec: Galápagos National Park visit rules, reissued in the Registro Oficial of 14 September 2026.
- se: allemansrätten (Naturvårdsverket).
- no: allemannsretten (Norwegian Environment Agency); camp at least 150 m from homes, up to 2 nights.
- fi: everyone's rights (Ministry of the Environment).

**Next:** fr, it, es, gb, de, us and others have no such national etiquette page; look for site-level rules (for example Venice's access fee, the Acropolis) or leave them as ask-locally.

## 2026-11-01 19:20 AEST, Grok: year-ahead, official dated events, batch 1 (5 places, 6 events)

Events are tagged `"by": "official-events"`, so the election and watch scripts won't replace them.
- it/veneto: Venice access fee runs 72 days from 26 March to 15 August 2027 (Comune di Venezia).
- br/rio-de-janeiro: Carnival parades 5 to 9 February 2027 (Riotur); Women's World Cup opener 24 June 2027 and final 25 July 2027 at the Maracanã (FIFA).
- br: Women's World Cup, 24 June to 25 July 2027.
- de/bavaria: Oktoberfest, 18 September to 3 October 2027 (oktoberfest.de).
- rs/city-of-belgrade: Expo 2027, 15 May to 15 August (BIE).

**Not added:**
- Thailand's tourism entry fee: only a news report (THB 450, possibly April 2027); no Royal Gazette notice yet.
- Hajj 2027 dates: expected around 14 to 19 May, subject to moon sighting; no official date.
- Japan's departure tax rise to JPY 3,000: already took effect on 1 July 2026, so it's in the past.

## 2026-11-01 16:55 AEST, Grok: photo review, batch 1 of 4 (ad to cz, 68 photos)

Luke asked me to apply the verdicts myself: approve the confirmed photos, reject the denied ones, and keep the unsure list short.
- **Method:** I looked at each place photo as a 330 px thumbnail and judged it against its place. I also read each file's camera EXIF on Commons to enforce the no-drone rule.
- **Approved:** marked with `review: approved` plus the file title in `site/heroes/place-photo-choices.json`.
- **Rejected:** set to `use: none` with `review: rejected` and the reason.
- **Script change:** `place_photos.py` now carries an approval through a rebuild, but only for the exact file that was judged.
- **Audit trail:** `data/photo-review-recommendations.json` and `docs/PHOTO-REVIEW-RECOMMENDATIONS.md`.
- **Batch 1:** 65 confirmed, 3 denied (au/nsw and au/sa are orbit views; au/qld is generic palm fronds), 0 unsure.

## 2026-11-01 16:33 AEST, Grok: photo review, batch 2 of 4 (dj to kz, 73 photos)

Same method and mechanism as batch 1: 63 confirmed and approved, 10 denied and rejected, 0 unsure. Denied: fj gf gn id io jm jo jp ke km . Reasons are in docs/PHOTO-REVIEW-RECOMMENDATIONS.md.

## 2026-11-01 16:33 AEST, Grok: photo review, batch 3 of 4 (lb to sz, 89 photos)

Same method and mechanism as batch 1: 85 confirmed and approved, 4 denied and rejected, 0 unsure. Denied: md mo ms pf . Reasons are in docs/PHOTO-REVIEW-RECOMMENDATIONS.md.

## 2026-11-01 16:33 AEST, Grok: photo review, batch 4 of 4 (tc to zw, 86 photos)

Same method and mechanism as batch 1: 67 confirmed and approved, 19 denied and rejected, 0 unsure. Denied: tl tm tn us/delaware us/florida us/indiana us/maryland us/michigan us/montana us/new-mexico us/ohio us/papahanaumokuakea us/tennessee us/texas us/virginia us/west-virginia us/wisconsin vc yt . Reasons are in docs/PHOTO-REVIEW-RECOMMENDATIONS.md.

## 2026-11-01 16:38 AEST, Grok: replacement photos, batch 1 (9 places)

For photos rejected in review, I approved openly licensed Wikimedia Commons replacements (curated file plus a choices entry that keeps the rejected title). Each one was viewed, has a CC or public-domain licence and is at least 1600 px wide, with no drone camera in EXIF. Places: au/nsw, au/qld, au/sa, fj, gf, id, jm, jo, jp.

## 2026-11-01 16:38 AEST, Grok: replacement photos, batch 2 (9 places)

For photos rejected in review, I approved openly licensed Wikimedia Commons replacements (curated file plus a choices entry that keeps the rejected title). Each one was viewed, has a CC or public-domain licence and is at least 1600 px wide, with no drone camera in EXIF. Places: ke, km, md, mo, ms, pf, tl, tm, tn.

## 2026-11-01 16:38 AEST, Grok: replacement photos, batch 3 (15 places)

For photos rejected in review, I approved openly licensed Wikimedia Commons replacements (curated file plus a choices entry that keeps the rejected title). Each one was viewed, has a CC or public-domain licence and is at least 1600 px wide, with no drone camera in EXIF. Places: us/delaware, us/florida, us/indiana, us/maryland, us/michigan, us/montana, us/new-mexico, us/ohio, us/tennessee, us/texas, us/virginia, us/west-virginia, us/wisconsin, vc, yt.

## 2026-11-01 16:39 AEST, Grok: photo review status and the au correction

- **au (Uluṟu sunset):** I approved this in batch 1 by mistake. It is back to pending, because Luke is deciding.
- **PHOTO-REVIEW.md updated:** 313 places have a photo (312 approved, 1 pending). 3 rejected places still have no replacement: gn, io, us/papahanaumokuakea.

## 2026-11-01 16:40 AEST, Grok: year-ahead, official dated events, batch 2 (10 places)

- gb/scotland, gb/wales and fr: Tour de France 2027. Team presentation 30 June in Edinburgh; stage 1 from Edinburgh 2 July; stage 3 to Cardiff 4 July; French stages 6 to 25 July (letour.fr, City of Edinburgh Council).
- kr/seoul: World Youth Day, 3 to 8 August 2027 (Holy See dicastery and WYD Seoul).
- sa: AFC Asian Cup, 7 January to 5 February 2027 (AFC).
- pe/lima-department: Pan American Games, 23 July to 8 August 2027 (Panam Sports).
- in/maharashtra: Nashik-Trimbakeshwar Kumbh Amrit Snan dates. The Kumbh Mela Authority plan marks these as interim.
- za, zw and na: ICC Men's Cricket World Cup, 2 October to 21 November 2027 (ICC).

## 2026-11-01 16:42 AEST, Grok: high-visitor regions, batch (10 records)

- th: cannabis flower has been a controlled herb since 23 June 2025 and needs a Thai prescription (TAT notice via thailand.go.th).
- th/phuket and th/krabi: DMCR beach smoking order 864/2563 covers Patong and three Ko Lanta beaches, with a penalty of up to THB 100,000. The order was for two years; a renewal is not confirmed, and the rule says so.
- hr/dubrovnik-neretva-county: no swimwear in the old town (Grad Dubrovnik).
- gr/south-aegean-region: Santorini and Mykonos cruise fee of EUR 20 in peak season (Ministry of Tourism).
- pt/lisbon: EUR 4 tourist tax (Câmara Municipal de Lisboa).
- ae/emirate-of-dubai: Tourism Dirham (Dubai Legislation Portal).
- jp/kyoto-prefecture: Kyoto City accommodation tax, JPY 200 to 10,000 from March 2026.
- es/balearic-islands: ITS sustainable tourism tax.
- it/lazio: EUR 2 Trevi Fountain ticket since 2 February 2026 (Roma Capitale).

Fees are filed under the local-law topic work-and-payment, because money-and-cost uses nearest-level inheritance and a regional record would hide the national currency notes.

## 2026-11-01 16:44 AEST, Grok: culture, national and regional guidance (10 records)

- community-published: gb (Countryside Code, GOV.UK), gb/scotland (Scottish Outdoor Access Code, NatureScot), us/hawaii (DLNR Nā Wahi Pana and HTA responsible travel), de (deutschland.de etiquette guide, read directly), it/lombardy (Milan Duomo regulation, July 2025).
- partly-mapped: us (NPS Leave No Trace and archaeological-site guidelines), es (spain.info hours, greetings and tipping), ca (Parks Canada wildlife distances and cultural sites).
- ask-locally: it and fr. Neither has a national government etiquette page (italia.it and france.fr checked); site rules apply.

## 2026-11-01 16:46 AEST, Grok: visa preparation, "Do not travel" countries, part 1 (11 records)

Reread Smartraveller's visa text for af, bf, cd, cf, ht, iq, ir, kp, lb, ly and ml. No page states a fee, so all 11 stay needs_recheck with a dated recheck_note giving the visa rule (Do not travel first). Added as batch DNT in scripts/visa_prep_rechecks.py.

## 2026-11-01 16:46 AEST, Grok: visa preparation, "Do not travel" countries, part 2 (10 records)

- ve: verified from Smartraveller. In most cases no visa is needed for tourist visits under 90 days; the Do not travel note is kept.
- ne, ps, sd, so, ss, sy, td, ye and ru: flagged with the reread visa rules; no fees stated.

## 2026-11-01 16:47 AEST, Grok: culture, "Do not travel" countries (4 records)

Smartraveller customs sections drafted as ask-locally for af, ml, so and ye. cd, cf, ht, ru and ve have no customs section ("nothing new"). This is a short batch because it is the whole remainder of the Do-not-travel culture list.

## 2026-11-01 16:49 AEST, Grok: Culture from FCDO customs guidance, batch 1 (12 records)

New script scripts/fcdo_culture.py takes only customs subheadings (dress, behaviour, religion, Ramadan) from FCDO's laws and cultural differences section. Status is partly-mapped, and each record is flagged as written for British travellers. Laws stay in local-law. Places: ag ai be bm cn cz dk dm eh gd gq ki.

## 2026-11-01 16:49 AEST, Grok: Culture from FCDO, batch 2 (7 partly-mapped, 7 ask-locally) (14 records)

Same method as batch 1. Places where FCDO has no customs subheading get ask-locally, naming the government and tourism office as authority. Places: km la lc mc ms pt tt bb kn ky ug zw ad ao.

## 2026-11-01 16:50 AEST, Grok: Culture from FCDO, batch 3 (ask-locally) (15 records)

FCDO has no customs subheading for these places and no national etiquette page was found, so they are ask-locally with the named authority. Places: ar aw bi bs bw bz cg ch cl co cu cv cw cy do.

## 2026-11-01 16:50 AEST, Grok: correction to culture batches 2 and 3 (22 records)

The ask-locally text said no national etiquette page was found, but I had not searched for one. The text and notes now say a national page has not been searched for yet. The batch 3 entry above overstated this. The script wording is fixed too.

## 2026-11-01 16:50 AEST, Grok: Culture from FCDO, batch 4 (ask-locally) (15 records)

FCDO has no customs subheading for these places, so they are ask-locally with the named authority. National etiquette pages have not been searched yet. Places: ee fk ga gf gi gp gw gy hk ie io jm li ls lt.

## 2026-11-01 16:51 AEST, Grok: Culture from FCDO, batch 5 (ask-locally) (15 records)

FCDO has no customs subheading for these places, so they are ask-locally with the named authority. National etiquette pages have not been searched yet. Places: lu lv me mq mt ni nl nr pl py re rw sh si sm.

## 2026-11-01 16:51 AEST, Grok: Culture from FCDO, batch 6 (ask-locally) (13 records)

FCDO has no customs subheading for these places, so they are ask-locally with the named authority. National etiquette pages have not been searched yet. Places: sr st sv sz tc tg tv tw vc vg yt za zm.

## 2026-11-01 16:52 AEST, Grok: Culture for places with no FCDO page, batch 1 (aq, sj official; as, ax, bl, bq, cq, fo, gg, gl ask-locally) (10 records)

- aq: Antarctic Treaty General Guidelines for Visitors (ats.aq).
- sj: Governor of Svalbard rules (polar-bear distances, pre-1946 heritage, firearms) and Visit Svalbard.
- The other 8 are ask-locally with the named authority and no sources. No official etiquette page has been searched for them yet.

## 2026-11-01 16:52 AEST, Grok: Culture for places with no FCDO page, batch 2 (ask-locally) (14 records)

gs, gu, im, je, mf, mp, pm, pn, pr, sx, tf, tk, vi and wf are ask-locally with the named authority (for example Tokelau's Taupulega village councils and Wallis and Futuna's customary kingdoms). No official etiquette page has been searched for these yet.

## 2026-11-01 16:52 AEST, Grok: Culture, Do-not-travel places from FCDO (5 records)

cd, cf, ht, ru and ve have no Smartraveller customs section, so these come from FCDO's laws and cultural differences section, written for British travellers.

## 2026-11-01 16:53 AEST, Grok: STATUS.md gaps revised

Rewrote the hand-written gap list to current counts (culture 244 of 247; local law missing for 35; substances missing for 72; visa prep 60 baseline; photos reviewed).

Correction: 206 of the 244 culture records are ask-locally, not about 80 (fixed in STATUS.md).

## 2026-11-01 16:55 AEST, Grok: Culture national-source search ad-ba (12 records)

Searched national tourism boards and government etiquette pages for 12 ask-locally culture records. Upgraded 9: ad, am, az and at are partly mapped; ae, ar, as, aw and ax are community-published. Searched with none found for 3 (al, ao, ba), which stay ask-locally and are recorded under national_search. The ad source is French Government advice, written for French travellers.

## 2026-11-01 16:56 AEST, Grok: Culture national-source search bb-bs (12 records)

Searched national tourism boards and government etiquette pages for 12 ask-locally culture records. Upgraded 9: bb, bd, bg, bh, bj, bl, bo, bq and bs are partly mapped; bn is community-published. Searched with none found for bi and br.

## 2026-11-01 16:57 AEST, Grok: Culture national-source search bt-co (10 records)

Searched national tourism boards and government etiquette pages for 10 ask-locally culture records. Upgraded 8: bw, bz, ch, cl and co are partly mapped; bt, ck and cm are community-published. Searched with none found for by and ci. Correction to the bb-bs entry: 10 records were upgraded, not 9 (bn is community-published, plus 9 partly mapped).

## 2026-11-01 16:58 AEST, Grok: Year-ahead 2027 official events by category (11 records)

Extended the year-ahead schema (version 2) with an optional event category field; validate.py now checks it. Event category list for Claude: wellbeing-spiritual, technology, music, dating-marriage-adult, film, national-day, arts-culture, sport, religious-pilgrimage, election, other. Added 13 official-events entries across 11 records: ad, ae, am, ar, at (2), de (2), dk, fr, hu, id and jp. All sources are organiser or government pages. Skipped (no official 2027 dates yet): GITEX Global, Web Summit, TIFF and Tomorrowland. Rock in Rio is biennial, with no 2027 edition. ad and ae are fixed-date national days, cited from government holiday pages.

## 2026-11-01 16:59 AEST, Grok: Year-ahead 2027 official events batch 2 (11 records)

Added 12 official-events entries across 11 records: gb__scotland (Fringe), gb (Glastonbury), it (Biennale Architettura), es__catalonia (MWC), mx (Independence Day), in__uttarakhand (International Yoga Festival), gh (Independence Day), ch (Montreux Jazz), cl (Viña del Mar), co (Barranquilla Carnaval) and pt (Primavera Porto, NOS Alive). Skipped (no official 2027 dates yet): Slush, Avignon, Mawazine, TIFF and Biennale Arte. Lisdoonvarna Matchmaking Festival 2027 is not yet confirmed on its official site, and the Kenya and Philippines national days had no official 2027 source in hand. Categories as in the earlier entry.

## 2026-11-01 17:01 AEST, Grok: Year-ahead 2027 events: tech, adult and national days (10 records)

Added 11 official-events entries across 10 records. Technology: IFA (de), CES (us), COMPUTEX (tw), VivaTech (fr). Dating-marriage-adult: Folsom Europe (de), Fetish Weekend London (gb). Other: EuroPride Torino (it). National days: al, am, bb and bs, from government or statute pages for fixed dates. New watchlist data/calendar/pending-official-dates.json holds 12 events without official 2027 dates (GITEX, Web Summit, Slush, Tomorrowland, TIFF, Lisdoonvarna, Avignon, Mawazine, Biennale Arte, Rock in Rio, and the ke and ph national days) for routines to add later. The Castres erotic fair has no exact 2027 date, so it was not added.

## 2026-11-01 17:01 AEST, Grok: Culture national-source search cq-eg (11 records)

Searched national tourism boards and government pages for 11 ask-locally culture records. Upgraded 7: cq, cv, cy, ee and eg are partly mapped; cw and do are community-published. Searched with none found for cr, cu, dj and dz.

## 2026-11-01 17:03 AEST, Grok: Activities: tourism confirm-in-writing upgraded from official entry sources (15 records)

15 tourism activity checks marked confirm-in-writing already had official entry records, so I upgraded them using those citations. Low: ag, bb, cq, dm, fo, gd, gg, gl, im, je, ki, kn, vc. Conditional (visa or e-Visa before travel): lc, tg. Other activities (work, speaking and so on) are unchanged because they need labour or immigration pages for each activity. 49 tourism checks remain confirm-in-writing, mostly places whose entry record also lacks an official source.

## 2026-11-01 17:04 AEST, Grok: Entry and tourism: official immigration sources replace confirm-in-writing (10 records)

Researched official immigration pages for 10 places whose tourism check was confirm-in-writing; updated both the entry and the tourism activity. Visa-free (low): aw, bq, cw and sx (Kingdom of the Netherlands no-visa list, read directly), ai (Anguilla visa-required list from 2018, Australia absent, read directly) and fk (Falkland Islands Government, snapshot). Visa on arrival (low): sn (Senegal Embassy London Category B list, read directly). Visa or e-Visa before travel (conditional): cv (Australia absent from the gov.cv exempt list, read directly; EASE pre-registration), ci (SNEDAI e-Visa, snapshot) and gn (PAF e-Visa, snapshot). Tried and still unconfirmed: bm (Order 2026 list not readable) and gm (gambia.gov.gm timed out).

## 2026-11-01 17:05 AEST, Grok: Entry and tourism: official sources for overseas France, TCI, BVI, Gibraltar (11 records)

Upgraded 11 confirm-in-writing tourism checks (and their entry records) to visa-free, low. gf, gp, mq, re and pm: Légifrance arrêté of 26 July 2011. bl and mf: arrêté of 18 April 2012 as amended in 2021. yt: arrêté of 4 February 2015 as amended in 2021. In every French case the exemption excludes paid work without French authorisation. tc: TCI Border Force exempt list. vg: BVI visa-required list, Australia absent. gi: Gibraltar notice 558.1/2026 (Schengen alignment from 15 July 2026). All read via search-index snapshots. Not upgraded: ky (Australia not visible in the snapshot of the list), to (only a Tongan embassy page in China found), tf and wf (separate legal regimes, not yet found).

## 2026-11-01 17:06 AEST, Grok: Entry and tourism: Schengen micro-states, Caribbean and African territories (10 records)

Upgraded 10 confirm-in-writing tourism checks. ad, mc, sm and va: Regulation (EU) 2018/1806 Annex II (Australia visa-exempt), low. ky: Cayman CBC country list, read directly, visa not required. ms: Montserrat visa-not-required list, low. km: visa on arrival (Comoros national tourism office), low. sr: Entry Fee before travel via the official VFS partner, conditional. st: visa needed, not on the exempt list, conditional. aq: tourism set to conditional on Australian Antarctic Division environmental authorisation, citing the existing entry source. Remaining non-conflict: bm, cg, eh, gm, gq, gs, gw, io, sh, sj, tf, to, tv, wf.

## 2026-11-01 17:07 AEST, Grok: Culture national-source search er-gl (10 records)

Searched national tourism boards and government pages for 10 ask-locally culture records. Upgraded 6: er, fm and ge are partly mapped; fj, fo and gl are community-published. Searched with none found for et, fr, ga and gh. The fm source is the FSM Embassy in Japan's visitor guide.

## 2026-11-01 17:07 AEST, Grok: Year-ahead 2027: less-visited countries (10 records)

Added 10 official-events entries across 10 records. National days: bw, bz (Belize 2027 holiday list), fj, ge, jm, ke, cv, and mn (Naadam, by law). Music: Sauti za Busara (tz) and Gnaoua Essaouira (ma). Watchlist: removed ke (now added); added Paro Tshechu and Bhutan National Day (no official source), Lake of Stars (dates to come), and FESPACO 20 to 27 March, held for the Do-not-travel pass because bf is Do not travel.

## 2026-11-01 17:08 AEST, Grok: Activities: paid-speaking from official labour and immigration law (10 records)

Upgraded the paid-speaking check from confirm-in-writing to conditional for 10 places, with citations. gf, gp, mq, re, pm, bl, mf and yt: the French entry arrêtés exclude paid activity that needs an autorisation de travail. vg: BVI Immigration Department FAQ (work permit for gainful employment). ky: Cayman Immigration Regulations guest-speaker exemption (single or occasional event, up to 10 days) and WORC Business Visitor's Permit. Other activities stay confirm-in-writing.

## 2026-11-01 17:08 AEST, Grok: user note on separate datasets

User note: world-travel-patterns, aura-affinity, outreach-cms, global-founder-atlas and right-time-right-place are separate, standalone datasets. The user's oracle pulls from each one in batches on request. Do not link them, import between them or integrate them. No cross-repo wiring.

## 2026-11-01 17:10 AEST, Grok: Entry and activities: last non-conflict confirm-in-writing tourism checks (10 records)

Upgraded the entry and tourism checks for 10 places from official sources. tv: Immigration Regulations 2014, visitor permit on arrival; all 14 work and speaking activities set from regulation 2 (business endorsement; conferences explicitly count as business). sj: Governor of Svalbard and UDI, no visa or work permit; all activities low, with a means requirement. gs: Entry Control Ordinance 2022 visitor or work permits; Regulated Activity Permit for filming and research. wf: Légifrance arrêté, Australia exempt; paid activities conditional. sh: St Helena permit on arrival, Ascension e-visa. tf: TAAF visa and prefect approval (specialist). io: BIOT permit applications paused since 31 March 2026. to: visa on arrival. gq: e-Visa. cg: visa before travel. Still open: bm, eh, gm and gw, plus the Do-not-travel places af, bf, ps and so.

## 2026-11-01 17:11 AEST, Grok: Culture national-source search gm-hr (10 records)

Searched national tourism boards and government pages for 10 ask-locally culture records. Upgraded 8: gp, gr, gu, gy and hn are partly mapped; gm, gs and hk are community-published. Searched with none found for gt and hr. gn and gw were not covered in this batch.

## 2026-11-01 17:12 AEST, Grok: Year-ahead 2027: national days and festivals, gy to sv (10 records)

Added 10 official-events entries (all national days) across 10 records: gy (Mashramani), hr, is, id (2027 SKB decree), gt, hu (St Stephen's Day programme), ie (St Patrick's Festival), cr, sv and fo (Ólavsøka). Honduras was dropped because the only source was a private legal database. Watchlist additions: Iceland Airwaves, Hornbill, Jerash and the Fes Sacred Music festival (no official 2027 dates).

## 2026-11-01 17:13 AEST, Grok: Activities: work and speaking checks from official labour and immigration rules (ad to bb) (10 records)

Read each country's official labour or immigration source once and applied it only to the activities it covers. Places: ad (form H1 short-term work notice), ag (Labour Department work permit), ai (Department of Labour permits), al (Law 79/2021: business visitors under a month exempt; lecturers only under agreements), am (Law on Foreigners lecturer exemption), ao (SME: paid work needs a work visa), aw (DIMAS short-term project permits), az (Migration Code lecturer exemption and 90-day business-trip list), ba (Article 77: lecturers, artists and conference lecturers up to 90 days with Form 17), bb (Immigration Act: short-term work permit). Activities the sources don't address stay confirm-in-writing.

## 2026-11-01 17:14 AEST, Grok: Entry and activities: gm and gw tourism, and work and speaking checks (ax, bd, bh, bj, bn, bo, bs, fi) (10 records)

gm entry is now visa-free (Australia is on the Gambia's exemption list). gw is now visa on arrival (France Diplomatie and the U.S. State Department). Work and speaking: fi and ax (Migri: lecturers, experts and artists can work 90 days without a permit), bh (LMRA: temporary work under 15 days exempt), bd (B and T visas; BIDA permit for paid work), bj (business e-visa), bn (Professional Visit Visa), bo (Objeto Determinado visa), bs (Short Term Work Permit; entertainers 30 days ahead). Sources were read via search-index snapshots.

## 2026-11-01 17:15 AEST, Grok: Culture: national etiquette upgrades (hu to jm) (10 records)

Upgraded hu, id (2025 Bali circular for foreign tourists), ie, il (Western Wall and Shabbat), im (Fairy Bridge custom), in, it (St Peter's and Pantheon dress rules, Florence fines), je and jm to partly-mapped from national tourism or official sources. io: searched, none found. Sources were read via search-index snapshots.

## 2026-11-01 17:16 AEST, Grok: Year-ahead: 2027 national days (ag to lt) (10 records)

Added national-day events from official holiday laws or government pages for ag, ao, aw, ax, az, be, bg, cz, ee and lt. These are fixed statutory dates. bd was skipped because the official 2027 gazette isn't out yet. Antigua Carnival 2027 (20 July to 3 August) appears only in news reports, so it wasn't added.

## 2026-11-01 17:17 AEST, Grok: Activities: Nordic and central European speaker and artist exemptions (cz, dk, ee, hu, lv, no, pl, se, si, sk) (10 records)

Applied each country's official work-permit exemption rules to speaking, teaching, artist and research activities. se (lecturers up to 3 months, artists via listed arrangers for 14 days), no (lecturers under 3 months, artists 14 days with police notice), dk (lecturers 90 days, speakers 1 to 2 days), cz (s.98(d): 7 days per engagement, 30 a year), pl (lectures and performances 30 days a year from December 2025), ee (5 days in 30 without registration), hu (10 working days), sk (30 days), lv (artists 14 days), si (lecturers at professional meetings outside the Act). Read via search-index snapshots.

## 2026-11-01 17:18 AEST, Grok: Activities: speaker and artist work rules (bg, hr, is, lt, lu, me, mk, mt, ro, rs) (10 records)

Applied official rules: lu (conference speakers and lecturers exempt under 3 months), is (artists and academics 90 days with notice), rs (Article 3: lecturers at professional meetings and artistic work 90 days in 180), hr (work registration certificate up to 90 days), me (work registration), mk (artists 7 days), lt (performers and lecturers need no work permit but still need a residence route), ro (minister's order), bg (single permit, no labour-market test), mt (employment licence under six months). Read via search-index snapshots.

## 2026-11-01 17:18 AEST, Grok: Culture: national etiquette upgrades (jo to lk) (10 records)

Upgraded jo, ke, kg, kh (APSARA Angkor dress code), kn (camouflage clothing illegal), kw, ky (public nudity offence), kz, li and lk (Buddha imagery) to partly-mapped from national tourism or government sources. Read via search-index snapshots.

## 2026-11-01 17:19 AEST, Grok: Activities: Americas, Africa and Asia speaker and artist routes (bt, bw, by, bz, co, cr, cu, cv, do, ec) (10 records)

Notable: co (Resolution 5477/2022: paid speakers and artists need the V Eventos visa even when visa-exempt), bz (entertainer TEP from BZ$600 for a week or less), by (invited university lecturers exempt for 90 days), bw (Emergency Work Permit up to 3 months), plus cr, cu, cv, do, ec and bt visa routes. Read via search-index snapshots.

## 2026-11-01 17:20 AEST, Grok: Culture: national etiquette upgrades and searches (lr to mg) (10 records)

Upgraded ls, lu, ma (Hassan II Mosque visit rules), md, mf (2024 Saint-Martin Tourism Code) and mg (fady taboos) to partly-mapped. lr, lt, lv and me: searched, none found (Budva's swimwear fines appeared only in news reports). Read via search-index snapshots.

## 2026-11-01 17:21 AEST, Grok: Activities: Crown Dependencies and other speaker routes (gd, ge, gg, gh, gi, gl, il, im, je, ph) (10 records)

Notable for speakers: je and im (pre-arranged paid lectures, conference talks and artistic work allowed for visitors within 30 days), gg (paid engagement up to a month), gl (invited lecturers under 3 months exempt), gi (free route for presentations under 48 hours), ge (short-term registration since March 2026), ph (Special Work Permit for artists), il (B/1 fast track), gh, gd. Read via search-index snapshots.

## 2026-11-01 17:23 AEST, Grok: Entry and activities: bm and eh tourism, and Caribbean work rules (dm, gy, jm, kn, lc, sr, tt, vc) (10 records)

bm is visa-free (180 days). eh is visa-free under Moroccan rules, but tourism is conditional because independent travellers may be turned back. Notable: tt (no work permit for one period of up to 30 days in 12 months). Elsewhere, paid speakers and artists need a permit or exemption: lc, dm, sr, vc, jm and kn. gy treats seminars and events as visitor purposes. Read via search-index snapshots.

## 2026-11-01 17:24 AEST, Grok: Culture: national etiquette upgrades (mh to mv), plus a vc text fix (11 records)

Upgraded mh, mk, mm (Shwedagon dress rules), mn (ger etiquette), mo, mp, mq (All Saints cemetery conduct), mt (St John's Co-Cathedral rules), mu and mv (local island rules) to partly-mapped. Also fixed a stray backslash in vc's work-permit fee text from the previous batch. Read via search-index snapshots.

## 2026-11-01 17:24 AEST, Grok: Year-ahead: 2027 national days (bh to pl) (10 records)

Added fixed-date national days from official holiday laws, calendars or circulars for bh, bn, bo, cy, es (the 2027 BOE calendar is already published), fi, gr, lv, mt and pl.

## 2026-11-01 17:25 AEST, Grok: Activities: Gulf, Central and South Asia speaker rules (kg, kw, kz, la, mn, np, om, pk, tj, uz) (10 records)

Notable: uz (lecturers and master classes under one month exempt), kz (artists exempt; business trips up to 120 days a year), pk (the Others visa covers conferences and cultural events; apply 6 weeks ahead), kw (visit visa forbids speaking work; PAM permit needed), plus om, mn, kg, la, np and tj. qa had no remaining confirm-in-writing entries. Read via search-index snapshots.

## 2026-11-01 17:26 AEST, Grok: Year-ahead: 2027 technology, music and arts events (br, ca, ch, de, es, fr, gb, it, sa, tw) (10 records)

Strengthened technology with organiser-published 2027 dates: MWC Barcelona (1 to 4 March), LEAP Riyadh (12 to 15 April), Web Summit Vancouver (25 to 28 May), COMPUTEX (1 to 4 June), VivaTech (16 to 19 June) and gamescom (23 to 29 August). Also added Oktoberfest (18 September to 3 October), Venice Carnival (23 January to 9 February), Rio Sambadrome (5 to 13 February), Edinburgh Fringe (6 to 30 August) and Montreux Jazz (2 to 17 July). Watchlist: GITEX status updated (December 2027 only), Lisdoonvarna noted (runs through September, 2027 programme pending), TechCrunch Disrupt added. Dating-marriage-adult is still thin; no 2027 official dates found yet. Read via search-index snapshots.

## 2026-11-01 17:27 AEST, Grok: Culture: national etiquette upgrades and searches (mx to nu) (10 records)

Upgraded mx (INAH site rules), my (mosque rules), na (photography fees), nc (customary gesture), nl (Amsterdam ban zones), np, nr and nu (Sunday rules) to partly-mapped. mz and ni: searched, none found. Read via search-index snapshots.

## 2026-11-01 17:28 AEST, Grok: Activities: southern and east African speaker routes (mu, mw, na, rw, sc, sz, tz, ug, zm, zw) (10 records)

Notable: mu (entertainers exempt for public shows up to 90 days a year), na (short-term work visa names speakers and conference facilitators; about 10 working days), rw (V5 conference visa; R special pass for paid work), sc (even unpaid work needs a Gainful Occupation Permit), ug (Special Pass USD 400), plus tz, zm, zw, mw and sz. Read via search-index snapshots.

## 2026-11-01 17:29 AEST, Grok: Activities: Pacific, Timor-Leste and West Africa speaker routes (ci, cm, fm, ki, pg, pw, sb, sn, tl, ws) (10 records)

Notable: sb (30 days with no permit if paid by your normal overseas employer), fm (visitors can do contract work under 90 days), sn (temporary artistic or literary activity up to 4 months on a stay authorisation, which suits book tours), tl (specialised-activity visa), pg (the business visa doesn't cover paid talks), plus ws, pw, ki, ci and cm. vu, ck and nu were already resolved. Read via search-index snapshots.

## 2026-11-01 17:30 AEST, Grok: Culture: national etiquette upgrades and searches (om to pr) (10 records)

Upgraded om (heritage ministry dress guidelines), pa (Guna Yala rules), pf (marae rules), pg, ph (Boracay guide), pk, pm, pn (Sabbath, no alcohol in public) and pr to partly-mapped. pl: searched, none found. Read via search-index snapshots.

## 2026-11-01 17:31 AEST, Grok: Work: gm, sl, lr, st, lk, kh, gh, ke, cv, bd (10 records)

Work and speaking rules from official immigration and labour sources for gm (GMB2), sl, lr, st, lk (Business ETA covers conferences under one month), kh, gh, ke (KFCB filming licence), cv (EASE) and bd. Madagascar was skipped because no official source was found. Read via search-index snapshots.

## 2026-11-01 17:32 AEST, Grok: Culture: cg, fk, gf, gg, gi, gn, gw, mr, mw, ng (10 records)

Upgraded fk (Countryside Code), gf (Parc amazonien village conduct), gg, gi (macaque feeding penalty GBP 500), mw, gw (IBAP sacred sites) and ng to partly-mapped. mr, cg and gn: searched, none found. Read via search-index snapshots.

## 2026-11-01 17:32 AEST, Grok: Culture: pw, py, qa, re, ro, rs, rw, sa, sb, sc (10 records)

Upgraded pw (Palau Pledge, sunscreen ban), qa, sa (public decency fines), rw (plastic ban), ro (regional Harghita code), rs, re (Tamil temples), py (tereré) and sb (kastom permission) to partly-mapped. sc: searched, none found. Read via search-index snapshots.

## 2026-11-01 17:33 AEST, Grok: Culture: sg, sh, si, sk, sl, sm, sn, sr, st, sv (10 records)

Upgraded sg (gum import ban, litter fines), sh, si, sk and sv to partly-mapped. sm, sn, sr, sl and st: searched, none found. Read via search-index snapshots.

## 2026-11-01 17:34 AEST, Grok: Culture: sx, sz, tc, tf, tg, tj, tk, tl, tm, tn (10 records)

Upgraded tn, tc (protected-area fines), sz (Incwala), tk (Taupulega permit), tl (Pledge, Jaco day only), tf (landing authorisation) and sx to partly-mapped. tj, tm and tg: searched, none found. Read via search-index snapshots.

## 2026-11-01 17:34 AEST, Grok: Culture: to, tr, tv, tw, tz, ua, ug, uy, uz, vc (10 records)

Upgraded to (Sunday law), tr (Diyanet mosque rules), tw (regional temple etiquette), tz, ug (UWA gorilla rules), uz and uy to partly-mapped. tv, ua and vc: searched, none found. Read via search-index snapshots.

## 2026-11-01 17:35 AEST, Grok: Culture: vg, vi, vn, vu, wf, ws, xk, yt, za, zm, zw (11 records)

Upgraded vn (Decision 718 code), vu, ws (Sa curfew), vi (sunscreen ban), wf, za, zm and zw to partly-mapped. yt, vg and xk: searched, none found. All non-Do-not-travel culture records have now been searched. Read via search-index snapshots.

## 2026-11-01 17:36 AEST, Grok: Events 2027: ma, kz, ke, mn, rs, pf, de, br, qa, sa (10 records)

Added official 2027 dates: GITEX Africa, GITEX AI Kazakhstan, Africa Tech Summit Nairobi, Naadam, Expo 2027 Belgrade, Pacific Games Tahiti, documenta 16, Web Summit Rio, Web Summit Qatar and the AFC Asian Cup. The Cricket World Cup, Biennale and Sauti za Busara were already recorded. Bhutan tsechus (tentative) and Lake of Stars (no official dates) skipped. Read via search-index snapshots.

## 2026-11-01 17:37 AEST, Grok: Work: gt, hn, pa, pe, py, sv, ni, cr, do, ec (10 records)

Work and speaking rules from official migration and labour sources: gt (invited speakers on traveller visa), hn, pa, pe (lecturer fees allowed 30 days in 12 months), py (90-day occasional residence for invited guests), sv (PEI permit for conferences), ni, cr, do (PADEI) and ec (visitor visa covers conferences 180 days). Read via search-index snapshots.

## 2026-11-01 17:38 AEST, Grok: Work: ma, tn, eg, md, ge, mk, ua, xk, me, bw (10 records)

Work and speaking rules from official labour and migration sources: ma (TAECHIR), tn (30-day show authorisation), eg, md (90-day creative exemption), ge (4 months a year registered short-term activity), mk (7 days, 30 a year), ua (artists exempt), xk (lecturers 90 in 180 days), me (90-day registration) and bw (emergency permit). Read via search-index snapshots.

## 2026-11-01 17:39 AEST, Grok: Work: bi, bj, dj, er, et, ga, gq, km, ls, mz (10 records)

Work and speaking rules from official immigration sources for et (Conference Visa), mz, ls, dj, bj, ga, bi, km, gq and er. Read via search-index snapshots.

## 2026-11-01 17:41 AEST, Grok: Work: French overseas (gf, gp, mq, re, yt, bl, mf, pm), mc, ad; watchlist adds (10 records)

Work and speaking rules: Code du travail D5221-2-1 3-month exemption for events, seminars and performers (gf, gp, mq, re, yt), plus local permit regimes for bl, mf and pm, Monaco (permit always required) and Andorra (30-day notice regime). Watchlist: added the Bhutan tshechus (tentative only) and Lake of Stars (no dates). Read via search-index snapshots.

## 2026-11-01 17:42 AEST, Grok: Work: cw, aw, bq, sx, ky, bm, vg, tc, ms, ai (10 records)

Work and speaking rules from official sources: Cayman (guest speakers exempt 10 days), Bermuda (non-public conference presenters 14 days), BVI (event speakers exempt 7 days with 48-hour notice), Montserrat (writers exempt), TCI, Anguilla and the Dutch Caribbean (permits required). Read via search-index snapshots.

## 2026-11-01 17:43 AEST, Grok: Work: cy, fo, gl, fk, im, je, gg, sh, sm, gi (10 records)

Work and speaking rules: Faroe Islands and Greenland (invited lecturers exempt under 3 months; Greenland also artists), Isle of Man (conference work 30 days, performers 48 days), Jersey and Guernsey (permitted paid engagements 1 month), St Helena, Falklands, Cyprus, San Marino and Gibraltar (permits). Read via search-index snapshots.

## 2026-11-01 17:43 AEST, Grok: Work: ng, mr, tg, gn, cg, zm, zw, tz, ug (9 records)

Work and speaking rules from official immigration sources: ng (F4A business visa covers conferences), mr, tg, gn, cg, zm (30 business days a year free), zw (Conferencing Visa), tz (Business Visa USD 250) and ug. Correction: commit ab9a95d was pushed by mistake with placeholder message "x" and only 9 records (below the 10-record minimum); this entry replaces the placeholder text. No force-push was used.

## 2026-11-01 17:44 AEST, Grok: Work: bb, bs, bz, ag, gd, bh, jo, bn, bo, eh (and log fix) (10 records)

Work and speaking rules: Grenada (no permit for conferences up to 14 days a year), Bahamas (conference participants exempt 3 days), Barbados, Belize, Antigua, Bahrain, Jordan, Brunei (Business Visit Visa), Bolivia and Western Sahara (Moroccan rules). Also corrected the placeholder log entry for ab9a95d. Read via search-index snapshots.

## 2026-11-01 17:45 AEST, Grok: Work: mv, il, al, ba, mm, by, np, om, kw, tm (10 records)

Work and speaking rules: Maldives (14-day on-arrival Meeting Visa), Bosnia (Form 17, 90 days), Albania (lecturers 1 month exempt), Belarus (lecturer and cultural exemptions), Israel (B/1), Myanmar, Nepal, Oman, Kuwait and Turkmenistan. Read via search-index snapshots.

## 2026-11-01 17:46 AEST, Grok: Do-not-travel: tourism af, bf, ps, so; culture ir, iq, ve, lb, kp, ht (10 records)

Do-not-travel pass (last, as agreed): entry and tourism records for af (visa before travel), bf (eVisa 90 days), ps (entry via Israel) and so (eVisa since 1 Sep 2025). Culture: ir (official dress code), iq (KRG), ve (tourism law) upgraded; lb, kp and ht searched, none found. Smartraveller advice recorded as information. Read via search-index snapshots.

## 2026-11-01 17:46 AEST, Grok: Do-not-travel culture: ps, sy, ml, ne, sd, td, af, bf, cd, cf (10 records)

Do-not-travel culture pass: ps upgraded (Ministry of Tourism and Antiquities behaviour code); sy, ml, ne, sd, td, af, bf, cd and cf searched, none found. Read via search-index snapshots.

## 2026-11-01 17:48 AEST, Grok: Do-not-travel culture fresh searches (af, bf, cd, cf, ye, so, ly, ss) and The Outing 2027 matchmaking event (9 records)

Finishes the Do-not-travel culture category. Fresh, separate searches for af, bf, cd and cf replace the generic 897e1c1 entries. af upgraded (MoIC coordination letter, Virtue and Vice law dress rules); cf upgraded (France Diplomatie: Ministry of Tourism photo authorisation); bf and cd none found, with sites checked and unofficial pages excluded. ye upgraded (Yemen Tourism Promotion Board); so, ly, ss none found. Event: The Outing matchmaking 12 to 14 Feb 2027, Ennis (organiser). Venus Berlin 2027 was already recorded. Read via search-index snapshots.

## 2026-11-01 17:49 AEST, Grok: Work rules for business visitors and speakers: lc, mu, na, uz, rs, sr, gy, jm, kz, kg, tj (11 records)

Work rules filled from official sources: Saint Lucia business-visitor regulations; Mauritius business visitor terms (90 days a trip, 120 a year); Namibia business, MICE e-visa, and short-term work visa for speakers; Uzbekistan visa-free or business e-visa; Serbia Article 3 (90 days in 180 for lecturers and artists at events); Suriname business e-visa; Guyana business visa on arrival with sponsor; Jamaica arts and education exemption application; Kazakhstan B1 covers lectures; Kyrgyzstan B visa 60 days; Tajikistan visa-free 30 days. Read via search-index snapshots.

## 2026-11-01 17:50 AEST, Grok: Work rules: event and business visas for la, pk, rw, sc, sz, sn, co, mo, to, cu (10 records)

Work rules from official sources: Colombia (visa-exempt speakers and artists at events, under 180 days, no Colombian salary); Macao (Regulation 17/2004, invited academic or cultural activity 45 days in 6 months); Pakistan Other Visa for conferences (apply 6 weeks ahead); Rwanda V5 Conference Visa USD 50; Seychelles Visitor's Permit and 1-month GOP; Laos 30-day business stays; Eswatini 1-month business visit; Senegal business visa details; Tonga written notice; Cuba business and event visas. Read via search-index snapshots.

## 2026-11-01 17:51 AEST, Grok: Work rules for open places (aq, io, va, mg, dz) and Pacific territories (pf, nc, ki, mh) (9 records)

Open work entries closed with official sources: Antarctica (AAD environmental authorisation for all activity), BIOT (entry permits paused from 31 March 2026), Vatican (via Italy, Schengen rules), Madagascar non-immigrant visa under 90 days, Algeria business or cultural visa with official invitation. Pacific: French Polynesia exempts conferences and artistic events under 3 months; New Caledonia requires prior work authorisation for all foreigners; Kiribati business visitor 1 month (4 in 12); Marshall Islands work permit plus E-1. Guinea-Bissau still has no official source (eVisa portal suspended). Read via search-index snapshots.

## 2026-11-01 17:51 AEST, Grok: Work rules for remote territories: Sark, French Southern Lands, Wallis and Futuna (3 records)

Final work-rule batch: Sark (Bailiwick rules plus Chief Pleas permission), TAAF (prefect authorisation, Marion Dufresne rotations only), Wallis and Futuna (prefect work authorisation, no published short-visit exemption). Searched without a usable official answer: Guinea-Bissau, and St Vincent, St Kitts and Dominica, whose published exemptions cover CARICOM nationals only. Read via search-index snapshots.

## 2026-11-01 17:52 AEST, Grok: Refresh STATUS.md gaps and add Claude handoff to activity log (0 records)

Docs only: STATUS.md items 1, 3 and 4 revised to current figures (867 confirm-in-writing checks, 24%; 56 culture records ask-locally after national searches; year-ahead and watchlist). Handoff for Claude added at the top of this log.

## 2026-11-01 17:54 AEST, Grok: Remote work and digital nomad visas: ee, hr, hu, mt, is, lv, ro, mu, na, ca, co (11 records)

Remote-work checks filled from official sources: Estonia digital nomad visa (sources conflict: EUR 4,500 a month vs EUR 132 a day, flagged); Croatia EUR 3,622.50 a month (2026); Hungary White Card EUR 3,000 net; Malta EUR 42,000 a year; Iceland ISK 1,000,000 a month, 90 to 180 days; Latvia OECD employer, EUR 4,538; Romania 3 times average gross salary; Mauritius Premium Visa USD 1,500; Namibia USD 2,000, 6 months; Canada visitors may work for a foreign employer up to 6 months; Colombia 3 minimum wages. Seychelles Workcation and Saint Lucia Live It reported closed by unofficial sources only, so not recorded. Read via search-index snapshots.

## 2026-11-01 17:55 AEST, Grok: Remote work rules: cz, tw, bg, no, fi, si, kz, kg, pl, lt, hk (11 records)

Remote-work checks: Czech Digital Nomad Program (Australia eligible, IT and marketing only); Taiwan digital nomad visitor visa (USD 40,000 income); Bulgaria 2025 permit (50 times minimum wage); Norway UDI says remote work as a visitor is not allowed (not-fit); Finland Migri allows it while legally present; Slovenia permit (twice average net salary); Kazakhstan Neo Nomad Visa (USD 3,000 a month); Kyrgyzstan status, Australian eligibility unconfirmed; Poland, Lithuania and Hong Kong publish no remote-work allowance, left confirm-in-writing with detail. Read via search-index snapshots.

## 2026-11-01 17:55 AEST, Grok: Book launch and lecture exemptions: no, se, dk, fi, pl, cz, ee, lv (8 records)

Book-launch checks from official exemption lists: Poland (since 1 December 2025, occasional lectures and artistic work 30 days a year without permit); Czech s 98(d) 7 consecutive or 30 days; Finland 90 days for invited lecturers and artists; Estonia 5 days in 30 without registration; Latvia 14 days for guest performances; Norway, Sweden and Denmark have no author exemption, only narrow lecturer and artist rules (left confirm-in-writing with detail). Read via search-index snapshots.

## 2026-11-01 17:56 AEST, Grok: Book launch and lecture exemptions: hu, hr, sk, ro, lu, is, us, si, li, plus pl source title fix (10 records)

Book-launch checks: Slovenia (cultural creators incl. literature exempt; authors up to 3 months); Iceland (90 days, notify Directorate of Labour by day 1); Luxembourg (speakers and lecturers under 3 months); Hungary (10 working days a year); Croatia (no permit at organised meetings or cultural events); Slovakia (30 days a year); Romania (via cultural or teaching institution, confirm); US (book promotion not named, no US appearance fee, honorarium rule); Liechtenstein (no exempt activities). Poland source title corrected to Dz.U. 2025 item 1620. Read via search-index snapshots.

## 2026-11-01 17:57 AEST, Grok: Correct Liechtenstein work rule sources (replace misattributed EU portal link) (1 records)

Fix forward for 94c0948: li activity rules cited a generic EU portal page attributed to the Liechtenstein Migration and Passport Office, and an unverified '8 days in 90' rule. Replaced with the Ausländer- und Passamt's own pages: gainful activity needs a permit whatever the length; artists are exempt from service notification only. Read via search-index snapshots.

## 2026-11-01 17:58 AEST, Grok: Research visits: sg, ie, mx, kr, br, th, tr, ke, za, ph, ae (11 records)

Research checks from official sources: Brazil VIVIS allows unpaid research and teaching 90 days (and volunteering); Korea C-3-1 academic data collection 90 days; Mexico unpaid academic 180 days, field sampling needs authorisation; Ireland visitor under 90 days or Stamp 0; Türkiye research via institution, archaeology via embassy; Kenya NACOSTI licence; South Africa research visitor visa; Philippines 9(a); Singapore, Thailand and UAE do not list research as exempt (confirm). Read via search-index snapshots.

## 2026-11-01 17:58 AEST, Grok: Volunteering rules: de, nl, in, ch, fr, cn, at, es, it, pt, be (11 records)

Volunteering checks: Germany allows qualifying voluntary work for visa-exempt visitors up to 90 days in 12 months; India e-Tourist visa up to 1 month unpaid; Belgium exempt under the 2005 volunteer law if lawfully staying; Netherlands needs a UWV volunteer permit; France, Spain, Portugal need long-stay volunteering visas; Italy only via authorised European programmes; Switzerland, China and Austria do not address short volunteering (confirm). Read via search-index snapshots.

## 2026-11-01 17:59 AEST, Grok: Volunteering rules: jp, ar, gr, ph (4 records)

Volunteering checks: Japan Temporary Visitor bars paid or profit-making activity, unpaid volunteering not named; Argentina needs an exchange or volunteering permit via a RENURE-registered organisation; Greece D visa over 3 months; Philippines 47(a)(2) visa via PNVSCA. Read via search-index snapshots.

## 2026-11-01 17:59 AEST, Grok: Update Claude handoff and STATUS gaps after activity passes (0 records)

Docs only: handoff section rewritten with today's activity passes, the Liechtenstein correction and next priorities; STATUS.md item 1 updated (796 confirm-in-writing, 22%; 476 outside Do-not-travel places).

## 2026-11-01 20:31 AEST, Grok: Volunteering rules: ca, ie, mx, th, fi, se, dk, no, kr, mt, hr, hu, cz (13 records)

Volunteering checks from official sources: Mexico visitor status covers unpaid activity (180 days); Canada allows incidental volunteering that is not 'work'; Thailand needs an O visa and work permit even unpaid; Ireland's short stay excludes volunteering, the scheme is over 3 months; Denmark volunteer permit only ages 18 to 30; Finland, Norway, Malta via programmes; Sweden visitor's permit; Croatia, Hungary, Czechia permits; Korea not named (confirm). Read via search-index snapshots.

## 2026-11-01 20:32 AEST, Grok: Volunteering rules for EU states (bg, ee, lt, lu, lv, ro, sk, pl) and Canada source fix (9 records)

Volunteering checks from the European Commission EU Immigration Portal (read directly): Slovakia allows 90 days without residence if reported to the Foreign Police within 3 working days; Latvia ages 18 to 30 only; Bulgaria, Estonia, Lithuania, Poland via European or recognised programmes; Luxembourg and Romania need authorisation before arrival. Slovenia's page has no information (left open). Fix: e802e79 cited a third-party mirror (migova.ca) for Canada's charitable versus volunteer guidance; replaced with the canada.ca original (read directly).

## 2026-11-01 20:33 AEST, Grok: Volunteering rules: is, co, rw, tr, pg, jm, tt, tl, mh, fm (10 records)

Volunteering checks: Micronesia allows unpaid volunteering on any entry permit; Trinidad and Tobago no permit for 30 days in 12 months; Timor-Leste 120-day temporary stay; Marshall Islands V-1 with MOA, 90 days; Iceland, Colombia, Rwanda, PNG and Jamaica need specific permits; Türkiye has no general volunteer exemption (confirm). Read via search-index snapshots.

## 2026-11-01 20:34 AEST, Grok: Remote work rules: Dominica WIN visa, Serbia, Sweden, and the US and its territories (8 records)

Remote-work checks: Dominica Work in Nature visa (USD 50,000 income, USD 800 fee); Serbia and Sweden list no remote-work exemption; the US (and pr, gu, vi, mp under US law) does not address remote work for a foreign employer on ESTA or B visas, left confirm-in-writing with detail. Fiji, Vanuatu and Samoa have no official nomad page (only third-party sites), not recorded. Read via search-index snapshots.

## 2026-11-01 20:35 AEST, Grok: Remote work (am, ck, to, sb) and research visits (tw, us, pr, gu, vi, mp, na, uz, tj) (13 records)

Remote work: Armenia allows remote work for a foreign employer without a permit (hartak.am); Cook Islands, Tonga and Solomon Islands do not address it (confirm). Research: US B-1 allows independent unpaid research benefiting no US institution (also pr, gu, vi, mp); Taiwan visitor up to 180 days; Namibia NCRST permit 4 months ahead; Uzbekistan A-3 and Tajikistan O2 visas. A Vietnam research entry was drafted from a misread Taiwan page and dropped before commit. Read via search-index snapshots.

## 2026-11-01 20:35 AEST, Grok: Book launch rules: mt, az, am, kz, ax, rs, lt (7 records)

Book-launch checks: Armenia exempts invited lecturers and touring performers; Serbia Article 3 cultural events 90 days in 180; Kazakhstan B1 covers lectures; Åland follows Finland (90 days); Malta, Azerbaijan and Lithuania do not address short unpaid launches (confirm with detail). Read via search-index snapshots.

## 2026-11-01 20:36 AEST, Grok: Filming rules: ca, jp, za, ie, br, co, cl, hk, uz (9 records)

Filming checks from official sources: Ireland crews up to 14 days on visitor entry; Canada exempts producers of foreign-funded films, most crew need permits (canada.ca read directly); Japan needs Entertainer status (visitor only for scouting); Brazil ANCINE notification; Colombia V courtesy visa; Chile, South Africa (STAGES), Hong Kong and Uzbekistan (UzbekKino, 2 months) need permits. Read via search-index snapshots unless noted.

## 2026-11-01 20:36 AEST, Grok: Docs: handoff and STATUS updated after volunteering, remote work, research, book launch and filming passes (0 records)

Docs only: handoff and STATUS.md item 1 updated (743 confirm-in-writing, 20%; 423 outside Do-not-travel places).

## 2026-11-01 23:15 AEST, Grok: Entrepreneur rules: tw, mu, sc, mn, am, az (6 records)

Entrepreneur checks from official sources (search-index snapshots): Taiwan Entrepreneur Visa criteria; Mauritius investor OP USD 100,000 or innovative start-up; Seychelles visitor permit for business; Mongolia 10-day K1 e-visa; Armenia business residency; Azerbaijan needs 5 local staff (80% citizens).

## 2026-11-01 23:15 AEST, Grok: Entrepreneur rules: vu, ws, pw, rw, jm, tt (6 records)

Entrepreneur checks from official sources (search-index snapshots): Vanuatu FIRC then licence; Samoa Foreign Investment Certificate; Palau FIAC with citizen-reserved activities; Rwanda business investor permit 150,000 Frw; Jamaica work permit; Trinidad and Tobago 30 days in 12 months.

## 2026-11-01 23:15 AEST, Grok: Docs: handoff and STATUS updated after entrepreneur passes (0 records)

Docs only: handoff and STATUS.md item 1 updated (731 confirm-in-writing; 411 outside Do-not-travel places; entrepreneur 31).

## 2026-11-01 23:16 AEST, Grok: Entrepreneur rules: rs, kg, uz, tj, la, bt, mo, pf, tn (9 records)

Entrepreneur checks from official sources (search-index snapshots): Serbia self-employment or startup permit; Kyrgyz investment visa 10 million som; Uzbekistan investment visa 8,500 base units; Tajikistan C visa USD 500,000; Laos NI-B2 via one-stop; Bhutan investor card over Nu. 15 million; Macao company set-up open to foreigners; French Polynesia SEFI trader card; Tunisia investor residence card.

## 2026-11-01 23:17 AEST, Grok: Filming rules: pk, uy, tn, sn, mx, qa; Kyrgyz Digital Nomad status (7 records)

Filming checks from official sources (search-index snapshots): Pakistan media visa; Uruguay ICAU and local permits; Tunisia authorisation within a week; Senegal 300,000 FCFA feature fee; Mexico COMEFILM support letter for crew paid from abroad; Qatar QNA permit 20 days ahead. Remote work: Kyrgyzstan Digital Nomad status, 60 days then yearly up to 10 years (mlsp.gov.kg read directly).

## 2026-11-01 23:18 AEST, Grok: Volunteering (at, ch, si) and research (sg, th, ar) rules (6 records)

Official sources (search-index snapshots): Austria volunteer permit only for European Solidarity Corps (EUR 218); Switzerland unpaid work can count as gainful (canton decides, stays confirm-in-writing with detail); Slovenia volunteer residence permit; Singapore NParks field research permit; Thailand NRCT approval 90 days ahead; Argentina scientist residence via RENURE host.

## 2026-11-01 23:18 AEST, Grok: Book launch and speaking rules: na, mn, ro (3 records)

Official sources (search-index snapshots): Namibia speaking needs a short-term work visa (attending is fine on a visitor visa); Mongolia K4 visa for cultural and arts events (book launch and unpaid speaking); Romania exemption for artistic activity in cultural institutions under Ordinance 25/2014.

## 2026-11-01 23:19 AEST, Grok: Entrepreneur rules: co, kz, pk, mg, cm, sr (6 records)

Entrepreneur checks from official sources (search-index snapshots): Colombia Visa M investor over 650 minimum wages; Kazakhstan USD 300,000 investor visa to 10-year residence; Pakistan investor visas 1, 3 or 5 years; Madagascar EDBM investor visa; Cameroon API support; Suriname business permit plus residence.

## 2026-11-01 23:19 AEST, Grok: Filming rules: rs, rw, pg, sb, ar (5 records)

Filming checks from official sources (search-index snapshots): Serbia exempts actors and creative team (crew need permits); Rwanda Irembo permit in 4 days; PNG film-maker visa; Solomon Islands commercial film-maker visa; Argentina RENURE invitation and INCAA residence.

## 2026-11-01 23:20 AEST, Grok: Volunteering rules: kr, tr (2 records)

Official sources (search-index snapshots): Korea working holiday guide lists volunteer activities for H-1 holders; Türkiye exemption list does not name volunteering (stays confirm-in-writing with detail).

## 2026-11-01 23:20 AEST, Grok: Docs: handoff and STATUS updated after entrepreneur, filming, volunteering, research and book launch passes (0 records)

Docs only: handoff and STATUS.md item 1 refreshed with current confirm-in-writing counts.

## 2026-11-01 23:21 AEST, Grok: Entrepreneur rules: ao, sn, na, sz, ki, ck (6 records)

Entrepreneur checks from official sources (search-index snapshots): Angola investor visa via AIPEX registration; Senegal APIX business creation; Namibia Investor Permit from 1 September 2026 (5 years, N$2,600); Eswatini EIPA 5-year director permits; Kiribati Foreign Investment Certificate; Cook Islands foreign enterprise registration.

## 2026-11-01 23:21 AEST, Grok: Filming rules: la, gy, cm (3 records)

Filming checks from official sources (search-index snapshots): Laos authorisation via a Lao embassy under Decree 246/GOV; Guyana Tourism Authority request a month ahead; Cameroon Ministry of Arts and Culture authorisation.

## 2026-11-01 23:22 AEST, Grok: Research rules: hk, sa, vn (3 records)

Research checks from official sources (search-index snapshots): Hong Kong visitors may do research and academic lectures up to 14 days under the facilitation scheme; Saudi Arabia needs an accredited host; Viet Nam via host under the science and technology experts decree.

## 2026-11-01 23:23 AEST, Grok: Docs: handoff and STATUS updated with current counts (0 records)

Docs only: handoff and STATUS.md item 1 refreshed.

## 2026-11-01 23:24 AEST, Grok: Mixed missions: derived from each place's cited paid-work source (31 places) (31 records)

Mixed-mission checks for 31 places (am ax az bg bt ci cm cu dk dm fm gy jm kg kn lc mh mn mt mu mw na se sn sr sz tj tl uz vc ws) resolved by reusing the official source already cited for paid speaking in the same record: a combined trip is governed by its strictest element, so status follows the paid-work rule (low raised to conditional). No new sources; detail says so.

## 2026-11-01 23:24 AEST, Grok: Fix mixed missions: restore cu, dk, se (still confirm) and keep earlier detail for ax, bg, fm, mh, mt, ws (9 records)

Correction to dbe7dca: the bulk derivation overwrote mixed-mission detail that had been read deliberately. Cuba, Denmark and Sweden restored to their earlier confirm-in-writing entries (status unchanged from before dbe7dca). For ax, bg, fm, mh, mt and ws the earlier detail is kept ahead of the derived text (detail updated, status as derived).

## 2026-11-01 23:25 AEST, Grok: Book launch and unpaid speaking: reuse cited pages for am, sc, to, mu, gy, cu (6 records)

Resolved from the official source already cited for the sibling activity in the same record: Armenia unpaid talks fit the invited-lecturer exemption; Seychelles and Tonga launches turn on whether they count as work (permit needed if so); Mauritius business visitors may not sell directly; Guyana events under 3 months are visitor purposes; Cuba uses an events visa. All set conditional, no new sources.

## 2026-11-01 23:25 AEST, Grok: Entrepreneur rules: ci, lc, vc, dz, dm, nc (6 records)

Entrepreneur checks from official sources (search-index snapshots): Côte d'Ivoire CEPICI registration with residence certificate; Saint Lucia non-CARICOM trade licence EC$500 to EC$1,000; Saint Vincent annual trader's licence; Algeria AAPI foreign investment one-stop shop; Dominica registration then self-employed work permit; New Caledonia self-employment allowed with FDI declaration.

## 2026-11-01 23:26 AEST, Grok: Fix stray escape characters in Saint Lucia entrepreneur source note (1 records)

Correction to 1b4e6f5: removed backslashes accidentally left in the Saint Lucia source 'supports' text (EC$500 and EC$1,000). Detail and status unchanged.

## 2026-11-01 23:26 AEST, Grok: Filming rules: dz, mg, ci (3 records)

Filming checks from official sources (search-index snapshots): Algeria Ministry of Culture authorisation 30 days ahead via a licensed Algerian producer; Madagascar filming visa plus ISSM authorisation 15 days ahead; Côte d'Ivoire Cinéma authorisation.

## 2026-11-01 23:26 AEST, Grok: Docs: handoff and STATUS updated with current counts (0 records)

Docs only: handoff and STATUS.md item 1 refreshed after mixed-mission, book launch, entrepreneur and filming passes.

## 2026-11-01 11:55 AEST, Grok: Review fixes to 26d61c3: Central Land Council permit link, Minjerribah festival source labelled as a signal (2 records)

Quality review of 26d61c3 (kept, not reverted): schema valid and sources are land councils, WA and Queensland government pages, BoM and AIATSIS. Fixed: the Central Land Council permit layer linked to the Northern Land Council page (now clc.org.au/permits); the Minjerribah culture-cycles entry cited National Indigenous Times as community evidence, now labelled a signal. Noted: NT and WA permit lead times are planning buffers, as the records already say.

## 2026-11-01 11:55 AEST, Grok: Australia light pass: 2027 writers' and arts festivals for NSW, SA and WA (3 records)

Australia light pass (state level): Sydney Writers' Festival 17 to 23 May 2027, Adelaide Writers' Week 27 February to 4 March 2027, Perth Festival 5 to 28 February 2027, from the festivals' own pages (search-index snapshots).

## 2026-11-01 11:55 AEST, Grok: Australia light pass: Melbourne and Byron writers' festivals 2027 (2 records)

Australia light pass (state level): Melbourne Writers Festival 6 to 9 May 2027 (VIC) and Byron Writers Festival 20 to 22 August 2027 (NSW), from the festivals' own pages (search-index snapshots). Brisbane Writers Festival 2027 dates not yet published.

## 2026-11-01 11:56 AEST, Grok: Scope rule: Australia light pass only, international work first (routines and handoff) (0 records)

Rule change from Luke (2 November 2026): Australia is no longer fully excluded. Added a scope block to the three routines (monthly-cycles, weekly-place-passes, window-watch) and replaced the 'Australia is out of scope' standing note in the handoff: state, territory and notable-region level only, no council or ward depth (p4a.xyz), visa and work patterns stay skipped for au, international work is the priority.

## 2026-11-01 11:56 AEST, Grok: Entrepreneur rules: gy, kn (2 records)

Entrepreneur checks from official sources (search-index snapshots): Guyana equal treatment, 5-year business-person visa US$140, work permit for working locally; St Kitts and Nevis business licence, Alien Landholding Licence, work permits.

## 2026-11-01 11:56 AEST, Grok: Docs: handoff and STATUS updated after Australia light pass and entrepreneur checks (0 records)

Docs only: handoff and STATUS.md item 1 refreshed; handoff records the 26d61c3 review, the Australia light pass and the remaining international counts.

## 2026-11-01 11:57 AEST, Grok: Entrepreneur (as, cu) and filming (ki, to) rules (4 records)

Official sources (search-index snapshots): American Samoa foreign corporation permit and business licence; Cuba Law 118 foreign investment forms, non-residents only in senior or technical posts; Kiribati research and filming permit from the Office of the President; Tonga ministerial land-use permit for filming on Crown land.

## 2026-11-01 11:58 AEST, Grok: Unpaid speaking, book launches and research from already-cited pages: az, tt, ws, tl, kg, tj, bg (7 records)

Resolved 9 activities in 7 records by reusing the official source already cited in the same record: Azerbaijan unpaid talks exempt when invited by a university; Trinidad and Tobago research within the 30-day paid-or-unpaid allowance; Samoa talks and launches need work permission; Timor-Leste temporary stay visa for cultural engagements; Kyrgyzstan, Tajikistan and Bulgaria launches need a permit if they count as work. All conditional; no new sources.

## Handoff, 2026-11-02 (Grok)

Confirm-in-writing: 624 of 3,705 activity checks (306 outside the DNT set and Australia). Outside DNT remaining: remote-work 62, volunteering 51, research 36, book-launch 33, mixed-mission 23, unpaid-speaking 22, trade 18, conference 15, ai-teaching 13, meetings 13, filming 10 (ck cu fm kg kz nu sz tj tl), paid-speaking 5, artist 3. Entrepreneur is finished. Next: filming leftovers, then volunteering, book launches, unpaid speaking, research, remote work, then DNT work rules, then ask-locally culture and 2027 events. The Australia light-pass rule still applies.

## 2026-11-01 11:58 AEST, Grok: Docs: handoff and STATUS counts after the reuse batch (0 records)

Recomputed counts; handoff updated.

## 2026-11-01 12:00 AEST, Grok: 2027 events from organiser sites: SXSW, Sundance, Burning Man, Primavera Sound, Hay Festival, Jaipur Literature Festival (6 records)

Added 6 official 2027 events to year-ahead records (us__texas, us__colorado, us__nevada, es__catalonia, gb__wales, in__rajasthan), each sourced to the organiser's site.

## 2026-11-02 12:00 AEST, Grok: 2027 events: Ubud Writers and Readers Festival; pending official dates rechecked (1 records)

Added Ubud Writers and Readers Festival 20 to 24 October 2027 (organiser page, read directly) to id__bali. Rechecked Web Summit Lisbon, Slush, Tomorrowland and Iceland Airwaves: still no official 2027 dates. Added Venice Film Festival, WOMAD and Coachella 2027 to the pending list (dates only from third parties).

## 2026-11-02 12:01 AEST, Grok: Culture: conduct rules from UK FCDO advice for fr, pl, hr, lv, me, lt, cr (ask-locally to partly-mapped) (7 records)

Seven ask-locally culture records moved to partly-mapped using the FCDO laws and cultural differences sections, read directly on 2026-11-02 (Croatia shirtless and swimwear fines in Split and Dubrovnik, Poland and Latvia public drinking bans, France ID within 4 hours and face-covering ban, Montenegro photography ban). San Marino left as ask-locally: drugs only.

## 2026-11-02 12:02 AEST, Grok: Culture: conduct rules from UK FCDO advice for al, ao, ba, br, ci, cu, dj, dz, et, ga, gh, gn, gt (ask-locally to partly-mapped) (13 records)

Thirteen ask-locally culture records moved to partly-mapped from FCDO laws and cultural differences sections, read directly on 2026-11-02. Congo (cg) left as ask-locally: only an ID rule is listed.

## 2026-11-02 12:03 AEST, Grok: Culture: conduct rules from UK FCDO advice for bi, by, lr, mr, mz, ni, sc, sl, sn, st, tg, tj, tm, tv, ua, vg, xk (ask-locally to partly-mapped) (17 records)

Seventeen ask-locally culture records moved to partly-mapped from FCDO laws and cultural differences sections, read directly on 2026-11-02. Suriname (sr) left as ask-locally: only drugs and money are listed. British Indian Ocean Territory (io) and St Vincent and the Grenadines (vc) have no such section.

## 2026-11-02 12:03 AEST, Grok: Culture: conduct rules from UK FCDO advice for Do-not-travel places bf, cd, ht, kp, lb, ly, ml, ne, sd, so, ss, sy, td (ask-locally to partly-mapped) (13 records)

Thirteen ask-locally culture records in the Do-not-travel set moved to partly-mapped from FCDO laws and cultural differences sections, read directly on 2026-11-02. Travel status is unchanged; these remain Do not travel.

## 2026-11-02 12:04 AEST, Grok: Filming: Timor-Leste Press Council accreditation for foreign media (Media Law Article 25) (1 records)

tl filming moved from confirm-in-writing to specialist, citing Article 25 of the Media Law (WTO-hosted informal translation, read directly). Cook Islands, Niue and Eswatini searched: only fixer, news or event-specific pages found, left as confirm-in-writing.

## 2026-11-02 12:05 AEST, Grok: Filming: Tajikistan MFA media accreditation and category Ж visa (1 records)

tj filming moved from confirm-in-writing to specialist, citing the MFA Consular Department media visa page (read directly).

## Handoff, 2026-11-02 midday (Grok)

This run: 7 new official 2027 events (SXSW, Sundance in Boulder, Burning Man, Primavera Sound Barcelona, Hay Festival, Jaipur Literature Festival, Ubud Writers and Readers Festival); pending-official-dates rechecked (Web Summit Lisbon, Slush, Tomorrowland, Iceland Airwaves still unpublished; Venice Film Festival, WOMAD and Coachella 2027 added as pending). Culture: 50 of 56 ask-locally records moved to partly-mapped from UK FCDO "laws and cultural differences" sections (read directly); left: cg, sm, sr (thin sections), io, vc (no section), yt. Filming: tl (Press Council, Media Law Art. 25) and tj (MFA accreditation, Ж visa) resolved; 8 left outside DNT (as ck cu fm kg kz nu sz; American Samoa was missing from the earlier list), fm's NACH policy PDF is behind a JS challenge, Eswatini and Cook Islands have only fixer sources.

Confirm-in-writing: 622 of 3,705. Outside DNT and Australia: remote-work 62, volunteering 51, research 36, book-launch 33, mixed-mission 23, unpaid-speaking 22, trade 18, conference 15, ai-teaching 13, meetings 13, filming 8, paid-speaking 5, artist 3.

Next: more 2027 events (wellbeing-spiritual, dating-marriage-adult, national-day gaps), recheck the pending list in December (Tomorrowland says details in December 2026), remaining 6 culture records via national tourism pages, then work-rule categories.

## 2026-11-02 12:05 AEST, Grok: Docs: handoff and STATUS after the events, culture and filming run (0 records)

Handoff updated with counts and next steps.

## 2026-11-02 12:06 AEST, Grok: Docs: handoff filming list now names all 8 places left (adds American Samoa) (0 records)

Corrected the filming list in the handoff.

## 2026-11-02 12:07 AEST, Grok: 2027 events: ASSC 30 Beijing, Mind Body Spirit London and Brisbane, RSAC, Annecy, Sydney Mardi Gras (6 records)

Added 6 official 2027 events (cn, gb__england, au__qld, us__california, fr__auvergne-rhone-alpes, au__nsw), each from the organiser site (RSAC from the Moscone Center venue page).

## 2026-11-02 12:08 AEST, Grok: 2027 national days from government holiday pages: Singapore, United States, South Africa (3 records)

Added Singapore National Day 9 Aug (MOM), US Independence Day observed 5 Jul (OPM), South Africa Freedom Day 27 Apr (gov.za), all read directly.

## 2026-11-02 12:09 AEST, Grok: 2027 national days from government sources: India Independence Day, New Zealand Waitangi Day (2 records)

India 15 Aug 2027 from the DoPT 2027 holiday memorandum (read directly); New Zealand Waitangi Day 6 Feb 2027, Mondayised 8 Feb, from govt.nz (search snapshot).

## 2026-11-02 12:09 AEST, Grok: 2027 events: Folsom Street Fair, Fantasy Fest, New Orleans Mardi Gras, GITEX AI Asia, SuperAI, Frankfurt Book Fair (5 records)

Added 6 official 2027 events across 5 records (us__california, us__florida, us__louisiana, sg twice, de__hesse), each read directly on the organiser or official tourism site.

## 2026-11-02 12:11 AEST, Grok: Culture: conduct rules from Government of Canada advice for vc, yt, sr, sm (ask-locally to partly-mapped) (4 records)

Four ask-locally culture records moved to partly-mapped using the travel.gc.ca laws and culture sections, read directly on 2026-11-02: St Vincent camouflage ban and criminalised same-sex relations; Mayotte under French law with low local acceptance of homosexuality; Suriname driving permits; San Marino public drunkenness rules. Congo (cg) and British Indian Ocean Territory (io) stay ask-locally.

## 2026-11-02 12:12 AEST, Grok: Culture: Republic of the Congo conduct rules from Government of Canada advice (ask-locally to partly-mapped) (1 records)

cg moved to partly-mapped from the travel.gc.ca laws and culture section, read directly: ID and visa at all times, photography bans, export tax on crafts. Only British Indian Ocean Territory (io) remains ask-locally; neither the UK nor the Canadian advice page has a laws section for it.

## Handoff, 2026-11-02 afternoon (Grok)

This run: 17 new official 2027 events. Wellbeing-spiritual: ASSC 30 Beijing 16 to 19 Jun, Mind Body Spirit London 28 to 31 May, MindBodySpirit Brisbane 26 to 28 Feb. Technology: RSAC 5 to 8 Apr, GITEX AI Asia 29 to 30 Apr, SuperAI 8 to 9 Sep. Dating-marriage-adult: Folsom Street Fair 26 Sep (Up Your Alley 25 Jul), Fantasy Fest 22 to 31 Oct. National days: Singapore 9 Aug, US 4 Jul (observed 5 Jul), South Africa Freedom Day 27 Apr, India 15 Aug, NZ Waitangi Day 6 Feb (Mondayised 8 Feb). Arts-culture and film: Annecy 13 to 19 Jun, Sydney Mardi Gras parade 6 Mar, New Orleans Mardi Gras 9 Feb, Frankfurt Book Fair 6 to 10 Oct. Culture: all but io now partly-mapped (vc, yt, sr, sm, cg from Government of Canada advice). Filming list fixed: 8 left outside DNT (as ck cu fm kg kz nu sz).

Still unverified on official sites: Philippines 2027 Independence Day proclamation (only lawphil and doe.gov.ph seen), Malaysia 2027 holidays (only an FMM copy), Google I/O 2027, Edinburgh Book Festival 2027 (TBC), WorldPride (none in 2027).

Confirm-in-writing unchanged at 622 of 3,705 (306 outside DNT and Australia). Next: more national days as governments publish 2027 lists, recheck the pending list in December, then the work-rule categories.

## 2026-11-02 12:12 AEST, Grok: Docs: handoff and STATUS after the 2027 events and culture run (0 records)

Handoff updated; corrected an unsourced remark about io in the previous log entry.

## 2026-11-02 12:12 AEST, Grok: Docs: correct handoff event count to 17 (0 records)

The handoff said 20 events; the run added 17 (6 + 3 + 2 + 6).

## 2026-11-02 12:17 AEST, Grok: DNT work rules: kp, sy, ye, ru, ir activity checks set to not-fit citing Smartraveller Do not travel (69 checks) (5 records)

69 confirm-in-writing activity checks in North Korea, Syria, Yemen, Russia and Iran set to not-fit. Each cites the Smartraveller page (read directly 2026-11-02, Do not travel, with its update date) and the existing Smartraveller visa note; no activity work rules are invented. Travel advisory status unchanged.

## 2026-11-02 12:18 AEST, Grok: DNT work rules: af, iq, lb, ps activity checks set to not-fit citing Smartraveller (55 checks); ye quote corrected (5 records)

55 confirm-in-writing activity checks in Afghanistan, Iraq, Lebanon and Palestine set to not-fit, citing Smartraveller Do not travel (read directly 2026-11-02) and the existing Smartraveller visa notes. Yemen's quoted line replaced with the explicit Do not travel sentence (detail only, status unchanged). Travel advisory status unchanged.

## 2026-11-02 12:18 AEST, Grok: DNT work rules: bf, cd, cf, ly, ml, ne, sd, so, ss, td activity checks set to not-fit citing Smartraveller (140 checks) (10 records)

140 confirm-in-writing activity checks in ten African Do-not-travel places set to not-fit, each citing its Smartraveller page (read directly 2026-11-02, Do not travel line quoted with update date) and the existing Smartraveller visa note. Travel advisory status unchanged.

## 2026-11-02 12:18 AEST, Grok: DNT work rules: ht, ve activity checks set to not-fit citing Smartraveller (28 checks) (2 records)

28 confirm-in-writing activity checks in Haiti and Venezuela set to not-fit, citing Smartraveller Do not travel (read directly 2026-11-02). Venezuela detail adds Smartraveller's note that workers should bring an employer letter and local contact details with a Spanish translation. Travel advisory status unchanged.

## 2026-11-02 12:19 AEST, Grok: Sark (cq): activity checks from States of Guernsey visitor guidance (14 checks) (1 records)

cq had been wrongly grouped with the Do-not-travel set; it is not on Smartraveller's Do not travel list. 14 confirm-in-writing checks set to conditional (non-paid) or specialist (paid), citing States of Guernsey pages: UK visit permission across the CTA, no employment as a visitor, and Sark's own local rules (not read).

## Handoff, 2026-11-02 evening (Grok)

Do-not-travel pass done. The DNT set is the 21 Smartraveller "Do not travel" places in scripts/visa_prep_rechecks.py (af bf cd cf ht iq ir kp lb ly ml ne ps sd so ss sy td ve ye ru); each page was read directly on 2 November 2026 and still says Do not travel. All 292 of their confirm-in-writing activity checks are now not-fit, citing the Smartraveller page (Do not travel line quoted with its update date) plus the existing Smartraveller visa note. No activity work rules were invented; travel advisory status is unchanged. Venezuela adds Smartraveller's note that workers bring an employer letter and local contact details with a Spanish translation.

Correction: earlier runs grouped gw (Guinea-Bissau) and cq (Sark) with DNT. They are not on the Smartraveller Do not travel list, so earlier "outside DNT" counts left out their 28 checks. Sark's 14 are now resolved from States of Guernsey pages; Guinea-Bissau's 14 remain.

Confirm-in-writing: 316 of 3,705, all outside DNT and Australia: remote-work 63, volunteering 52, research 37, book-launch 34, mixed-mission 24, unpaid-speaking 23, trade 19, conference 16, ai-teaching 14, meetings 14, filming 9 (as ck cu fm gw kg kz nu sz), paid-speaking 6, artist 4, entrepreneur 1 (gw). Next: Guinea-Bissau's 14 from official French or Guinea-Bissau sources, then volunteering, research, book launches, unpaid speaking, remote work, then filming.

## 2026-11-02 12:19 AEST, Grok: Docs: handoff and STATUS after the Do-not-travel pass; DNT set corrected to 21 places (0 records)

STATUS activities paragraph rewritten with current counts; handoff records the DNT pass and the gw/cq correction.

## 2026-11-02 12:20 AEST, Grok: Guinea-Bissau: meetings, conference and trade from France's travel advice (3 checks) (1 records)

gw meetings, conference and trade set to conditional, citing France Diplomatie business-travel advice (no tourist and business distinction; 1 to 12-month multiple-entry visas). The other 11 gw checks stay confirm-in-writing: no official source on work permits was found.

## 2026-11-02 12:21 AEST, Grok: Remote work: Åland (Migri remote-work rule) and Fiji (21-day Business Visitors Permit) (2 records)

ax remote-work set to conditional citing Migri (remote work for a foreign employer allowed during a legal stay). fj remote-work set to conditional citing Fiji Immigration (holiday permit bars all work; Australians get a 21-day Business Visitors Permit on arrival).

## 2026-11-02 12:21 AEST, Grok: Volunteering and research: Hong Kong (ImmD), Switzerland (VZAE), Vanuatu (visitor work authority) (3 records)

hk volunteering specialist (visitors may not take paid or unpaid employment without approval); ch volunteering specialist (unpaid work counts as gainful employment); vu research conditional (12-week authority on a visitors permit).

## 2026-11-02 12:22 AEST, Grok: Remote work: Samoa (Visitor Permit bars work; Business Visitor Permit is for short visits) (1 records)

ws remote-work set to specialist citing the Immigration Division permits page, read directly.

## 2026-11-02 12:23 AEST, Grok: Filming: American Samoa (NPS permit, Commerce) and Kyrgyzstan (MFA media accreditation) (2 records)

as and kg filming set to specialist: as cites the National Park of American Samoa permits page (read directly) and the Department of Commerce application centre; kg cites the MFA foreign media accreditation page (search snapshot).

## Handoff, 2026-11-02 late (Grok)

This run resolved 11 checks: Guinea-Bissau meetings, conference and trade (France Diplomatie business-travel advice; its other 11 stay open, no official work-permit source found); remote work in Åland (Migri), Fiji (21-day Business Visitors Permit) and Samoa (Visitor Permit bars work); volunteering in Hong Kong (ImmD: no paid or unpaid employment without approval) and Switzerland (VZAE: unpaid work can be gainful employment); research in Vanuatu (12-week authority on a visitors permit); filming in American Samoa (NPS permit) and Kyrgyzstan (MFA accreditation).

Confirm-in-writing outside DNT and Australia: 305 (remote work 60, volunteering 50, research 36, book launch 34, mixed mission 24, unpaid speaking 23, trade 18, conference 15, ai teaching 14, meetings 13, filming 7, paid speaking 6, artist 4, entrepreneur 1). Filming left: ck cu fm gw kz nu sz. Sources tried and rejected: EY and law-firm summaries for remote work in Sweden, Slovakia, Luxembourg and Poland (not official); Saint Lucia's former Live It programme (closed). Dominica's WIN visa was checked but dm remote-work was already resolved.

Next: Pacific and Caribbean volunteering and research from immigration sites (Solomon Islands, Palau, Marshall Islands, Nauru, Tonga, Tuvalu, St Kitts, St Vincent), Danish and Swedish remote-work wording, then filming (ck cu fm gw kz nu sz).

## 2026-11-02 12:23 AEST, Grok: Docs: handoff and STATUS after the Guinea-Bissau, remote-work, volunteering and filming run (0 records)

Counts recomputed; handoff updated.

## 2026-11-02 12:23 AEST, Grok: Docs: correct handoff resolved-check count to 11 (0 records)

3 gw + 3 remote work + 2 volunteering + 1 research + 2 filming = 11.

## 2026-11-02 12:24 AEST, Grok: Pacific and Caribbean work rules: Solomon Islands, Tonga, Palau, St Kitts and Nevis (14 checks) (4 records)

sb remote-work conditional (30-day allowance for work arising from employment abroad), unpaid-speaking and book-launch specialist; to volunteering specialist (employment visa for voluntary work) and research specialist (Government Research Permit); pw volunteering and remote-work specialist (written exemption), research, book-launch and unpaid-speaking conditional; kn volunteering, unpaid-speaking, book-launch and research specialist (Immigration Act s19). All from official sites via search snapshots.

## 2026-11-02 12:25 AEST, Grok: Pacific work rules: Marshall Islands, Nauru, Tuvalu (8 checks) (3 records)

mh book-launch and unpaid-speaking conditional, remote-work specialist (V-1 visitor visa bars employment and business); nr volunteering and remote-work specialist, unpaid-speaking conditional (visitor visa bars business and employment); tv volunteering and remote-work specialist (Immigration Regulations 2014). Official sites via search snapshots.

## Handoff 2026-11-02 (Pacific and Caribbean pass)

- 743d7f7: sb, to, pw, kn, 14 checks (its title is right).
- a218127: mh, nr, tv. Its title says 8 checks, but only 7 changed (tv volunteering was already resolved, so only tv remote-work moved). Corrected here, not by rewriting history.
- Open outside DNT and Australia: 284 confirm-in-writing. Remote work 56, volunteering 45, research 33, book launch 30, mixed mission 24, unpaid speaking 18, trade 18, conference 15, ai teaching 14, meetings 13, filming 7, paid speaking 6, artist 4, entrepreneur 1.
- Not done this run: vc (the official pages only cover paid work permits, so nothing is settled), the DK and SE remote-work wording, the wider book-launch and unpaid-speaking sweep, and filming for ck cu fm gw kz nu sz.

## 2026-11-02 12:26 AEST, Grok: St Vincent, Denmark and Sweden: detail updated, still confirm (7 checks) (3 records)

vc volunteering, research, unpaid-speaking, book-launch, remote-work: detail updated, still confirm (official pages only cover visitor entry and paid work permits). dk and se remote-work: detail updated, still confirm (nyidanmark.dk and migrationsverket do not address remote work for a foreign employer).

## 2026-11-02 12:30 AEST, Grok: Rules stacks: home-base outbound stack (Australia, Queensland, Redland City filled; Minjerribah not yet checked) and destination law-stack skeleton for 3,767 international places (3 records)

New pattern home-obligations (inherit stack, home_only) applies to the place in config/home-base.json (au/minjerribah) and every level above it. Records: au partly-mapped with 11 obligations (ABF duty free and IPC, DAFF biosecurity, Smartraveller subscriptions and insurance, Consular Services Charter, AFP extraterritorial child sex offences, AGD foreign bribery s 70.2, Defence DSGL technology permits, ATO tax residency, Medicare and reciprocal agreements, PBS medicines, AEC overseas electors); au/qld partly-mapped with 3 (IDPs, vehicle registration, ECQ telephone voting); au/qld-council-6250 (Redland City) partly-mapped with rates; au/minjerribah not yet checked (ferry access, animals). Place pages show it as 'Home obligations while away (home-base stack)' next to each destination's local-law stack. build_site.py now writes site/data/law-stacks.json: every international place's local-law stack country first, null = not yet checked; 3,767 places, 224 levels filled, 3,543 not yet checked; home stack 3 of 4 levels filled. New tests/test_rules_stacks.py (6 tests). All official sources read via search-index snapshots.

## 2026-11-02 12:30 AEST, Grok: Talks and launches: Saint Lucia, Suriname, Uzbekistan, Malawi (8 checks) (4 records)

lc book-launch and unpaid-speaking specialist (Labour Act s317, ministerial exemption); sr both conditional (business e-visa); uz unpaid-speaking conditional (A-3 academic visa), book-launch detail updated, still confirm; mw book-launch and unpaid-speaking detail updated, still confirm.

## 2026-11-02 12:31 AEST, Grok: Filming: Cuba specialist, Cook Islands detail updated, still confirm (2 checks) (2 records)

cu filming specialist (D-6 press visa and CPI accreditation, MINREX). ck filming detail updated, still confirm (only the Ministry of Transport drone rule is on record).

## Handoff 2026-11-02 (rules stacks, talks, filming)

- HEAD checks rerun on ba98a21: all passed with no changes. From now on docs commits go through `D` in /tmp/C.sh, which runs the full checks first.
- Rules-stack design (ce770f7):
  - Destination side: the existing local-law pattern (inherit stack) already resolves every level from the country down. build_site.py now writes site/data/law-stacks.json, the skeleton for every international place (Australia excluded as the home side), with each level's status or null for not yet checked. Totals: 3,767 places and levels, 224 filled, 3,543 not yet checked. National level: 212 of 247 filled; 35 national or territory levels are still not checked (aq as ax bl bq cc cq cx eh fo gf gg gl gp gs gu im io je mf mp mq nf pm pn pr re sj sx tf tk vc vi wf yt). Sub-national: 12 of 3,520 filled. No sub-national rules were invented.
  - Home side: new pattern patterns/home-obligations.json (inherit stack, home_only). lib.home_chain() reads config/home-base.json, and applies() limits the pattern to that chain, so changing the one id moves the whole stack.
  - Records: au has 11 obligations (ABF, DAFF, Smartraveller, Consular Services Charter, AFP, AGD, Defence, ATO, Services Australia, AEC). au/qld has 3 (IDP, registration, ECQ telephone voting). Redland City has 1 (rates). Minjerribah is not yet checked: ferry access and animal rules, because SeaLink is an operator, not a government source.
  - Site: the place page has a "Home obligations while away (home-base stack)" section after "Local law (destination stack)" on every place page. It resolves against the home base, so a trip view shows home duties next to the destination layers.
  - Tests: tests/test_rules_stacks.py (6 tests).
- Work rules: c18307f (vc 5 checks plus dk and se remote work: detail updated, still confirm), b7c1cd8 (lc, sr, uz, mw talks and launches), 2506cba (cu filming specialist; ck detail updated, still confirm).
- Open outside DNT and Australia: 278 confirm-in-writing.
- Not done: kz filming (only unofficial mirrors of the MFA accreditation rules were found), plus fm gw nu sz filming. Also the remaining book launches and unpaid talks (ao bt ci cm dm gw la ma ni sz tn and others), and filling the 35 missing national law levels from official FCDO or Smartraveller local-law sections.

## 2026-11-02 12:32 AEST, Grok: Home-base stack: Minjerribah island level partly mapped, Redland pet registration added (2 records)

au/minjerribah home-obligations partly-mapped: ferry access (Redland City Council), resident VAP fee exemption renewed yearly (qld.gov.au, DETSI policy, RAM Regulation s58); QYAC obligations recorded as not yet checked under new topic camping-and-native-title. au/qld-council-6250: dog and cat registration renewed every 12 months, Local Law 2. Home stack now has records at 4 of 4 levels.

## 2026-11-02 12:33 AEST, Grok: Home-base stack: Minjerribah cultural heritage duty of care (QYAC, Queensland); resident QYAC permits still not yet checked (1 records)

au/minjerribah camping-and-native-title item rewritten from QYAC Cultural Heritage page and qld.gov.au duty of care page; resident-specific QYAC permits remain not yet checked.

## 2026-11-02 12:35 AEST, Grok: National law levels: 11 of 35 missing filled (bq eh mf bl pn gs gu cx cc nf aq) (11 records)

local-law records, partly-mapped: bq, eh, mf, bl, pn, gs from UK FCDO laws and cultural differences sections (read directly); gu from Smartraveller local laws (read directly); cx and cc (Commonwealth plus applied WA law, Infrastructure department), nf (Applied Laws Ordinance 2016), aq (Australian Antarctic Division environmental approval) via search snapshots. The other 24 have no FCDO or Smartraveller local-law section (French departments, US territories, Crown Dependencies, Nordic territories, tk, vc, wf, yt, sx, io, sj, tf) and stay not yet checked.

## 2026-11-02 12:35 AEST, Grok: Sub-national law levels: alcohol prohibition in Bihar, Gujarat, Mizoram, Nagaland, Lakshadweep and Sharjah (6 levels) (6 records)

local-law records at region level from UK FCDO India and UAE safety-and-security pages (read directly): Indian dry states and Lakshadweep (arrest without bail, 5 to 10 years' prison); Sharjah alcohol ban.

## 2026-11-02 12:36 AEST, Grok: Sub-national law level: Quebec cannabis rules (age 21, possession limits, public-use ban) (1 records)

ca/quebec local-law partly-mapped from Gouvernement du Québec cannabis legislation page (search snapshot).

## 2026-11-02 12:36 AEST, Grok: Filming: Kazakhstan specialist (MFA journalist accreditation, 1 check) (1 records)

kz filming specialist from the MFA accreditation rules on the official Adilet database (search snapshot).

## Handoff 2026-11-02 (home level, national and sub-national law levels)

- ff4dde3 and aec6ff7: Minjerribah home level.
  - Ferry access (Redland City Council).
  - Resident vehicle access permit fee exemption, renewed yearly (qld.gov.au, DETSI policy, RAM Regulation s58).
  - Cultural heritage duty of care (QYAC; qld.gov.au, with fines up to AUD 166,900).
  - Redland dog and cat registration, renewed every 12 months.
  - New home-obligations topic: camping-and-native-title.
  - Resident-specific QYAC permits: not yet checked. Home stack: 4 of 4 levels have records.
- 1e9b2fa: 11 of 35 missing national law levels filled.
  - From FCDO, read directly: bq eh mf bl pn gs.
  - From Smartraveller, read directly: gu.
  - From search snapshots: cx and cc (Commonwealth plus applied WA law), nf (NSW applied laws), aq (Antarctic environmental approval).
  - Still not yet checked: 24 (as ax cq fo gf gg gl gp im io je mp mq pm pr re sj sx tf tk vc vi wf yt). Their FCDO pages have no laws section, or there is no FCDO or Smartraveller page.
- 1a33cba and 91045c3: sub-national levels.
  - Alcohol prohibition in Bihar, Gujarat, Mizoram, Nagaland and Lakshadweep (FCDO India) and in Sharjah (FCDO UAE).
  - Quebec cannabis rules (Gouvernement du Québec).
- c34bd13: kz filming moved to specialist (MFA accreditation rules, Adilet).
- Law stacks: 242 of 3,767 levels filled, 3,525 not yet checked. Work rules open outside DNT and Australia: 277.
- Next:
  - Crown Dependencies from gov.je, gov.gg and gov.im.
  - French overseas departments from French government pages.
  - US territories.
  - More sub-national levels: US state cannabis and alcohol, Malaysian states (Kelantan, Terengganu), German Länder.
  - fm gw nu sz filming.
  - Remaining talks and launches.

## 2026-11-02 12:37 AEST, Grok: National law levels: Jersey, Isle of Man, Guernsey, Sark (4 levels) (4 records)

local-law partly-mapped from gov.je, gov.im, gov.gg, Guernsey Legal Resources and sarkgov.co.uk (search snapshots): visitor driving, duty free and prohibited imports, travelling with controlled medicines, Sark vehicle law.

## 2026-11-02 12:38 AEST, Grok: National law levels: French overseas departments and collectivities (re gp mq gf yt pm wf, 7 levels) (7 records)

local-law partly-mapped from the Conseil constitutionnel overseas page and Légifrance article 73 (search snapshots): French law applies by right in re, gp, mq, gf, yt; pm and wf follow their own statutes under article 74.

## 2026-11-02 12:39 AEST, Grok: National law levels: American Samoa and Puerto Rico (2 levels) (2 records)

as local-law partly-mapped (own entry laws and visitor permit, legalaffairs.as.gov); pr partly-mapped (medical-only cannabis, Law 42-2017, salud.pr.gov). Both via search snapshots. mp and vi remain not yet checked.

## 2026-11-02 12:39 AEST, Grok: Sub-national law level: California cannabis rules (1 level) (1 records)

us/california local-law partly-mapped from the Department of Cannabis Control and HSC 11362.1 (search snapshots).

## 2026-11-02 12:40 AEST, Grok: Filming: Micronesia and Niue detail updated, still confirm (2 checks) (2 records)

fm and nu filming: detail updated, still confirm; no official page settles filming on a visitor basis. gw and sz filming untouched (no official source found).

## 2026-11-02 12:40 AEST, Grok: Talks and launches: Dominica detail updated, still confirm (2 checks) (1 records)

dm book-launch and unpaid-speaking: detail updated, still confirm (Labour Division page does not address visitor talks or launches).
