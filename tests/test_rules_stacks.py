"""Destination law stacks and the home-base (outbound) stack. Run with: python -m unittest discover tests"""
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lib import ancestors, applies, home_chain, load_patterns, load_places, read, vetting_path  # noqa: E402


class HomeBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.places, cls.patterns = load_places(), load_patterns()
        cls.home = read(ROOT / "config/home-base.json")["place"]

    def test_chain_runs_country_to_home(self):
        chain = home_chain()
        self.assertEqual(chain[-1], self.home)
        self.assertEqual(chain, list(reversed([self.home] + ancestors(self.places, self.home))))

    def test_pattern_applies_only_on_home_chain(self):
        pat = self.patterns["home-obligations"]
        self.assertTrue(pat["home_only"])
        for pid in ("fj", "us", "au/nsw"):
            if pid in self.places:
                self.assertFalse(applies(pat, self.places[pid]), pid)
        for pid in home_chain():
            self.assertTrue(applies(pat, self.places[pid]), pid)

    def test_home_records_are_sourced(self):
        pat = self.patterns["home-obligations"]
        for pid in home_chain():
            body = read(vetting_path(pid), {"patterns": {}})["patterns"].get("home-obligations")
            if not body:
                continue
            self.assertTrue(body["sources"], pid)
            for law in body["laws"]:
                self.assertIn(law["topic"], pat["topics"], pid)
                self.assertTrue(law["source"].startswith("https://"), pid)
                self.assertNotIn("\u2014", law["rule"], pid)


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

    def test_home_stack_paired(self):
        self.assertEqual([lp for lp, _ in self.data["home"]["stack"]], home_chain())


if __name__ == "__main__":
    unittest.main()
