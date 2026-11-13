"""Offline metadata checks for the legal change watchlist."""
import csv
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "change_watchlist", REPO / "scripts/audit_legal_change_watchlist.py"
)
assert spec and spec.loader
watch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(watch)


class ChangeWatchlistTests(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = dict(
            id="OR-AR-2026", jurisdiction="Oregon",
            source_type="official_legislative_index", status="OFFICIAL_GUIDANCE",
            official_url="https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2026OrLawAR.pdf",
        )
        self.claim = dict(
            claim_id="OR-INDEX", topic="amendment_index", jurisdiction="Oregon",
            source_id="OR-AR-2026", review_status="INDEX_SCOPE_CHECKED",
            scope_checked="ORS_646A570_to_589",
            evidence_url=self.source["official_url"],
            last_checked="2026-11-13", next_review_target="2027-02-01",
            open_question="New_uncodified_laws_not_verified",
        )
        self.write()

    def write(self, source_rows=None, claims=None):
        p = self.root / watch.SOURCES
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(self.source))
            writer.writeheader()
            writer.writerows([self.source] if source_rows is None else source_rows)
        p = self.root / watch.WATCHLIST
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=watch.WATCHLIST_COLUMNS)
            writer.writeheader()
            writer.writerows([self.claim] if claims is None else claims)

    def test_repository_watchlist(self):
        self.assertEqual(watch.audit(REPO), [])

    def test_fixture(self):
        self.assertEqual(watch.audit(self.root), [])

    def test_duplicate_id(self):
        self.write(claims=[self.claim, self.claim])
        self.assertTrue(any("duplicate claim_id" in x for x in watch.audit(self.root)))

    def test_missing_source(self):
        self.write(claims=[dict(self.claim, source_id="UNKNOWN")])
        self.assertTrue(any("unknown source_id" in x for x in watch.audit(self.root)))

    def test_bad_date(self):
        self.write(claims=[dict(self.claim, last_checked="2026-02-30")])
        self.assertTrue(any("date not ISO" in x for x in watch.audit(self.root)))

    def test_review_date_order(self):
        self.write(claims=[dict(self.claim, next_review_target="2026-01-01")])
        self.assertTrue(any("precedes" in x for x in watch.audit(self.root)))

    def test_wrong_index_type(self):
        self.write(source_rows=[dict(self.source, source_type="state_statute")])
        self.assertTrue(any("index status requires" in x for x in watch.audit(self.root)))

    def test_claimed_primary_must_not_be_an_index(self):
        self.write(claims=[dict(self.claim, review_status="TARGETED_PRIMARY_TEXT_CHECKED")])
        self.assertTrue(any("requires primary-law source" in x for x in watch.audit(self.root)))

    def test_evidence_url_must_match(self):
        self.write(claims=[dict(self.claim, evidence_url="https://example.com/law")])
        self.assertTrue(any("evidence URL differs" in x for x in watch.audit(self.root)))

    def test_judicial_order_claim_accepted(self):
        court = dict(
            self.source, source_type="judicial_order",
            status="OFFICIAL_JUDICIAL_ORDER",
            official_url="https://www.ca5.uscourts.gov/opinions/pub/25/25-50096-CV1.pdf"
        )
        claim = dict(
            self.claim, review_status="JUDICIAL_ORDER_CHECKED",
            evidence_url=court["official_url"],
            scope_checked="Fifth_Circuit_October_2026_en_banc_vacatur"
        )
        self.write(source_rows=[court], claims=[claim])
        self.assertEqual(watch.audit(self.root), [])

    def test_judicial_order_cannot_be_any_statute(self):
        self.write(claims=[dict(self.claim, review_status="JUDICIAL_ORDER_CHECKED")])
        self.assertTrue(any("requires judicial_order source" in x for x in watch.audit(self.root)))

    def test_judicial_order_requires_official_status(self):
        court = dict(
            self.source, source_type="judicial_order", status="REQUIRES_FURTHER_REVIEW"
        )
        self.write(source_rows=[court], claims=[
            dict(self.claim, review_status="JUDICIAL_ORDER_CHECKED")
        ])
        self.assertTrue(any("requires authenticated official judicial order" in x
                            for x in watch.audit(self.root)))

    def test_pending_requires_open_question(self):
        self.write(claims=[dict(self.claim, review_status="PENDING_REVIEW", open_question="")])
        self.assertTrue(any("empty open_question" in x for x in watch.audit(self.root)))


if __name__ == "__main__":
    unittest.main()
