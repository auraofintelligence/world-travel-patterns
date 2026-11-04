# Automation checklist

What future automations should check, and when. Generated 2026-11-04 by `scripts/recheck_plan.py` from repo data (machine copy: `config/recheck-plan.json`). Rebuild instead of editing by hand.

Rules that always apply: a failed fetch is not evidence of a change; never use projected or third-party dates; travel windows (config/cadence.json phases: 90, 30, 7 days out, daily in place) tighten everything below.

## A. Global checks per pattern

| Pattern | What to check | Official source | How often | Why |
|---|---|---|---|---|
| advisory | Smartraveller advice level and 'latest update' for every destination | Smartraveller destinations export (smartraveller.gov.au/destinations-export) | daily (1 d) | Levels can change overnight after conflict, unrest or disaster. |
| activities | What an Australian may do on each entry route (tourism, meetings, speaking, remote work) | Destination immigration and labour authorities | quarterly (90 d) | Work rules are the most common 'confirm in writing' gap. |
| affection-and-relationships | Public affection, relationships, LGBTQIA+ law | Legislation; Smartraveller local customs | quarterly (90 d) | Law reforms happen in both directions. |
| consular | Australian embassy or consulate and its contact details | DFAT mission list; Smartraveller | quarterly (90 d) | Missions open, close or suspend services. |
| entry | Visa-free status, max stay, arrival cards and refusals for an ordinary Australian passport | Destination immigration authority or embassy in Australia; Smartraveller entry section | quarterly (90 d) | Waivers and exemptions are often time-limited (China, South Korea, Belarus) or cut at short notice (Thailand, Sep 2026). |
| health-entry | Vaccination certificates (yellow fever), health declarations, outbreak rules | Destination health authority; Smartraveller health section; WHO | quarterly (90 d) | Outbreaks add requirements quickly. |
| local-law | Laws that catch visitors: ID, photography, dress, LGBTQIA+, alcohol | The level's own legislation; Smartraveller local laws | quarterly (90 d) | Laws stack from country to state to city. |
| money-and-cost | Currency, cash limits, card acceptance, tourist taxes | Central bank or government | quarterly (90 d) | Rates move daily but rules (cash limits, tourist taxes) change slowly. |
| psychoactive-substances | Alcohol, cannabis, psilocybin, prescription medicines | Legislation and health regulator; Smartraveller drugs section | quarterly (90 d) | Several programs have start dates (e.g. New Mexico psilocybin). |
| visa-preparation | Visa fees, e-visa portals, processing times, documents | Destination e-visa or embassy page | quarterly (90 d) | Fees and portals change with little notice; atlas baselines must be rechecked. |
| year-ahead | Elections, major events and dated rule changes in the next 12 months | Electoral commissions; organisers; data/watch.json | quarterly (90 d) | Organisers announce next year's dates on known months; elections get called. |
| zone-requirements | Permits for restricted areas, land councils, parks, island governments, border zones | The zone authority itself | quarterly (90 d) | Permit lead times decide when the approach phase starts. |
| home-obligations | Home-base duties while away (see section D) | Commonwealth, Queensland and council pages | yearly (180 d) | Renewals fall due while travelling. |
| births-and-family-support | Birth rates and family support | UN WPP; national statistics | yearly (365 d) | Annual data releases. |
| culture-and-protocol | Etiquette, respecting Country, community visitor guidance | The community's own guidance | yearly (365 d) | Slow-changing. |
| culture-cycles | Public holidays, Ramadan and Islamic months, lunar new year, festivals | National calendars; Nager.Date as a signal | yearly (365 d) | Lunar and Islamic calendars move every year; next year's holidays are often announced late in the year. |
| languages | Official and widely spoken languages | Constitution, census | yearly (365 d) | Very slow-changing. |
| seasons-and-flow | Weather seasons, crowds, cyclone and monsoon windows | National met service; tourism statistics | yearly (365 d) | Slow-changing, but check before a trip. |
| works-and-purpose | Luke's own work tie-ins (venues, partners, events) | Luke's repos; venue pages | yearly (365 d) | Tagged places only. |
| (cross-cutting) | ETIAS and EES rollout (Schengen and EU) | travel-europe.europa.eu/etias_en and /ees_en | monthly | Start date not settled; watch item eu-etias (check every 30 days). |
| (cross-cutting) | Official source pages still alive (hash and 404 check) | data/source-status.json via scripts/source_watch.py | weekly | A changed hash flags a page to reread; a failed fetch is not evidence of a rule change. |
| (cross-cutting) | Next year's public holidays file (data/calendar/holidays-<next year>.json) | National calendars; Nager.Date | yearly (October to December) | Governments publish next year's holiday lists late in the year; Islamic dates are confirmed by moon sighting nearer the time. |

## B. Dated triggers (sorted by date; undated at the end)

