"""Draft psychoactive-substances records from Smartraveller destination pages.

Reads the full advice (safety, health, local laws) sentence by sentence and sorts what it finds by
substance: alcohol, tobacco and vaping, cannabis, MDMA, psilocybin, ayahuasca and DMT, kava, khat, and
drug law in general (each sentence goes to the first substance it names). Each item is law, custom or safety, and dated changes are flagged. A first draft
for a place pass: check every item against the page.

    python scripts/smartraveller_substances.py --dir PAGES th nl jm
    python scripts/smartraveller_substances.py --all --dir PAGES

Writes psychoactive-substances into data/vetting/<id>.json, dated today, evidence "official"
(Australian Government advice), keeping any items not written by this script.
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from consular import fetch, page_text  # noqa: E402
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402
from smartraveller_draft import clean, sections  # noqa: E402

NOT_HEADS = re.compile(r"assault|crime|scam|fraud|kidnap|terror|insurance|hiv|disease|emergenc|contacts?$|dating|social media|insect|rabies|mpox|ebola|conflict|unrest|armed|security|border|altitude", re.I)
SUBSTANCES = [
    ("ayahuasca-and-dmt", re.compile(r"ayahuasca|\bDMT\b|san pedro|mescaline|peyote|iboga", re.I)),
    ("psilocybin", re.compile(r"psilocybin|magic mushroom|hallucinogenic mushroom|mushroom", re.I)),
    ("mdma", re.compile(r"\bMDMA\b|ecstasy", re.I)),
    ("cannabis", re.compile(r"cannabis|marijuana|\bCBD\b|\bTHC\b|hashish|\bweed\b", re.I)),
    ("kava", re.compile(r"\bkava\b|\byaqona\b|\bsakau\b", re.I)),
    ("khat", re.compile(r"\bkhat\b|\bqat\b|\bmiraa\b", re.I)),
    ("tobacco-and-vaping", re.compile(r"vape|vaping|e-cigarette|tobacco|cigarette|smoking|\bsmoke in\b|nicotine|hookah|shisha", re.I)),
    ("alcohol", re.compile(r"alcohol|drink-driving|drunk|liquor|beer|wine|spirits|methanol|drink spiking|intoxicat", re.I)),
    ("drugs-in-general", re.compile(r"\bdrugs?\b|narcotic|trafficking", re.I)),
]
LAW = re.compile(r"authorities|illegal|\blegal|\blaws?\b|arrest|penalt|prison|jail|\bfines?\b|criminal|prosecut|death penalty|corporal|"
                 r"offence|banned|\bban\b|prohibit|licen[cs]|permit|allowed|not allowed|decriminali[sz]|legali[sz]|prescription|declare|confiscat", re.I)
SAFETY = re.compile(r"methanol|spik|poison|counterfeit|fake|contaminat|laced|overdose", re.I)
CHANGING = re.compile(r"decriminali[sz]|legali[sz]ed|since (19|20)\d\d|in (19|20)\d\d|from \d{1,2} \w+ 20\d\d|new law|recently|came into force|took effect", re.I)
SKIP = re.compile(r"legal advice|smartraveller|consular|Australian Government|more information|see source|contact the|^See |"
                  r"Australian laws|could be charged in Australia|Carry a copy of your prescription|drone|altitude|"
                  r"^Drink spiking can happen anywhere|^Methanol is highly toxic|^Methanol can be added|^Taking drugs will weaken|"
                  r"^Penalties for drug offences are severe\.$|^Don't carry or use illegal drugs\.$", re.I)


def items_from(secs, url, on):
    found, seen, per = [], set(), {}
    for title, body in secs:
        if NOT_HEADS.search(title):
            continue
        text = clean(body)
        for sentence in re.split(r"(?<=[.!?])\s+(?=[A-Z])|(?<=[a-z])\s+(?=(?:The|If|Avoid|You|Penalties|Possession|Using|It is|It's) )", text):
            s = sentence.strip()
            if len(s) < 25 or SKIP.search(s) or s in seen:
                continue
            hits = [(m.start(), k) for k, rx in SUBSTANCES[:-1] for m in [rx.search(s)] if m]
            sub = min(hits)[1] if hits else ("drugs-in-general" if SUBSTANCES[-1][1].search(s) else None)
            if not sub:
                continue
            per[sub] = per.get(sub, 0) + 1
            if per[sub] > 4:
                continue
            seen.add(s)
            kind = "safety" if SAFETY.search(s) else "law" if LAW.search(s) else "custom"
            item = {"substance": sub, "kind": kind, "text": s[:320], "source": url, "checked": on, "by": "smartraveller_substances"}
            if CHANGING.search(s):
                item["changing"] = True
            found.append(item)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("places", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--skip-region", action="append", default=[])
    ap.add_argument("--dir")
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    adv = read(ROOT / "data/advisories.json", {"destinations": {}})["destinations"]
    todo = args.places or [pid for pid, p in places.items() if args.all and p.get("smartraveller") and p.get("region") not in args.skip_region]
    counts = {"written": 0, "nothing": 0}
    for pid in todo:
        key = places[pid].get("smartraveller")
        dest = adv.get(key)
        if not dest:
            continue
        page = pathlib.Path(args.dir) / f"{key}.html" if args.dir else None
        raw = page.read_text(encoding="utf-8", errors="replace") if page and page.exists() else fetch(dest["url"])
        if not raw:
            print(f"{pid}: fetch failed, nothing written")
            continue
        lines = page_text(raw)
        secs = sections(lines)
        full = next((i for i, (t, _) in enumerate(secs) if t == "Full advice"), 0)
        stop = next((i for i in range(full + 1, len(secs)) if secs[i][0] in ("Travel", "Local contacts")), len(secs))
        items = items_from(secs[full + 1:stop], dest["url"], D)
        if not items:
            counts["nothing"] += 1
            continue
        updated = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("Updated:")), "")
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].setdefault("psychoactive-substances", {"status": "partly-mapped", "evidence": "official", "items": [], "sources": [],
                                                                     "notes": "Read from the Australian Government's travel advice; confirm with the country's own law."})
        body["items"] = [i for i in body.get("items", []) if i.get("by") != "smartraveller_substances"] + items
        body["checked"] = D
        src = {"title": f"{dest['title']} travel advice (updated {updated})", "authority": "Smartraveller, Australian Government",
               "url": dest["url"], "checked": D, "supports": "drugs, alcohol, vaping and local laws as read on " + D}
        body["sources"] = [s for s in body.get("sources", []) if s["url"] != dest["url"]] + [src]
        write(path, rec)
        counts["written"] += 1
    print(counts)


if __name__ == "__main__":
    main()
