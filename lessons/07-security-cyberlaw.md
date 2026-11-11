# Lesson 07 — Security, unauthorized access and incident response

**Goal:** Understand where security engineering intersects legal obligations.

## 1. Security duties come from multiple places
Privacy statutes, sector-specific rules, contracts, consumer representations, litigation duties and regulator orders can all matter. No single statutory security checklist governs every U.S. startup.

## 2. Computer Fraud and Abuse Act
[Law] 18 U.S.C. §1030 addresses specified unauthorized computer-access behavior. [Official statute](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section1030&num=0&edition=prelim).

**Case holding:** *Van Buren v. United States*, 593 U.S. 374 (2021), interpreted “exceeds authorized access” in a narrower, gates-up-or-down way than the government argued: accessing information one is entitled to access does not become CFAA “exceeding authorized access” solely because it was obtained for an improper purpose. This does **not** grant blanket permission to test third-party services or bypass access restrictions. [Official Supreme Court opinion](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf).

## 3. Privacy and security representations
FTC's [Start with Security](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) extracts practical lessons from enforcement allegations: minimize collection, restrict access, enforce sensible authentication, secure service providers, and test whether systems honor privacy claims. The guidance is not itself a universal regulation.

## 4. Incident-response sequence
Detect → contain → preserve evidence → determine affected systems/data/individuals → assess jurisdictional and contractual notification duties → remediate → communicate accurately → learn. Avoid publishing a fixed “72-hour rule” as universal: GDPR Article 33 has particular timing and conditions for controllers, while U.S. state breach-notification rules differ. [GDPR Article 33](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## 5. Engineering checklist
- Threat-model identity, billing, model prompts, secrets, cross-tenant data and production backups.
- Test least privilege server-side; do not rely on UI guards.
- Manage secrets and rotate credentials; retain tamper-evident authorization logs.
- Vet SDK data collection and processor contractual obligations.
- Use a documented authorization scope for penetration tests and coordinated vulnerability disclosures.
- Establish severity thresholds and an on-call incident response decision tree.

## Hypothetical
A recruiter API accidentally lets Employer A retrieve Employer B's candidate records through an ID parameter. This is a broken-object-level-authorization vulnerability; it may trigger contract, privacy, breach-notification, and unfair/deceptive practice analysis depending on actual data exposure and applicable law.

## Exercise
Draft an incident memo containing: occurrence timeline, authorization root cause, impacted data, relevant laws/contractual duties, notices requiring counsel decision, corrective tests, and evidence preservation.

## Sources
- [18 U.S.C. §1030](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section1030&num=0&edition=prelim) [law].
- [Van Buren v. United States, Supreme Court](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf) [case holding].
- [FTC Start with Security](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) [guidance].
- [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) [law; if applicable].