| Date | Kind | Place | What | Check |
|---|---|---|---|---|
| 2026-11-05 | election | gd | House of Representatives election (snap) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-11-07 | election | nz | General election (House of Representatives) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-11-13 | law-or-rule-date | us/new-jersey | psychoactive-substances: ...stribution licences could sell low-dose hemp drinks (no more than 5 mg THC a serving, 10 mg a container) only until 13 November 2026; from 14 November 2 | Recheck the official source about 60 days before, and again on the date. |
| 2026-11-14 | law-or-rule-date | us/new-jersey | psychoactive-substances: ...d sell low-dose hemp drinks (no more than 5 mg THC a serving, 10 mg a container) only until 13 November 2026; from 14 November 2026 those drinks are tr | Recheck the official source about 60 days before, and again on the date. |
| 2026-11-15 | election | cv | Presidential election | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-11-29 | election | ch | Federal referendum | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-11-29 | election | es | General election, Congress and Senate (snap) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-12-05 | election | gm | Presidential election | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-12-06 | election | cy | Assembly election in the north of Cyprus (snap) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-12-06 | election | gw | Presidential and National Assembly elections (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-12-09 | election | fj | Referendum (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-12-22 | election | ss | Presidential and legislative elections (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-12-24 | election | fj | General election (Parliament) (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2026-12-31 | law-or-rule-date | by | entry: 30-day visa-free entry until 31 December 2026, up to 90 days a ca | Recheck the official source about 60 days before, and again on the date. |
| 2026-12-31 | law-or-rule-date | cn | entry: ...ordinary Australian passports, up to 30 days for business, tourism, visiting family and friends, or transit, until 31 December 2026. | Recheck the official source about 60 days before, and again on the date. |
| 2026-12-31 | law-or-rule-date | kr | entry: Visa-free tourist stays up to 90 days, and no K-ETA needed until 31 December 2026. | Recheck the official source about 60 days before, and again on the date. |
| 2026-12-31 | election | so | Presidential and House of the People elections (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-01-01 | rule-change | by | Belarus's 30-day visa-free entry for Australians runs until 31 December 2026. | Look for an extension before 1 January 2027. |
| 2027-01-01 | rule-change | cn | China's 30-day visa waiver for ordinary Australian passports runs until 31 December 2026. | Look for an extension notice from the Chinese Embassy in Australia or China's Ministry of Foreign Affairs before 1 January 2027. |
| 2027-01-01 | rule-change | kr | South Korea's K-ETA exemption for Australian passport holders runs until 31 December 2026. | Check the official K-ETA site for an extension before 1 January 2027. |
| 2027-01-01 | law-or-rule-date | my/labuan | local-law: Budget 2027 proposes a single limit of RM10,000 (about A$3,505) of new goods for Labuan and Langkawi from 1 January 2027, after a stay of at | Recheck the official source about 60 days before, and again on the date. |
| 2027-01-16 | election | ng | Presidential, Senate and House of Representatives elections | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-01-27 | election | kg | Presidential election (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-01 (month only) | law-or-rule-date | ch/canton-of-basel-stadt | psychoactive-substances: ...nabis to enrolled participants through selected pharmacies in Basel-Stadt. Planned to run from September 2022 to January 2027, with up to 374 par | Recheck the official source about 60 days before, and again on the date. |
| 2027-02-28 | election | ch | Federal referendum (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-02 (month only) | law-or-rule-date | dz | culture-and-protocol: Carry your passport for hotels and domestic flights. During Ramadan (next from February 2027) do not eat, drink, | Recheck the official source about 60 days before, and again on the date. |
| 2027-02-28 | election | sv | Legislative Assembly election (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-03-02 | election | fm | Congress election (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-03-07 | election | ee | Parliamentary election | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-03-31 | law-or-rule-date | es/catalonia | local-law: ...night, for up to 7 nights at the same place; under-17s are exempt. Outside Barcelona city, from 1 April 2026 to 31 March 2027: EUR 4.50 at five-s | Recheck the official source about 60 days before, and again on the date. |
| 2027-04-10 | election | gm | National Assembly election (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-04-18 | election | fi | Parliamentary election (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-04-18 | election | fr | Presidential election (first round) (date not yet confirmed) | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-06 (month only) | law-or-rule-date | ch/canton-of-geneva | psychoactive-substances: ...main partner, sells cannabis to enrolled participants from a single outlet in Vernier. Planned from June 2023 to June 2027, with up to 1,080 p | Recheck the official source about 60 days before, and again on the date. |
| 2027-06 (month only) | law-or-rule-date | ch/canton-of-vaud | psychoactive-substances: ...on a non-profit basis to enrolled participants through a specialised shop in Lausanne. Planned from July 2023 to June 2027, with up to 1,600 p | Recheck the official source about 60 days before, and again on the date. |
| 2027-07-01 | law-or-rule-date | gs | entry: Visitor permit needed before arrival (Entry Control Ordinance 2022): GBP 250 from 1 July 2026 and GBP 275 from 1 July 2027, valid 40 days. App | Recheck the official source about 60 days before, and again on the date. |
| 2027-07-01 | law-or-rule-date | us/virginia | psychoactive-substances: ...y 2027 the first offence is a civil penalty of up to US$25 (about A$36 at RBA 30 Oct 2026, A$1 = USD 0.7040); from 1 July 2027 it rises to up to U | Recheck the official source about 60 days before, and again on the date. |
| 2027-07-18 | election | ht | Presidential, Senate and Chamber of Deputies elections | Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission. |
| 2027-08 (month only) | law-or-rule-date | bt | zone-requirements: ...checkpost), Gelephu (Aipoli Bridge) and Samdrup Jongkhar (Pinchinna checkpost) don't pay the SDF (2 June 2026 to August 2027). Going beyond the | Recheck the official source about 60 days before, and again on the date. |
| 2027-08-31 | law-or-rule-date | bt | visa-preparation: Sustainable Development Fee, per adult per night (discount from USD 200, to 31 August 2027) | Recheck the official source about 60 days before, and again on the date. |
| 2027-12-31 | law-or-rule-date | us/new-mexico | psychoactive-substances: ...or depression, PTSD, substance use disorders and end-of-life care. The Act requires the program to be running by 31 December 2027; one Department of | Recheck the official source about 60 days before, and again on the date. |
| 2028-10 (month only) | law-or-rule-date | ch/canton-of-basel-landschaft | psychoactive-substances: ...nabis to enrolled participants through specialised shops in Liestal and Allschwil. Planned from November 2023 to October 2028, with up to 3,950 p | Recheck the official source about 60 days before, and again on the date. |
| date not announced | pending-event-date | ae | GITEX Global 2027 | organiser lists December 2027 in Dubai, no exact dates (checked 2026-11-01). Date not announced; check monthly from November 2026. |
| date not announced | rule-change | at, be, bg, hr, cy, cz +24 | EU travel authorisation (ETIAS) for visa-exempt visitors. | Watch the official ETIAS page for a confirmed start date. The country list is the expected scope; confirm it from the same page. |
| date not announced | pending-event-date | be | Tomorrowland Belgium 2027 | FAQ says info at end of 2026; rechecked 2026-11-02, still no official dates. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | bf | FESPACO 30th edition, 20 to 27 March 2027 | dates reported officially; hold until the Do-not-travel pass (bf is Do not travel). Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | br | Rock in Rio | biennial; next edition September 2028. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | bt | Paro Tshechu 2027 (reported 18 to 22 March, lunar) | only private operators list dates. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | bt | National Day 2027 (17 December) | need official Bhutan government holiday list. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | bt | Bhutan tshechu festivals 2027 (Punakha, Paro, Thimphu and others) | only tentative 2027 dates published (lunar calendar, subject to change); no confirmed official dates (checked 2026-11-01). Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | ca | Toronto International Film Festival 2027 | no dates published. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | fi | Slush 2027 (Helsinki) | organiser lists 2026 only; rechecked 2026-11-02, still no official dates. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | fr | Festival d'Avignon 2027 | no dates published. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | gb__england | WOMAD 2027 (Neston Park) | 22 to 25 July 2027 reported; not readable on the organiser site (checked 2026-11-02). Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | ie | Lisdoonvarna Matchmaking Festival 2027 | official FAQ says the festival runs through September; 2027 programme not yet published. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | in__nagaland | Hornbill Festival 2027 (usually 1 to 10 Dec) | official site lists 2026 only. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | is | Iceland Airwaves 2027 | no 2027 dates published; rechecked 2026-11-02, still no official dates. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | it | Biennale Arte (next edition) | 2027 is an Architecture year: Biennale Architettura 8 May to 21 November 2027 (added to it year-ahead 2026-11-04); next Biennale Arte 2028. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | it | 84th Venice International Film Festival 2027 | only third-party sites list 1 to 11 September 2027 (checked 2026-11-02). Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | jo | Jerash Festival 2027 | only 'July 2027' seen. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | ma | Mawazine 2027 | no dates found. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | ma | Fes Festival of World Sacred Music 2027 | unconfirmed. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | mw | Lake of Stars 2027 | postponed from 2026; dates to be announced. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | mw | Lake of Stars festival 2027 | postponed to 2027 per Malawi Tourism; no official dates (checked 2026-11-01). Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | ph | Independence Day 2027 (12 June) | need official gov.ph proclamation page. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | pt | Web Summit 2027 (Lisbon) | return to Lisbon confirmed, no dates; rechecked 2026-11-02, still no official dates. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | us | TechCrunch Disrupt 2027 | no official dates. Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | us | Coachella 2027 | 2027 passes advertised, no dates on the official site (checked 2026-11-04). Date not announced; check monthly from November 2026. |
| date not announced | pending-event-date | us__california | Coachella 2027 | 9 to 11 and 16 to 18 April 2027 reported by trade press; not seen on the organiser site (checked 2026-11-02). Date not announced; check monthly from November 2026. |

Not in the repo yet: Brisbane Writers Festival 2027 (no record found in data/; add it to pending-official-dates.json before automations can watch it).

## C. Per-location watch list

Cadence: weekly = Do not travel; fortnightly = Reconsider your need to travel, an open watch item or legacy-baseline evidence; monthly = high degree of caution, pending event dates, dated rules, elections or snapshot-only evidence; quarterly = only confirm-in-writing gaps.

341 locations have specific watch items.

| Place | Advisory | Recheck | Why | Watch items |
|---|---|---|---|---|
| af | Do not travel | weekly | confirm in writing, high advisory, snapshot evidence | 1 confirm-in-writing |
| bf | Do not travel | weekly | high advisory, pending event, snapshot evidence | pending date: FESPACO 30th edition, 20 to 27 March 2027 |
| by | Do not travel | weekly | dated rule, high advisory, snapshot evidence, watch item | by-visa-free-2026; entry date 2026-12-31 |
| cd | Do not travel | weekly | confirm in writing, high advisory, snapshot evidence | 1 confirm-in-writing |
| cf | Do not travel | weekly | confirm in writing, high advisory, snapshot evidence | 1 confirm-in-writing |
| ht | Do not travel | weekly | confirm in writing, election, high advisory | election 2027-07-18; 1 confirm-in-writing |
| iq | Do not travel | weekly | high advisory, snapshot evidence |  |
| ir | Do not travel | weekly | confirm in writing, high advisory, snapshot evidence | 1 confirm-in-writing |
| kp | Do not travel | weekly | confirm in writing, high advisory | 1 confirm-in-writing |
| lb | Do not travel | weekly | high advisory |  |
| ly | Do not travel | weekly | confirm in writing, high advisory | 1 confirm-in-writing |
| ml | Do not travel | weekly | confirm in writing, high advisory | 1 confirm-in-writing |
| mm | Do not travel | weekly | high advisory, snapshot evidence |  |
| ne | Do not travel | weekly | confirm in writing, high advisory | 1 confirm-in-writing |
| ps | Do not travel | weekly | confirm in writing, high advisory, snapshot evidence | 1 confirm-in-writing |
| ru | Do not travel | weekly | high advisory |  |
| sa | Do not travel | weekly | confirm in writing, high advisory, snapshot evidence | 1 confirm-in-writing |
| sd | Do not travel | weekly | confirm in writing, high advisory | 1 confirm-in-writing |
| so | Do not travel | weekly | election, high advisory, snapshot evidence | election 2026-12-31 |
| ss | Do not travel | weekly | election, high advisory | election 2026-12-22 |
| sy | Do not travel | weekly | confirm in writing, high advisory | 1 confirm-in-writing |
| td | Do not travel | weekly | confirm in writing, high advisory | 1 confirm-in-writing |
| ua | Do not travel | weekly | high advisory, snapshot evidence |  |
| ve | Do not travel | weekly | high advisory, snapshot evidence |  |
| ye | Do not travel | weekly | confirm in writing, high advisory, snapshot evidence | 1 confirm-in-writing |
| ad |  | fortnightly | legacy baseline, snapshot evidence |  |
| ag |  | fortnightly | legacy baseline, snapshot evidence |  |
| at | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| bb |  | fortnightly | legacy baseline, snapshot evidence |  |
| be | Exercise normal safety precautions | fortnightly | pending event, snapshot evidence, watch item | eu-etias; pending date: Tomorrowland Belgium 2027 |
| bg | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| bh | Reconsider your need to travel | fortnightly | high advisory, snapshot evidence |  |
| bi | Reconsider your need to travel | fortnightly | high advisory, snapshot evidence |  |
| cg |  | fortnightly | legacy baseline, snapshot evidence |  |
| ch | Exercise normal safety precautions | fortnightly | election, snapshot evidence, watch item | eu-etias; election 2026-11-29; election 2027-02-28 |
| cn | Exercise a high degree of caution | fortnightly | confirm in writing, dated rule, snapshot evidence, watch item | cn-visa-waiver-2026; entry date 2026-12-31; 1 confirm-in-writing |
| cu | Reconsider your need to travel | fortnightly | confirm in writing, high advisory, snapshot evidence | 5 confirm-in-writing |
| cv |  | fortnightly | confirm in writing, election, legacy baseline, snapshot evidence | election 2026-11-15; 1 confirm-in-writing |
| cy | Exercise a high degree of caution | fortnightly | election, legacy baseline, snapshot evidence, watch item | eu-etias; election 2026-12-06 |
| cz | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| de | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| dk | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 3 confirm-in-writing |
| dm |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 7 confirm-in-writing |
| ee | Exercise normal safety precautions | fortnightly | election, snapshot evidence, watch item | eu-etias; election 2027-03-07 |
| eh |  | fortnightly | legacy baseline, snapshot evidence |  |
| er | Reconsider your need to travel | fortnightly | confirm in writing, high advisory, legacy baseline, snapshot evidence | 1 confirm-in-writing |
| es | Exercise normal safety precautions | fortnightly | election, snapshot evidence, watch item | eu-etias; election 2026-11-29 |
| et | Reconsider your need to travel | fortnightly | high advisory, snapshot evidence |  |
| fi | Exercise normal safety precautions | fortnightly | election, legacy baseline, pending event, snapshot evidence, watch item | eu-etias; pending date: Slush 2027 (Helsinki); election 2027-04-18 |
| fr | Exercise a high degree of caution | fortnightly | election, pending event, snapshot evidence, watch item | eu-etias; pending date: Festival d'Avignon 2027; election 2027-04-18 |
| gd |  | fortnightly | election, legacy baseline, snapshot evidence | election 2026-11-05 |
| gh | Exercise a high degree of caution | fortnightly | legacy baseline, snapshot evidence |  |
| gq |  | fortnightly | legacy baseline, snapshot evidence |  |
| gr | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| gw |  | fortnightly | confirm in writing, election, legacy baseline, snapshot evidence | election 2026-12-06; 11 confirm-in-writing |
| hr | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| hu | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| il | Reconsider your need to travel | fortnightly | high advisory, snapshot evidence |  |
| is | Exercise normal safety precautions | fortnightly | pending event, snapshot evidence, watch item | eu-etias; pending date: Iceland Airwaves 2027 |
| it | Exercise normal safety precautions | fortnightly | pending event, snapshot evidence, watch item | eu-etias; pending date: Biennale Arte (next edition); pending date: 84th Venice International Film Festival 2027 |
| jo | Reconsider your need to travel | fortnightly | high advisory, pending event, snapshot evidence | pending date: Jerash Festival 2027 |
| ki |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 3 confirm-in-writing |
| km |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 1 confirm-in-writing |
| kn |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 5 confirm-in-writing |
| kr | Exercise normal safety precautions | fortnightly | dated rule, snapshot evidence, watch item | kr-keta-2026; entry date 2026-12-31 |
| kw | Reconsider your need to travel | fortnightly | high advisory, snapshot evidence |  |
| lc |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 4 confirm-in-writing |
| li |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence, watch item | eu-etias; 3 confirm-in-writing |
| lt | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 4 confirm-in-writing |
| lu |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence, watch item | eu-etias; 1 confirm-in-writing |
| lv | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| mc |  | fortnightly | legacy baseline, snapshot evidence |  |
| mr | Reconsider your need to travel | fortnightly | high advisory, snapshot evidence |  |
| mt | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 1 confirm-in-writing |
| ng | Reconsider your need to travel | fortnightly | election, high advisory, snapshot evidence | election 2027-01-16 |
| nl | Exercise normal safety precautions | fortnightly | snapshot evidence, watch item | eu-etias |
| no | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 1 confirm-in-writing |
| nr |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 1 confirm-in-writing |
| om | Reconsider your need to travel | fortnightly | high advisory, snapshot evidence |  |
| pk | Reconsider your need to travel | fortnightly | confirm in writing, high advisory, snapshot evidence | 4 confirm-in-writing |
| pl | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 1 confirm-in-writing |
| pt | Exercise normal safety precautions | fortnightly | pending event, snapshot evidence, watch item | eu-etias; pending date: Web Summit 2027 (Lisbon) |
| ro | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 2 confirm-in-writing |
| rw | Exercise normal safety precautions | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 2 confirm-in-writing |
| se | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 3 confirm-in-writing |
| si | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 1 confirm-in-writing |
| sk | Exercise normal safety precautions | fortnightly | confirm in writing, snapshot evidence, watch item | eu-etias; 1 confirm-in-writing |
| sm |  | fortnightly | legacy baseline, snapshot evidence |  |
| sr |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 3 confirm-in-writing |
| st |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 1 confirm-in-writing |
| tg |  | fortnightly | legacy baseline, snapshot evidence |  |
| tv |  | fortnightly | legacy baseline, snapshot evidence |  |
| va |  | fortnightly | legacy baseline, snapshot evidence |  |
| vc |  | fortnightly | confirm in writing, legacy baseline, snapshot evidence | 8 confirm-in-writing |
| ae | Exercise a high degree of caution | monthly | confirm in writing, pending event, snapshot evidence | pending date: GITEX Global 2027; 1 confirm-in-writing |
| ai |  | monthly | snapshot evidence |  |
| al | Exercise a high degree of caution | monthly | snapshot evidence |  |
| am | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 4 confirm-in-writing |
| ao | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| aq |  | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| ar | Exercise normal safety precautions | monthly | snapshot evidence |  |
| as |  | monthly | confirm in writing, snapshot evidence | 6 confirm-in-writing |
| au |  | monthly | snapshot evidence |  |
| au/minjerribah |  | monthly | snapshot evidence |  |
| au/nsw |  | monthly | snapshot evidence |  |
| au/qld |  | monthly | snapshot evidence |  |
| au/qld-council-6250 |  | monthly | snapshot evidence |  |
| au/sa |  | monthly | snapshot evidence |  |
| au/vic |  | monthly | snapshot evidence |  |
| au/wa |  | monthly | snapshot evidence |  |
| aw |  | monthly | snapshot evidence |  |
| ax |  | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| az | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| ba | Exercise a high degree of caution | monthly | snapshot evidence |  |
| bd | Exercise a high degree of caution | monthly | snapshot evidence |  |
| bj | Exercise a high degree of caution | monthly | snapshot evidence |  |
| bl |  | monthly | snapshot evidence |  |
| bm |  | monthly | snapshot evidence |  |
| bn | Exercise normal safety precautions | monthly | snapshot evidence |  |
| bo | Exercise a high degree of caution | monthly | snapshot evidence |  |
| bq |  | monthly | snapshot evidence |  |
| br | Exercise a high degree of caution | monthly | pending event, snapshot evidence | pending date: Rock in Rio |
| br/rio-de-janeiro | Exercise a high degree of caution | monthly | snapshot evidence |  |
| bs | Exercise a high degree of caution | monthly | snapshot evidence |  |
| bt | Exercise normal safety precautions | monthly | confirm in writing, dated rule, pending event, snapshot evidence | pending date: Paro Tshechu 2027 (reported 18 to 22 March, lunar); pending date: National Day 2027 (17 December); pending date: Bhutan tshechu festivals 2027 (Punakha, Paro, Thimphu and others); zone-requirements date 2027-08-28; +2 more |
| bw | Exercise normal safety precautions | monthly | snapshot evidence |  |
| bz | Exercise a high degree of caution | monthly | snapshot evidence |  |
| ca | Exercise normal safety precautions | monthly | confirm in writing, pending event, snapshot evidence | pending date: Toronto International Film Festival 2027; 2 confirm-in-writing |
| ca/alberta | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/british-columbia | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/manitoba | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/new-brunswick | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/newfoundland-and-labrador | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/northwest-territories | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/nova-scotia | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/nunavut | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/ontario | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/prince-edward-island | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/quebec | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/saskatchewan | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ca/yukon | Exercise normal safety precautions | monthly | snapshot evidence |  |
| cc |  | monthly | snapshot evidence |  |
| ch/canton-of-basel-landschaft | Exercise normal safety precautions | monthly | dated rule | psychoactive-substances date 2028-10-28 |
| ch/canton-of-basel-stadt | Exercise normal safety precautions | monthly | dated rule | psychoactive-substances date 2027-01-28 |
| ch/canton-of-geneva | Exercise normal safety precautions | monthly | dated rule | psychoactive-substances date 2027-06-28 |
| ch/canton-of-vaud | Exercise normal safety precautions | monthly | dated rule | psychoactive-substances date 2027-06-28 |
| ci | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| ck | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| cl | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| cm | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| cn/beijing | Exercise a high degree of caution | monthly | snapshot evidence |  |
| cn/chongqing | Exercise a high degree of caution | monthly | snapshot evidence |  |
| cn/shanghai | Exercise a high degree of caution | monthly | snapshot evidence |  |
| cn/xinjiang | Exercise a high degree of caution | monthly | snapshot evidence |  |
| co | Exercise a high degree of caution | monthly | snapshot evidence |  |
| cq |  | monthly | snapshot evidence |  |
| cr | Exercise a high degree of caution | monthly | snapshot evidence |  |
| cw |  | monthly | snapshot evidence |  |
| cx |  | monthly | snapshot evidence |  |
| de/bavaria | Exercise normal safety precautions | monthly | snapshot evidence |  |
| dj | Exercise a high degree of caution | monthly | snapshot evidence |  |
| do | Exercise a high degree of caution | monthly | snapshot evidence |  |
| dz | Exercise a high degree of caution | monthly | confirm in writing, dated rule, snapshot evidence | culture-and-protocol date 2027-02-28; 2 confirm-in-writing |
| ec | Exercise a high degree of caution | monthly | snapshot evidence |  |
| eg | Exercise a high degree of caution | monthly | snapshot evidence |  |
| es/catalonia | Exercise normal safety precautions | monthly | dated rule, snapshot evidence | local-law date 2027-03-31 |
| fj | Exercise normal safety precautions | monthly | election, snapshot evidence | election 2026-12-09; election 2026-12-24 |
| fk |  | monthly | snapshot evidence |  |
| fm | Exercise normal safety precautions | monthly | confirm in writing, election, snapshot evidence | election 2027-03-02; 5 confirm-in-writing |
| fo |  | monthly | snapshot evidence |  |
| ga | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| gb | Exercise a high degree of caution | monthly | snapshot evidence |  |
| gb/scotland | Exercise a high degree of caution | monthly | snapshot evidence |  |
| gb/wales | Exercise a high degree of caution | monthly | snapshot evidence |  |
| gb__england |  | monthly | pending event | pending date: WOMAD 2027 (Neston Park) |
| ge | Exercise normal safety precautions | monthly | snapshot evidence |  |
| gf |  | monthly | snapshot evidence |  |
| gg |  | monthly | snapshot evidence |  |
| gi |  | monthly | snapshot evidence |  |
| gl |  | monthly | snapshot evidence |  |
| gm | Exercise a high degree of caution | monthly | confirm in writing, election, snapshot evidence | election 2026-12-05; election 2027-04-10; 1 confirm-in-writing |
| gn | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| gp |  | monthly | snapshot evidence |  |
| gs |  | monthly | dated rule, snapshot evidence | entry date 2027-07-01 |
| gt | Exercise a high degree of caution | monthly | snapshot evidence |  |
| gu | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| gy | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 4 confirm-in-writing |
| hk | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| hn | Exercise a high degree of caution | monthly | snapshot evidence |  |
| id | Exercise a high degree of caution | monthly | snapshot evidence |  |
| id/bali | Exercise a high degree of caution | monthly | snapshot evidence |  |
| ie | Exercise normal safety precautions | monthly | pending event, snapshot evidence | pending date: Lisdoonvarna Matchmaking Festival 2027 |
| im |  | monthly | snapshot evidence |  |
| in | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/arunachal-pradesh | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/goa | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/maharashtra | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/manipur | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/mizoram | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/nagaland | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/rajasthan | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/sikkim | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/uttarakhand | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in/west-bengal | Exercise a high degree of caution | monthly | snapshot evidence |  |
| in__nagaland |  | monthly | pending event | pending date: Hornbill Festival 2027 (usually 1 to 10 Dec) |
| io |  | monthly | snapshot evidence |  |
| it/lombardy | Exercise normal safety precautions | monthly | snapshot evidence |  |
| it/veneto | Exercise normal safety precautions | monthly | snapshot evidence |  |
| je |  | monthly | snapshot evidence |  |
| jm | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| jp | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ke | Exercise a high degree of caution | monthly | snapshot evidence |  |
| kg | Exercise a high degree of caution | monthly | confirm in writing, election, snapshot evidence | election 2027-01-27; 2 confirm-in-writing |
| kh | Exercise a high degree of caution | monthly | snapshot evidence |  |
| kr/seoul | Exercise normal safety precautions | monthly | snapshot evidence |  |
| ky |  | monthly | snapshot evidence |  |
| kz | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| la | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| lk | Exercise a high degree of caution | monthly | snapshot evidence |  |
| lr | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| ls | Exercise a high degree of caution | monthly | snapshot evidence |  |
| ma | Exercise a high degree of caution | monthly | confirm in writing, pending event, snapshot evidence | pending date: Mawazine 2027; pending date: Fes Festival of World Sacred Music 2027; 4 confirm-in-writing |
| md | Exercise a high degree of caution | monthly | snapshot evidence |  |
| me | Exercise normal safety precautions | monthly | snapshot evidence |  |
| mf |  | monthly | snapshot evidence |  |
| mg | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| mh | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| mk | Exercise normal safety precautions | monthly | snapshot evidence |  |
| mn | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| mo | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| mp |  | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| mq |  | monthly | snapshot evidence |  |
| ms |  | monthly | snapshot evidence |  |
| mu | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| mv | Exercise a high degree of caution | monthly | snapshot evidence |  |
| mw | Exercise a high degree of caution | monthly | confirm in writing, pending event, snapshot evidence | pending date: Lake of Stars 2027; pending date: Lake of Stars festival 2027; 4 confirm-in-writing |
| mx | Exercise a high degree of caution | monthly | snapshot evidence |  |
| my | Exercise normal safety precautions | monthly | snapshot evidence |  |
| my/labuan | Exercise normal safety precautions | monthly | dated rule | local-law date 2027-01-01 |
| mz | Exercise a high degree of caution | monthly | snapshot evidence |  |
| na | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| nc | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| nf |  | monthly | snapshot evidence |  |
| ni | Exercise a high degree of caution | monthly | snapshot evidence |  |
| np | Exercise a high degree of caution | monthly | snapshot evidence |  |
| nu | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 9 confirm-in-writing |
| nz | Exercise normal safety precautions | monthly | election, snapshot evidence | election 2026-11-07 |
| pa | Exercise a high degree of caution | monthly | snapshot evidence |  |
| pe | Exercise a high degree of caution | monthly | snapshot evidence |  |
| pe/lima-department | Exercise a high degree of caution | monthly | snapshot evidence |  |
| pf | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| pg | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| ph | Exercise a high degree of caution | monthly | pending event, snapshot evidence | pending date: Independence Day 2027 (12 June) |
| pm |  | monthly | snapshot evidence |  |
| pn |  | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| pr |  | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| pw | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| py | Exercise a high degree of caution | monthly | snapshot evidence |  |
| qa | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| re |  | monthly | snapshot evidence |  |
| rs | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| rs/city-of-belgrade | Exercise normal safety precautions | monthly | snapshot evidence |  |
| sb | Exercise normal safety precautions | monthly | snapshot evidence |  |
| sc | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| sg | Exercise normal safety precautions | monthly | snapshot evidence |  |
| sh |  | monthly | snapshot evidence |  |
| sj |  | monthly | snapshot evidence |  |
| sl | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| sn | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 5 confirm-in-writing |
| sv | Exercise a high degree of caution | monthly | election, snapshot evidence | election 2027-02-28 |
| sx |  | monthly | snapshot evidence |  |
| sz | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 4 confirm-in-writing |
| tc |  | monthly | snapshot evidence |  |
| tf |  | monthly | snapshot evidence |  |
| th | Exercise a high degree of caution | monthly | snapshot evidence |  |
| tj | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| tk |  | monthly | snapshot evidence |  |
| tl | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| tm | Exercise a high degree of caution | monthly | snapshot evidence |  |
| tn | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 9 confirm-in-writing |
| to | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| tr | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| tt | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 4 confirm-in-writing |
| tw | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 1 confirm-in-writing |
| tz | Exercise a high degree of caution | monthly | snapshot evidence |  |
| ug | Exercise a high degree of caution | monthly | snapshot evidence |  |
| us | Exercise normal safety precautions | monthly | confirm in writing, pending event, snapshot evidence | pending date: TechCrunch Disrupt 2027; pending date: Coachella 2027; 2 confirm-in-writing |
| us/alabama | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/alaska | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/arizona | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/arkansas | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/california | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/colorado | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/connecticut | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/delaware | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/district-of-columbia | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/florida | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/georgia | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/hawaii | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/idaho | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/illinois | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/indiana | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/iowa | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/massachusetts | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/michigan | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/nebraska | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/nevada | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/new-hampshire | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/new-jersey | Exercise normal safety precautions | monthly | dated rule, snapshot evidence | psychoactive-substances date 2026-11-13; psychoactive-substances date 2026-11-14 |
| us/new-mexico | Exercise normal safety precautions | monthly | dated rule, snapshot evidence | psychoactive-substances date 2027-12-31 |
| us/new-york | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/north-carolina | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/north-dakota | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/ohio | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/oklahoma | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/oregon | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/rhode-island | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/south-carolina | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/south-dakota | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/tennessee | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/texas | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/utah | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/virginia | Exercise normal safety precautions | monthly | dated rule | psychoactive-substances date 2027-07-01 |
| us/washington | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/west-virginia | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/wisconsin | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us/wyoming | Exercise normal safety precautions | monthly | snapshot evidence |  |
| us__california |  | monthly | pending event | pending date: Coachella 2027 |
| uy | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 2 confirm-in-writing |
| uz | Exercise a high degree of caution | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| vg |  | monthly | snapshot evidence |  |
| vi |  | monthly | confirm in writing, snapshot evidence | 3 confirm-in-writing |
| vn | Exercise normal safety precautions | monthly | snapshot evidence |  |
| vu | Exercise normal safety precautions | monthly | confirm in writing, snapshot evidence | 4 confirm-in-writing |
| wf |  | monthly | confirm in writing, snapshot evidence | 7 confirm-in-writing |
| ws | Exercise normal safety precautions | monthly | snapshot evidence |  |
| xk | Exercise a high degree of caution | monthly | snapshot evidence |  |
| yt |  | monthly | snapshot evidence |  |
| za | Exercise a high degree of caution | monthly | snapshot evidence |  |
| zm | Exercise normal safety precautions | monthly | snapshot evidence |  |
| zw | Exercise a high degree of caution | monthly | snapshot evidence |  |

## D. Home base (au/minjerribah) obligations to recheck while travelling

Recheck every 180 days, and before any trip over a renewal date. Levels: au/minjerribah > au/qld-council-6250 > au/qld > au.

| Level | Topic | Obligation | Source |
|---|---|---|---|
| au/minjerribah | island-access | Passenger and vehicle ferries run from Toondah Harbour, Cleveland, to Dunwich (passenger about 25 minutes, vehicle about 45). Council lists the operators; book the vehicle ferry directly with the operator. Check that a hire car may travel to the island. | https://www.redland.qld.gov.au/info/20125/our_suburbs_and_islands/205/north_stradbroke |
| au/minjerribah | driving-and-vehicles | Residents who reasonably need a vehicle access permit to reach their home through the Minjerribah Recreation Area can apply for a fee exemption, with evidence, each year (Recreation Areas Management Regulation 2017 s58). Traditional Owners exercising native title rights are exempt from the fee; for  | https://www.qld.gov.au/environment/parks/permits/exemption-vap-fee |
| au/minjerribah | camping-and-native-title | QYAC manages cultural heritage on Quandamooka Country under the Aboriginal Cultural Heritage Act 2003: anyone carrying out a land-use activity owes a duty of care (fines up to AUD 166,900 for individuals), and anything that may be cultural heritage should be left untouched and reported to QYAC. Resi | https://qyac.net.au/cultural-heritage/ |
| au/qld-council-6250 | property-and-rates | Redland City rates are billed quarterly; they can be paid online, by BPAY, phone, direct debit, post or in person, so set up payment before a long trip. | https://www.redland.qld.gov.au/Rates-fees-and-infringements/Rates |
| au/qld-council-6250 | animals | Dogs and cats must be microchipped and registered with Council, and registration renewed every 12 months (online through myServices or Quick Pay, by phone or in person), so a renewal can fall due while you are away. A carer must keep the animal on your property and follow Local Law 2 (Animal Managem | https://www.redland.qld.gov.au/Animals-and-pets/Dogs-and-cats/About-dogs-and-cats |
| au/qld | driving-and-vehicles | Queensland does not issue international driving permits; check the destination's licensing rules, and get an IDP from the motoring club if needed, carrying your Queensland licence with it. | https://www.qld.gov.au/transport/licensing/driver-licensing/overseas/driving-interstate-or-overseas |
| au/qld | driving-and-vehicles | Vehicle registration can be renewed online from overseas; renew by the due date to avoid a late fee. An expired registration makes the vehicle unregistered and driving it is an offence. | https://www.qld.gov.au/transport/registration/fees/pay/online |
| au/qld | voting | For Queensland state elections, eligible voters who are overseas can vote by telephone during the early voting period. | https://www.ecq.qld.gov.au/how-to-vote/ways-to-vote |
| au | departure-and-return | On return, complete the Incoming Passenger Card accurately (a digital Australia Travel Declaration is being piloted on some Qantas flights). Adults can bring AUD 900 of general goods duty free; over the allowance, duty and tax apply to every item of that type. Goods claimed under the Tourist Refund  | https://www.abf.gov.au/entering-and-leaving-australia/duty-free |
| au | departure-and-return | Declare food, plant material and animal products, including goods you took overseas and brought back. Clean hiking, fishing and camping gear and footwear. Declared goods are not penalised under the Biosecurity Act 2015 even if refused; false or missing declarations can bring an infringement notice o | https://www.agriculture.gov.au/biosecurity-trade/policy/faqs |
| au | travel-advice-and-insurance | Smartraveller offers free email and SMS updates for each destination, and says that if you can't afford travel insurance, you can't afford to travel. | https://www.smartraveller.gov.au/consular-services/resources/travel-smart |
| au | consular-help-and-limits | Consular help is not a legal right and may be limited if your actions were illegal or repeatedly reckless. DFAT may replace passports (fee), give lists of doctors and lawyers, check on you if detained, contact family with consent and provide some notarial and voting services. It can't give legal adv | https://www.smartraveller.gov.au/our-role/consular-services-charter |
| au | laws-that-follow-you | Australian citizens and residents can be prosecuted in Australia for child sex offences committed overseas (Criminal Code Division 272); the AFP investigates. | https://afp.gov.au/crimes/crimes-against-children/travelling-child-sex-offenders |
| au | laws-that-follow-you | Bribing a foreign public official is an offence for Australians anywhere (Criminal Code s 70.2), with up to 10 years' imprisonment for individuals. | https://www.ag.gov.au/crime/foreign-bribery/foreign-bribery-offences-and-penalties |
| au | laws-that-follow-you | Supplying technology on the Defence and Strategic Goods List overseas, including by email, cloud access or screen-sharing, generally needs a Defence permit unless an exemption applies. Relevant only if your work touches controlled technology. | https://www.defence.gov.au/business-industry/exporting/compliance/obligations-requirements |
| au | tax-residency | You generally stay an Australian resident for tax if you go overseas temporarily and do not set up a permanent home elsewhere; moving from country to country does not create one. Residents declare worldwide income and may claim a foreign income tax offset. You can lodge from overseas through myTax ( | https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/your-tax-residency/australian-resident-for-tax-purposes |
| au | health-cover | Medicare does not cover you overseas. Reciprocal health care agreements with 11 countries (Belgium, Finland, Ireland, Italy, Malta, the Netherlands, New Zealand, Norway, Slovenia, Sweden, the UK) may cover urgent care, usually with a co-payment; they don't cover evacuation and don't replace travel i | https://www.smartraveller.gov.au/travel-essentials/travel-health/using-healthcare-agreement-medical-care |
| au | health-cover | Strict rules apply to taking PBS medicines overseas; carry them for personal use and check they are legal at the destination. | https://www.servicesaustralia.gov.au/health-care-planning-when-going-overseas?context=60040 |
| au | voting | Federal voting is not compulsory while overseas, but tell the AEC (overseas notification form) or you will be asked to explain. Enrolled voters leaving for longer can register as an overseas elector up to 3 months before or within 3 years after leaving, valid 6 years; vote by post or in person at se | https://www.aec.gov.au/overseas/overseas-elector.htm |

Topics not yet recorded at any level (vet these first): none.
Rates notices, vehicle registration and the VAP fee exemption have no due dates in the repo: date not recorded; check each renewal notice and add the date when known.
