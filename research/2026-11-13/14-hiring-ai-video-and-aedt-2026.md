# Milestone 20B — Automated hiring and recorded video: Illinois and New York City

**Research cutoff:** November 13, 2026. **Source standard:** identified Illinois statutory sections and public acts, NYC Local Law 144, implementation rules and DCWP explanations. Original educational commentary; not legal advice, a vendor certification, independent bias audit or a validity study.

## 1. Separate four mechanisms before building the product

1. **Illinois recorded AI video interviews** — [820 ILCS 42/5, /10, /15, /20](https://my.ilga.gov/Legislation/ILCS/Articles?ActID=4015&Chapter=EMPLOYMENT&ChapterID=68&MajorTopic=BUSINESS+AND+EMPLOYMENT). The Artificial Intelligence Video Interview Act has **specific** notice/consent, restricted sharing, applicant-request deletion and conditional demographic reporting. It is not a general video surveillance statute for every AI model.
2. **Illinois AI employment discrimination** — [775 ILCS 5/2-102(L)](https://www.ilga.gov/legislation/ilcs/fulltext?DocName=077500050K2-102), made operative in relevant part by **P.A. 103-804 effective January 1, 2026**. Governs use of AI in specified employment practices with discriminatory effects or protected-class ZIP-code proxies and employer notice; this is independent of recorded-interview consent.
3. **NYC covered AEDT** — [NYC Administrative Code §§20-870–20-872](https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=4344524) under Local Law 144 (2021), [6 RCNY §§5-300–5-304](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-138391), and [DCWP official FAQ](https://www.nyc.gov/site/dca/businesses/faq-automated-employment-decision-tools.page). Covered employers and employment agencies must ensure a recent independent bias audit and specified publication/notices. “AI” alone does not classify every tool as an AEDT.
4. **Federal employment protections** — [Title VII, 42 U.S.C. §2000e-2](https://www.govinfo.gov/link/uscode/42/2000e-2) and [ADA/EEOC technical materials](https://www.eeoc.gov/laws/guidance/employment-tests-and-selection-procedures) are separate from the city audit requirement. Demonstrating a city audit does not prove a selection cutoff is job-related or nondiscriminatory.

## 2. Illinois Artificial Intelligence Video Interview Act — four separate sections

| Provision | Legal content | Implementation evidence |
|---|---|---|
| **820 ILCS 42/5** | For applicant-submitted **recorded video interviews** analyzed by AI for jobs **based in Illinois**, employer must give **pre-interview** AI-use notice, explanation of how AI functions/types of characteristics and obtain **consent before interview**; cannot use AI to evaluate applicant without it | Timestamped notice/consent versions, job location, explanation and consent withdrawal scenarios |
| **820 ILCS 42/10** | Applicant recordings cannot be shared except with persons whose expertise or technology is **necessary** to evaluate fitness | Recipient inventory, purpose-limited vendor access, no default training reuse |
| **820 ILCS 42/15** | On applicant request, employer has **30 days after receiving request** to delete video interviews and instruct other recipients to delete **including electronically generated backup copies** | Delete request event, downstream recipient instructions, verifiable purge status; preserve lawful evidence of fulfillment without keeping unnecessary video |
| **820 ILCS 42/20** | **Only where employer relies solely** on AI video analysis to select for an **in-person interview**, employer must collect/report race/ethnicity of advanced vs not advanced and hires to Illinois DCEO **annually by December 31**, covering 12 months ending previous **November 30** | Decision-mode evidence, permitted demographic record handling, report scope and supporting data |

**Source provenance:** The General Assembly's [820 ILCS 42 article](https://my.ilga.gov/Legislation/ILCS/Articles?ActID=4015&Chapter=EMPLOYMENT&ChapterID=68&MajorTopic=BUSINESS+AND+EMPLOYMENT) prints all four sections. **P.A. 101-260** added the 2020 framework; [P.A. 102-47](https://www.ilga.gov/Legislation/PublicActs/PrinterFriendly/102-0047) added reporting from 2022. Nothing in these provisions means that an ordinary **text-only** coding test automatically triggers the recorded-video law.

**Important boundary:** 42/20's "solely" condition is narrower than §5's notice/consent rule. Do not treat the December 31 demographic report as mandatory for every employer that uses an AI support tool. Likewise, do not import 42/15's 30-day deadline into other, unrelated data-processing requirements.

## 3. Illinois Human Rights Act — a separate 2026 rule

Under [775 ILCS 5/2-102(L)](https://www.ilga.gov/legislation/ilcs/fulltext?DocName=077500050K2-102), the 2026 operative provision addresses AI use in recruitment, hiring, promotion and other employment contexts having discriminatory effects on covered protected classes, using ZIP codes as protected-class proxies, and required **employee** notices. The statute directs implementing rulemaking. Read actual notices and pending/emerging agency rules rather than asserting a universal notice template.

**Version trap:** Illinois's official code shows **text before and after P.A. 104-793**, with the **later version stated effective January 1, 2027**. As of November 13, 2026, do **not** copy a future-effective text into a purported 2026 compliance obligation. For a 2027 decision, recheck the version on the exact decision date.

## 4. NYC Local Law 144 — employer and employment-agency duties

According to the NYC [DCWP published rule and FAQ](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page), a covered **automated employment decision tool** uses specified computation to substantially assist or replace discretion in screening **candidates who applied to a specific job or employees considered for promotion**. The operative rule defines substantial assistance more narrowly than "uses an LLM in any way," and the city location/employment-decision definitions condition application.

For a covered tool:
- **Independent bias audit:** the employer/agency must ensure the tool was audited **no more than one year** before use. A bias audit calculates prescribed selection/scoring rates and impact ratios for sex, race/ethnicity and intersectional categories. Publicly post the audit summary and tool distribution date.
- **Notice:** provide covered NYC-resident candidates/employees information about use and the job qualifications/characteristics assessed, including reasonable-accommodation request instructions, generally **at least 10 business days before use** through permitted channels. This is distinct from Illinois's **pre-recorded-interview** consent rule.
- **Data/retention transparency:** the city rule specifies website data retention/source notices and written-request pathways; use the operative [6 RCNY §5-304](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-138391) for exact response conditions.
- **Who is legally responsible?** DCWP's FAQ assigns the audit-use condition to **employers/employment agencies**. A **vendor** may coordinate an independent audit, but the vendor's own employee cannot serve as the independent auditor. That does not rule out other vendor liability under separate laws/contracts.

**Do not conflate legal controls:** DCWP says the AEDT law requires audits and notices but does **not** prescribe a specific remedial action solely because a bias audit finds a disparity. Independent anti-discrimination obligations still apply; a vendor should not publish an “unbiased” certificate just because a city-format audit exists.

## 5. Matrix: same scoring pipeline, different uses

| Workflow | Potential legal questions |
|---|---|
| Candidate independently takes a public coding practice quiz | Is this an employment decision at all? Do not infer NYC AEDT or Illinois video coverage from the presence of AI |
| NYC employer relies heavily on algorithmic ranking of actual applicants | Local Law 144 AEDT classification; employer independent audit and timely notice; separate federal/state job-related and anti-discrimination review |
| Illinois employer AI-scores applicant-recorded interviews | 820 ILCS 42/5 explanation and affirmative consent; 42/10 sharing; 42/15 on-request deletion; 42/20 only if solely AI chooses in-person interviews |
| Illinois employer uses AI to rank résumés without a recorded video | Investigate 775 ILCS 5/2-102(L) and other law; do not mechanically impose Illinois *video* requirements |
| Vendor signs a test-score certificate | Authenticity and current revocation are separate from validity, fairness, lawful use, independent audit, accreditation and candidate notice |

## 6. Applied founder assessment (100 points)

A startup markets a proprietary code-assessment credential; Employer A (NYC) screens applicants with a heavily weighted scoring API. Employer B (Illinois) asks job candidates to record videos, uses AI to score them, retains vendor copies and uses the AI scores as one of several factors when choosing in-person interviews.

**Answer outline:** establish candidate's job location/residency, actual tool role/weight, separate employer and vendor roles, whether NYC AEDT thresholds are met, when independent city audit and candidate notices must occur, and whether Illinois video pre-interview consent/description was given. For B, §42/20's solely-AI trigger may **not** be met; §42/15 deletion and instructions still require analysis on request. For both, federal discrimination and accommodations questions remain; signed scores are not professional accreditation or scientific job validity.

**Rubric:** 20 scope, 20 statutory distinctions and dates, 20 consent/notice and deadlines, 20 audit/validation and vendor responsibilities, 20 technical proof and unresolved exceptions.

## Evidence limitations

Official Illinois codification (820 ILCS 42 and 775 ILCS 5), Illinois enacted P.A. 102-47, NYC enacted Local Law/administrative rules and DCWP explanatory FAQ were examined for these **selected** claims. Not a full effective-date citator for every 2026/2027 act, current agency rule inventory, scientifically valid employment evaluation, licensed legal treatise or claim about an actual customer's legal duties. Preserve these limits in the [Milestone 20B source audit](../../quality/MILESTONE20_HIRING_SOURCE_AUDIT_2026-11-13.md).
