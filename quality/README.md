# Milestone 5 — Legal scholarship quality-assurance system

**Review date:** 2026-11-11. This is educational editorial QA, **not** a lawyer's opinion, a commercial citator result, or a guarantee that every linked page remains current.

## Deliverables

1. [Citation and legal-claim validation standard](citation-standards.md): reproducible citation, pinpoint, status and temporal review rules.
2. [Case briefing manual](case-briefing.md): doctrine, procedural posture, majority/dissent and limiting facts.
3. [Cross-book graded assessment](final-examination.md): 100-point scenario with a detailed answer key and issue taxonomy.
4. [Audit matrix and open issues](audit-matrix.md): verified checks, limitations and required corrections.
5. [Machine-checkable curriculum manifest](curriculum-manifest.json): referenced instructional units and authority classifications.

## Evidence grades
- **A** — official controlling text and operative section read, relevant page/pinpoint documented, change/status review performed.
- **B** — official text located, doctrine and date inspected, but subsequent judicial treatment or precise version updates not exhaustively checked.
- **C** — official publisher landing page or guidance referenced; specific proposition not checked against full current underlying instrument.
- **PENDING** — original source unverified or disputed. Do not present as authenticated.

These are **editorial grades**, not judicial authority rankings or outcome confidence.

## Mandatory release gates for every textbook
- Exact source type and jurisdiction.
- Citation to section or opinion, preferably pinpoint.
- Date of opinion/publication, effective and amendment dates where material.
- Holding versus dicta versus administrative allegation versus consent order versus guidance.
- One counterargument and a set of missing facts for each material application.
- Text-license provenance distinct from site accessibility.
- No wholesale copying of third-party reports, legal treatises, licensed code, templates, or judicial PDFs.
- For law-sensitive launch recommendations, qualified practitioner review and live current-law check.

## Practical cadence
Quarterly recheck regulatory deadlines and link integrity; review amendments at each launch or financing. Perform case subsequent-history checks before relying on precedent in a filing or transaction. A passing course test does not confer legal or compliance certification.

## Milestone 16: source and breach-law record integrity (November 13, 2026)

The [six-state statute audit](MILESTONE16_BREACH_SOURCE_AUDIT_2026-11-13.md) documents the CA/TX/IL/MA/WA/FL breach-notification research receipt. The [source-register policy](SOURCE_REGISTER_POLICY.md) and `scripts/audit_source_register.py` add offline CSV metadata validation, reference-status guardrails and nine regression checks to the GitHub Actions workflow. These tests do **not** verify live laws, source URL availability, legal interpretation, subsequent court history or product compliance.

## Milestone 18 — amendment-index and claim-review controls (November 13, 2026)

The [Oregon 2026 legislative amendment receipt](MILESTONE18_OREGON_SOURCE_AUDIT_2026-11-13.md) is backed by a separate [claim-level review watchlist](legal-change-watchlist.csv), its [evidence-grade and manual-review policy](LEGAL_CHANGE_REVIEW_POLICY.md), and `scripts/audit_legal_change_watchlist.py`. It records exact checked scope, source IDs, unresolved questions and next *manual* review targets. Unit tests and GitHub Actions reject mismatched source types and malformed records. These checks do **not** browse government sites, operate a legal change alert, guarantee laws are current or certify a product.

## Milestone 21 — court-order source and version discipline

The [child online-safety court/source audit](MILESTONE21_CHILD_SAFETY_LITIGATION_AUDIT_2026-11-13.md) distinguishes **official court opinions and en banc orders** from enacted primary law, draft legislation and third-party chaptered reproductions. The source watchlist now supports `JUDICIAL_ORDER_CHECKED` only for `judicial_order` entries with `OFFICIAL_JUDICIAL_ORDER` source status. The **July 24, 2026 Fifth Circuit Texas SCOPE panel opinion was vacated on October 28**, so it remains historical and cannot be treated as controlling appellate law. The code checks provenance labels, not present-day docket status, merits, injunction coverage or actual legal obligations.
