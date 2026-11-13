# Chapter 5 — Building a defensible compliance architecture

## 5.1 Separate a legal applicability map from a security checklist
Create **two artifacts**:
1. **Obligation register:** law/article, jurisdiction, controller/provider/deployer role, trigger, exemptions, operative date, interpretation, owner, counsel decision.
2. **Evidence register:** design document, test name, control ID, code/version/commit, audit results, production telemetry, reviewer, remediation date.

Security best practices can be valuable without being imposed by a particular article. A legal citation alone does not demonstrate the product meets the cited rule.

## 5.2 Reference system design for candidate AI assessments
**Data:** candidate account → uploaded material → processing grant → versioned assessment form → model/rubric → result → verifier signature → publication consent → restricted employer access → deletion/revocation pipeline.

**Threats:** employer enumeration, cross-tenant access, stale candidate grant, weak signed-score binding, model drift, unsupported validity claim, vendor data retention, automated exclusion, unfair adverse outcomes.

**Controls and proof:**
| Control | Proof |
|---|---|
| Server-side tenant scope | adversarial 2-candidate/2-employer authorization tests |
| Versioned form/rubric/model | release hashes and signed evidence |
| Explicit candidate grant | permission revision and revocation tests |
| Meaningful human review | reviewer workflow and audit trail |
| Outcome analysis | prespecified subgroup/validity evaluation |
| Truthful public claims | claim registry linked to evaluation |
| Deletion | complete inventory + processor/backup tests |
| Legal date gate | dated applicability and obligations register |

## 5.3 Five-part product hypothetical
A U.S. company markets AI scoring to EU and California employers. It uses a third-party model, automatically rejects bottom-ranked candidates, stores CVs indefinitely and calls every score “scientifically certified.”

**Issue-spotting answer:**
1. **EU:** Article 2 territorial facts, AI Act Article 6/Annex III employment classification, current staged obligations, GDPR Articles 3/6/22 and other provisions.
2. **California:** CCPA covered-business determination and 2026–2027 ADMT obligations, including which company actually makes the significant decision.
3. **Federal U.S.:** FTC representation substantiation; Title VII discriminatory treatment and impact analysis.
4. **Contract/security:** processor/vendor retention, candidate publication consent, authorization boundaries, deletion mechanisms.
5. **Evidence:** validation study, true/false claims, model card, audit logs, consent and revocation tests.

**Counterargument:** Some laws may not apply because of territorial scope, covered-business threshold, role, actual decision type, or exemptions. That is a fact-finding step, not a blanket exemption.

## 5.4 Graduating exercise (100 points)
- 20: Write a 2-page jurisdiction/role map.
- 20: Analyze GDPR Art. 6 and Art. 22 for a real decision use.
- 20: Determine AI Act category and current phased applicability with pinpoint cites.
- 15: Analyze CPPA risk assessment/ADMT timing and covered-business status.
- 15: Draft an FTC/Title VII claim and validation risk memo.
- 10: Produce a 20-control engineering evidence matrix.

**Passing:** 85 shows solid course understanding, not independent legal qualification. Legal counsel remains necessary for real high-stakes hiring deployment.

## 5.5 Source updates
Before using this work for launch, re-open the [AI Act 2026 consolidation](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [CPPA final regulations](https://cppa.ca.gov/regulations/ccpa_updates), [FTC §5](https://www.govinfo.gov/link/uscode/15/45) and [Title VII](https://www.govinfo.gov/link/uscode/42/2000e-2). Check whether a later act, regulation, order or case changes the analysis.
