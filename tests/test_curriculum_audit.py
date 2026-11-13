"""Offline tests for the Tech-Law Markdown structure auditor."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("audit_curriculum", ROOT / "scripts/audit_curriculum.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class AuditCurriculumTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.old_root = audit.ROOT
        audit.ROOT = Path(self.tmp.name)
        audit.ISSUES.clear()
        audit.WARNINGS.clear()
        self.addCleanup(self.restore)

    def restore(self):
        audit.ROOT = self.old_root
        audit.ISSUES.clear()
        audit.WARNINGS.clear()

    def write(self, rel, content):
        p = audit.ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return p

    def test_valid_local_file_and_heading(self):
        self.write("chapters/one.md", "# First topic\n")
        doc = self.write("README.md", "[Read](chapters/one.md#first-topic)\n")
        audit.audit_md(doc)
        self.assertEqual(audit.ISSUES, [])
        self.assertEqual(audit.WARNINGS, [])

    def test_missing_target_is_error(self):
        doc = self.write("README.md", "[Missing](none.md)\n")
        audit.audit_md(doc)
        self.assertTrue(any("missing local target" in x for x in audit.ISSUES))

    def test_escape_root_is_error(self):
        doc = self.write("README.md", "[Outside](../../outside.md)\n")
        audit.audit_md(doc)
        self.assertTrue(any("out-of-repository" in x for x in audit.ISSUES))

    def test_unknown_anchor_is_warning(self):
        self.write("chapter.md", "# Known heading\n")
        doc = self.write("README.md", "[Anchor](chapter.md#wrong)\n")
        audit.audit_md(doc)
        self.assertEqual(audit.ISSUES, [])
        self.assertTrue(any("unchecked heading anchor" in x for x in audit.WARNINGS))


if __name__ == "__main__":
    unittest.main()