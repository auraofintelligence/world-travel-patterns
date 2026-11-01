"""Build site/data/index.json, the compact index the website reads.

The website reads vetting records, feeds and advisories straight from data/, and uses this index
for the place tree, freshness, pattern coverage and the run list. It never reads private/.
It also writes sitemap.xml and llms.txt for search discovery (robots.txt is hand-kept).
Run after due.py: python scripts/build_site.py
"""
import json
import pathlib
import sys
from urllib.parse import quote

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, VETTING, applies, is_active, load_patterns, load_places, read, today  # noqa: E402


def main():
    places, patterns = load_places(), load_patterns()
    queue = read(ROOT / "queue/due.json", {"summary": {}, "queue": []})
    due = {entry["place"]: entry["due"] for entry in queue["queue"]}
    vetted = {read(p)["place"]: read(p)["patterns"] for p in VETTING.glob("*.json")}
    agent = [p for p in patterns.values() if p["method"] != "machine"]

    rows = []
    for pid, p in places.items():
        own = vetted.get(pid, {})
        applicable = [pat["id"] for pat in agent if applies(pat, p) and not (pat.get("skip_home") and pid == "au")]
        due_here = {d["pattern"]: d["reason"] for d in due.get(pid, [])}
        fresh = [x for x in applicable if x in own and x not in due_here]
        row = {
            "id": pid, "name": p["name"], "kind": p["kind"], "parent": p.get("parent"),
            "tags": p.get("tags", []), "zone": bool(p.get("zone_scan")), "overlay": bool(p.get("overlay")),
            "region": p.get("region"), "aliases": p.get("aliases", [])[:4], "children": len(p["children"]),
            "active": is_active(p), "smartraveller": p.get("smartraveller"),
            "applicable": len(applicable), "records": len([x for x in applicable if x in own]),
            "fresh": len(fresh), "due": due_here, "vetted": pid in vetted, "sk": p.get("source_kind"),
        }
        rows.append({k: v for k, v in row.items() if v not in (None, [], {}, False) or k in ("records", "fresh")})

    coverage = {}
    for pat in agent:
        targets = [r for r in rows if r.get("active") and applies(pat, places[r["id"]])]
        coverage[pat["id"]] = {"active_places": len(targets),
                               "with_record": sum(1 for r in targets if pat["id"] in vetted.get(r["id"], {})),
                               "fresh": sum(1 for r in targets if pat["id"] in vetted.get(r["id"], {}) and pat["id"] not in r.get("due", {}))}

    runs = sorted((p.name for p in (ROOT / "docs/runs").glob("*.md")), reverse=True)
    out = ROOT / "site/data/index.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "built_on": today().isoformat(),
        "counts": {"places": len(rows), "spine": sum(1 for r in rows if "/" not in r["id"]),
                   "active": sum(1 for r in rows if r.get("active")), "patterns": len(patterns),
                   "with_records": len(vetted)},
        "queue_summary": queue.get("summary", {}),
        "next": [{"place": e["place"], "name": e["name"], "due": len(e["due"]),
                  "reasons": sorted({d["reason"] for d in e["due"]})} for e in queue["queue"][:24]],
        "watch_checks": queue.get("watch_checks", []),
        "patterns": [dict(p, coverage=coverage.get(p["id"])) for p in patterns.values()],
        "places": rows,
        "runs": runs,
        "has_change_log": (ROOT / "data/logs/advisory-changes.jsonl").exists(),
    }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"site index: {len(rows)} places, {len(runs)} run notes")
    write_discovery(rows)


SITE = "https://auraofintelligence.github.io/world-travel-patterns/"
PAGES = [("", "Home", "Search any place and see what each place page covers."),
         ("places.html", "Places", "Every country and territory, and the states, councils, islands, nations and permit zones inside them."),
         ("advisories.html", "Advisories", "Smartraveller advice levels for every destination, checked daily, and each change."),
         ("upcoming.html", "Upcoming", "Dated events and open calls from GAJRA Earth Ahead, by month and place."),
         ("patterns.html", "Patterns", "The sixteen questions every place is checked against."),
         ("how.html", "How it works", "The checks, how rules reach down from country to council, culture and permit zones."),
         ("queue.html", "Queue", "What gets checked next."),
         ("site-map.html", "Site map", "Every page, and every country and territory by region.")]


def write_discovery(rows):
    """sitemap.xml lists the real pages: the site pages plus a page per country, territory or place with records."""
    on = today().isoformat()
    places = sorted((r for r in rows if "/" not in r["id"] or r.get("records")), key=lambda r: r["id"])
    urls = [SITE + path for path, _, _ in PAGES] + [f"{SITE}place.html?id={quote(r['id'], safe='')}" for r in places]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{u.replace('&', '&amp;')}</loc><lastmod>{on}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    lines = ["# World Travel Patterns", "",
             "A Luke × Claude travel research site for Australian passport holders: entry, local law, culture and protocol, permit zones, "
             "seasons and festivals, and consular help for each place, with every rule linked to its source and dated.", "",
             "A planning aid, not legal advice. A level marked \"not yet checked\" has unknown rules, not no rules. Rules come from the government, "
             "authority or community that owns them; anything else is labelled a signal. Original material uses the Strange But True Public Source "
             "Licence; third-party rights remain separate. This voluntary guide grants no additional reuse or AI-training rights.", "",
             "## Pages", ""]
    lines += [f"- [{title}]({SITE + path}): {about}" for path, title, about in PAGES]
    lines += ["", "## Place pages", "",
              f"- One page per place at {SITE}place.html?id=<place id>, for example [Fiji]({SITE}place.html?id=fj) "
              f"and [Minjerribah]({SITE}place.html?id=au%2Fminjerribah). The sitemap lists {len(places)} of them.", "",
              "## Data", "",
              "- [Place records](https://github.com/auraofintelligence/world-travel-patterns/tree/main/data/vetting): one JSON file per place",
              "- [Patterns](https://github.com/auraofintelligence/world-travel-patterns/tree/main/patterns): the sixteen questions",
              f"- [Licence]({SITE}LICENCE.md)", ""]
    (ROOT / "llms.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"discovery: sitemap.xml with {len(urls)} pages, llms.txt")


if __name__ == "__main__":
    main()
