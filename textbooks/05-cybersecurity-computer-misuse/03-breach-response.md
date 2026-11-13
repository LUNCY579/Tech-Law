# Chapter 3 — Data breaches: classification, evidence and notification

## Step 1: preserve and contain
Document incident detection time, affected systems, scope, logs, key state, access paths, containment and forensic integrity. Avoid prematurely deleting evidence or emailing sensitive records to broad distribution lists.

## Step 2: classify whether the law is triggered
Ask **which data** (personal, health, financial, credentials), **whose data** (states/countries, customers/employees), **which actor** (controller, processor, covered financial institution, registrant), **what incident** (access, acquisition, disclosure, loss of availability), **how many** people, and what exceptions apply. A security bug by itself is not always a legally reportable breach.

## Step 3: evaluate separate reporting tracks

| Possible framework | Trigger to investigate | Time rule |
|---|---|---|
| GDPR Art. 33 | Applicable controller's personal data breach, risk threshold and awareness | Generally without undue delay and where feasible within 72 hours, with statutory qualifications |
| GDPR Art. 34 | High risk to individuals | Communication without undue delay, with exceptions |
| FTC Safeguards, 16 CFR §314.4(j) | Covered financial institution; specified 500-person unencrypted information notification event | No later than 30 days after discovery |
| SEC Form 8-K Item 1.05 | Covered domestic public registrant; material cyber incident | Generally four business days after materiality determination, subject to legal delay process |
| U.S. state breach statutes | Residency, covered data, acquisition and other statutory conditions | Jurisdiction-specific |
| B2B contracts / DPAs | Negotiated incident definition, recipient and notice clock | Contract-specific |

[GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj); [FTC guide](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know); [SEC guide](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure).

## Step 4: decision log
Record event ID, detection and discovery timestamps, attorney contact, affected subjects, jurisdictions, impacted secrets/keys, exfiltration evidence, legal theory, notification deadline **if actually applicable**, notices sent, ongoing updates and remediation evidence.

## Six-state breach research supplement (Milestone 16)

The [primary-source comparison of California, Texas, Illinois, Massachusetts, Washington and Florida](../../research/2026-11-13/03-breach-notifications.md) and its [normalized recipient-specific matrix](../../research/2026-11-13/breach-obligations.csv) distinguish **the date of discovery from a later legal determination**, residents from regulators, and `more than 500` from `500 or more`. The [casebook](../../research/2026-11-13/07-breach-timeline-casebook.md) includes exercises at 250, 500 and 501 affected residents.

These notes are **not** a general state-law notice deadline calculator. The analysis still requires the operative statute for the actual incident date, covered data/actors, exceptions and counsel review.

## Hypothetical
An AI recruiting platform leaks 300 California candidate CVs to another tenant; a worker notices the problem on Tuesday. No universal notice time can be inferred from “300” or “Tuesday.” Classify data and incident under applicable California law, relevant contracts, FTC claims and other statutes. Do not automatically apply a financial-institution 500-person threshold or a public issuer's Form 8-K deadline.

## Exercise / answer
**Question:** Is a 72-hour timer always triggered by every U.S. software security event?  
**Answer:** No. GDPR Art. 33 has territorial/material and risk conditions, and other laws have separate triggers. Start with actual facts and legally relevant jurisdiction.
