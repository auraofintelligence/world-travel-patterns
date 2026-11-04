import pathlib, sys, unittest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "scripts"))
from money_rates import fallback_rate


class FallbackRate(unittest.TestCase):
    rba = {"aud_to": {"USD": 0.704, "EUR": 0.6293}}
    cb = {"rates": {"PLN": {"base": "AUD", "rate": 2.7598}, "PEN": {"base": "USD", "rate": 3.467},
                    "XPF": {"base": "EUR", "rate": 119.3317}, "ZZZ": {"base": "GBP", "rate": 2}}}

    def test_direct(self):
        self.assertEqual(fallback_rate("PLN", self.cb, self.rba), 2.7598)

    def test_cross(self):
        self.assertAlmostEqual(fallback_rate("PEN", self.cb, self.rba), 2.4408, places=4)
        self.assertAlmostEqual(fallback_rate("XPF", self.cb, self.rba), 75.0954, places=3)

    def test_missing(self):
        self.assertIsNone(fallback_rate("IRR", self.cb, self.rba))
        self.assertIsNone(fallback_rate("ZZZ", self.cb, self.rba))


if __name__ == "__main__":
    unittest.main()
