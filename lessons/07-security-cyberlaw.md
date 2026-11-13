# Lesson 07 — Security, unauthorized access and incident response

**Goal:** Understand where security engineering intersects legal obligations.

## 1. Security duties come from multiple places
Privacy statutes, sector-specific rules, contracts, consumer representations, litigation duties and regulator orders can all matter. No single statutory security checklist governs every U.S. startup.

## 2. Computer Fraud and Abuse Act
[Law] 18 U.S.C. §1030 addresses specified unauthorized computer-access behavior. [Official statute](https://www.govinfo.gov/link/uscode/18/1030).

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
- [18 U.S.C. §1030](https://www.govinfo.gov/link/uscode/18/1030) [law].
- [Van Buren v. United States, Supreme Court](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf) [case holding].
- [FTC Start with Security](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) [guidance].
- [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) [law; if applicable].

## Advanced seminar — authorized access, security and breaches

### A. CFAA close reading
18 U.S.C. §1030(a)(2) and §1030(e)(6) require careful attention to *without authorization* versus *exceeds authorized access*. In *Van Buren v. United States*, 593 U.S. 374 (2021), the Court rejected the theory that a person's misuse purpose alone converts authorized database access into “exceeding authorized access” for the relevant provision. It did not resolve every authorization issue or create universal permission to scrape/scan systems.

### B. Apply to defensive testing
Before scanning any external environment, obtain express written authorization, define systems, dates, permitted techniques, test accounts, sensitive-data handling and emergency contacts. Avoid testing production tenants without consent. Authorization engineering and legal authorization are distinct.

### C. Tenant isolation scenario
Employer A changes `/api/candidates/123` to `/api/candidates/124` and reads Employer B's data. **Root cause:** endpoint relies on object ID without verifying tenant and candidate-grant scope. **Fix:** server-side subject-object-action policy checks; transactional consent/version validation; negative cross-tenant tests; audit records; least privilege. **Legal questions:** applicable privacy statutes, affected entities, notice triggers, contractual incident definitions, regulator authority, and preservation duties.

### D. Breach-notification drill
Create a decision log with: known facts, confidence, first discovery time, actual unauthorized access, affected records and jurisdictions, encryption/key status, applicable controller/processor role, notification obligations, counsel decisions and updates. GDPR Article 33 has a qualified 72-hour controller-notification formulation; it is *not* a global notification rule.

### E. Crosswalk
FTC Start with Security: collect minimally; control access; authenticate; secure in transit/storage; monitor; vet suppliers; patch; secure devices. Map these to actual tests and owners. Label this as **regulatory guidance and sound practice**, not an enumerated universal statute.
