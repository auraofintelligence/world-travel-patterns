"""Build the recheck plan: what future automations should check, and when, for each location.

Reads only repo data (no network): patterns/*.json, data/watch.json, data/advisories.json,
data/calendar/pending-official-dates.json, data/vetting/*.json.

    python scripts/recheck_plan.py            -> config/recheck-plan.json and docs/AUTOMATION-CHECKLIST.md
    python scripts/recheck_plan.py --check    -> exit 1 if either file is stale
"""
import argparse
import datetime
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_patterns, load_places, read, today  # noqa: E402

PLAN = ROOT / "config/recheck-plan.json"
DOC = ROOT / "docs/AUTOMATION-CHECKLIST.md"
MONTHS = "January February March April May June July August September October November December".split()
MRX = "|".join(MONTHS)
DATE_RX = re.compile(r"\b(until|by|ends?|starts?|expires?|from|before|to)\s+(?:(\d{1,2}) )?(%s) (20\d\d)" % MRX)
SKIP_PATTERNS = {"year-ahead", "culture-cycles", "seasons-and-flow", "births-and-family-support", "works-and-purpose"}
SKIP_KEYS = ("supports", "title", "url", "source", "authority")
LEVEL_RANK = {"Do not travel": 4, "Reconsider your need to travel": 3, "Exercise a high degree of caution": 2,
              "Exercise normal safety precautions": 1}
TIERS = [(1, "daily"), (7, "weekly"), (30, "monthly"), (90, "quarterly"), (365, "yearly")]

# Plain-English reason and official source for each pattern. Frequency comes from the pattern's baseline_days.
GLOBAL = {
    "advisory": ("Smartraveller advice level and 'latest update' for every destination", "Smartraveller destinations export (smartraveller.gov.au/destinations-export)", "Levels can change overnight after conflict, unrest or disaster."),
    "entry": ("Visa-free status, max stay, arrival cards and refusals for an ordinary Australian passport", "Destination immigration authority or embassy in Australia; Smartraveller entry section", "Waivers and exemptions are often time-limited (China, South Korea, Belarus) or cut at short notice (Thailand, Sep 2026)."),
    "visa-preparation": ("Visa fees, e-visa portals, processing times, documents", "Destination e-visa or embassy page", "Fees and portals change with little notice; atlas baselines must be rechecked."),
    "activities": ("What an Australian may do on each entry route (tourism, meetings, speaking, remote work)", "Destination immigration and labour authorities", "Work rules are the most common 'confirm in writing' gap."),
    "health-entry": ("Vaccination certificates (yellow fever), health declarations, outbreak rules", "Destination health authority; Smartraveller health section; WHO", "Outbreaks add requirements quickly."),
    "zone-requirements": ("Permits for restricted areas, land councils, parks, island governments, border zones", "The zone authority itself", "Permit lead times decide when the approach phase starts."),
    "money-and-cost": ("Currency, cash limits, card acceptance, tourist taxes", "Central bank or government", "Rates move daily but rules (cash limits, tourist taxes) change slowly."),
    "consular": ("Australian embassy or consulate and its contact details", "DFAT mission list; Smartraveller", "Missions open, close or suspend services."),
    "local-law": ("Laws that catch visitors: ID, photography, dress, LGBTQIA+, alcohol", "The level's own legislation; Smartraveller local laws", "Laws stack from country to state to city."),
    "psychoactive-substances": ("Alcohol, cannabis, psilocybin, prescription medicines", "Legislation and health regulator; Smartraveller drugs section", "Several programs have start dates (e.g. New Mexico psilocybin)."),
    "affection-and-relationships": ("Public affection, relationships, LGBTQIA+ law", "Legislation; Smartraveller local customs", "Law reforms happen in both directions."),
    "culture-cycles": ("Public holidays, Ramadan and Islamic months, lunar new year, festivals", "National calendars; Nager.Date as a signal", "Lunar and Islamic calendars move every year; next year's holidays are often announced late in the year."),
    "culture-and-protocol": ("Etiquette, respecting Country, community visitor guidance", "The community's own guidance", "Slow-changing."),
    "year-ahead": ("Elections, major events and dated rule changes in the next 12 months", "Electoral commissions; organisers; data/watch.json", "Organisers announce next year's dates on known months; elections get called."),
    "seasons-and-flow": ("Weather seasons, crowds, cyclone and monsoon windows", "National met service; tourism statistics", "Slow-changing, but check before a trip."),
    "languages": ("Official and widely spoken languages", "Constitution, census", "Very slow-changing."),
    "births-and-family-support": ("Birth rates and family support", "UN WPP; national statistics", "Annual data releases."),
    "works-and-purpose": ("Luke's own work tie-ins (venues, partners, events)", "Luke's repos; venue pages", "Tagged places only."),
    "ancient-sites-and-mysteries": ("Access, tickets, permits, diving rules and heritage-law protection at ancient, underground and underwater sites", "UNESCO World Heritage Centre; national heritage or antiquities authorities; site and park authorities", "Opening, ticket caps and closures change; lore stays labelled as claims."),
    "australian-law-abroad": ("Australian law and guidance that applies to Australians overseas", "Commonwealth agency pages (DFAT, ABF, DAFF, ATO, Services Australia, AEC, AFP, AGD, Defence)", "Rules and thresholds change."),
}
EXTRA_GLOBAL = [
    ("ETIAS and EES rollout (Schengen and EU)", "travel-europe.europa.eu/etias_en and /ees_en", "monthly", "Start date not settled; watch item eu-etias (check every 30 days)."),
    ("Official source pages still alive (hash and 404 check)", "data/source-status.json via scripts/source_watch.py", "weekly", "A changed hash flags a page to reread; a failed fetch is not evidence of a rule change."),
    ("Next year's public holidays file (data/calendar/holidays-<next year>.json)", "National calendars; Nager.Date", "yearly (October to December)", "Governments publish next year's holiday lists late in the year; Islamic dates are confirmed by moon sighting nearer the time."),
]


