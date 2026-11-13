# Milestone 21A — Washington biometric law, compared with Illinois and Texas

**Reviewed:** November 13, 2026. **Scope:** Washington RCW chapter 19.375, with limited comparative references to the Illinois BIPA and Texas commercial-biometric collection statute. **Purpose:** original educational research and hypotheticals; not legal advice, a licensed citator, or an audit of any live biometric product.

## 1. Start with the actual defined *enrollment* and *commercial purpose*

The [Washington Legislature's **RCW 19.375.010**](https://app.leg.wa.gov/RCW/default.aspx?cite=19.375.010) defines **biometric identifier** as qualifying automatic measurements of individual biological characteristics *used to identify a specific person*. Examples include a fingerprint, voiceprint, retina or iris pattern. Its definition expressly **excludes** photographs, video and audio recordings *and data generated from them*, plus specified HIPAA information. Such exclusions are **Washington-specific**: do not copy them into Illinois or federal COPPA analysis.

An **enrollment** under **RCW 19.375.010(5)** means capturing an identifier, creating a reference template that cannot be reconstructed into the original output image, and keeping that template in a database that matches it to a specific individual. **Commercial purpose** is narrower than "any business use": **§19.375.010(4)** focuses on selling/disclosing the identifier to a third party to market unrelated goods or services; security and law-enforcement purposes are expressly excluded.

**Important negative inference:** an ordinary login anti-fraud system, a video file, a face-identification database and an advertiser's biometric match list cannot all be given the same RCW 19.375 coverage label without assessing purpose, technical representation, data category and statutory exclusions. Do not interpret this as a blanket privacy exemption under every other law.

## 2. Washington §19.375.020: what the enacted rule actually says

| Provision | Legal question | Teaching / implementation takeaway |
|---|---|---|
| **§19.375.020(1)–(2)** | Before enrolling an identifier in a database for a **commercial purpose**, has the person **given notice, obtained consent, *or* provided a mechanism preventing subsequent commercial use**? | These are **statutory alternatives**, not a universal BIPA-style rule requiring affirmative written release in all Washington cases. The notice and context-dependent consent analysis differs from Illinois law. |
| **§19.375.020(3)** | Was the identifier later sold, leased or disclosed commercially without consent? Does an enumerated exception apply? | Review service/transaction necessity, court/statutory authorization, contractual no-redisclosure promise, legal process and subsection consistency; do **not** teach "all sharing prohibited." |
| **§19.375.020(4)** | Are reasonable protective measures and a purpose-limited retention period in place for qualifying commercial-enrollment records? | Maintain protection and retention evidence; statutory exceptions include courts/law, fraud/security/claims and providing original services. There is **no universal fixed 30-day biometric purge rule** here. |
| **§19.375.020(5)** | Is a new use materially inconsistent with the original terms? | Consent may be required for the new commercial use or disclosure terms; keep purpose/version provenance. |
| **§19.375.020(6)–(7)** | Has an identifier been **unenrolled**? Is the activity performed for a defined **security purpose**? | Disclosure and retention limitations address unenrolled data differently; the section expressly does not require notice/consent for security-purpose collection/capture/enrollment. Do not turn this into permission to ignore every security, privacy or other statute. |

The law's [§19.375.040](https://app.leg.wa.gov/RCW/default.aspx?cite=19.375.040) also contains GLBA financial-institution and HIPAA-related exceptions. Its [§19.375.030(2)](https://app.leg.wa.gov/RCW/default.aspx?cite=19.375.030) says **only the Washington Attorney General** may enforce this chapter using the Consumer Protection Act. Do not advertise an Illinois-style private BIPA damages claim as a remedy under Washington RCW 19.375.

## 3. Compare three states without importing one state's rule into another

| Dimension | Washington (RCW 19.375) | Illinois (740 ILCS 14) | Texas (Bus. & Com. Code 503.001) |
|---|---|---|---|
| Core activation | Defined *commercial-purpose enrollment* and specified subsequent activity | Covered biometric identifier/information collection, possession and disclosure | Capture/use of defined biometric identifier for a *commercial purpose*, subject to exceptions |
| Initial notice/consent | **Notice, consent, or a prevention mechanism** in §.020(1), contextual detail | **Written notice and release** conditions in §15 for covered collection; 2024 e-signature amendment | Specified notice and consent framework; 2026 AI development/training/evaluation exclusions may apply subject to later identification use |
| Legal remedies | **Washington Attorney General only** under §.030(2) | Private right of action under §20, as amended by **P.A. 103-769** | Texas AG enforcement; do not imply Illinois BIPA private remedies |
| AI/biometrics overlap | Photograph/audio/video and derivative exclusion in chapter definition, narrow commercial purpose | Different statutory definitions; data derived from an image may require separate treatment | 2026 specific exceptions and *subsequent commercial use* rules under §503.001(e)–(f) |

Sources: [WA definitions](https://app.leg.wa.gov/RCW/default.aspx?cite=19.375.010), [WA duties](https://app.leg.wa.gov/RCW/default.aspx?cite=19.375.020), [WA AG enforcement](https://app.leg.wa.gov/RCW/default.aspx?cite=19.375.030), [Illinois BIPA](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004), [IL 2024 amendment](https://www.ilga.gov/Legislation/publicacts/view/103-0769), [TX §503.001](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.503.htm#503.001).

## 4. Technical product scenarios (hypothetical)

**Voice authentication:** A SaaS login system extracts speaker embeddings. Determine whether an identifier is generated by automatic measurement, used to identify a person, and *enrolled* into the specified irreversible-reference template system; ask whether its purpose is security or commercial sharing. Even when Washington's security-purpose exception applies, other jurisdictions and laws may not provide identical coverage.

**Biometric ad targeting:** A game collects users' face-derived templates and shares matching identifiers with an advertising network for unrelated product recommendations. Investigate whether Washington's **photograph/derivative exclusion** is implicated, what technology actually produces and stores, how the service uses it to identify individuals, and whether the data was enrolled commercially. Then independently test Illinois/Texas definitions and rules; do not automatically classify every feature from its marketing description.

**Identity and credentials:** An employment assessment can sign and authenticate a credential without legally establishing that a faceprint's collection was lawful or that the score was scientifically validated for the job. Keep claims of authenticity, legal permission, fairness and accreditation separate.

## 5. 100-point assignment

Prepare (a) a **data-category/technical-enrollment table** (20 points), (b) actor and purpose analysis including commercial/security use (20), (c) the *actual* Washington statutory notice/consent/prevention alternatives and transfer exceptions (20), (d) Illinois/Texas distinction and enforcement (20), and (e) evidence: consent versions, process purpose, retention, vendor downstream instructions, protected storage and unknown legal facts (20).

**Limitations / source receipt:** Targeted RCW 19.375.010, .020, .030 and .040 official texts inspected November 13, 2026, and existing curated IL/TX primary references. No complete 2026 legislative-amendment sweep, case-history verification, other state survey, privacy counsel opinion or actual biometric system examination. See [Milestone 21 source audit](../../quality/MILESTONE21_BIOMETRIC_AUDIT_2026-11-13.md).