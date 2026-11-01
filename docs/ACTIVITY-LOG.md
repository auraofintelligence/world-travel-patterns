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
