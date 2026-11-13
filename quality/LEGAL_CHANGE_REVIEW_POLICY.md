# Milestone 18B — legal-change review watchlist and evidence levels

**As of:** November 13, 2026. The [structured claim watchlist](legal-change-watchlist.csv) provides *editorial metadata*, not continuous legal monitoring, legal advice, a deadline calculator, or an external permission to reproduce source documents.

## Why a second ledger?

The [source register](../research/2026-11-13/source-register.csv) identifies a publication and its high-level status. The **watchlist** records the *specific proposition or open question*, the reviewed statutory scope, the documentary evidence, the date last reviewed, a proposed date for the next manual check and the remaining uncertainty. Different claims backed by the same statute may have different verification completeness.

| Claim-level status | What it supports | What it does not support |
|---|---|---|
| `INDEX_SCOPE_CHECKED` | An official amendment table was inspected for a named section range | A claim that every newly enacted or uncodified law is absent or that the underlying law is current in every respect |
| `TARGETED_PRIMARY_TEXT_CHECKED` | Specific cited primary-law section(s) were examined | A full subsequent-history review, proof all amendments/definitions were captured, or a company's compliance |
| `PENDING_REVIEW` | A useful unresolved legal question has a source and next manual review target | Any assertion that the issue is closed or that someone is monitoring it automatically |

The statuses are **not** judicial authority rankings or numeric probability/confidence scores.

## Source and review metadata

Each watchlist row must have: unique `claim_id`; source-linked jurisdiction; descriptive `topic`; existing `source_id`; **scope actually checked**; `review_status`; source-matching `evidence_url`; ISO-formatted `last_checked`; `next_review_target`; and a nonempty `open_question` or consequential limitation.

For an amended or reversed authority, create a **new dated receipt** and explain what changed. Preserve older dated research notes, including original access failures, rather than silently rewriting the historical record. A new index check can close an **access problem** without closing a **complete legal-currentness** review.

## Technical gate

Run from repo root:

```sh
python3 scripts/audit_curriculum.py
python3 scripts/audit_source_register.py
python3 scripts/audit_legal_change_watchlist.py
python3 -m unittest discover -s tests -v
```

CI runs these steps on PRs and `main`. The watchlist audit checks schema, unique IDs, nonempty scope/limitations, valid dates, chronological date order, source/jurisdiction and official URL equality, and credible source-type/status combinations. An **index check cannot masquerade as reviewed enacted text** in that metadata.

**Explicitly outside automated scope:** visiting legal websites; reading statute text; tracing uncodified law, pending bills, agency regulation or case citations; validating source usage permissions; confirming the law at a later date; contacting qualified counsel; or performing a scheduled follow-up. `next_review_target` is only a *human planning field*.

## Immediate editorial follow-ups

- Oregon: widen beyond the direct-amendment check for ORS 646A.570–.589. The [Milestone 19 ALPR chapter](../research/2026-11-13/12-oregon-alpr-law-and-vendor-contracts.md) already identifies **2026 Ch.77**, a separate agency/vendor rule missed by OCPA-only section index scanning. Other new and uncodified enactments, judicial later history and case-specific exceptions remain open. See [Milestone 18 source review](MILESTONE18_OREGON_SOURCE_AUDIT_2026-11-13.md).
- Maryland: compare post-2024 signed acts and the most current codified MODPA sections.
- California: for live incident response, corroborate state-published 2026 Civil Code §1798.82 excerpts with the operative legislature code and exception facts.
- Historical judicial cases: continue locating issuing-court originals for *Specht* and *Van Gorkom*, without relabeling unofficial reproductions as originals.

Do not treat a completed CI check, one state statute, or a target review date as legal certification.
