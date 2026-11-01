"""Write the "changing" area of affection-and-relationships: dated law changes and official marriage figures.

Two inputs:
- UN DESA World Marriage Data 2019 (official): singulate mean age at marriage (SMAM), the average age at first
  marriage, for women and men, earliest and latest figures. Pass the downloaded workbook with --wmd.
  https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2019_wmd_marital_status.xlsx
- data/sources/marriage-equality.json (signal): the year same-sex marriage became legal, from Pew Research Center.

    python scripts/affection_trends.py --wmd PATH/undesa_pd_2019_wmd_marital_status.xlsx

Replaces earlier items written by this script (marked "by": "affection_trends"); leaves every other item alone.
Needs openpyxl to read the workbook.
"""
import argparse
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, load_places, read, today, vetting_path, write  # noqa: E402

WMD_URL = "https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2019_wmd_marital_status.xlsx"
WMD_SRC = {"title": "World Marriage Data 2019", "authority": "United Nations, Department of Economic and Social Affairs, Population Division",
           "url": WMD_URL, "supports": "average age at first marriage (SMAM) over time, from national censuses and surveys"}
# UN names that don't match a place name or alias.
UN_NAMES = {"Bolivia (Plurinational State of)": "bo", "China, Hong Kong SAR": "hk", "China, Macao SAR": "mo", "China, Taiwan Province of China": "tw",
            "Côte d'Ivoire": "ci", "Czechia": "cz", "Dem. People's Republic of Korea": "kp", "Democratic Republic of the Congo": "cd",
            "Iran (Islamic Republic of)": "ir", "Lao People's Democratic Republic": "la", "Micronesia (Fed. States of)": "fm",
            "Republic of Korea": "kr", "Republic of Moldova": "md", "Russian Federation": "ru", "Syrian Arab Republic": "sy",
            "United Republic of Tanzania": "tz", "Venezuela (Bolivarian Republic of)": "ve", "Viet Nam": "vn", "Congo": "cg",
            "United States of America": "us", "United States Virgin Islands": "vi", "State of Palestine": "ps", "Cabo Verde": "cv",
            "Eswatini": "sz", "Swaziland": "sz", "North Macedonia": "mk", "TFYR Macedonia": "mk", "Brunei Darussalam": "bn",
            "Holy See": "va", "Falkland Islands (Malvinas)": "fk", "Saint Helena": "sh", "Curaçao": "cw", "Réunion": "re",
            "Wallis and Futuna Islands": "wf", "Sint Maarten (Dutch part)": "sx", "Saint Martin (French part)": "mf",
            "Bonaire, Sint Eustatius and Saba": "bq", "Kosovo": "xk", "Kosovo (autonomous province)": "xk", "Turkey": "tr", "Türkiye": "tr",
            "Dem. People's Rep. of Korea": "kp", "Faeroe Islands": "fo", "Lao People's Dem. Republic": "la",
            "Lao People’s Democratic Republic": "la", "The former Yugoslav Republic of Macedonia": "mk"}


def norm(s):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower())


def matcher(places):
    by = {}
    for pid, p in places.items():
        if "/" not in pid:
            for name in [p["name"]] + p.get("aliases", []):
                by[norm(name)] = pid
    return lambda name: UN_NAMES.get(name) or by.get(norm(name))


def years(a, b):
    return str(a) if a == b else f"{a} to {b}"


def smam(path, find):
    import openpyxl
    ws = openpyxl.load_workbook(path, read_only=True)["SMAM"]
    rows = list(ws.iter_rows(values_only=True))
    head = next(i for i, r in enumerate(rows) if r and r[0] == "Country or area")
    series = {}
    for r in rows[head + 1:]:
        if not r or not r[0] or r[5] is None:
            continue
        pid = find(r[0])
        if pid:
            series.setdefault(pid, {}).setdefault(r[4], []).append((r[3], r[2], float(r[5])))
    out = {}
    for pid, by_sex in series.items():
        parts = []
        for sex, label in (("Women", "women"), ("Men", "men")):
            pts = sorted(by_sex.get(sex, []))
            if not pts:
                continue
            first, last = pts[0], pts[-1]
            if last[0] - first[0] >= 10:
                parts.append(f"{label} {first[2]:.1f} in {years(first[1], first[0])}, {last[2]:.1f} in {years(last[1], last[0])}")
            else:
                parts.append(f"{label} {last[2]:.1f} in {years(last[1], last[0])}")
        if parts:
            out[pid] = "Average age at first marriage: " + "; ".join(parts) + "."
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wmd", required=True)
    ap.add_argument("--skip-region", action="append", default=[])
    args = ap.parse_args()
    D = today().isoformat()
    places = load_places()
    find = matcher(places)
    figures = smam(args.wmd, find)
    equality = read(ROOT / "data/sources/marriage-equality.json")
    legal = {}
    for c in equality["countries"]:
        pid = find(c["name"])
        if pid:
            legal[pid] = f"Same-sex marriage became legal in {c['year']}." + (f" {c['note']}" if c.get("note") else "")
    src_eq = dict(equality["source"], checked=D, supports="year same-sex marriage became legal")
    wmd = dict(WMD_SRC, checked=D)
    written = 0
    for pid in sorted(set(figures) | set(legal)):
        p = places.get(pid)
        if not p or p.get("region") in args.skip_region or pid == "au":
            continue
        path = vetting_path(pid)
        rec = read(path, {"place": pid, "patterns": {}})
        body = rec["patterns"].setdefault("affection-and-relationships", {
            "status": "partly-mapped", "checked": D, "evidence": "official", "items": [], "sources": [],
            "notes": "Custom differs between communities and places; ask locally."})
        body["items"] = [i for i in body.get("items", []) if i.get("by") != "affection_trends"]
        if pid in legal:
            body["items"].append({"area": "changing", "kind": "law", "evidence": "signal", "text": legal[pid], "source": src_eq["url"], "checked": D, "by": "affection_trends"})
        if pid in figures:
            body["items"].append({"area": "changing", "kind": "figure", "evidence": "official", "text": figures[pid], "source": WMD_URL, "checked": D, "by": "affection_trends"})
        urls = {s["url"] for s in body.get("sources", [])}
        for s, used in ((src_eq, pid in legal), (wmd, pid in figures)):
            if used and s["url"] not in urls:
                body["sources"].append(s)
        body["checked"] = D
        write(path, rec)
        written += 1
    print(f"changing: {written} places ({len(figures)} with UN marriage figures, {len(legal)} with a same-sex marriage year)")


if __name__ == "__main__":
    main()
