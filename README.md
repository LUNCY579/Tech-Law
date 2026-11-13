# Tech Law for AI Startup Founders

**November 2026 research supplement:** [source-linked legal updates](RESEARCH_UPDATES.md) compare the later milestone archive with applicable state and federal law and the amended EU AI Act, with explicit evidentiary limits.

An evidence-first, self-study curriculum in technology law, startup formation, software/IP licensing, data protection, AI governance, and commercial launch risks.

**Scope:** Primarily United States federal law, with Delaware corporate law, California privacy law, and EU AI law for comparison. **As-of:** 2026-11-10. **Educational only, not legal advice.** Laws and agency interpretations change; verify the current official text before reliance.

## Milestone 8: repository-wide legal QA (targeted, not certification)

- **[Milestone 8 findings and open gates](quality/MILESTONE8_AUDIT_2026-11-11.md)** — structural review of PR patch content, targeted official-source currency checks, corrected EU–US DPF litigation history and transparent limitations.
- **[Repeatable structural link/manifest audit](scripts/audit_curriculum.py)** — run locally with `python3 scripts/audit_curriculum.py`. This is a no-network structure check; it cannot verify legal correctness or outside link availability.
- **[Updated EU–U.S. DPF litigation section](textbooks/07-international-technology-law/02-data-transfers.md)** — 2025 *Latombe* judgment and pending appeal noted without assuming a final appellate outcome.

**Historical Milestone 8 gate:** PR #1 was subsequently merged into main on November 13, 2026. The earlier audit did not exhaustively verify every external URL, every amendment, every judicial subsequent history, or legal reuse rights for all linked materials.

## Milestone 7: International Technology Law and Cross-Border Commercialization

- **[Textbook VII — International Technology Law](textbooks/07-international-technology-law/README.md)** — cross-border jurisdiction, GDPR Chapter V data transfers, EU–U.S. DPF and SCCs, AI Act and DSA market entry, BIS export controls, OFAC sanctions, EU VAT and international SaaS contracting.
- **[Source ledger](textbooks/07-international-technology-law/SOURCE_LEDGER.md)** — official publisher verification, unresolved legal questions and copyright-safe sourcing.
- **[100-point cross-border commercialization capstone](textbooks/07-international-technology-law/06-capstone-exam.md)** — U.S. AI credential startup selling to EU employers and consumers.

## Milestone 6: Cybersecurity and Employment AI textbooks

- **[Textbook V — Cybersecurity, Computer Misuse & Data Breach Law](textbooks/05-cybersecurity-computer-misuse/README.md)** — CFAA, *Van Buren*, FTC Safeguards, SEC public-company cyber disclosures, incidents, vendor controls and exams.
- **[Textbook VI — Employment Law & AI Assessment](textbooks/06-employment-ai-assessments/README.md)** — Title VII, ADA, scientific assessment validity, impact testing, credential provenance and graded exams.
- **[Milestone 6 official source audit](textbooks/SOURCE_NOTES_2026-11-11_MILESTONE6.md)** — regulates the distinction between law, official guidance and conditional applicability.

## Milestone 5: scholarship QA and cross-book assessment

- **[Citation and legal-claim standards](quality/citation-standards.md)** — authority hierarchy, exact sections and case pinpoints, version control, reuse constraints.
- **[Case briefing manual](quality/case-briefing.md)** — procedural posture, holdings, concurrence and dissent, distinctions.
- **[Cross-book 100-point examination with answer key](quality/final-examination.md)** — integrated AI startup fact pattern.
- **[Targeted audit and open issues](quality/audit-matrix.md)** — explicit checks and limitations, not an exhaustive citator audit.
- **[Machine-readable manifest](quality/curriculum-manifest.json)** — textbook inventory and source-status distinctions.

## Intellectual Property and Contracts textbooks (Milestone 4)

