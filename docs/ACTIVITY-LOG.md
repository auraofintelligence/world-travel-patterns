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
