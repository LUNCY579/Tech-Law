# Milestone 19B — Oregon automated license-plate readers: agency and vendor law

**As-of:** November 13, 2026. **Primary law:** [**Oregon Laws 2026, chapter 77 (SB 1516), §§3–9**](https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2026orLaw0077.pdf), **effective March 31, 2026** under the Act's emergency provision, §14. This is **sector-specific public-safety technology/data law**, not an amendment to the general Oregon Consumer Privacy Act (**ORS 646A.570–646A.589**). Educational analysis, not a legal opinion or engineering certification.

The official 11-page enactment's **pp. 2–5 and 11** were inspected as page images. See [source audit](../../quality/MILESTONE19_OREGON_ALPR_SOURCE_AUDIT.md).

## 1. What data and which actors?

Under **§3(3)–(4)**, an automated license-plate recognition system (ALPR) combines cameras and algorithms to convert license plates or other vehicle characteristics to machine-readable data; captured data includes coordinates, timestamps, video, photos, plates, vehicle details and related information. The statute expressly excludes certain traffic-signal/photographic radar systems.

Separate **law-enforcement agencies**, **authorized agency users**, **contracted vendors**, and **other government recipients**. Do not assume a private mobile game with user-submitted vehicle pictures is automatically a government ALPR vendor. Actual contracted service and statutory definitions determine coverage.

## 2. Agency collection, querying and retention — §4

- **Authorized purposes (§4(1)–(2)):** the law constrains agency ALPR use to defined tasks including qualifying crime-related, warrant, missing-person, uninsured/unregistered vehicle, parking-facility and secure-access functions. These are not unlimited statewide surveillance permissions.
- **Retention (§4(3)):** captured data **not related to court proceedings or ongoing criminal investigations** may generally be kept **no more than 30 days after collection**. Related data can follow the normal evidence-retention period; **audit information** has a distinct treatment under §4(3)(c).
- **Search records (§4(5)):** log authorized user identifier, agency, search input, date/time, relevant reference number, purpose and crime category where applicable.
- **Human verification (§4(6)):** before a traffic stop based on an alert, an officer/authorized user must visually confirm plate, issuing state and other vehicle attributes and comply with policy/law.
- **Sharing (§5):** limited other-agency queries and tightly constrained sharing; certain out-of-state/federal recipients may get relevant data for an authorized purpose without unrestricted ongoing access. Court-process exceptions may apply.

**Hypothetical:** A contractor proposes indefinite vehicle-location retention to “improve the model.” This conflicts with the default 30-day rule for noninvestigative/noncourt data and with agency purpose/vendor restrictions if the statute applies. An analytics objective does not itself create an exception.

## 3. Contractor and vendor obligations — §§6–9

| Provision | Statutory subject | Engineering/legal review question |
|---|---|---|
| **§6(1)** | Vendors provide **monthly searchable system audits**, including cameras/devices, fixed locations, searches, agencies with access, alerts, unique vehicles and selected search-log data | Can monthly exports be reproduced and reconciled without over-disclosing personal information? |
| **§6(2)** | Vendors provide **quarterly searchable audits** concerning queries made on behalf of other government entities | Is external-agency query provenance preserved? |
| **§6(3)** | Agencies publish audit results **within 2 days** of receiving them, or require vendors to provide public access, subject to the referenced disclosure limitations | Publication is subject to redactions; do not expose personally identifiable plate information in an open dashboard |
| **§7(1)–(2)** | Agencies publish policies for use, storage, access, retention and destruction; vendor contracts must contain specified provisions | Map policies and controller approvals to contract versions and actual security evidence |
| **§7(2)(e)** | Captured data is **agency property**; vendor redirects data-access requests to owner agency; minimum **end-to-end encryption**, **CJIS** requirements, audit rights and prompt security incident notification | A generic SaaS DPA or “encrypted at rest” badge does not demonstrate all specified duties |
| **§9(1)** | Contractor-vendor may not access, disclose, sell, share or otherwise use captured data except narrow **agency-consented technical support** and specified audit delivery | A broad AI model-training reuse clause must be reviewed against the statutory prohibition |
| **§9(2)–(4)** | Intentional/grossly negligent prohibited access/use supports an **individual damages/equitable-relief** action; injunctive action has a separately described scope, and this section states exclusivity | Do not imply strict damages liability for every ordinary software defect |

**Transition (§8):** pre-effective-date vendor contracts have a limited grandfathering mechanism until expiration, but agency compliance with **§4** still applies regardless of contract date; extensions, renewals and new contracts must satisfy the law's specified requirements.

## 4. Founder architecture and implementation evidence

A cloud vendor serving Oregon police should retain a **purpose-limited security and contracts dossier**, including: customer agency registry and contracts; authorized-account identities; hot-list provenance and update cadence; each query's legal purpose and timestamp; default TTL and preservation holds; encryption configuration and key custody; CJIS evidence; incident timelines; technical-support consent; audit exports with controlled redaction; subcontractor access; renewal/version matrix; and approval and retention evidence.

**Do not create a public dashboard containing raw plate histories or identify real individuals in coursework.** Use synthetic identifiers in practice systems.

## 5. Applied graded exercise

**Scenario:** A vendor hosts ALPR data for an Oregon agency and would like to (i) retain all coordinates for 180 days, (ii) use raw data to improve a commercial AI recognition model, (iii) permit a federal agency to query every plate without agency mediation, and (iv) publish raw monthly logs. The existing contract was signed in February 2026.

**Model issue map:** (i) §4(3) default versus qualifying investigation/court evidence; (ii) §7(2)(e) and §9(1) restrictions, limited consented technical support; (iii) §5 access purpose, bounded disclosure and contract access routing; (iv) §6(3) audit transparency plus protected PII; (v) §8 existing-contract transition does **not** exempt agency §4 duties. Whether the precise arrangement is unlawful requires actual contract, deployment and evidence review.

**Rubric (100 points):** role and system definition 20; purpose/retention 25; §5 sharing and logs 20; §§6–9 vendor/audit contract controls 25; exceptions, transition and source/currentness 10.

## Scope and evidence limitations

Verified from Oregon's enacted law and official bill record for the stated sections and effective date. **Not** reviewed exhaustively: any later administrative rule, local agency policy, actual CJIS technical conformance, litigation outcomes, every contract transition condition, or all other Oregon privacy laws. This source remains legally distinct from the [Oregon OCPA and 2026 chapter 96 analysis](10-oregon-session-law-reconciliation.md).