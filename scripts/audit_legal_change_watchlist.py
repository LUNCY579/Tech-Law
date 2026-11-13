#!/usr/bin/env python3
"""Offline structural audit for claim-level legal-source review receipts.

Checks metadata ONLY. It does not fetch legal text, verify currentness, determine
legal applicability, or schedule any follow-up work. Run from the repo root:
  python3 scripts/audit_legal_change_watchlist.py
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WATCHLIST = "quality/legal-change-watchlist.csv"
SOURCES = "research/2026-11-13/source-register.csv"
WATCHLIST_COLUMNS = (
    "claim_id", "topic", "jurisdiction", "source_id", "review_status",
    "scope_checked", "evidence_url", "last_checked",
    "next_review_target", "open_question",
)
STATUSES = {
    "INDEX_SCOPE_CHECKED", "TARGETED_PRIMARY_TEXT_CHECKED",
    "JUDICIAL_ORDER_CHECKED", "PENDING_REVIEW",
}
PRIMARY_SOURCE_TYPES = {
    "primary_session_law", "state_statute", "federal_statute",
    "primary_regulation", "enacted_state_law",
}


def iso_date(value: str) -> bool:
    try:
        if len(value) != 10 or date.fromisoformat(value).isoformat() != value:
            return False
    except (TypeError, ValueError):
        return False
    return True


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    source_file = root / SOURCES
    watch_file = root / WATCHLIST
    if not source_file.is_file():
        return [f"missing source register: {SOURCES}"]
    if not watch_file.is_file():
        return [f"missing watchlist: {WATCHLIST}"]
    with source_file.open(newline="", encoding="utf-8-sig") as handle:
        sources = {r["id"]: r for r in csv.DictReader(handle)}
    with watch_file.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(WATCHLIST_COLUMNS):
            return [f"{WATCHLIST}: invalid columns: {reader.fieldnames!r}"]
        rows = list(reader)
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        key = (row.get("claim_id") or "").strip()
        if not key or key in seen:
            errors.append(f"{WATCHLIST}:{index}: missing or duplicate claim_id {key!r}")
        seen.add(key)
        for col in WATCHLIST_COLUMNS:
            if not (row.get(col) or "").strip():
                errors.append(f"{WATCHLIST}:{index}: empty {col}")
        if None in row:
            errors.append(f"{WATCHLIST}:{index}: extra CSV fields")
        status = row.get("review_status")
        if status not in STATUSES:
            errors.append(f"{WATCHLIST}:{index}: invalid review status {status!r}")
        checked = row.get("last_checked") or ""
        target = row.get("next_review_target") or ""
        if not iso_date(checked) or not iso_date(target):
            errors.append(f"{WATCHLIST}:{index}: date not ISO YYYY-MM-DD")
        elif target < checked:
            errors.append(f"{WATCHLIST}:{index}: review target precedes last check")
        sid = row.get("source_id") or ""
        source = sources.get(sid)
        if not source:
            errors.append(f"{WATCHLIST}:{index}: unknown source_id {sid!r}")
            continue
        if source.get("jurisdiction") != row.get("jurisdiction"):
            errors.append(f"{WATCHLIST}:{index}: source jurisdiction mismatch")
        if source.get("official_url") != row.get("evidence_url"):
            errors.append(f"{WATCHLIST}:{index}: evidence URL differs from registered source")
        if status == "INDEX_SCOPE_CHECKED":
            if source.get("source_type") != "official_legislative_index":
                errors.append(f"{WATCHLIST}:{index}: index status requires legislative-index source")
            if not row.get("scope_checked"):
                errors.append(f"{WATCHLIST}:{index}: index claim requires scope")
        elif status == "TARGETED_PRIMARY_TEXT_CHECKED":
            if source.get("source_type") not in PRIMARY_SOURCE_TYPES:
                errors.append(f"{WATCHLIST}:{index}: primary-text status requires primary-law source")
            if source.get("status") != "ENACTED_AND_APPLICABLE":
                errors.append(f"{WATCHLIST}:{index}: primary-text claim references non-operative source")
        elif status == "JUDICIAL_ORDER_CHECKED":
            if source.get("source_type") != "judicial_order":
                errors.append(f"{WATCHLIST}:{index}: judicial claim requires judicial_order source")
            if source.get("status") != "OFFICIAL_JUDICIAL_ORDER":
                errors.append(f"{WATCHLIST}:{index}: judicial claim requires authenticated official judicial order status")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = audit(args.root.resolve())
    for error in errors:
        print("ERROR:", error)
    if errors:
        print(f"Legal change watchlist metadata audit FAILED: {len(errors)}")
        return 1
    print("Legal change watchlist metadata audit PASS")
    print("No current-law, evidence-content, URL accessibility or external monitoring verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
