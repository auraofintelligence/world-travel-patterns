"""Destination law stacks and the Australian-law-abroad record. Run with: python -m unittest discover tests"""
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lib import applies, load_patterns, load_places, read, vetting_path  # noqa: E402


class AustralianLawAbroad(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.places, cls.patterns = load_places(), load_patterns()

    def test_pattern_applies_only_to_australia(self):
        pat = self.patterns["australian-law-abroad"]
        for pid in ("fj", "us", "au/nsw", "au/qld"):
            if pid in self.places:
                self.assertFalse(applies(pat, self.places[pid]), pid)
        self.assertTrue(applies(pat, self.places["au"]))

    def test_records_are_sourced(self):
        pat = self.patterns["australian-law-abroad"]
        body = read(vetting_path("au"), {"patterns": {}})["patterns"].get("australian-law-abroad")
        self.assertTrue(body["sources"])
        for law in body["laws"]:
            self.assertIn(law["topic"], pat["topics"])
            self.assertTrue(law["source"].startswith("https://"))
            self.assertNotIn("\u2014", law["rule"])


class DestinationStacks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(ROOT / "scripts/build_site.py")], check=True, capture_output=True)
        cls.data = json.loads((ROOT / "site/data/law-stacks.json").read_text())
        cls.places = load_places()

    def test_every_stack_runs_country_to_place(self):
        for pid, stack in self.data["destinations"].items():
            self.assertFalse(pid.split("/")[0] == "au", pid)
            self.assertEqual(stack[-1][0], pid)
            self.assertEqual(stack[0][0], pid.split("/")[0] if "/" in pid else pid)

    def test_unchecked_levels_are_null_not_dropped(self):
        levels = {lp: st for stack in self.data["destinations"].values() for lp, st in stack}
        s = self.data["summary"]
        self.assertEqual(len(levels), s["levels"])
        self.assertEqual(sum(1 for v in levels.values() if v is None), s["levels_not_yet_checked"])

    def test_repositories_sit_beside_the_stack(self):
        repos = self.data.get("repositories") or {}
        levels = {lp for stack in self.data["destinations"].values() for lp, st in stack}
        self.assertEqual(self.data["summary"].get("levels_with_sources"), len(repos))
        for pid, srcs in repos.items():
            self.assertIn(pid, levels)
            self.assertTrue(srcs)
            for src in srcs:
                self.assertTrue(src["url"].startswith("http"))
                self.assertTrue(src["name"])


if __name__ == "__main__":
    unittest.main()
