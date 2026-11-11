# Chapter 2 — Security standards, binding rules and regulatory authority

## 1. Three categories
1. **Generally useful engineering practices**: risk assessments, least privilege, encryption, monitoring, backups and testing.
2. **Contractual requirements**: customer MSAs/DPAs, vendor commitments, cloud-security schedules and sector-specific contracts.
3. **Potential binding legal duties**: requirements triggered by the organization, data, jurisdiction and industry.

A compliance checklist should record the **trigger** before citing a regulation.

## 2. FTC Act §5
[15 U.S.C. §45](https://www.govinfo.gov/link/uscode/15/45) prohibits unfair or deceptive practices in specified commerce. Security promises inconsistent with actual practices can raise deception questions; inadequate security can raise unfairness issues where statutory elements are satisfied. [FTC Start with Security](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) is official guidance informed by enforcement matters, **not** a generally applicable security regulation.

**Hypothetical:** “All uploads are end-to-end encrypted” is advertised while servers routinely decrypt and retain documents. Examine the precise marketing representation, architectural facts, user expectations, and FTC jurisdiction. The mere presence of TLS does not prove end-to-end encryption.

## 3. FTC Safeguards Rule
[16 CFR Part 314](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314) applies to **covered financial institutions** subject to the FTC's jurisdiction, not all software companies. The covered organization must have a written information-security program appropriate to its size, activities and sensitivity. Rule text and exceptions should govern the particular analysis. [Official FTC explanation](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know).

**Incident duty:** §314.4(j) calls for notification to the FTC upon qualifying unauthorized acquisition of at least 500 consumers' unencrypted information, **as soon as possible and no later than 30 days after discovery**. “Unencrypted” can include data where an encryption key was accessed. This is **not** a general 30-day rule for every startup.

## 4. Public company disclosure
The SEC's 2023 cybersecurity rules generally require a **covered public-company domestic registrant** to file a material cybersecurity incident report on Form 8-K Item 1.05 **within four business days of determining materiality**, subject to defined delay provisions; the deadline is **not measured from discovery**. [Official SEC guide](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure). A typical newly formed private startup is not automatically an SEC registrant subject to that rule.

## 5. Voluntary frameworks
[NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) is a valuable risk management tool; framework alignment should not be represented as regulatory certification. Contracts and specific laws can incorporate external standards, so check the actual text.

## Exam
A private productivity SaaS suffers a database leak. Founder claims it must notify the SEC within four business days and FTC within 30 days. **Model answer:** The two cited obligations have specific regulated-actor and event triggers; establish registrant status and financial-institution scope before asserting deadlines, then investigate actually applicable state, federal, international and contractual duties.
