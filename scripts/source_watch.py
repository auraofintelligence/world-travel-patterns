"""Machine check of every cited source: is it still there, and has its text changed?

For each URL in data/vetting, fetch it, normalise the visible text and hash it. A changed hash
marks every claim citing that page as "source-changed" in the queue, so the routine rechecks
only what moved. Pages that change on every load can be marked noisy in
data/source-status.json; those are rechecked on age instead. Stdlib only.
"""
import concurrent.futures
import hashlib
import html
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import ROOT, VETTING, read, today, write  # noqa: E402

OUT = ROOT / "data/source-status.json"
UA = {"User-Agent": "Mozilla/5.0 (compatible; world-travel-patterns/1.0; +https://github.com/auraofintelligence)"}


def collect():
    used = {}

    def walk(node, where):
        if isinstance(node, dict):
            url = node.get("url")
            if isinstance(url, str) and url.startswith("http"):
                used.setdefault(url, set()).add(where)
            for value in node.values():
                walk(value, where)
        elif isinstance(node, list):
            for value in node:
                walk(value, where)

    for path in VETTING.glob("*.json"):
        record = read(path)
        for pattern_id, body in record["patterns"].items():
            walk(body, f"{record['place']}#{pattern_id}")
    return used


SOFT_404_URL = re.compile(r"(?i)(/404(\b|[/?._-])|not[-_]?found|/error(\b|[/?._-])|pagenotfound)")
SOFT_404_TITLE = re.compile(r"(?is)<title[^>]*>[^<]*(404|page not found|not found|page cannot be found)[^<]*</title>")


def soft_404(url, final_url, raw_html=""):
    """True when a 200 response is really a not-found page: a redirect to a 404-style URL, or a not-found title."""
    if final_url and final_url != url and SOFT_404_URL.search("/" + final_url.split("://", 1)[-1].partition("/")[2]):
        return True
    return bool(raw_html and SOFT_404_TITLE.search(raw_html[:20000]))


def fingerprint(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as response:
            raw = response.read(3_000_000)
            status, final = response.status, response.url
    except urllib.error.HTTPError as error:
        return {"status": error.code}
    except Exception as error:  # network failures are recorded, never treated as a rule change
        return {"status": "error", "error": type(error).__name__}
    text = raw.decode("utf-8", errors="replace")
    if "pdf" not in url.lower() and soft_404(url, final, text):
        return {"status": "soft-404", "final_url": final}
    if "pdf" not in url.lower():
        text = re.sub(r"(?is)<(script|style|nav|header|footer|noscript)[^>]*>.*?</\1>", " ", text)
        text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", text))
    text = re.sub(r"\s+", " ", text).strip()
    return {"status": status, "final_url": final, "sha256": hashlib.sha256(text.encode()).hexdigest()}


def main():
    on = today().isoformat()
    used = collect()
    previous = read(OUT, {"sources": {}})["sources"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = dict(zip(used, pool.map(fingerprint, used)))
    sources, changed, dead = {}, [], []
    for url, result in results.items():
        before = previous.get(url, {})
        entry = {**before, "status": result["status"], "checked": on, "used_by": sorted(used[url])}
        if result.get("final_url") and result["final_url"] != url:
            entry["final_url"] = result["final_url"]
        if result.get("sha256"):
            if before.get("sha256") and before["sha256"] != result["sha256"] and not before.get("noisy"):
                entry["changed_on"] = on
                changed.append(url)
            entry["sha256"] = result["sha256"]
        if result["status"] in (404, 410, "soft-404"):
            entry["dead_since"] = before.get("dead_since", on)
            dead.append(url)
        else:
            entry.pop("dead_since", None)
        sources[url] = entry
    write(OUT, {"checked_on": on, "rule": "A blocked or failed fetch is not evidence of a rule change.", "sources": sources})
    print(f"## Source watch, {on}\n\n{len(sources)} sources: {len(changed)} changed, {len(dead)} not found.\n")
    for url in dead:
        print(f"- not found: {url} (used by {', '.join(sources[url]['used_by'][:3])})")
    for url in changed:
        print(f"- changed: {url}")


if __name__ == "__main__":
    main()
