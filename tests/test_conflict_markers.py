"""Conflict-marker check in validate.py. Run with: python -m unittest discover tests"""
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import validate  # noqa: E402


class ConflictMarkers(unittest.TestCase):
    def test_detects_start_and_end_markers(self):
        start = "<" * 7 + " Updated upstream"
        end = ">" * 7 + " Stashed changes"
        text = "ok line\n{0}\nkept\n{1}\n".format(start, end)
        self.assertEqual(validate.conflict_marker_lines(text), [2, 4])

    def test_ignores_markdown_heading_rule_and_mid_line_mention(self):
        start = "<" * 7
        text = "Title\n=======\nA sentence about " + start + " is fine if it is not a marker line.\n"
        self.assertEqual(validate.conflict_marker_lines(text), [])

    def test_detects_indented_markers(self):
        start = "    " + "<" * 7 + " HEAD"
        self.assertEqual(validate.conflict_marker_lines(start + "\n"), [1])

    def test_repo_has_no_conflict_markers(self):
        before = list(validate.problems)
        validate.problems.clear()
        try:
            validate.check_tracked_conflict_markers()
            leftover = [p for p in validate.problems if "conflict marker" in p]
        finally:
            validate.problems[:] = before
        self.assertEqual(leftover, [])

    def test_json_and_markdown_temp_text_is_caught(self):
        start = "<" * 7 + " HEAD"
        with tempfile.TemporaryDirectory() as tmp:
            md = pathlib.Path(tmp) / "note.md"
            js = pathlib.Path(tmp) / "data.json"
            md.write_text("hello\n" + start + "\n", encoding="utf-8")
            js.write_text(start + "\n", encoding="utf-8")
            self.assertEqual(validate.conflict_marker_lines(md.read_text(encoding="utf-8")), [2])
            self.assertEqual(validate.conflict_marker_lines(js.read_text(encoding="utf-8")), [1])


if __name__ == "__main__":
    unittest.main()
