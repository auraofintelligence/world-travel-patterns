"""Draft local law, culture and protocol, and money records from a Smartraveller destination page.

A first draft for a place pass, not the finished record: the agent reads the printed visa text and
writes the entry record itself, and checks every drafted law against the page before committing.
Smartraveller describes the rules; the country's own sources remain the place to confirm them.

    python scripts/smartraveller_draft.py at id ie            # fetch pages with curl
    python scripts/smartraveller_draft.py --dir PAGES at id   # read <key>.html already fetched
    python scripts/smartraveller_draft.py --print at          # show the visa and medication text only

Writes local-law, culture-and-protocol and money-and-cost into data/vetting/<id>.json, dated today,
evidence "official" (Australian Government advice), unless that pattern was already checked today.
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from consular import fetch, page_text  # noqa: E402
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402

# Advice that appears on every page, word for word or nearly: not a local rule.
GENERIC = re.compile(r"^(When you travel to another country|The Australian Government is limited|Court proceedings can go on|"
                     r"Some Australian laws still apply|You could be charged in Australia|Not all medications|Ensure your medication|"
                     r"Carry a copy of your prescription|More information|Read the Consular Services Charter|If you're a dual national|"
                     r"However, we may only be able|Always travel on your Australian passport|Take care not to offend\.$|"
                     r"Ask for local advice if you're unsure|If in doubt, ask for local advice|-? ?medication names$|-? ?your required dosage$|"
                     r"-? ?that the medications are for your personal use)", re.I)
# No phone numbers or emails in a public record.
CONTACTS = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+|\+?\(?\d[\d ()-]{6,}\d")
SKIP_HEADS = {"Local law", "Local laws", "Australian laws", "Dual nationality", "Dual nationals"}
TOPICS = [
    (r"identity|identification|internet|vpn|exit ban|registration", "conduct-and-public-order"),
    (r"satellite|radio|telecom", "currency-and-goods"),
    (r"drug|cannabis|narcotic|medic", "drugs-and-prescription-medicines"),
    (r"alcohol|drink|drunk|liquor", "alcohol"),
    (r"relig|ramadan|blasphem|preach|speech|insult|monarch|royal|lese|flag|politic|criticis|social media|online", "speech-religion-and-respect"),
    (r"vap|cigar|tobacco|smok", "e-cigarettes-and-tobacco"),
    (r"film|media", "filming"),
    (r"photo", "photography"),
    (r"dress|cloth|modest|nudity|swimwear", "dress-and-public-behaviour"),
    (r"lgbt|same-sex|relationship|marriage|cohabit|sexual|affection|surrogacy|abortion|reproductive|dowr", "relationships-and-cohabitation"),
    (r"wildlife|biosecurity|souvenir|antiqu|coral|heritage|artefact|protected|export|war material", "wildlife-biosecurity-and-souvenirs"),
    (r"camp|bushfire|campfire|trespass|hiking|trekking|restricted area", "camping-fires-and-access"),
    (r"driv|road|licen", "driving-and-licences"),
    (r"currency|customs|import|goods", "currency-and-goods"),
    (r"work|employ|business|volunteer|overstay|visa", "work-and-payment"),
]


def sections(lines):
    out, title, body = [], None, []
    for line in lines:
        if line.startswith("## "):
            if title is not None:
                out.append((title, body))
            title, body = line[3:].strip(), []
        else:
            body.append(line)
    if title is not None:
        out.append((title, body))
    return out


def clean(body):
    keep = []
    for line in body:
        if GENERIC.match(line) or re.match(r"^- [A-Z][^.]{0,60}$", line) and not line.endswith(":"):
            continue  # boilerplate, or a bare "- Link title" bullet
        keep.append(line[2:] if line.startswith("- ") else line)
    text = " ".join(keep).replace(" " + chr(0x2014) + " ", ", ").replace(chr(0x2014), ", ").replace(chr(0x2013), "-")
    text = CONTACTS.sub("[see source]", re.sub(r":\s+", ": ", text))
    return re.sub(r"\s+", " ", text).strip()


def trim(text, n):
    """Cut at the last full sentence within n characters."""
    if len(text) <= n:
        return text
    cut = text[:n]
    end = max(cut.rfind(". "), cut.rfind(".\u201d"))
    return cut[:end + 1] if end > n // 2 else cut


def topic_for(title, text):
    for pattern, topic in TOPICS:
        if re.search(pattern, title, re.I):
            return topic
    for pattern, topic in TOPICS:
        if re.search(pattern, text[:160], re.I):
            return topic
    return "conduct-and-public-order"


def block(secs, start, stop):
    """Sections between the full-advice heading `start` and the next heading named in `stop`."""
    full = [i for i, (t, _) in enumerate(secs) if t == "Full advice"]
    i0 = full[0] if full else 0
    begin = next((i for i in range(i0, len(secs)) if secs[i][0].lower() == start.lower()), None)
    if begin is None:
        return []
    end = next((i for i in range(begin + 1, len(secs)) if secs[i][0].lower() in {x.lower() for x in stop}), len(secs))
    return secs[begin + 1:end]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("places", nargs="+")
    ap.add_argument("--dir")
    ap.add_argument("--print", action="store_true", dest="show")
    ap.add_argument("--force", action="store_true", help="redraft patterns already checked today")
    ap.add_argument("--only", help="comma list of patterns to write: local-law,culture,money (default all)")
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    adv = read(ROOT / "data/advisories.json", {"destinations": {}})["destinations"]
    for pid in args.places:
        key = places[pid].get("smartraveller")
        dest = adv.get(key)
        if not dest:
            print(f"{pid}: no Smartraveller page")
            continue
        if args.dir and (pathlib.Path(args.dir) / f"{key}.html").exists():
            raw = (pathlib.Path(args.dir) / f"{key}.html").read_text(encoding="utf-8", errors="replace")
        else:
            raw = fetch(dest["url"])
        if not raw:
            print(f"{pid}: fetch failed, nothing written")
            continue
        lines = page_text(raw)
        secs = sections(lines)
        updated = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("Updated:")), "")
        src = {"title": f"{dest['title']} travel advice (updated {updated})", "authority": "Smartraveller, Australian Government",
               "url": dest["url"], "checked": D, "supports": "local laws, customs and money as read on " + D}

        laws_secs = block(secs, "Local laws", {"Travel", "Local contacts"})
        travel = block(secs, "Travel", {"Local contacts"})
        health = block(secs, "Health", {"Local laws"})
        visa = [(t, clean(b)) for t, b in travel if re.search(r"visa|entry|border|passport validity|^validity|arrival", t, re.I)]
        meds = [(t, clean(b)) for t, b in health if re.search(r"^medication", t, re.I)]
        if args.show:
            print(f"===== {pid} {dest['title']} (updated {updated})")
            for t, txt in visa + meds:
                if txt:
                    print(f"## {t}\n{txt[:900]}")
            continue

        laws, customs, in_customs = [], "", False
        for title, body in laws_secs:
            text = clean(body)
            if title.lower().startswith("local custom"):
                in_customs = True  # subheadings after it (Ramadan, Dress...) belong to customs
            if in_customs:
                if text:
                    customs = (customs + " " + (text if title.lower().startswith("local custom") else f"{title}: {text}")).strip()
                continue
            if not text or title in SKIP_HEADS or title.startswith("Dual"):
                continue
            laws.append({"topic": topic_for(title, text), "rule": text[:700], "level": "country", "source": dest["url"], "checked": D,
                         "heading": title})
        for title, text in meds:
            if text:
                laws.append({"topic": "drugs-and-prescription-medicines", "rule": text[:700], "level": "country", "source": dest["url"],
                             "checked": D, "heading": title})
        for title, body in travel:
            text = clean(body)
            if re.search(r"driving permit|driver", title, re.I) and text:
                laws.append({"topic": "driving-and-licences", "rule": text[:500], "level": "country", "source": dest["url"], "checked": D, "heading": title})
            if re.search(r"^customs|biosecurity", title, re.I) and text:
                laws.append({"topic": "currency-and-goods", "rule": text[:500], "level": "country", "source": dest["url"], "checked": D, "heading": title})
        money = next((clean(b) for t, b in travel if t == "Money"), "")
        currency = re.search(r"(?:local currency|currency of [^.]*?) is (?:the )?([^.,]+?\)?)(?:\.|,| and )", money)

        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        pats = rec["patterns"]
        wrote = []
        only = set(args.only.split(",")) if args.only else {"local-law", "culture", "money"}
        if "local-law" not in only:
            laws = []
        if "culture" not in only:
            customs = ""
        if "money" not in only:
            money = ""
        if laws and (args.force or pats.get("local-law", {}).get("checked") != D):
            pats["local-law"] = {"status": "partly-mapped", "checked": D, "evidence": "official", "laws": laws, "sources": [src]}
            wrote.append(f"local-law ({len(laws)})")
        if customs and (args.force or pats.get("culture-and-protocol", {}).get("checked") != D):
            pats["culture-and-protocol"] = {"status": "ask-locally", "checked": D, "evidence": "official", "dress_and_conduct": trim(customs, 900),
                                            "cultural_authority": "Ask locally, through your host.",
                                            "note": "Read from the Australian Government's description of local customs.", "sources": [src]}
            wrote.append("culture")
        if money and (args.force or pats.get("money-and-cost", {}).get("checked") != D):
            pats["money-and-cost"] = {"status": "noted", "currency": currency.group(1).strip() if currency else None,
                                      "cash_card_notes": money[:600], "daily_cost_aud": None, "checked": D, "evidence": "official", "sources": [src]}
            wrote.append("money")
        write(path, rec)
        print(f"{pid}: {', '.join(wrote) or 'nothing new'}")


if __name__ == "__main__":
    main()
