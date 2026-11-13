# Chapter 4 — U.S. consumer protection and automated hiring

## 4.1 FTC Act: claims must match evidence
The FTC Act §5 (15 U.S.C. §45) addresses unfair and deceptive practices in commerce. “Fully unbiased AI,” “never trains on data” and “99% accurate” are testable marketing or product claims; their materiality, net impression, substantiation and truth matter. Evaluate deception separately from statutory unfairness analysis under §45(n).

**Source:** [15 U.S.C. §45](https://www.govinfo.gov/link/uscode/15/45).

## 4.2 Case example — Everalbum is a consent order, not litigated law
In *In re Everalbum*, FTC File 192-3172, the FTC alleged misleading practices concerning face recognition and deletion; a 2021 **administrative consent order** imposed respondent-specific obligations. An order is legally significant but does not establish a broad judicial holding that all AI models trained on deleted personal data must always be erased.

**Official source:** [FTC proceeding and order](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter).

## 4.3 Children’s personal information: FTC COPPA amendments

The [FTC's 2025 final COPPA Rule (16 CFR part 312)](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm) became effective June 23, 2025; most amended obligations had an April 22, 2026 compliance date, with earlier safe-harbor dates. The [supplemental children's-privacy study](../../research/2026-11-13/13-coppa-2026-children-and-games.md) addresses child-directed and knowingly under-13 services, separate verifiable parental consent for certain third-party disclosures, added biometric and government identifiers, purpose-limited retention, and security requirements. Scope, permitted exceptions, actual service and parent/vendor consent processes must be verified. A video-game feature is not automatically compliant merely because the account age field says 13 or because no names are collected.

## 4.4 Employment law and algorithmic assessment
**Title VII, 42 U.S.C. §2000e-2** prohibits specified employment discrimination, including in hiring. Distinguish **disparate treatment** (intentional discrimination) and **disparate impact** (facially neutral practice with disproportionate impact subject to governing standards). Test job relevance and statistical adequacy rather than assuming a model that passes a benchmark is validated for employment selection. Employment law can apply to use of a vendor tool even when the vendor writes “experimental” in a model card.

**Source:** [42 U.S.C. §2000e-2](https://www.govinfo.gov/link/uscode/42/2000e-2).

## 4.5 Actual measured validity vs credential authenticity
An exam can produce an authentic score without proving the score predicts job performance. Distinguish:
- Identity verification: person is the test-taker.
- Instrument integrity: form and grading evidence were not altered.
- Psychometric validity: assessment measures the intended construct for a population.
- Job-related validity: the measure supports the relevant hiring decision under applicable standards.
- Fairness: subgroup outcomes, reasonable accommodations, alternatives and ongoing monitoring.

**Example:** A coding-assessment portal can credibly say “the score was signed by our verifier” while being unable to say “score predicts success across all software jobs.” The latter needs separate validity evidence.

## 4.6 FTC and employment incident review
If an employer sees a “bias-free” badge while the underlying model was never validated, possible issues include misleading marketing, downstream employer reliance, discrimination risks, contract disputes and privacy. Different authorities impose different requirements, and liability is not established just by identifying the possibility.

### Assessment
**Q1:** A founder says “the test is fair because the model was instructed not to discriminate.”  
**Model answer:** A prompt is not validation. Require job-relevance evidence, subgroup analysis, accommodation review, intended-use boundaries and independent testing where appropriate.

**Q2:** Does Everalbum establish a statute requiring every facial recognition system to delete all derived models?  
**Answer:** No; it is a consent settlement with party-specific obligations, while other statutes or contracts might create separate obligations.

**References:** [FTC §5](https://www.govinfo.gov/link/uscode/15/45), [Everalbum docket](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter), [Title VII](https://www.govinfo.gov/link/uscode/42/2000e-2).
