# Chapter 4 — Software liability, privacy promises and breach response

## 1. Multiple legal theories may coexist
A flawed AI service can raise (a) breach of a contract promise, (b) deceptive/unfair practice, (c) negligence or other tort questions under applicable state law, (d) statutory privacy/security duties, and (e) third-party IP claims. But an incident does **not** automatically prove each cause of action; element, standing, damage, causation, exclusions and remedies differ.

## 2. FTC claims and consent proceedings
[15 U.S.C. §45](https://www.govinfo.gov/link/uscode/15/45) is an important federal unfair/deceptive-practices source. [*In re Everalbum*, FTC File No. 192-3172](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter) resulted in a consent resolution around alleged facial-recognition and deletion representations. **Status:** agency complaint allegations and respondent-specific consent duties, **not** universal judicial holdings.

## 3. Security control evidence
Consider access authorization, tenant isolation, secret management, backups, subprocessor controls, software supply chain, vulnerability response, disaster recovery, audit logging and incident escalation. The [FTC Start with Security guide](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) is agency guidance derived from enforcement experience, not a universal statute.

## 4. Incidents: notification depends on jurisdiction
A privacy/security incident requires: preserve evidence; bound the data and actor set; contain; identify controllers/processors and contracts; classify applicable state/federal/EU notification standards; compare deadlines and exceptions; communicate accurately. The GDPR Article 33 **qualified 72-hour** supervisory-authority notification rule may apply to controllers in specified circumstances, but is not a universal U.S. deadline.

## 5. Example: AI gateway cross-tenant leak
A user changes a numeric URL to retrieve another customer's private prompts. Analyze server-side authorization and exposure; check misleading “isolated tenant” claims; examine DPA and privacy notice; identify breach-law triggers; assign forensic remediation. A terms-of-service “use at your own risk” clause cannot by itself prove this is lawful.

## 6. Liability-cap red teaming
For each limitation clause, test:
- What claims fall inside/outside definition of “claims”?
- Does the cap aggregate across parties and 12-month periods?
- Do indemnity, confidentiality, data protection and deliberate wrongdoing have carveouts?
- Are statutory remedies waivable?
- Is mandatory consumer law applicable?
- Is there sufficient consideration, notice and assent?

**Exercise:** Draft a 1,000-word factual incident memo that compares contract duties, FTC representations and possible privacy notification. Use provisional language, not “automatically liable.”

**Sources:** [FTC Act](https://www.govinfo.gov/link/uscode/15/45), [FTC Everalbum](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter), [FTC security guidance](https://www.ftc.gov/business-guidance/resources/start-security-guide-business), [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
