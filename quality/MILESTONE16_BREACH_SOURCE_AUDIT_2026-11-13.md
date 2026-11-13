# Milestone 16 — primary-source breach-notification audit

**2026-11-13 / status: targeted source verification and six-state teaching update; no attorney signoff.**

## Question and method

Milestone 15's archive and the November 13 repository left California and Texas statutory deadlines unverified and Illinois/Massachusetts qualitative timelines unexpanded. This milestone reads the specified current law from six official state publishers and records exact statutory subsections, clock anchors, threshold operators and notices by recipient. It does **not** determine that a particular incident is reportable.

## Verified authorities

| State | Official publication checked | Section / pinpoint | Observation |
|---|---|---|---|
| California | California Department of Real Estate, **2026 Real Estate Law**, Civil Code excerpts pp. **107–109**; California DOJ filing page | Civil Code **1798.82(a)(2), (b), (c), (f)** | Enacted SB 446 (2025 Stats. ch. 319) amended statute effective Jan. 1, 2026. 30-calendar-day general resident clock; >500 AG sample within 15 calendar days **after** resident notices |
| Texas | Texas Legislature, Business & Commerce Code ch. 521 | **§521.053(b), (c), (h), (i)** | 60-day generally resident vs 30-day AG at ≥250 Texas residents; maintainer immediate owner notification |
| Illinois | Illinois General Assembly, 815 ILCS 530 (current codification search extract) | **§10(a), (b), (e)** | No generic numeric consumer limit; >500 AG by consumer notice, with specified exclusion |
| Massachusetts | Massachusetts General Court, ch. 93H | **§3(a)–(b)** | Owner/licensor vs maintainer and regulator/consumer notices; no generic 30 days in §3 |
| Washington | Washington Legislature, RCW | **19.255.010(1)–(3), (7)–(8)** | Discovery-based 30-day scheme, >500 AG; risk-of-harm and delays |
| Florida | Florida Senate, 2026 statute | **501.171(3)–(4), (6)** | Determination/reason-to-believe 30-day tracks; 500+ Department threshold |

## Unresolved and source confidence limits

- The California Legislature's dynamic code viewer returned **403**, but state-published 2026 statutory excerpts and the DOJ's state website directly resolved **the deadline and threshold propositions**. This does **not** establish a complete 2026 legislative subsequent-history search.
- Illinois General Assembly section text was available through the official indexed section result, but an ordinary direct page open intermittently timed out; verify current authenticated legislative text before relying in an active matter.
- No case-law citator, every-sector overlay, contract-specific clock, email notice delivery validation or complete state-by-state link audit.
- This repository's **static CI checks** are not legal-law currentness testing. No automated deadline engine was implemented.

## Reconciliation

The earlier statement in [November 13 audit](RESEARCH_RECONCILIATION_2026-11-13.md) that the CA breach provision remained unauthenticated was accurate **at that earlier milestone**. The current targeted state-published-text check resolves that narrow P0 question; do not silently rewrite historical receipts. The six-state research [chapter](../research/2026-11-13/03-breach-notifications.md) and [normalized matrix](../research/2026-11-13/breach-obligations.csv) document the updated disposition.

**Next gate:** check other state incident laws and transaction- or date-specific source versions; authenticate precedent and later judicial treatment; add metadata/review tooling without automating legal conclusions.