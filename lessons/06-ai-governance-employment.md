# Lesson 06 — AI regulation, employment decisions and model governance

**Goal:** Classify real deployments rather than asserting one universal “AI law.”

## 1. Identify the regulated role and use case
An AI model developer, general-purpose model provider, downstream system provider, deployer, employer and software reseller may have different duties. An AI code assistant and an AI tool ranking job applicants present very different risks.

## 2. EU AI Act: classify before implementing
[Law] Regulation (EU) 2024/1689: Article 3 definitions, Article 5 prohibited AI practices, Article 6 and Annex III high-risk classification, Article 9 risk-management, Article 10 data governance, Article 13 transparency, Article 14 human oversight, Article 27 fundamental-rights impact assessment where applicable, and Articles 53–55 GPAI obligations. Read the **current consolidated text and amendments**, not only an old infographic. [Official EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=OJ%3AL_202401689). Check Articles 111 and 113 for transitional/application dates; provisions phase in at different times and may have been amended.

Employment recruitment/selection AI is within Annex III's employment category when conditions are met; do not assume every AI function is automatically high-risk without examining statutory criteria and exemptions.

## 3. U.S. employment discrimination rules apply to AI-supported decisions
[Law] Title VII, 42 U.S.C. §2000e-2, prohibits certain employment discrimination; the use of a model does not remove an employer's legal duties. [Official statute](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title42-section2000e-2&num=0&edition=prelim).

Consider disparate treatment and disparate impact separately. Model outputs should be tested with job-relevant validation, representative evaluation populations, accommodation/accessibility analysis, and documented human review. An employer cannot assume the vendor will bear every legal risk.

## 4. AI marketing and opaque decisions
Promising “bias-free,” “100% compliant,” or “perfectly objective” creates substantiation risk. FTC Act §5 applies to potentially deceptive representations. Keep evidence for stated metrics, populations, data leakage controls and limitations.

## Founder hypothetical
A hiring platform displays a “verified employability score” from an unvalidated coding exam. The score may be materially misleading; candidate and employer audiences could misunderstand what is independently validated. Separate self-reported skills, credential authenticity, exam performance, and any scientific validity claims.

## Practical implementation matrix
| Risk | Product control | Evidence |
|---|---|---|
| Misleading claim | Claim registry and approved language | Benchmark version, reviewer |
| Bias/discrimination | Job-related validation and subgroup testing | Study protocol/results |
| Privacy | Candidate consent, role checks, deletion | Access tests and audit logs |
| Automation harm | Human review and contest/appeal path where appropriate | Decision logs and policy |
| Model changes | Version pinning and regression tests | Release attestation |
| External models | Provider and data-use audit | Contract / retention matrix |

## Exercise
A product screens candidates for EU employers, uses a general-purpose model via API, and returns a ranking. List which roles it may occupy, which EU AI Act provisions need review, and which U.S. employment questions arise if sold domestically. **Answer:** Identify providers/deployers and possible high-risk employment classification under current text; test Article 6/Annex III, obligations, jurisdiction, effective dates, possible exceptions, and Title VII/ADA and relevant state/local law. Do not make a final classification without actual product facts.

## Sources
- [EU AI Act, official EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=OJ%3AL_202401689) [law].
- [Title VII, 42 U.S.C. §2000e-2](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title42-section2000e-2&num=0&edition=prelim) [law].
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) [voluntary framework, not law].
- [FTC Act §5](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section45&num=0&edition=prelim) [law].