def tier(days):
    for limit, name in TIERS:
        if days <= limit:
            return name
    return "yearly"


def fdate(d):
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def text_dates(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if not k.endswith(SKIP_KEYS):
                yield from text_dates(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for v in obj:
            yield from text_dates(v, path)
    elif isinstance(obj, str):
        for m in DATE_RX.finditer(obj):
            day = int(m.group(2)) if m.group(2) else None
            mon, year = MONTHS.index(m.group(3)) + 1, int(m.group(4))
            d = datetime.date(year, mon, day) if day else datetime.date(year, mon, 28)
            s = max(0, m.start() - 110)
            snippet = obj[s:m.end() + 20].strip()
            yield d, bool(day), path, ("..." if s else "") + snippet


def build(on):
    places, patterns = load_places(), load_patterns()
    adv = read(ROOT / "data/advisories.json")["destinations"]
    watch = read(ROOT / "data/watch.json")["items"]
    pending = read(ROOT / "data/calendar/pending-official-dates.json")["events"]
    horizon = on + datetime.timedelta(days=400)

    glob_rows = []
    for pid, pat in sorted(patterns.items(), key=lambda kv: kv[1].get("baseline_days", 999)):
        what, src, why = GLOBAL.get(pid, (pat.get("question", ""), "; ".join(pat.get("sources", [])), ""))
        glob_rows.append({"pattern": pid, "check": what, "source": src, "baseline_days": pat.get("baseline_days"),
                          "frequency": tier(pat.get("baseline_days", 365)), "why": why})
    extra = [{"check": c, "source": s, "frequency": f, "why": w} for c, s, f, w in EXTRA_GLOBAL]

    triggers, per = [], {}

    def loc(pid):
        return per.setdefault(pid, {"place": pid, "items": [], "reasons": set()})

    for w in watch:
        if w.get("status") == "resolved":
            continue
        eff = w.get("effective")
        triggers.append({"date": eff, "kind": "rule-change", "places": w["places"], "what": w["what"],
                         "check": w.get("next", ""), "source": (w.get("sources") or [""])[0], "id": w["id"],
                         "cadence": f"every {w.get('check_every_days', 30)} days until resolved"})
        for pid in w["places"]:
            loc(pid)["items"].append(w["id"])
            loc(pid)["reasons"].add("watch item")
    for e in pending:
        triggers.append({"date": None, "kind": "pending-event-date", "places": [e["place"]], "what": e["event"],
                         "check": f"{e['status']}. Date not announced; check monthly from {MONTHS[on.month - 1]} {on.year}.",
                         "source": e.get("official_url", ""), "cadence": "monthly until the organiser publishes"})
        loc(e["place"])["items"].append("pending date: " + e["event"])
        loc(e["place"])["reasons"].add("pending event")

    for f in sorted((ROOT / "data/vetting").glob("*.json")):
        rec = read(f)
        pid = rec.get("place") or f.stem.replace("__", "/")
        pats = rec.get("patterns", {})
        evid, seen = set(), set()
        confirm = snapshot = 0
        for name, body in pats.items():
            if not isinstance(body, dict):
                continue
            blob = json.dumps(body)
            evid.update(re.findall(r'"evidence": "([a-z-]+)"', blob))
            confirm += blob.count('"confirm-in-writing"')
            snapshot += len(re.findall(r"snapshot", blob, re.I))
            if name == "year-ahead":
                for ev in body.get("events", []):
                    d = ev.get("date")
                    if ev.get("by") in ("elections",) and d and on.isoformat() <= d <= horizon.isoformat():
                        triggers.append({"date": d, "kind": "election", "places": [pid], "what": ev["what"],
                                         "check": "Recheck advisory and local law 30 days before and in the week of the vote; confirm the date with the electoral commission.",
                                         "source": ev.get("url", ""), "cadence": "monthly; weekly in the final 30 days"})
                        loc(pid)["items"].append(f"election {d}")
                        loc(pid)["reasons"].add("election")
                continue
            if name in SKIP_PATTERNS:
                continue
            for d, exact, path, snip in text_dates(body):
                if d < on or d > horizon + datetime.timedelta(days=365) or (pid, d) in seen:
                    continue
                seen.add((pid, d))
                triggers.append({"date": d.isoformat(), "date_exact": exact, "kind": "law-or-rule-date", "places": [pid],
                                 "what": f"{name}: {snip}", "check": "Recheck the official source about 60 days before, and again on the date.",
                                 "source": "", "cadence": "monthly; weekly in the final 60 days"})
                loc(pid)["items"].append(f"{name} date {d.isoformat()}")
                loc(pid)["reasons"].add("dated rule")
        if "legacy-baseline" in evid:
            loc(pid)["reasons"].add("legacy baseline")
        if snapshot:
            loc(pid)["reasons"].add("snapshot evidence")
        if confirm:
            loc(pid)["items"].append(f"{confirm} confirm-in-writing")
            loc(pid)["reasons"].add("confirm in writing")

    # Advisory risk
    for pid, p in places.items():
        slug = p.get("smartraveller")
        if slug and slug in adv and pid in per or (slug in adv and LEVEL_RANK.get(adv[slug]["level"], 0) >= 3 if slug else False):
            level = adv[slug]["level"]
            r = loc(pid)
            r["advisory"] = level
            if LEVEL_RANK.get(level, 0) >= 3:
                r["reasons"].add("high advisory")

    rows = []
    for pid, r in per.items():
        country = pid.split("/")[0]
        level = r.get("advisory")
        if not level and country in places and places[country].get("smartraveller") in adv:
            level = adv[places[country]["smartraveller"]]["level"]
        rank = LEVEL_RANK.get(level, 0)
        reasons = r["reasons"]
        if rank == 4:
            cad = "weekly"
        elif rank == 3 or reasons & {"watch item", "legacy baseline"}:
            cad = "fortnightly"
        elif reasons & {"pending event", "dated rule", "election", "snapshot evidence"} or rank == 2:
            cad = "monthly"
        else:
            cad = "quarterly"
        items = list(dict.fromkeys(r["items"]))
        rows.append({"place": pid, "name": places.get(pid, {}).get("name", pid), "advisory": level or "",
                     "cadence": cad, "reasons": sorted(reasons), "items": items})
    order = {"weekly": 0, "fortnightly": 1, "monthly": 2, "quarterly": 3}
    rows.sort(key=lambda x: (order[x["cadence"]], x["place"]))
    triggers.sort(key=lambda t: (t["date"] is None, t["date"] or "", t["places"][0]))

    return {"generated": on.isoformat(), "note": "Built by scripts/recheck_plan.py from repo data only. Read-only plan for future automations; never a reason to skip an official recheck.",
            "global": glob_rows, "global_extra": extra, "triggers": triggers, "locations": rows}


def esc(s):
    return str(s).replace("|", "/").replace("\n", " ")


def render(plan):
    L = ["# Automation checklist", "",
         f"What future automations should check, and when. Generated {plan['generated']} by `scripts/recheck_plan.py` from repo data (machine copy: `config/recheck-plan.json`). Rebuild instead of editing by hand.",
         "", "Rules that always apply: a failed fetch is not evidence of a change; never use projected or third-party dates; travel windows (config/cadence.json phases: 90, 30, 7 days out, daily in place) tighten everything below.",
         "", "## A. Global checks per pattern", "", "| Pattern | What to check | Official source | How often | Why |", "|---|---|---|---|---|"]
    for g in plan["global"]:
        L.append(f"| {g['pattern']} | {esc(g['check'])} | {esc(g['source'])} | {g['frequency']} ({g['baseline_days']} d) | {esc(g['why'])} |")
    for g in plan["global_extra"]:
        L.append(f"| (cross-cutting) | {esc(g['check'])} | {esc(g['source'])} | {g['frequency']} | {esc(g['why'])} |")
    L += ["", "## B. Dated triggers (sorted by date; undated at the end)", "", "| Date | Kind | Place | What | Check |", "|---|---|---|---|---|"]
    for t in plan["triggers"]:
        d = t["date"] or "date not announced"
        if t.get("date_exact") is False:
            d = d[:7] + " (month only)"
        L.append(f"| {d} | {t['kind']} | {', '.join(t['places'][:6])}{' +' + str(len(t['places']) - 6) if len(t['places']) > 6 else ''} | {esc(t['what'])[:260]} | {esc(t['check'])[:220]} |")
    L += ["", "Not in the repo yet: Brisbane Writers Festival 2027 (no record found in data/; add it to pending-official-dates.json before automations can watch it).",
          "", "## C. Per-location watch list", "",
          "Cadence: weekly = Do not travel; fortnightly = Reconsider your need to travel, an open watch item or legacy-baseline evidence; monthly = high degree of caution, pending event dates, dated rules, elections or snapshot-only evidence; quarterly = only confirm-in-writing gaps.",
          "", f"{len(plan['locations'])} locations have specific watch items.", "", "| Place | Advisory | Recheck | Why | Watch items |", "|---|---|---|---|---|"]
    for r in plan["locations"]:
        items = "; ".join(r["items"][:4]) + (f"; +{len(r['items']) - 4} more" if len(r["items"]) > 4 else "")
        L.append(f"| {r['place']} | {esc(r['advisory'])} | {r['cadence']} | {', '.join(r['reasons'])} | {esc(items)} |")
    L += [""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    on = datetime.date.fromisoformat(a.date) if a.date else today()
    plan = build(on)
    js, md = json.dumps(plan, indent=1, ensure_ascii=False, default=sorted) + "\n", render(plan)
    if a.check:
        ok = PLAN.exists() and PLAN.read_text(encoding="utf-8") == js
        sys.exit(0 if ok else 1)
    PLAN.write_text(js, encoding="utf-8")
    DOC.write_text(md, encoding="utf-8")
    print(f"recheck plan: {len(plan['triggers'])} triggers, {len(plan['locations'])} locations")


if __name__ == "__main__":
    main()
