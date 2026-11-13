# Chapter 4 — Third-party processors, contracting and security evidence

## Vendor due diligence
Inventory API providers, infrastructure, analytics, email, payment, model inference, embeddings, logging and customer-support tools. Capture for each: data fields, purpose, retention, region, subprocessor chain, access rights, deletion, security representation, audit and incident notice. A provider's public marketing claim is not necessarily the executed contractual commitment.

## Example contractual conflicts
SaaS agreement: “customer content never leaves the U.S.”  
Actual model gateway: prompts are routed internationally and observability logs persist.  
**Questions:** Was the representation materially misleading? Which customer agreement version applies? Who is processor/controller? What lawful international transfer conditions are relevant? Does vendor contract authorize the observed activity?  
**Fix:** change systems and/or representations truthfully, review required DPA/data rights, and demonstrate tests.

## Authorization controls
For employer/candidate applications implement central **subject–object–action–purpose** policy checks on the server and enforce tenant isolation, revocation, session/MFA, grant scopes and immutable logs. A UI that hides a button does not prevent direct API access.

**Synthetic test suite (safe, local only):**
1. Two employers try to read each other's private candidates.
2. Revoke evidence grant concurrently with an ongoing read.
3. Block an employer before its queued introduction is delivered.
4. Revoke session and replay a token.
5. Trigger duplicate quota requests concurrently.

Do not claim “legally compliant” simply because these tests pass; they demonstrate bounded technical behavior.

## Incident evidence packet
Preserve hash-labeled logs and snapshots, role maps, access policy versions, grant history, data-flow diagram, third-party notices, legal analysis and remediation test output. Avoid retaining sensitive personal data indefinitely just for “audit” without lawful justification.

### Exercise
Draft a vendor risk schedule for model API X with customer data prompts, optional training, a 30-day retention default, and a deletion request SLA. Include five contractual questions, five engineering checks and one unresolved jurisdictional question.

**Source anchors:** [FTC §5](https://www.govinfo.gov/link/uscode/15/45); [GDPR Art. 28](https://eur-lex.europa.eu/eli/reg/2016/679/oj) when applicable; [FTC security guidance](https://www.ftc.gov/business-guidance/resources/start-security-guide-business).
