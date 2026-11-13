# Lesson 06 — AI regulation, employment decisions and model governance

**Goal:** Classify real deployments rather than asserting one universal “AI law.”

## 1. Identify the regulated role and use case
An AI model developer, general-purpose model provider, downstream system provider, deployer, employer and software reseller may have different duties. An AI code assistant and an AI tool ranking job applicants present very different risks.

## 2. EU AI Act: classify before implementing
[Law] Regulation (EU) 2024/1689: Article 3 definitions, Article 5 prohibited AI practices, Article 6 and Annex III high-risk classification, Article 9 risk-management, Article 10 data governance, Article 13 transparency, Article 14 human oversight, Article 27 fundamental-rights impact assessment where applicable, and Articles 53–55 GPAI obligations. Read the **current consolidated text and amendments**, not only an old infographic. [Official EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=OJ%3AL_202401689). Check Articles 111 and 113 for transitional/application dates; provisions phase in at different times and may have been amended.

Employment recruitment/selection AI is within Annex III's employment category when conditions are met; do not assume every AI function is automatically high-risk without examining statutory criteria and exemptions.

## 3. U.S. employment discrimination rules apply to AI-supported decisions
[Law] Title VII, 42 U.S.C. §2000e-2, prohibits certain employment discrimination; the use of a model does not remove an employer's legal duties. [Official statute](https://www.govinfo.gov/link/uscode/42/2000e-2).

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
- [Title VII, 42 U.S.C. §2000e-2](https://www.govinfo.gov/link/uscode/42/2000e-2) [law].
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) [voluntary framework, not law].
- [FTC Act §5](https://www.govinfo.gov/link/uscode/15/45) [law].

## Advanced seminar — AI Act classification and employment validation

### A. Time-aware regulatory analysis
The official EUR-Lex page for Regulation (EU) 2024/1689 points to a consolidated version dated **27 July 2026**. Before relying on any AI Act deadline, compare the operative consolidated text, amendments and transitional articles. A course based only on the original 2024 document may omit later changes.

### B. Classification workflow
1. Define feature and actual intended purpose.
2. Map provider, deployer, importer, distributor and general-purpose-model roles where applicable.
3. Assess territorial scope, prohibited practices and any Annex III categories.
4. For potential high-risk functions, check Article 6 and relevant exemptions/conditions rather than stopping at a category label.
5. Separate provider duties from deployer duties, including oversight, information and monitoring.
6. Examine phased dates, transitional provisions and amendments before specifying obligations.

### C. Employment law issue tree
**Title VII:** differentiate intentional differential treatment from facially neutral selection methods with disparate impact. For impact analysis, consider protected groups, selection rates, sample size, job relatedness/business necessity, alternative methods and local legal requirements. The mere presence of a metric is not a judicial validation of the assessment.

### D. Worked AI assessment example
A recruiting platform calls a candidate “verified” after a single uncalibrated coding test. **Potential problems:** ambiguous verification claim, unsupported psychometric validity, disparate impact, candidate data handling and downstream employer reliance. **Engineering controls:** explicitly label what is verified; separate identity/authenticity from job-performance prediction; record assessment form/model/version; require appropriately independent scientific review; implement correction/appeal workflows; prohibit opaque high-stakes automatic disqualification without legal and validation review.

### E. Exercise
Write a 1,000-word EU/U.S. comparison for a fictional AI résumé screener. Cite exact AI Act articles and Title VII section, and distinguish legal applicability, recommended risk controls and unknown facts. Do not assume NIST AI RMF is binding law.
