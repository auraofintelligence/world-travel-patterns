"""Run with: python -m unittest discover tests"""
import datetime
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
from recheck_plan import build, text_dates, tier  # noqa: E402


class RecheckPlan(unittest.TestCase):
    def test_tier(self):
        self.assertEqual(tier(1), "daily")
        self.assertEqual(tier(90), "quarterly")
        self.assertEqual(tier(365), "yearly")

    def test_text_dates(self):
        got = list(text_dates({"rule": "Waiver runs until 31 December 2026.", "url": "until 1 May 2030"}))
        self.assertEqual([g[0] for g in got], [datetime.date(2026, 12, 31)])

    def test_plan_from_repo(self):
        plan = build(datetime.date(2026, 11, 4))
        dated = [t["date"] for t in plan["triggers"] if t["date"]]
        self.assertEqual(dated, sorted(dated))
        self.assertTrue(any(t.get("id") == "cn-visa-waiver-2026" for t in plan["triggers"]))
        self.assertTrue(plan["locations"])
        self.assertNotIn("home", plan)


if __name__ == "__main__":
    unittest.main()
