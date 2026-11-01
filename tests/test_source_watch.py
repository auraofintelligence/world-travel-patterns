"""Run with: python -m unittest discover tests"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
from source_watch import soft_404  # noqa: E402


class SoftNotFound(unittest.TestCase):
    def test_redirect_to_404_page(self):
        url = "https://www.mofa.gov.ae/en/Missions/Canberra/Contact-Us/FAQS"
        final = "https://www.mofa.gov.ae/404?item=%2fmissions%2fcanberra&site=LDSC"
        self.assertTrue(soft_404(url, final))

    def test_redirect_to_not_found_path(self):
        self.assertTrue(soft_404("https://a.gov/x", "https://a.gov/page-not-found"))

    def test_not_found_title(self):
        self.assertTrue(soft_404("https://a.gov/x", "https://a.gov/x", "<html><title>Page Not Found | Ministry</title>"))

    def test_ordinary_redirect_is_fine(self):
        self.assertFalse(soft_404("https://icp.gov.ae/en/uae-green-residency/", "https://icp.gov.ae/en/services/uae-green-residency/", "<title>Green residency</title>"))

    def test_404_in_host_or_number_is_fine(self):
        self.assertFalse(soft_404("https://a.gov/x", "https://a.gov/news/2404-visas", "<title>News</title>"))


if __name__ == "__main__":
    unittest.main()
