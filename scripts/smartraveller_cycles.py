"""Draft seasons-and-flow hazard windows and culture-cycle notes from Smartraveller destination pages.

A first draft for a place pass. Hazard months come only from sentences that name a month range in a
weather, cyclone, monsoon, hurricane, typhoon, fire, flood, snow or heat section; the agent reviews the
printed windows before committing. Culture cycles get Ramadan (when the page has a Ramadan section),
holiday-linked closures, the machine holiday count and Easter. Visitor flow is left empty: it needs
tourism statistics.

    python scripts/smartraveller_cycles.py --dir PAGES --print  ID...   # show what would be drafted
    python scripts/smartraveller_cycles.py --dir PAGES ID...            # write, skipping patterns already checked today
"""
import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from consular import fetch, page_text  # noqa: E402
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402
from smartraveller_draft import clean, sections  # noqa: E402

MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
HAZARD_HEAD = re.compile(r"weather|cyclone|monsoon|hurricane|typhoon|fire|flood|snow|heat|storm|tornado|avalanche|climate|rain|season|dust|winter|natural disaster", re.I)
RANGE = re.compile(r"\b(" + "|".join(MONTHS) + r")\b\s*(?:to|and|until|through|-|–)\s*(?:the end of\s+|early\s+|late\s+|mid-?\s*)?\b(" + "|".join(MONTHS) + r")\b", re.I)
LABEL = [(r"typhoon", "typhoon season"), (r"hurricane", "hurricane season"), (r"cyclone", "cyclone season"), (r"monsoon", "monsoon season"),
         (r"wet season|rainy season|rains", "wet season"), (r"bushfire|forest fire|wildfire|fire", "fire season"), (r"flood", "flood risk"),
         (r"avalanche", "avalanche risk"), (r"snow|blizzard|\bice\b", "winter conditions"), (r"heat", "extreme heat"), (r"dust|sand", "dust storms"),
         (r"tornado", "tornadoes"), (r"(?<!dust )storms?\b", "storm season")]


def span(a, b):
    a, b = MONTHS.index(a.lower()) + 1, MONTHS.index(b.lower()) + 1
    return list(range(a, b + 1)) if a <= b else list(range(a, 13)) + list(range(1, b + 1))


