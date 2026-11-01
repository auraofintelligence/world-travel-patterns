"""Invariants for carried-over visa preparation data. Run with: python -m unittest discover tests"""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATE = re.compile(r"\d{4}-\d{2}-\d{2}$")


def records():
    for path in sorted((ROOT / "data/vetting").glob("*.json")):
        record = json.loads(path.read_text())
        body = record["patterns"].get("visa-preparation")
        if body:
            yield record["place"], body


class VisaPreparation(unittest.TestCase):
    def test_no_australian_records(self):
        for place, _ in records():
            self.assertFalse(place == "au" or place.startswith("au/"), place)

    def test_baselines_flagged_with_provenance(self):
        for place, body in records():
            if body["status"] in ("imported", "baseline-only"):
                self.assertTrue(body["needs_recheck"], place)
                self.assertEqual(body["evidence"], "legacy-baseline", place)
                self.assertTrue(body["provenance"]["repo"].startswith("https://github.com/auraofintelligence/"), place)
                self.assertTrue(DATE.match(body["last_reviewed"]), place)

    def test_rechecked_records_have_sources(self):
        for place, body in records():
            if body.get("needs_recheck") is False:
                self.assertTrue(body.get("sources"), place)

    def test_checklist_items_flagged(self):
        data = json.loads((ROOT / "data/preparation/checklist.json").read_text())
        ids = set()
        for section in data["sections"]:
            self.assertIn("repo", section["provenance"])
            for item in section["items"]:
                self.assertNotIn(item["id"], ids)
                ids.add(item["id"])
                self.assertTrue(DATE.match(item["checked"]), item["id"])
                self.assertIn("needs_recheck", item)


if __name__ == "__main__":
    unittest.main()
