"""Write one pattern record into a place's vetting file, safely when several agents work at once.

    python scripts/put_record.py <place-id> <pattern-id> <record.json>   # replace that pattern's record
    python scripts/put_record.py <place-id> <pattern-id> --show          # print the current record, if any

The place must exist in the tree. A lock file stops two writers changing the same place file at the same moment.
Only the named pattern is touched; every other pattern in the file stays as it was.
"""
import json
import os
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import VETTING, load_patterns, load_places  # noqa: E402


def lock(path):
    lockfile = path.with_suffix(".lock")
    for _ in range(200):
        try:
            return os.open(lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY), lockfile
        except FileExistsError:
            time.sleep(0.05)
    sys.exit(f"could not lock {path.name}: remove {lockfile.name} if no writer is running")


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    place, pattern, arg = sys.argv[1:]
    if place not in load_places():
        sys.exit(f"unknown place {place}")
    if pattern not in load_patterns():
        sys.exit(f"unknown pattern {pattern}")
    path = VETTING / f"{place.replace('/', '__')}.json"
    if arg == "--show":
        rec = json.loads(path.read_text(encoding="utf-8"))["patterns"].get(pattern) if path.exists() else None
        print(json.dumps(rec, ensure_ascii=False, indent=1) if rec else "none")
        return
    body = json.loads(pathlib.Path(arg).read_text(encoding="utf-8"))
    if "—" in json.dumps(body, ensure_ascii=False):
        sys.exit("no em dashes: rewrite with a colon, semicolon, comma or full stop")
    fd, lockfile = lock(path)
    try:
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"place": place, "patterns": {}}
        data["patterns"][pattern] = body
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        os.replace(tmp, path)
    finally:
        os.close(fd)
        os.remove(lockfile)
    print(f"wrote {place} {pattern}")


if __name__ == "__main__":
    main()
