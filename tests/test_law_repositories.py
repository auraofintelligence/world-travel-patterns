"""Law-source map schema and coverage. Run with: python -m unittest discover tests"""
import datetime
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lib import load_places, read  # noqa: E402
from law_repositories import coverage, is_verified, problems_in  # noqa: E402


class Verification(unittest.TestCase):
    def test_read_directly_is_verified(self):
        self.assertTrue(is_verified({"url": "https://example.gov/laws", "source": "read directly", "check": "needs a browser"}))

    def test_legacy_loaded_is_verified(self):
        self.assertTrue(is_verified({"url": "https://example.gov/laws", "check": "loaded"}))

    def test_search_snapshot_is_not_verified(self):
        self.assertFalse(is_verified({"url": "https://example.gov/laws", "source": "search snapshot", "check": "loaded"}))

    def test_unverified_and_missing_url(self):
        self.assertFalse(is_verified({"url": "https://example.gov/laws", "source": "unverified", "check": "loaded"}))
        self.assertFalse(is_verified({"source": "read directly"}))
        self.assertFalse(is_verified({"url": "https://example.gov/laws", "check": "timed out during automated check"}))


class Schema(unittest.TestCase):
    def setUp(self):
        self.places = {"ch": {"id": "ch", "kind": "country", "name": "Switzerland"},
                       "ch/zurich": {"id": "ch/zurich", "kind": "region", "source_kind": "first-level", "name": "Zurich", "parent": "ch"}}
        self.ok = {
            "name": "Zurich systematic collection",
            "publisher": "Canton of Zurich",
            "url": "https://www.zh.ch/gesetze",
            "kind": "statutes",
            "language": "German",
            "searchable": True,
            "check": "loaded",
            "checked": "2026-11-11",
            "source": "read directly",
        }

    def test_valid_record_has_no_problems(self):
        repos = {"places": {"ch/zurich": [self.ok]}, "groups": [], "not_yet_found": [], "no_online_source": {}}
        self.assertEqual(problems_in(repos, self.places, today=datetime.date(2026, 11, 11)), [])

    def test_unknown_kind_and_origin_are_rejected(self):
        bad = dict(self.ok, kind="portal")
        repos = {"places": {"ch/zurich": [bad]}}
        self.assertTrue(any("unknown kind" in m for m in problems_in(repos, self.places)))
        bad = dict(self.ok, source="official snapshot")
        repos = {"places": {"ch/zurich": [bad]}}
        self.assertTrue(any("source must be one of" in m for m in problems_in(repos, self.places)))

    def test_legacy_records_need_no_new_fields(self):
        legacy = {"name": "Fedlex", "publisher": "Federal Chancellery", "url": "https://www.fedlex.admin.ch/", "check": "loaded", "checked": "2026-11-01"}
        repos = {"places": {"ch": [legacy]}}
        self.assertEqual(problems_in(repos, self.places, today=datetime.date(2026, 11, 11)), [])

    def test_unknown_place_is_rejected(self):
        repos = {"places": {"xx/nowhere": [self.ok]}}
        self.assertTrue(any("unknown place" in m for m in problems_in(repos, self.places)))


class LiveFile(unittest.TestCase):
    def test_checked_in_file_validates(self):
        places = load_places()
        repos = read(ROOT / "data/law-repositories.json")
        self.assertEqual(problems_in(repos, places), [])

    def test_coverage_counts_only_first_level_places(self):
        places = load_places()
        repos = read(ROOT / "data/law-repositories.json")
        law = coverage(repos, places)
        self.assertEqual(law["first_level"], 3597)
        self.assertLessEqual(law["verified"], law["with_any_source"])
        self.assertEqual(law["verified"] + law["listed_unverified"], law["with_any_source"])
        self.assertGreater(law["spine_with_record"], 200)


if __name__ == "__main__":
    unittest.main()
