"""Unit tests and live-tree fixture for offline legal metadata audit."""
import csv
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("source_audit", ROOT / "scripts/audit_source_register.py")
assert spec and spec.loader
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class SourceRegisterAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = dict(
            id="CA-BREACH", jurisdiction="California", source_type="state_statute",
            status="ENACTED_AND_APPLICABLE", date="2026-01-01",
            official_url="https://dre.ca.gov/files/pdf/relaw/excerpts.pdf",
            critical_caveat="State published excerpts; original legislature viewer unavailable",
        )
        self.row = dict(
            id="CA-RESIDENT", jurisdiction="California", recipient="resident",
            legal_section="Civ_Code_1798.82(a)", condition="covered",
            clock_anchor="discovery", clock_statement="qualified_30_days",
            threshold="covered_resident", source_id="CA-BREACH",
            source_url=self.source["official_url"], verified_as_of="2026-11-13",
            limitation="statutory_exceptions_apply",
        )
        self.write()

    def write_table(self, relpath, fields, rows):
        file = self.root / relpath
        file.parent.mkdir(parents=True, exist_ok=True)
        with file.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def write(self, sources=None, rows=None):
        self.write_table(audit.SOURCES, audit.SOURCE_COLUMNS,
                         [self.source] if sources is None else sources)
        self.write_table(audit.MATRIX, audit.MATRIX_COLUMNS,
                         [self.row] if rows is None else rows)

    def test_valid_fixture(self):
        self.assertEqual(audit.audit(self.root), [])

    def test_repository_registers_are_structurally_consistent(self):
        self.assertEqual(audit.audit(ROOT), [])

    def test_duplicate_source_id(self):
        self.write(sources=[self.source, self.source])
        self.assertTrue(any("duplicate ID" in x for x in audit.audit(self.root)))

    def test_invalid_source_status(self):
        self.write(sources=[dict(self.source, status="GUESS")])
        self.assertTrue(any("invalid source status" in x for x in audit.audit(self.root)))

    def test_invalid_date(self):
        self.write(rows=[dict(self.row, verified_as_of="2026-02-30")])
        self.assertTrue(any("invalid ISO" in x for x in audit.audit(self.root)))

    def test_unofficial_http_url(self):
        self.write(sources=[dict(self.source, official_url="http://not-official.example")])
        self.assertTrue(any("nonofficial/non-HTTPS" in x for x in audit.audit(self.root)))

    def test_vetted_oregon_doj_legacy_host(self):
        self.assertTrue(audit.official_source_url(
            "https://www.doj.state.or.us/consumer-protection/id-theft-data-breaches/privacy/"))

    def test_spoofed_oregon_domain_rejected(self):
        self.assertFalse(audit.official_source_url(
            "https://www.doj.state.or.us.evil.example/mirror"))
        self.assertFalse(audit.official_source_url(
            "https://www.random.state.or.us/"))

    def test_official_judicial_order_status(self):
        court = dict(
            self.source, id="COURT-ORDER", source_type="judicial_order",
            status="OFFICIAL_JUDICIAL_ORDER",
            official_url="https://www.ca5.uscourts.gov/opinions/pub/25/25-50096-CV1.pdf"
        )
        self.write(sources=[self.source, court])
        self.assertEqual(audit.audit(self.root), [])

    def test_missing_source_reference(self):
        self.write(rows=[dict(self.row, source_id="MISSING")])
        self.assertTrue(any("unknown source_id" in x for x in audit.audit(self.root)))

    def test_url_mismatch(self):
        self.write(rows=[dict(self.row, source_url="https://oag.ca.gov/privacy/databreach/reporting")])
        self.assertTrue(any("URL differs" in x for x in audit.audit(self.root)))

    def test_research_pending_status_cannot_feed_deadline_matrix(self):
        self.write(sources=[dict(self.source, status="REQUIRES_FURTHER_REVIEW")])
        self.assertTrue(any("non-operative or unverified status" in x for x in audit.audit(self.root)))


if __name__ == "__main__":
    unittest.main()
