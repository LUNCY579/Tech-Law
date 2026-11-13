# Milestone 8 — repository-wide quality audit and source-currency review

**Audit date:** 2026-11-11. **Branch:** `curriculum/official-primary-sources-v1`. **Scope:** all content added in PR #1, including seven textbooks, 36 numbered chapters, foundational lessons, casebook, answer keys and quality files. **Status:** IMPORTANT — this is a targeted structural and authoritative-source *sampling* audit, not an exhaustive legal citator, exhaustive HTTP link crawler, paragraph-by-paragraph legal review, or attorney-approved textbook certification.

## What was actually checked

1. **Repository structure:** Inspected the GitHub PR's 71-file unified per-file patches (including the newly added static audit script at that point). Extracted and normalized internal relative Markdown link destinations against PR file paths. **66 relative links were parsed; zero missing destinations were identified in that pass.** This checks path existence, not whether the linked discussion is correct or complete. The separate `scripts/audit_curriculum.py` adds a repeatable repository-local check; its execution was **not** claimed as a completed CI run.
2. **Index and chapter counts:** Seven textbook indices and chapter path groups were present in the PR content: Textbooks I–VI have five numbered chapters each; Textbook VII has six. Total **36 substantive chapters**, excluding overview and source-note files.
3. **Case source spot checks:** The official Supreme Court PDFs for *Coinbase v. Suski* (2024) and *Warhol v. Goldsmith* (2023) were fetched; their captions/dates and syllabus warnings were checked. The syllabus is expressly not the majority opinion. *Bostock*'s official PDF is linked but too large for the source reader in this pass; do **not** claim a successful complete page-by-page Bostock inspection. *Specht* and *Van Gorkom* originals remain unauthenticated.
4. **Statute spot check:** [15 U.S.C. §8403](https://uscode.house.gov/us/usc/119-120/t15/s8403/) opened on the U.S. House OLRC site, marked current through Public Law 119-120 (October 7, 2026). This supports the three separate ROSCA requirements (pre-billing clear material terms, express informed consent, and simple mechanism for stopping recurring charges).
5. **Time-sensitive administrative law checks:** Current official EU AI Act [Article 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113?full=1), [California CPPA's final 2025 rulemaking/2026 implementation](https://cppa.ca.gov/regulations/ccpa_updates), [FTC February 2026 negative-option correction](https://www.ftc.gov/policy/public-comments/revision-negative-option-rule-withdrawal-cars-rule-removal-non-compete-rule-conform-these-rules-0), [IRS Form 15620](https://www.irs.gov/pub/irs-pdf/f15620.pdf), [EEOC UGESP Q&A](https://www.eeoc.gov/es/node/130157), [FTC Safeguards Rule guide](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know) and [SEC cyber-disclosure official rule](https://www.sec.gov/files/rules/final/2023/33-11216.pdf) were consulted for targeted claims.
6. **Case update:** Added the 2025 EU General Court *Latombe* dismissal and filed appeal C-703/25 P to Textbook VII's Chapter 2 and source ledger, distinguishing procedural status from blanket claims about the EU–U.S. DPF.

## Material findings and disposition

| ID | Area | Evidence or concern | Disposition / action |
|---|---|---|---|
| AUD-01 | Relative Markdown links | 66 referenced local destinations, zero missing in parsed PR patches | Structural path check passed in this pass; repeat local script after changes |
| AUD-02 | EU AI Act deadlines | Official consolidated Article 113 has Annex III high-risk requirements from **2 Dec 2027**, Annex I product-related high risk **2 Aug 2028**, with other phased rules and transition qualifications | Existing textbook timing retained, must be rechecked before real deployment |
| AUD-03 | CPPA 2026 regulations | Regulations effective **1 Jan 2026**; certain ADMT requirements begin **1 Jan 2027**; cybersecurity audit milestones are phased | Existing distinction preserved; never state one universal CCPA date |
| AUD-04 | FTC click-to-cancel | 2024 amendment vacated in 2025; FTC 2026 rule action restores earlier text; separate ROSCA §8403 still operates | Existing textbook properly separates law/regulation |
| AUD-05 | 83(b) election | IRS Form 15620 instructions specify generally **30 days after transfer**, with relevant weekend/holiday filing rules | Existing teaching verified; no personal tax recommendation |
| AUD-06 | Employment four-fifths ratio | EEOC calls it a **rule of thumb**, not a legal definition | Existing 0.50 worked ratio correct; do not equate with proven violation |
| AUD-07 | FTC Safeguards/SEC incidents | FTC covered financial institutions §314.4(j), generally 30 days after qualifying event discovery; SEC covered registrants Item 1.05, generally four business days after materiality determination | Existing conditional explanations verified; no universal deadline |
| AUD-08 | EU–US DPF later history | *Latombe*, T-553/23, dismissed annulment action 3 Sept 2025; appeal C-703/25 P filed 31 Oct 2025 | New case-procedure section and ledger entry added |
| AUD-09 | *Coinbase* and *Warhol* | Official Supreme Court opinions accessible; syllabus is not part of opinion | Casebook correctly distinguishes holding and scope; no later citator performed |
| AUD-10 | *Specht* and *Van Gorkom* | Authentic original court publication and later treatment not obtained | **OPEN, source authentication required** |
| AUD-11 | External links and source permissions | 110+ distinct external URL strings present in course patches; this audit did not HTTP-resolve every URL or independently establish each item's re-use license | **OPEN, external URL crawl / source-by-source rights review needed** |
| AUD-12 | Comprehensive case history | No Westlaw/Lexis/Shepard's/KeyCite type check and no complete current appellate/circuit authority survey | **OPEN; cannot certify later-history completeness** |
| AUD-13 | State-by-state law | Individual U.S. state privacy, auto-renewal, breach, and employment rules not fully enumerated | **OPEN; must scope jurisdiction and date before advising** |
| AUD-14 | Scientific validity | Teaching assessment statistics are illustrative, not an independent evaluation of a deployed AI assessment | **OPEN; qualified validation required for real employment claims** |

## Corrected/strengthened guidance

### EU–U.S. DPF case history
- [General Court *Latombe v Commission*, T-553/23](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62023TJ0553) dismissed the action seeking annulment of the Commission's 2023 DPF adequacy decision on 3 September 2025.
- [Notice of appeal, C-703/25 P](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AC_202506610) records an appeal filed 31 October 2025.
- A dismissal at first instance is **not** an unappealable permanent guarantee. An appeal filing does **not** itself invalidate the adequacy decision. Verify any later judgment and current Commission adequacy status before reliance.

### FTC/ROSCA
The FTC's vacated 2024 regulation must not be taught as current binding text. It is likewise misleading to conclude that cancellation regulation vanished: [15 U.S.C. §8403](https://uscode.house.gov/us/usc/119-120/t15/s8403/) independently governs covered online negative-option transactions, and state laws may add obligations.

### Government-hosted material and licensing
Use original commentary and necessary short citations. Official publisher status does **not** imply every embedded image, contractor work, third-party chart or non-U.S. government text is unrestricted for redistribution. No complete external source documents are mirrored in the curriculum.

## Priority backlog before merge or external publication

**P0 (accuracy):** authenticate original opinions and subsequent histories for *Specht* and *Van Gorkom*; review all law-sensitive, date-specific propositions and binding/guidance labels.  
**P1 (quality):** run the new repository-local static audit script and fix any warnings; independently HTTP-check external links; index all statute provisions with pinpoint citation records and current versions.  
**P1 (content):** full review of each exam answer against the exact operative law; correct any misleadingly universal language found in full editorial reading.  
**P2 (maintenance):** build recurring deadline and source-change alerts, document editorial ownership, and add section-level metadata for future reviews.

**Release disposition:** **DO NOT mark “fully legally verified.”** Appropriate description: *seven-book founder legal study library with primary-source-linked original commentary and a documented, incomplete legal QA pass*. Keep PR unmerged pending editorial and legal-source review.
