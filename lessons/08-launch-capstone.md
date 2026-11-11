# Lesson 08 — Founder legal-readiness capstone

**Goal:** Produce an evidence-backed risk register for a real AI/SaaS/game launch, not a falsely reassuring green-check checklist.

## 1. Define the company and launch footprint
Write a 1-page scope: entity, product, jurisdictions served, customer categories, minors?, regulated industries?, personal/biometric data?, pricing model, payment processors, subcontractors, AI providers, open-source components, asset licenses, and intended claims.

## 2. Build an obligation-to-evidence matrix
| Area | Question | Minimum evidence | Reference |
|---|---|---|---|
| Contract | Do users affirmatively accept applicable terms? | UX capture, versioned acceptance event | [FTC §5](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section45&num=0&edition=prelim) |
| Company | Was equity correctly authorized/documented? | Charter, board approvals, cap table | [DGCL](https://delcode.delaware.gov/title8/c001/) |
| Financing | Which registration exemption applies? | Counsel-approved offering process | [SEC exemptions](https://www.sec.gov/resources-small-businesses/exempt-offerings) |
| IP | Is each asset commercially usable? | License / provenance inventory | [17 USC §106](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title17-section106&num=0&edition=prelim) |
| Data | Are notices and deletion true in practice? | Data map and deletion test | [FTC Everalbum](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter) |
| AI | Are risk claims and human oversight evidenced? | Model card, evaluation, audit | [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=OJ%3AL_202401689) |
| Recruiting | Are automated selections validated/job-related? | Validation protocol and results | [Title VII](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title42-section2000e-2&num=0&edition=prelim) |
| Security | Is access limited and audited? | Cross-tenant test results | [FTC guidance](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) |
| Minors | Is COPPA triggered? | Audience and data analysis | [15 USC §6502](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section6502&num=0&edition=prelim) |

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