def windows(secs):
    found = []
    for title, body in secs:
        if not HAZARD_HEAD.search(title):
            continue
        for sent in re.split(r"(?<=\.)\s", clean(body)):
            for m in RANGE.finditer(sent):
                # Label from the words just before this range, then the sentence, then the heading.
                near = sent[max(0, m.start() - 90):m.end()]
                # The hazard word closest before the months wins ("...cyclones. The monsoon season is from June...").
                hits = [(max(x.start() for x in re.finditer(pat, near, re.I)), lab) for pat, lab in LABEL if re.search(pat, near, re.I)]
                label = max(hits)[1] if hits else next((lab for pat, lab in LABEL if re.search(pat, title, re.I)), None)
                if label:
                    found.append({"months": span(m.group(1), m.group(2)), "label": label, "sentence": sent[:240], "section": title})
    # One window per label: the union of the months each statement gives for it.
    # Ranges merge only within one sentence ("May to June and October to November"); a later sentence
    # may describe another region, so the first statement for each label stands.
    out = {}
    for w in found:
        if w["label"] not in out:
            out[w["label"]] = dict(w)
        elif out[w["label"]]["sentence"] == w["sentence"]:
            out[w["label"]]["months"] = sorted(set(out[w["label"]]["months"]) | set(w["months"]))
    return list(out.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("places", nargs="+")
    ap.add_argument("--dir")
    ap.add_argument("--print", action="store_true", dest="show")
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    adv = read(ROOT / "data/advisories.json", {"destinations": {}})["destinations"]
    hol = read(ROOT / f"data/calendar/holidays-{today().year + 1}.json", {"places": {}})["places"]
    for pid in args.places:
        key = places[pid].get("smartraveller")
        dest = adv.get(key) if key else None
        if not dest:
            print(f"{pid}: no Smartraveller page"); continue
        f = pathlib.Path(args.dir or ".") / f"{key}.html"
        raw = f.read_text(encoding="utf-8", errors="replace") if args.dir and f.exists() else fetch(dest["url"])
        if not raw:
            print(f"{pid}: fetch failed"); continue
        secs = sections(page_text(raw))
        wins = windows(secs)
        ramadan = any(re.search(r"ramadan", t, re.I) for t, _ in secs)
        closures = []
        full = next((i for i, (t, _) in enumerate(secs) if t == "Full advice"), 0)
        stop = next((i for i in range(full, len(secs)) if secs[i][0] in ("Local contacts", "Consular contacts")), len(secs))
        for t, b in secs[full:stop]:
            txt = clean(b)
            for sent in re.split(r"(?<=\.)\s", txt):
                if re.search(r"(religious holidays?|public holidays?|election days?|voting days?|Friday prayers?|weekend is|working week)", sent, re.I) and re.search(r"(closed?|closes|illegal|ban|can't|not be sold|working week)", sent, re.I):
                    closures.append(sent[:260])
        closures = list(dict.fromkeys(closures))[:3]
        h = hol.get(pid, [])
        easter = [x["date"] for x in h if x["name"] in ("Good Friday", "Easter Monday", "Easter Sunday")]
        src = {"title": f"{dest['title']} travel advice", "authority": "Smartraveller, Australian Government", "url": dest["url"], "checked": D,
               "supports": "hazard seasons and closures as read on " + D}
        if args.show:
            print(f"===== {pid} {dest['title']}" + ("  [Ramadan]" if ramadan else "") + f"  holidays {len(h)}")
            for w in wins:
                print(f"  {w['label']}: {w['months']} | {w['sentence'][:160]}")
            for c in closures:
                print(f"  closure: {c[:180]}")
            continue
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        pats, wrote = rec["patterns"], []
        if wins and pats.get("seasons-and-flow", {}).get("checked") != D:
            months = [{"month": m, "season": None, "hazard": "; ".join(w["label"] for w in wins if m in w["months"]) or None, "visitor_flow": None} for m in range(1, 13)]
            pats["seasons-and-flow"] = {"status": "partly-mapped", "checked": D, "evidence": "official", "months": months,
                                        "notes": "Hazard windows from Smartraveller; regional climates can differ. Weather seasons and visitor flow are still to be read from the national meteorological service and tourism statistics.",
                                        "sources": [src]}
            wrote.append(f"seasons ({', '.join(w['label'] for w in wins)})")
        if (h or ramadan or closures) and pats.get("culture-cycles", {}).get("checked") != D:
            moving = []
            if ramadan:
                moving.append("Ramadan: about 11 days earlier each year. Expect daytime fasting, shorter business hours and care with eating, drinking and smoking in public.")
            if easter:
                moving.append(f"Easter moves each year (next year: {', '.join(easter)}).")
            srcs = [src] if (ramadan or closures) else []
            if h:
                srcs.append({"title": "Public holidays (Nager.Date)", "authority": "Signal: machine holiday data", "url": "https://date.nager.at/", "checked": D, "supports": f"{len(h)} public holidays next year"})
            pats["culture-cycles"] = {"status": "partly-mapped", "checked": D, "evidence": "official" if (ramadan or closures) else "signal",
                                      "public_holidays": f"{len(h)} next year in data/calendar (machine data; the brief lists those in a trip window)" if h else "Not in the machine holiday data: ask locally.",
                                      "moving_calendars": moving, "festivals": [], "closures": closures, "protocol_notes": [],
                                      "note": "Festivals and community closures are still to be read from the place's own tourism office and communities.", "sources": srcs}
            wrote.append("cycles")
        write(path, rec)
        print(f"{pid}: {', '.join(wrote) or 'nothing new'}")


if __name__ == "__main__":
    main()
