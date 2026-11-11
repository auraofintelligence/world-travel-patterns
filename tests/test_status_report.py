import pathlib, sys, unittest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "scripts"))
from status_report import evidence_kind


class EvidenceKind(unittest.TestCase):
    def test_short_tokens(self):
        self.assertEqual(evidence_kind("official"), "official")
        self.assertEqual(evidence_kind("signal"), "signal")
        self.assertEqual(evidence_kind("operational"), "operational")
        self.assertEqual(evidence_kind("legacy-baseline"), "legacy-baseline")
        self.assertEqual(evidence_kind("community"), "community")

    def test_ancient_site_notes(self):
        self.assertEqual(evidence_kind("Official pages; read directly unless marked search snapshot."), "official")
        self.assertEqual(evidence_kind("UNESCO facts read from UNESCO open data on 6 Nov 2026; heritage laws are not yet read (see national.read)."), "official")
        self.assertEqual(evidence_kind("UNESCO pages and Smartraveller read directly; other official pages are search snapshots unless marked."), "official")
        self.assertEqual(evidence_kind("Official pages from search snapshots unless marked read directly."), "official")

    def test_missing(self):
        self.assertEqual(evidence_kind(""), "other")
        self.assertEqual(evidence_kind(None), "other")


if __name__ == "__main__":
    unittest.main()
