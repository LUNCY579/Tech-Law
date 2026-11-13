# EU AI Act: the enacted 2026 Digital Omnibus amendment

**As of:** 2026-11-13. This is a current-law supplement to [Textbook II](../../textbooks/02-ai-regulation-privacy/01-ai-act.md) and [Textbook VII](../../textbooks/07-international-technology-law/03-eu-ai-dsa.md).

## What changed

[Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1744), adopted July 8 and published July 24, 2026, is an **enacted regulation in force**, not merely an unpassed policy proposal. It amends the original [AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1689), among other acts. EUR-Lex lists the **July 27, 2026 consolidated version**. Read the consolidation for navigation and the underlying regulations for formal legal effect.

The [European Commission's implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline) states:
- **February 2, 2025:** the initial AI Act general provisions and specified prohibited practices began.
- **August 2, 2025:** general-purpose AI model provisions began, subject to transition rules.
- **August 2, 2026:** many other provisions, including specified transparency obligations, began.
- **December 2, 2026:** new specified prohibited-practice provisions and transition for certain existing synthetic-content generators.
- **December 2, 2027:** the amended timing for Annex III high-risk systems.
- **August 2, 2028:** the amended timing for Annex I regulated-product high-risk systems.

**Do not** use the original 2024 act's unamended date table or a blanket slogan that all high-risk systems were fully subject to their rules in August 2026. A scheduled date is not a conclusion about how transition provisions treat a particular pre-existing system.

## Four legal questions before engineering changes

1. **Territorial reach (Article 2):** EU market placement, putting into service, deployer location and output use must be assessed factually.
2. **Role (Article 3 and role provisions):** system provider, model provider, deployer, importer and distributor may have different requirements. A U.S. startup's use of a third-party GPAI API does not automatically eliminate its own role.
3. **Classification (Articles 5–6, Annex III, Article 50):** ordinary content assistance, candidate ranking, biometric identification and certain synthetic-content functions are legally different products.
4. **Applicable version and transition (Articles 111, 113, Regulation 2026/1744):** record source version, first placement date, substantial modification, affected provisions and enforcement stage.

**Hypothetical:** A U.S. vendor sells an applicant-ranking platform to employers established in the EU. The vendor should evaluate Annex III employment categories, Article 6 exceptions, provider/deployer roles, documentation, transparency, oversight, model lifecycle and the amended application date. The answer cannot be derived just from a model's parameter count or the fact that a human sees its score.

**Training exercise:** Write a two-column memo comparing a public-domain article summarizer with a high-impact recruitment scoring engine. Explain why the same underlying model can support distinct system classifications and duties.

**Evidence status:** primary enacted EU regulation and Commission explanatory timeline checked. Not a country-by-country transposition, conformity-assessment determination, product certification or legal opinion.