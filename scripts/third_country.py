"""Source priority: a destination's own official sources first, Smartraveller second. Another country's travel
advice (UK FCDO, US State Department, Canada, NZ SafeTravel, France, Germany) is never a source for somewhere else.

THIRD_COUNTRY(place_id, url) is True when the url is another government's traveller advice for that place.
Used by validate.py and by the one-off clean-up `python scripts/third_country.py --strip`.
"""
import json
import pathlib
import re
import sys

ADVICE = [
    (re.compile(r"gov\.uk/foreign-travel-advice"), ("gb",)),
    (re.compile(r"travel\.gc\.ca/destinations"), ("ca",)),
    (re.compile(r"travel\.state\.gov/.*travel-advisories"), ("us", "gu", "pr", "vi", "as", "mp", "um")),
    (re.compile(r"safetravel\.govt\.nz"), ("nz", "ck", "nu", "tk")),
    (re.compile(r"diplomatie\.gouv\.fr/fr/(conseils|information-par-pays)"), ("fr", "gf", "gp", "mq", "re", "yt", "pm", "bl", "mf", "pf", "nc", "wf", "tf")),
    (re.compile(r"auswaertiges-amt\.de"), ("de",)),
]
AUTH = re.compile(r"Foreign, Commonwealth|\bFCDO\b|U\.?S\.? Department of State|Global Affairs Canada|SafeTravel|Ministère de l'Europe|Auswärtiges Amt", re.I)


def third_country(place, url):
    for rx, home in ADVICE:
        if rx.search(url or ""):
            return place.split("/")[0] not in home
    return False


def is_third(place, x):
    if not isinstance(x, dict):
        return False
    urls = [x.get("url"), x.get("source")]
    if any(third_country(place, u) for u in urls if isinstance(u, str)):
        return True
    return bool(AUTH.search(str(x.get("authority", "")))) and not any(isinstance(u, str) and u for u in urls if u and not third_country(place, u)) and place.split("/")[0] not in ("gb", "us", "ca", "nz", "fr", "de")


def strip(place, body):
    """Remove third-country items and sources. Returns (body or None, flagged)."""
    flagged = False
    had_sources = bool(body.get("sources"))
    for k, v in list(body.items()):
        if isinstance(v, list) and any(is_third(place, x) for x in v):
            body[k] = [x for x in v if not is_third(place, x)]
            flagged = True
        elif isinstance(v, list):
            for x in v:
                if isinstance(x, dict) and isinstance(x.get("url"), str) and third_country(place, x["url"]):
                    x.pop("url"); flagged = True
        elif isinstance(v, str) and AUTH.search(v) and k in ("note", "notes"):
            body.pop(k); flagged = True
        elif isinstance(v, dict) and AUTH.search(json.dumps(v)):
            body.pop(k); flagged = True
    if not flagged:
        return body, False
    if (had_sources and not body.get("sources")) or any(k in body and not body[k] for k in ("laws", "items", "layers", "activities")):
        return None, True
    return body, True


if __name__ == "__main__" and "--strip" in sys.argv:
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    from lib import VETTING
    gone, kept = [], []
    for path in sorted(VETTING.glob("*.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for pid in list(rec["patterns"]):
            body, flagged = strip(rec["place"], rec["patterns"][pid])
            if not flagged:
                continue
            changed = True
            if body is None:
                del rec["patterns"][pid]; gone.append(f"{rec['place']}#{pid}")
            else:
                body["needs_recheck"] = True
                body["source_note"] = "Another country's travel advice was removed as a source on 4 November 2026; recheck the text against the place's own official sources."
                kept.append(f"{rec['place']}#{pid}")
        if changed:
            path.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("removed", len(gone)); print(" ".join(gone)); print("kept with flag", len(kept)); print(" ".join(kept))
