# Lesson 08 — Founder legal-readiness capstone

**Goal:** Produce an evidence-backed risk register for a real AI/SaaS/game launch, not a falsely reassuring green-check checklist.

## 1. Define the company and launch footprint
Write a 1-page scope: entity, product, jurisdictions served, customer categories, minors?, regulated industries?, personal/biometric data?, pricing model, payment processors, subcontractors, AI providers, open-source components, asset licenses, and intended claims.

## 2. Build an obligation-to-evidence matrix
| Area | Question | Minimum evidence | Reference |
|---|---|---|---|
| Contract | Do users affirmatively accept applicable terms? | UX capture, versioned acceptance event | [FTC §5](https://www.govinfo.gov/link/uscode/15/45) |
| Company | Was equity correctly authorized/documented? | Charter, board approvals, cap table | [DGCL](https://delcode.delaware.gov/title8/c001/) |
| Financing | Which registration exemption applies? | Counsel-approved offering process | [SEC exemptions](https://www.sec.gov/resources-small-businesses/exempt-offerings) |
| IP | Is each asset commercially usable? | License / provenance inventory | [17 USC §106](https://www.govinfo.gov/link/uscode/17/106) |
| Data | Are notices and deletion true in practice? | Data map and deletion test | [FTC Everalbum](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter) |
| AI | Are risk claims and human oversight evidenced? | Model card, evaluation, audit | [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=OJ%3AL_202401689) |
| Recruiting | Are automated selections validated/job-related? | Validation protocol and results | [Title VII](https://www.govinfo.gov/link/uscode/42/2000e-2) |
| Security | Is access limited and audited? | Cross-tenant test results | [FTC guidance](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) |
| Minors | Is COPPA triggered? | Audience and data analysis | [15 USC §6502](https://www.govinfo.gov/link/uscode/15/6502) |

## 3. Rank the risk
For each gap, record **severity** (critical/high/medium/low), **likelihood**, **scope**, **legal uncertainty**, **owner**, **proof**, **mitigation**, **decision**, and **next review date**. Avoid claiming mathematical precision for liability estimates.

**P0:** credible risk of unlawful public deployment, exposing data, unsupported regulated claims, unlicensed assets or unlawful fundraising.  
**P1:** control gaps that materially impair operational compliance.  
**P2:** documentation and monitoring enhancements that do not presently block launch.

## 4. Apply it to three fictional startups
1. **AI hiring portal**: candidate privacy, Title VII, model score validity, independent credential verification, employer access controls.
2. **Agentic document workspace**: vendor API permissions, prompt/data retention, model routing, terms and enterprise data protection.
3. **Indie game storefront**: code/music/font/texture rights, consumer pricing/returns, minors and mod-upload policies.

## 5. Final assessment: provide a memo
Write a 1,500-word report consisting of product facts, each potentially applicable jurisdiction, five statutory sections with actual element-by-element analyses, two case comparisons distinguishing holding from settlement, a prioritized remediation plan, and a source/permission appendix.

**Rubric (100):** authority precision 25; issue spotting 20; application to facts 20; counterarguments/uncertainty 15; evidence quality 10; clarity 10.

## 6. Source maintenance protocol
Before shipping: confirm official source URLs and the currently effective version; inspect amendments and agency rules; record a date-of-access; never reproduce entire third-party reports without permission; obtain professional review for material company decisions. A lesson is educational, not an individualized legal opinion.

For recurring updates, review the [U.S. Code](https://uscode.house.gov/), [Federal Register](https://www.federalregister.gov/), [SEC](https://www.sec.gov/), [FTC](https://www.ftc.gov/), [Copyright Office](https://www.copyright.gov/), [Delaware Code](https://delcode.delaware.gov/), and [EUR-Lex](https://eur-lex.europa.eu/).

## Advanced seminar — evidence-first launch dossier

### A. Seven separate review gates
1. **Entity/funding:** formation, ownership, board approval, safe fundraising communications.
2. **Data rights:** inventory, transparency, access, deletion and transfers.
3. **AI use:** role, risk classification, evaluation, human oversight and claims.
4. **IP:** code/model/dataset/assets provenance and distribution permissions.
5. **Contracts/billing:** real signup assent, refunds, subscriptions, B2B obligations.
6. **Security:** identity, tenant isolation, incident response, vendor assessments.
7. **Accessibility/consumer interface:** keyboard access, accurate disclosures, absence of deceptive UX.

### B. Evidence standard
For each control require `control_id, rule, jurisdiction, applies?(yes/no/uncertain), factual basis, current source + section, proof artifact, owner, severity, test result, remediation and counsel signoff`. “We have a privacy policy” is not adequate evidence that the policy matches the system.

### C. Example findings
**Finding LAUNCH-001:** API can export another tenant's candidate assessment. Severity P0. Evidence: two-account synthetic regression. Remediation: server-side access control and fixed consent scope; validate adversarial test.

**Finding LAUNCH-002:** Website claims “we never store prompts” but API vendor retains them by default. P0/P1 depending on actual representations and affected data. Evidence: vendor contract and telemetry configuration. Remediation: adjust system and/or truthful disclosure, seek review.

**Finding LAUNCH-003:** Commercial game includes a font licensed only for personal use. P0 before distribution. Evidence: font EULA and packaged binary. Remediation: replace or obtain commercial license.

### D. Graduation exercise
Produce an 8-page launch memo with 10 properly cited authoritative rules, three original case briefs, a documented source re-use assessment, an obligation matrix and 20 engineering controls each tied to test evidence. Mark unanswered jurisdictional questions rather than pretending compliance is proven.
