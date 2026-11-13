# Milestone 20A — Children's privacy: 2025 amended COPPA Rule operative in 2026

**Review date:** November 13, 2026. **Source type:** enacted U.S. federal agency rule, not merely a proposal. **Purpose:** original technology-law teaching and practical issue spotting for games, education, social features and child-directed AI. **Not legal advice or a product compliance signoff.**

## 1. Start from the actual 2025 final rule and timing

The FTC's [2025 COPPA Rule amendments, 90 Fed. Reg. 16918 (April 22, 2025), FR Doc. 2025-05904](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm), amended **16 CFR part 312** under the [Children's Online Privacy Protection Act, 15 U.S.C. §§6501–6506](https://www.govinfo.gov/link/uscode/15/6501). The final rule states **effective June 23, 2025**; except for specified safe-harbor provisions in **§312.11(d)(1), (d)(4) and (g)** with earlier compliance dates, covered entities had until **April 22, 2026** to comply. Both dates were past as of this review. Do not mistake the proposed 2024 NPRM for the binding final 2025 amended text, and do not teach 2026 as if all duties only *start* then.

**Applicability is conditional.** COPPA primarily governs operators of child-directed websites/online services and operators with actual knowledge they collect personal information from children **under 13**. A mixed-audience product can raise different age-screening and consent issues than a general-audience platform. Examine operator role, targeting/actual knowledge, service design, collection and rule exceptions—not just a privacy-policy sentence saying users must be 13.

## 2. Material amendments and engineering implications

| Legal provision | Targeted legal rule | Evidence to collect |
|---|---|---|
| **§312.2** | Amended definitions cover more forms of **personal information**, including government-issued identifiers and biometric identifiers that can be used for automated or semi-automated recognition; the final rule introduces a **mixed-audience** definition | Inventory face/voice templates and biometric identifiers separately from ordinary profile labels; map exact collection and recognition use |
| **§312.4** | Required direct and online parental notices, including disclosures concerning purposes, data practices and third-party disclosures; amendments address online disclosure and retention policy | Versioned notices and rendering screenshots, named categories of recipients, purpose and retention-policy links |
| **§312.5(a)(2)** | A separate verifiable parental consent requirement for disclosure of children's personal information to third parties **unless disclosure is integral to the nature of the service**; a parent can consent to collection/use without automatically authorizing non-integral disclosure | Independently versioned third-party-disclosure consent, exception analysis, refusal path and vendor-specific transfer trace |
| **§312.6** | Parents have rights to review and request deletion and to prevent further use or collection, subject to rule conditions | Authenticated parental request process, deletion propagation evidence and exception log |
| **§312.7** | Do not condition a child participating on more personal information than reasonably necessary | Data minimization table by feature, optional vs necessary collection |
| **§312.8** | Covered operators must establish and maintain reasonable security measures; security program and written safeguards strengthened by the amendments | Access control, risk assessment, vendor/security controls, incident log and review ownership |
| **§312.10** | Retain covered child information only for the time reasonably necessary for the specific collection purpose; **indefinite retention is not permitted**. Maintain a written retention policy addressing purpose, business need and deletion timeframe | Data-by-data retention schedule and tested deletion/backup lifecycle |

**Source distinction:** The [FTC announcement](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data) is **official explanatory material**. The Federal Register **final rule text** is the regulatory source for legal requirements and exceptions. An FTC announcement may summarize but does not replace the operative section.

## 3. Important rulemaking negatives

The FTC **did not finalize** all ideas from its 2024 proposal. The 2025 final-rule explanation expressly says it deferred particular proposed new school/education-technology authorization provisions while considering possible FERPA-rule changes. It also did not finalize every proposed push-notification limitation. Do **not** list those unadopted provisions as 2026 binding text, or assume schools can authorize unlimited child-data commercialization without examining current law and guidance.

**Milestone 21 court and state-law update:** COPPA's **under-13** federal operator standard is separate from state youth-platform laws and court injunctions. Read the [California AADC 2026 replacement / Texas SCOPE en banc source clinic](16-child-online-safety-and-injunctions-2026.md), particularly **California AB2246's proposed Jan. 2027 legal period** and the **October 28 Fifth Circuit vacatur of its July panel**. An appellate decision about the *old* California code does not decide the *replacement*, and a vacated panel opinion does not currently control Texas HB18 disputes.

**Other laws remain separate:** COPPA is not the same as state minors' social-media laws, state biometric privacy acts, the EU GDPR child-consent rules, or US FERPA obligations for covered educational institutions. A child aged **13–17** is not automatically under COPPA's under-13 core rule; their information can still be protected by other laws.

## 4. Worked hypothetical — multiplayer game with AI voice features

A US game company lets users post voice snippets, enter chat, purchase cosmetic items, and enable optional third-party personalized ads. One audience segment is under 13.

**Questions:** Is the operator child-directed, mixed-audience, or knowingly processing under-13 data? Is a voice snippet used only to fulfill a discrete voice command, converted to a biometric recognition template, or shared with a model/advertising vendor? Is disclosure integral to the game, or optional tracking requiring **separate verifiable parental consent**? What is the shortest appropriate purpose-specific retention period? How can a parent ask for review and deletion, including processors?

**Model answer (issue map):** First determine Rule coverage and exact §312.2 definitions. Classify audio, persistent identifiers, face/voice recognition, ads and public sharing separately. For an applicable non-integral third-party disclosure, evaluate §312.5(a)(2) and record affirmative parental consent separately from core gameplay consent. Keep parent notice, specific purposes, vendors, retention limits, deletion controls, security program and exceptions as versioned evidence. Never treat “all users clicked a Terms link” as proof of parental consent.

## 5. Evidence-centered study assignment (100 points)

- **20:** actor, under-13 and child-directed/mixed-audience applicability.
- **20:** data/biometric classification and collection limits.
- **20:** direct notice and **separate** third-party consent where required.
- **20:** retained-purpose, security, deletion and parent-control architecture.
- **20:** exact legal sections, effective/compliance dates, exceptions and unresolved facts.

**Release limitations:** selected operative provisions checked in the 2025 final Federal Register **HTML** and FTC explanatory materials as of November 13, 2026. This study does **not** prove complete present-day amendment history, independently evaluate a real company's implementation, establish FERPA or all state-law coverage, or authorize rehosting statutes or third-party content. For live children-related features, seek qualified legal review.
