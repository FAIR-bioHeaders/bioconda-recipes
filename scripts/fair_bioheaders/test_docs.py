from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/fair_bioheaders"))
from check_docs import check_file


class Documentation(unittest.TestCase):
    def test_local_links_and_external_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "present.md").write_text("# Present\n")
            page = root / "page.md"
            page.write_text("[local](present.md) [web](https://example.org) [section](#here)\n")
            self.assertEqual(check_file(page, root), [])
            page.write_text("[broken](missing.md)\n")
            self.assertIn("missing local target", check_file(page, root)[0])

    def test_reference_image_and_repository_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "page.md"
            page.write_text("![image](missing.png)\n[target]: ../escape.md\n")
            errors = check_file(page, root)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("escapes repository" in e for e in errors))

    def test_whitespace_and_conflict_markers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "page.md"
            page.write_text("trailing \n<<<<<<< branch\n")
            errors = check_file(page, root)
            self.assertEqual(len(errors), 2)
