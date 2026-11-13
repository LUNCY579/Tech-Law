#!/usr/bin/env python3
"""Offline metadata integrity checks for Tech-Law legal source and breach registers.

Checks CSV schema, unique IDs, date syntax, HTTPS government publisher hosts,
cross-reference integrity and explicit source status. Does NOT contact a URL or
verify legal currentness, statutory interpretation, or legal permissions.

Usage: python3 scripts/audit_source_register.py [--root /path/to/Tech-Law]
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path
import re
from urllib.parse import urlsplit

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
SOURCES = "research/2026-11-13/source-register.csv"
MATRIX = "research/2026-11-13/breach-obligations.csv"
SOURCE_COLUMNS = (
    "id", "jurisdiction", "source_type", "status", "date",
    "official_url", "critical_caveat",
)
MATRIX_COLUMNS = (
    "id", "jurisdiction", "recipient", "legal_section", "condition",
    "clock_anchor", "clock_statement", "threshold", "source_id",
    "source_url", "verified_as_of", "limitation",
)
STATUS_VALUES = {
    "ENACTED_AND_APPLICABLE",
    "ENACTED_FUTURE",
    "OFFICIAL_GUIDANCE",
    "WITHDRAWN",
    "VACATED",
    "REQUIRES_FURTHER_REVIEW",
}

# Oregon's DOJ retains a legacy .or.us official government hostname. This
# entry is vetted manually; do NOT accept all .or.us as governmental.
ADDITIONAL_OFFICIAL_HOSTS = {"www.doj.state.or.us"}


def valid_date(value: str) -> bool:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def official_source_url(value: str) -> bool:
    """Hostname allowlist is metadata hygiene, NOT legal authentication."""
    try:
        parsed = urlsplit(value)
        host = (parsed.hostname or "").lower()
        return (
            parsed.scheme == "https"
            and not parsed.username
            and not parsed.password
            and bool(host)
            and (host.endswith(".gov") or host.endswith(".europa.eu")
                 or host in ADDITIONAL_OFFICIAL_HOSTS)
        )
    except ValueError:
        return False


def read_table(root: Path, relpath: str, columns: tuple[str, ...],
               errors: list[str]) -> list[dict[str, str]]:
    path = root / relpath
    if not path.is_file():
        errors.append(f"{relpath}: missing CSV file")
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(columns):
            errors.append(
                f"{relpath}: unexpected columns {reader.fieldnames!r}; "
                f"expected {list(columns)!r}"
            )
            return []
        rows = list(reader)
    for number, row in enumerate(rows, start=2):
        if None in row:
            errors.append(f"{relpath}:{number}: extra values / malformed CSV row")
        for key in columns:
            if not (row.get(key) or "").strip():
                errors.append(f"{relpath}:{number}: blank {key}")
    return rows


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    source_rows = read_table(root, SOURCES, SOURCE_COLUMNS, errors)
    matrix_rows = read_table(root, MATRIX, MATRIX_COLUMNS, errors)
    sources: dict[str, dict[str, str]] = {}
    for line_no, row in enumerate(source_rows, start=2):
        sid = (row.get("id") or "").strip()
        if sid in sources:
            errors.append(f"{SOURCES}:{line_no}: duplicate ID {sid}")
        else:
            sources[sid] = row
        if row.get("status") not in STATUS_VALUES:
            errors.append(f"{SOURCES}:{line_no}: invalid source status {row.get('status')!r}")
        if not valid_date(row.get("date") or ""):
            errors.append(f"{SOURCES}:{line_no}: invalid ISO date {row.get('date')!r}")
        if not official_source_url(row.get("official_url") or ""):
            errors.append(f"{SOURCES}:{line_no}: nonofficial/non-HTTPS URL {row.get('official_url')!r}")

    seen: set[str] = set()
    for line_no, row in enumerate(matrix_rows, start=2):
        rid = (row.get("id") or "").strip()
        if rid in seen:
            errors.append(f"{MATRIX}:{line_no}: duplicate ID {rid}")
        seen.add(rid)
        if not valid_date(row.get("verified_as_of") or ""):
            errors.append(f"{MATRIX}:{line_no}: invalid ISO verification date")
        if not official_source_url(row.get("source_url") or ""):
            errors.append(f"{MATRIX}:{line_no}: nonofficial/non-HTTPS URL")
        source = sources.get(row.get("source_id") or "")
        if not source:
            errors.append(f"{MATRIX}:{line_no}: unknown source_id {row.get('source_id')!r}")
            continue
        if row.get("jurisdiction") != source.get("jurisdiction"):
            errors.append(f"{MATRIX}:{line_no}: jurisdiction differs from source_id {row.get('source_id')}")
        if row.get("source_url") != source.get("official_url"):
            errors.append(f"{MATRIX}:{line_no}: URL differs from source register")
        if source.get("status") != "ENACTED_AND_APPLICABLE":
            errors.append(
                f"{MATRIX}:{line_no}: deadline row references source with "
                f"non-operative or unverified status {source.get('status')}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    errors = audit(args.root.resolve())
    for issue in errors:
        print("ERROR:", issue)
    if errors:
        print(f"Source register audit FAILED: {len(errors)} error(s)")
        return 1
    print("Source register audit PASS: valid CSV schemas, IDs and cross-references.")
    print("No network checks, legal validity, or deadline correctness verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
