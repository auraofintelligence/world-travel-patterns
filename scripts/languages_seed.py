"""Write the languages pattern from data/sources: official languages (Wikidata, with hand-chosen regional languages),
English capacity (European Commission Special Eurobarometer 540 for EU members, official; EF English Proficiency
Index 2025, a signal) and English hotspots (EF capital, city and region scores).

    python scripts/languages_seed.py

Replaces earlier items written by this script (marked "by": "languages_seed"); leaves every other item alone.
"""
import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402


def band(score):
    return "very high" if score >= 600 else "high" if score >= 550 else "moderate" if score >= 500 else "low" if score >= 450 else "very low"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-region", action="append", default=[])
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    off = read(ROOT / "data/sources/official-languages-wikidata.json")
    ef = read(ROOT / "data/sources/ef-epi-2025.json")
    efp = read(ROOT / "data/sources/ef-epi-2025-places.json")["countries"]
    eb = read(ROOT / "data/sources/eurobarometer-540.json")
    reg = read(ROOT / "data/sources/regional-languages.json")
    src_off, src_ef = dict(off["source"], checked=D), dict(ef["source"], checked=D)
    src_eb, src_reg = dict(eb["source"], checked=D), dict(reg["source"], checked=D)
    written = 0
    for pid in sorted(set(off["countries"]) | set(ef["countries"])):
        p = places.get(pid)
        if not p or "/" in pid or p.get("region") in args.skip_region:
            continue
        items, sources = [], []
        langs = off["countries"].get(pid)
        if langs:
            items.append({"area": "official", "kind": "law", "evidence": "signal", "text": f"Official or national languages: {', '.join(langs)}.",
                          "source": src_off["url"]})
            sources.append(src_off)
        b = eb["countries"].get(pid)
        if b:
            items.append({"area": "english", "kind": "figure", "evidence": "official",
                          "text": f"{b['english']}% of people aged 15 and over said they can hold a conversation in English as a language other than "
                                  "their mother tongue (European Commission, Special Eurobarometer 540, surveyed in 2023).", "source": src_eb["url"]})
            sources.append(src_eb)
        e = ef["countries"].get(pid)
        if e:
            items.append({"area": "english", "kind": "figure", "evidence": "signal",
                          "text": f"English proficiency score {e['score']} ({band(e['score'])}), ranked {e['rank']} of 123 in the EF English Proficiency Index 2025, "
                                  "from adults who took EF's online English test.", "source": src_ef["url"]})
            cap = ef["capitals"].get(pid)
            if cap:
                diff = cap["score"] - e["score"]
                rel = "above" if diff > 0 else "below" if diff < 0 else "level with"
                items.append({"area": "hotspots", "kind": "figure", "evidence": "signal",
                              "text": f"{cap['city']} scored {cap['score']} ({band(cap['score'])}), {rel} the national {e['score']}.", "source": src_ef["url"]})
            pl = efp.get(pid, {})
            top = [c for c in pl.get("cities", []) if not cap or c[0] != cap["city"]][:3]
            if top:
                items.append({"area": "hotspots", "kind": "figure", "evidence": "signal",
                              "text": ("Highest-scoring other cities: " if cap else "Highest-scoring cities: ") +", ".join(f"{c} {v} ({band(v)})" for c, v in top) + ".", "source": pl["page"]})
            if pl.get("regions"):
                r0 = pl["regions"][0]
                items.append({"area": "hotspots", "kind": "figure", "evidence": "signal",
                              "text": f"Highest-scoring region: {r0[0]} {r0[1]} ({band(r0[1])}), of {len(pl['regions'])} scored.", "source": pl["page"]})
            sources.append(src_ef)
        elif langs and "English" in langs:
            items.append({"area": "english", "kind": "law", "evidence": "signal", "text": "English is an official or national language here.", "source": src_off["url"]})
        write_items(pid, items, sources, D)
        written += 1
    for rid, r in reg["regions"].items():
        if rid in places and places[rid].get("region") not in args.skip_region:
            write_items(rid, [{"area": "official", "kind": "law", "evidence": "signal", "text": f"Official or co-official languages here: {', '.join(r['languages'])}.",
                               "source": src_reg["url"]}], [src_reg], D)
            written += 1
    print(f"languages: {written} places")


def write_items(pid, items, sources, D):
    if items:
        for it in items:
            it.update({"checked": D, "by": "languages_seed"})
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].setdefault("languages", {"status": "partly-mapped", "evidence": "signal", "items": [], "sources": [],
                                                        "notes": "Signals until the place's own language law and census are read."})
        body["items"] = items + [i for i in body.get("items", []) if i.get("by") != "languages_seed"]
        urls = {s["url"] for s in body["sources"]}
        body["sources"] += [s for s in sources if s["url"] not in urls]
        body["checked"] = D
        write(path, rec)


if __name__ == "__main__":
    main()
