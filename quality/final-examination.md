# Cross-textbook final examination — AI startup legal reasoning

**Time:** 2–3 hours. **Maximum:** 100 points. This is a formative exam, not a legal license or compliance certification. All companies and facts below are fictional.

## Fact pattern
**AtlasForge AI, Inc.**, a Delaware corporation, builds a SaaS platform that (1) ranks applicants for employers in California and Germany; (2) uses a third-party model API that retains prompts for 30 days; (3) advertises “zero-retention” and “scientifically proven bias-free”; (4) bills users after a free trial but hides the price until after card entry; (5) uses code from an AGPL-licensed modified server, an MIT effects library, and music supplied under a noncommercial license; (6) signs a $500k SAFE with a $5M post-money valuation cap; (7) plans to solicit investors publicly under Rule 506(b); (8) presents a standard account arbitration agreement and conflicting promotion rules. A recruiter can change a numeric API ID and view a different employer's private candidate records.

For every answer: cite **the relevant exact section or authenticated court opinion**, distinguish current law from guidance, state missing facts and uncertainty, and recommend product controls.

## Questions

**Q1 — Entity/fundraising (15):** Identify authorization, dilution, SAFE and exemption issues. Explain why a $500k/$5M post-money cap does not guarantee a perpetual 10% stake.

**Q2 — Copyright/licensing (15):** Analyze AGPL, MIT, noncommercial music and model/dataset rights. Distinguish source code, weights, outputs and art.

**Q3 — Privacy/AI employment (20):** Apply GDPR territorial scope, legal bases and Art. 22; EU AI Act Article 6 and Annex III; California coverage and the phased ADMT rules; U.S. Title VII issues. Separate substantive duties from current application dates.

**Q4 — FTC and subscriptions (15):** Evaluate “zero-retention,” “bias-free,” pre-payment billing disclosures, ROSCA and the status of the 2024 FTC click-to-cancel amendment.

**Q5 — SaaS assent (10):** Analyze conflicting agreements under *Coinbase v. Suski*. What facts are necessary for a separate *Specht*-type assent question?

**Q6 — Cybersecurity (15):** Analyze tenant isolation, possible privacy/breach duties and the narrow CFAA rule from *Van Buren*. Provide three high-value adversarial tests.

**Q7 — Source and reuse quality (10):** Classify a federal statute, Supreme Court holding, agency summary, FTC settlement, license-publisher text, and unverified historical opinion. State what can and cannot be claimed about their authority or republication permissions.

---

# Model answer key — read after attempting the exam

## Q1 (15)
Board authorization for stock/SAFE issuance, accurate capitalization, founder IP and existing rights are needed. A SAFE is contractual and conversion depends on capitalization definitions, discounts, other convertibles, financing and subsequent dilution. The 10% heuristic under stated assumptions is not perpetual ownership. **Rule 506(b)** generally bars general solicitation; public securities promotion threatens this exemption. Compare [DGCL §§101–102 and §141](https://delcode.delaware.gov/title8/c001/), [15 U.S.C. §77e](https://www.govinfo.gov/link/uscode/15/77e), and [SEC 506(b) guidance](https://www.sec.gov/resources-small-businesses/exempt-offerings/private-placements-rule-506b). **Allocate:** 5 corporate authority, 5 SAFE/dilution, 5 solicitation/anti-fraud.

## Q2 (15)
Identify exact AGPL version and whether modified network-served program triggers source duties; MIT notice and ownership; noncommercial music restriction may block a paid product; model weight and training-data agreements are distinct from source-code permissions. A public repository is not a blanket grant. Consider copyright [§102](https://www.govinfo.gov/link/uscode/17/102), [§106](https://www.govinfo.gov/link/uscode/17/106), [§107](https://www.govinfo.gov/link/uscode/17/107), plus applicable actual license texts, including [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html). **Allocate:** 5 provenance, 5 trigger/obligation, 5 mitigations.

## Q3 (20)
**GDPR:** check Arts. 2–3, 4, 5, 6, 9, 22, 28, 32 and applicable international-transfer provisions. **EU AI Act:** establish actors and use, Article 6 and Annex III employment classification, then operative application dates in current text. **California:** check covered-business threshold and relevant 2026/2027 ADMT timing. **Title VII:** distinguish intentionally discriminatory scoring from disproportionate impact of facially neutral selection, and examine validity and job relevance rather than trusting marketing. Authorities: [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [AI Act consolidated 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02024R1689-20260727), [CPPA regulations](https://cppa.ca.gov/regulations/), [42 U.S.C. §2000e-2](https://www.govinfo.gov/link/uscode/42/2000e-2). **Allocate:** 5 GDPR, 5 EU AI, 5 CA, 5 employment.

## Q4 (15)
FTC Act §5 representations may be materially deceptive if “zero retention” contradicts provider logs or bias-free assertions lack evidence; independently consider substantiation and relevant unfairness analysis. [15 U.S.C. §45](https://www.govinfo.gov/link/uscode/15/45). Under [ROSCA, §8403](https://www.govinfo.gov/link/uscode/15/8403) covered offers must disclose material terms before billing information, obtain express informed consent, and provide a simple cessation mechanism. The amended FTC 2024 click-to-cancel rule was vacated in 2025 and the FTC [recodified prior text in 2026](https://www.ftc.gov/policy/public-comments/revision-negative-option-rule-withdrawal-cars-rule-removal-non-compete-rule-conform-these-rules-0). State automatic-renewal rules remain independently relevant. **Allocate:** 7 FTC evidence, 5 ROSCA, 3 temporal correction.

## Q5 (10)
[Coinbase v. Suski](https://www.supremecourt.gov/opinions/23pdf/23-3_879d.pdf), majority slip pp. 4–9: the court resolves the threshold conflict over which agreement delegates arbitrability. This does not automatically choose the winning agreement. User assent, scope, timing, integration, precedence and governing law still matter. *Specht*, 306 F.3d 17, is a historical notice-and-assent precedent whose original official opinion remains **unauthenticated in this repository**, so no invented pinpoint or link. **Allocate:** 5 doctrinal distinction, 5 factual analysis.

## Q6 (15)
Fix object-level authorization with server-side tenant/candidate checks and valid current access grants. Tests: (1) two employers request each other's candidate IDs, (2) race candidate revocation against an evidence download, (3) revoked sessions/replayed tokens request an object. Assess actual exposure, applicable privacy notice/contract and statutory breach thresholds; no universal 72-hour U.S. rule. [Van Buren v. United States](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf) narrowly addressed exceeding authorized access by misuse of otherwise permitted information, not a general legal license to cross tenant boundaries. **Allocate:** 5 authorization, 5 adversarial tests, 5 legal distinction.

## Q7 (10)
Federal statute = enacted law; Supreme Court majority holding = controlling precedent on decided question; agency summary = explanatory guidance; FTC consent order = party-specific enforceable settlement, not litigated finding; license-publisher text = potential operative contractual copyright license, not government regulation; unauthenticated historic opinion = research lead requiring official original and history verification. Official hosting does not universally grant reuse rights for third-party or state/EU contents. **Allocate:** 6 source classes, 4 permissions/scope.

## Grading and feedback
**90–100:** strong issue spotting and doctrinal distinctions; **75–89:** sound baseline with notable research gaps; **60–74:** needs targeted practice; **below 60:** revisit statutory parsing and case briefs. Passing does not prove legal compliance or professional licensure. Examiner should mark as incorrect confident assertions unsupported by legal elements, dates or source status.
