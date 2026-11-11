# Chapter 1 — European AI Act: scope, roles, classification and timing

## 1.1 Begin with the authoritative text
Regulation (EU) 2024/1689 has been amended. The official [consolidation dated July 27, 2026](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng) provides a practical reading view; a consolidated version is of documentary value, and the underlying legal acts determine authoritative legal effect. The [EUR-Lex official summary](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=LEGISSUM%3A4762484) reports staged application dates. Always compare Article 113 and transition rules against the applicable version.

## 1.2 Legal classification in six steps
1. **Is it an AI system?** Read Article 3 definitions. Do not equate every traditional deterministic function with an AI system.
2. **Does territorial scope apply?** Assess Article 2 facts, actors, market, and output use—not just server location.
3. **Which role?** Provider, deployer, importer, distributor or general-purpose AI model provider can bear different obligations. Outsourcing inference does not automatically remove downstream duties.
4. **Is it prohibited, high risk, transparency-scoped or otherwise regulated?** Begin Article 5, Article 6, Annex III, and Article 50, as appropriate.
5. **What requirements apply to this role and category?** High-risk examples involve Articles 9–15 (risk management, data governance, documentation, recordkeeping, transparency and oversight) and role-specific provisions; GPAI provisions have their own framework.
6. **When do they apply?** Staged effective dates and grandfather/transitional conditions matter. Avoid applying the original 2024 timetable mechanically.

## 1.3 Employment-related AI
Annex III includes categories covering AI intended for employment, worker management and access to self-employment. Under Article 6, qualifying systems can be high risk, with statutory conditions and specified exceptions. A resume-sorting system used to influence candidate selection raises a different classification question from a spelling corrector. Profiling provisions require special attention.

**Worked classification (hypothetical):** An AI hiring platform uses a foundation model to rank applicant suitability; employers rely on the score to shortlist candidates. Gather actual intended purpose, marketing, configuration, model provider contract, deployment location, decision use and evidence of oversight. Identify whether the company is provider and the employer deployer; do not label it “compliant” merely because a human can click override.

## 1.4 Correct 2026–2028 timeline discipline
As reflected in the current official EUR-Lex summary, some AI Act obligations applied in 2025, others in 2026, and Annex III high-risk requirements apply **from December 2, 2027**, with product-related Annex I high-risk requirements **from August 2, 2028**. Read the law and its amendments for specific exceptions and any changes after the snapshot date. Do not use the old “all high-risk obligations August 2026” shorthand.

## 1.5 Documentation for a model or agent
Maintain intended use, foreseeable misuse, training/evaluation provenance, model/version registry, performance and subgroup limitations, human oversight design, change control, incident and monitoring records, downstream instructions, and clear responsibility mapping. These are often sensible controls even when not each individually compelled for an unregulated use case.

### Exercise and analysis
**Q:** A U.S. company serves only U.S. customers but its site is reachable from Spain. Is its AI automatically in the Act's scope?  
**Answer:** No automatic conclusion from internet reachability. Investigate whether the system is placed on the EU market, put into service there, or outputs are used in the EU, and the relevant Article 2 rules.

**Q:** Does using a third-party model API necessarily mean the app developer has no provider duties?  
**Answer:** No. Determine the roles and legal definitions given system design, purpose, placement and branding.

**Sources:** [EU AI Act consolidated text](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng); [EUR-Lex summary](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=LEGISSUM%3A4762484).
