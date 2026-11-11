# Lesson 02 — Contracts for SaaS and AI services

**Goal:** Read and design agreements without confusing a website template with enforceable consent. **Scope:** U.S. general principles; state-specific law varies.

## 1. Formation: offer, acceptance, consideration
Begin with a valid offer, an objective manifestation of acceptance, consideration, and capacity/legality. A valid contract also depends on the jurisdiction and the applicable transaction. For a B2B API, a negotiated order form and master services agreement can govern pricing, service scope and risk. For a consumer application, consent design and notice are central.

## 2. Online terms: a visible link alone may be insufficient
Analyze whether the user had reasonable notice of the terms and manifested assent. Compare *Specht v. Netscape Communications Corp.*, 306 F.3d 17 (2d Cir. 2002): the court held the users were not bound to arbitration terms presented below the download button where adequate notice/assent was missing. [Official Second Circuit opinion on GovInfo](https://www.govinfo.gov/content/pkg/USCOURTS-ca2-01-07876/pdf/USCOURTS-ca2-01-07876-0.pdf) (confirm document URL before relying in a filing). The precise UI and governing law matter.

**Engineering translation:** show conspicuous terms near the affirmative action; version terms; record acceptance timestamp, user identity, version/hash, locale, and presentation state; maintain accessible copies.

## 3. Clauses to understand, not blindly paste
| Clause | Legal/operational question |
|---|---|
| Description of services | Are uptime, data retention, AI output quality and support promised? |
| Payment and renewal | Is pricing, trial conversion and cancellation clear and compliant with applicable laws? |
| IP ownership | Who owns inputs, outputs, code, embeddings and feedback? |
| Privacy and security | Are promises consistent with product behavior, vendor contracts and incident duties? |
| Warranty disclaimer | Does state law permit this disclaimer for this type of transaction? |
| Liability cap | What damages are excluded and what claims are carved out? |
| Indemnification | Who defends third-party claims and controls settlements? |
| Termination / export | Can users retrieve data? What happens to backups and credentials? |
| Governing law / disputes | Are consumer protections, arbitration and venue restrictions applicable? |

## 4. AI-specific drafting
Don't promise an AI feature is “always correct.” Describe human oversight, permitted uses, prohibited sensitive decisions, model/provider dependencies, data handling, output review, and service-change policies **only if reflected in actual controls**. A disclaimer cannot necessarily cure deceptive marketing or statutory duties.

## Worked hypothetical
Your model gateway markets “zero retention,” but its provider logs prompts for 30 days. This is simultaneously a potential breach-of-contract issue (depending on exact promises), consumer-protection issue and vendor-management failure. Remediation: document provider retention; revise claims; build appropriate controls; seek legal review before claiming compliance.

## Exercise and answer
**Question:** Is a copy-pasted arbitration clause automatically enforceable if a user never sees it?  
**Answer:** No. Analyze notice, assent, applicable contract law, consumer statutes and unconscionability. Preserve actual screen evidence, not just text in the repository.

## Primary-source reading
- [Federal Arbitration Act, 9 U.S.C. §2](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title9-section2&num=0&edition=prelim) [law].
- [FTC Act, 15 U.S.C. §45](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section45&num=0&edition=prelim) [law].
- [Federal judiciary opinions via GovInfo](https://www.govinfo.gov/app/collection/uscourts) [official judicial documents].
- [FTC business guidance](https://www.ftc.gov/business-guidance) [guidance].
**Practical assignment:** Inspect a SaaS signup screen, terms versioning, checkout consent and subscription cancellation. Write a 1-page issue-spotting memo.