- **[Textbook III — Intellectual Property, Open Source & AI Assets](textbooks/03-intellectual-property-open-source/README.md)**: copyright/fair use, software licenses, model/data rights, AI outputs, trademarks, patents, trade secrets, and a commercial-game/AI audit exam.
- **[Textbook IV — SaaS Contracts, Commerce & Technology Liability](textbooks/04-contracts-saas-liability/README.md)**: digital assent, contract hierarchy, AI service clauses, consumer subscription law, liability, cybersecurity, and a SaaS launch exam.
- **[Milestone 4 official-source notes](textbooks/SOURCE_NOTES_2026-11-11_MILESTONE4.md)**: status of case holdings, license texts, and the 2025 vacatur/2026 rollback of the FTC click-to-cancel amendment.

## Earlier: dedicated textbooks (Milestone 3)

- **[Textbook I — Startup Corporate Law & Securities](textbooks/01-startup-corporate-securities/README.md)**: formation, governance, equity, vesting and IP assignment, SAFE math, exempt fundraising, graded examinations.
- **[Textbook II — AI Regulation & Privacy](textbooks/02-ai-regulation-privacy/README.md)**: the 2026 EU AI Act text, GDPR, California 2026/2027 regulations, FTC and hiring discrimination, compliance architecture and applied examination.

Both textbooks provide original explanations with primary official sources and founder-focused hypotheticals. **They are educational primers, not exhaustive treatises or legal signoff.** All source versions and effective dates need transaction-specific rechecking.

## New: primary-source casebook (Milestone 2)

Read the [casebook index](casebook/README.md) for detailed judicial case briefs, the [statutory interpretation lab](casebook/statutory-reading-lab.md), and the [verification register](casebook/SOURCE_REGISTER.md). The casebook was merged through PR #1 on November 13, 2026; source-authentication work for some historical opinions remains open. Historic opinions without authenticated official copies are specifically marked **pending**, not represented as verified.

## Learning sequence

| Week | Module | Deliverable |
|---|---|---|
| 1 | [Legal method and authority](lessons/01-legal-method.md) | Source hierarchy and issue-spotting memo |
| 2 | [Contracts and SaaS](lessons/02-contracts-saas.md) | Contract risk matrix |
| 3 | [Corporate formation and fundraising](lessons/03-startup-corporate-securities.md) | Cap table / financing checklist |
| 4 | [Copyright and software licensing](lessons/04-copyright-open-source-ai.md) | Repository provenance inventory |
| 5 | [Privacy, data protection and FTC enforcement](lessons/05-privacy-consumer-protection.md) | Data-flow / deletion inventory |
| 6 | [AI regulation, recruitment and decisions](lessons/06-ai-governance-employment.md) | AI risk assessment |
| 7 | [Cybersecurity and computer misuse](lessons/07-security-cyberlaw.md) | Security control gap report |
| 8 | [Founder launch capstone](lessons/08-launch-capstone.md) | Evidence-backed launch dossier |

Each lesson contains objectives, legal rules, an analysis framework, a real government-sourced case or regulatory proceeding where available, a startup hypothetical, an exercise, and a source list.

## Research rules and re-use

1. Prefer **primary law** (statutes, rules, court opinions, regulatory orders) and official regulators' educational guidance; distinguish binding law from guidance.
2. Give pinpoint section numbers, jurisdiction and relevant dates. Explain when a source is an allegation, settlement, or binding judicial holding.
3. Use original paraphrases and short necessary quotations; **link to source material rather than copying** complete opinions, agency reports, or website content. Official availability does **not** automatically imply an unrestricted republication license.
4. Source URLs are references, **not assertions that the linked text is licensed for redistribution**. This repository contains original instructional commentary, not third-party textbook republications.
5. Always check changes, applicability thresholds, exceptions, preemption, and enforcement before asserting a compliance obligation.
6. Use `[law]` for statutory requirements, `[guidance]` for agency advice, `[case holding]` for judicial holdings, `[settlement]` for resolved allegations, and `[hypothetical]` for fictional examples.

## How to study

Read the first source before the lesson; write your own rule statement; solve each fact pattern *before* opening the answer key; make a one-page implementation checklist; repeat the exercise on your own product. Reserve qualified counsel for actual entity formation, securities offers, regulated deployment, or a live dispute.
