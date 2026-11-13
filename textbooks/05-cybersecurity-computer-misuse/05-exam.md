# Cybersecurity and technology-law examination (100 points)

**Scenario:** A private AI startup operating a candidate profile platform allows Employer A to view Employer B's private assessments through a changed URL ID. Its processor stores prompts for 30 days although marketing says “no logs.” A colleague says, “Report to the SEC in four days and FTC in 30 days.”

## Questions
1. **CFAA (20):** Distinguish purpose misuse from access beyond authorization. Apply §1030(a)(2), (e)(6), and *Van Buren*, identifying unknown facts.
2. **Authorization (20):** Write a least-privilege policy and five synthetic adversarial tests.
3. **Disclosure (25):** Build a law-specific notification decision matrix, avoiding invented universal deadlines.
4. **FTC and contracts (20):** Analyze representations, processor behavior and customer obligations.
5. **Evidence and critique (15):** Prepare an incident log and explain where professional legal review is needed.

## Model answers
**1:** *Van Buren* rejects treating improper purpose alone as exceeding authorization when the information area is otherwise permitted. Cross-tenant reads suggest different authorization boundaries; gather scope and mechanism evidence. Other CFAA subsections and independent laws can apply.

**2:** Verify authenticated actor, active employer status and role, tenant identity, candidate permission and current privacy revision on every sensitive read. Tests: A/B cross-read, revocation race, stale session, blocked employer, duplicated concurrent requests. A front-end filter is insufficient.

**3:** Determine jurisdiction, individuals, data categories, incident type, regulated status and exceptions. SEC public registrant Item 1.05 and FTC covered-financial-institution §314.4(j) may be **inapplicable**. State privacy and breach statutes, GDPR where applicable, and B2B contracts need separate analysis.

**4:** Verify “no logs” against model provider telemetry, contract and actual implementation; identify potential FTC §5 deception and breach of an express promise without claiming any completed liability finding.

**5:** Retain minimal tamper-resistant access evidence, timestamps, vendor notices, data map, containment steps, counsel-reviewed decisions and remediation tests.

**Scoring:** doctrine 25; missing facts 20; evidence 20; jurisdiction/timing 20; clarity 15. Scoring 85+ shows study competence, not legal certification.

**Authorities:** [18 U.S.C. §1030](https://uscode.house.gov/us/usc/119-120/t18/s1030/), [*Van Buren*](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf), [FTC Safeguards](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know), [SEC guide](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure).
