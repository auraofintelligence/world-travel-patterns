"""New residency, citizenship and enterprise patterns: schema, inheritance and status wording."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "scripts"))
from lib import load_patterns  # noqa: E402
from status_report import entries  # noqa: E402
from validate import PATTERN_KEYS  # noqa: E402

NEW_IDS = (
    "digital-residency",
    "physical-residency",
    "citizenship",
    "enterprise-establishment",
    "collective-ownership",
    "financial-infrastructure",
    "intellectual-property",
    "research-and-enterprise",
)


class StayAndEnterprisePatterns(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patterns = load_patterns()

    def test_eight_patterns_defined(self):
        for pid in NEW_IDS:
            self.assertIn(pid, self.patterns)
            pat = self.patterns[pid]
            self.assertTrue(PATTERN_KEYS <= set(pat), f"{pid} missing {sorted(PATTERN_KEYS - set(pat))}")
            self.assertEqual(pat["inherit"], "nearest")
            self.assertEqual(pat["method"], "agent")
            self.assertEqual(pat["layer"], "stay-and-enterprise")
            self.assertIn("unknown", pat["statuses"])
            self.assertIn("country", pat["applies_to"])
            self.assertIn("territory", pat["applies_to"])
            self.assertIn("state", pat["applies_to"])

    def test_separate_from_works_and_purpose(self):
        works = self.patterns["works-and-purpose"]
        self.assertTrue(works.get("only_tagged"))
        self.assertEqual(works["inherit"], "none")
        for pid in NEW_IDS:
            self.assertFalse(self.patterns[pid].get("only_tagged"))
            self.assertNotEqual(self.patterns[pid]["id"], "works-and-purpose")

    def test_facts_and_costs_count_as_entries(self):
        rec = {
            "facts": [{"label": "Dual citizenship", "text": "Allowed"}],
            "costs": [{"item": "Naturalisation", "amount": 100, "currency": "EUR"}],
        }
        self.assertGreaterEqual(entries(rec), 2)


if __name__ == "__main__":
    unittest.main()
