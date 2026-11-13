# Breach-notification law: six-state primary-source comparison (Milestone 16)

**Reviewed:** 2026-11-13. **Scope:** selected U.S. state laws applicable to private entities, not a 50-state analysis, incident-specific advice, or an automated legal deadline calculator. **Status:** the specific subsections cited below were checked against official state-published sources. Applicability, historical incident-date version, sector laws, later amendments and case treatment remain fact-specific.

## 1. First classify the event; then separate recipients and clocks

Collect the controller/owner versus processor/maintainer role, affected resident states, statutory category of *personal information*, actual or reasonably believed acquisition/access, encryption **and keys**, number of affected people per state, date of discovery and/or legal determination, and permitted investigation or law-enforcement delays. State agencies, financial institutions and health-sector entities may have distinct requirements.

An incident date is not necessarily the date of discovery; discovering unusual traffic is not necessarily the legally defined determination that a breach occurred. Preserve both as evidence and **do not run one universal countdown**.

## 2. Pinpointed comparison

| State | Consumer/resident notice | State regulator notice | Source and limitation |
|---|---|---|---|
| **California** | Civil Code **§1798.82(a)(2)(A)**: generally within **30 calendar days of discovery or notification of the breach** for a covered person/business and covered data, subject to **(a)(2)(B), (c)** investigation/law-enforcement delays | **§1798.82(f)**: if notice is required to **more than 500** California residents for one incident, submit a **single redacted sample** to the Attorney General **within 15 calendar days after consumer notice** | [CA Department of Real Estate, official 2026 statutory excerpts (Civil Code pp. 107–109)](https://dre.ca.gov/files/pdf/relaw/excerpts.pdf); [CA DOJ reporting form](https://oag.ca.gov/privacy/databreach/report-a-breach). Enacted amendment: 2025 **SB 446**, effective January 1, 2026 |
| **Texas** | Business & Commerce Code **§521.053(b)**: without unreasonable delay and generally **no later than 60 days after determining the breach occurred**; statutory scope, delay and exceptions apply | **§521.053(i)**: at least **250 Texas residents**, notice to AG as soon as practicable and **no later than 30 days after determination** | [Texas Legislature, Chapter 521](https://tcss.legis.texas.gov/resources/BC/htm/BC.521.htm). The AG deadline is not the consumer deadline |
| **Illinois** | Personal Information Protection Act, **815 ILCS 530/10(a)**: most expedient time possible and without unreasonable delay after discovery/notification; **no universal numeric consumer deadline** in this subsection | **§10(e)(2)**: if required to notify **more than 500** Illinois residents, tell AG without unreasonable delay and **no later than the consumer notice**; subsection (e)(1) has a specified health-sector exclusion | [Illinois General Assembly, §530/10](https://www.ilga.gov/documents/legislation/ilcs/documents/081505300K10.htm). A **data maintainer** not owning/licensing information notifies the owner/licensee **immediately** when (b) applies |
| **Massachusetts** | General Laws **ch. 93H, §3(b)**: when specified knowledge/reason-to-know conditions are met, the **owner/licensee** notifies resident **as soon as practicable and without unreasonable delay** | **§3(b)**: also notify **Attorney General and Director of Consumer Affairs and Business Regulation** under same general timing; no general numeric days in this section | [Massachusetts Legislature, Chapter 93H §3](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93H/Section3). **§3(a)** requires a *maintainer* to notify owner/licensee; incident-specific supplemental obligations apply |
| **Washington** | **RCW 19.255.010(8)**: most expedient time possible, without unreasonable delay, generally **within 30 calendar days of discovery**, with specified delays | **RCW 19.255.010(7)**: notice to AG for **more than 500** Washington residents, **within 30 days of discovery** | [Washington Legislature, RCW 19.255.010](https://app.leg.wa.gov/RCW/default.aspx?cite=19.255.010). Includes a risk-of-harm exception and separate owner notification |
| **Florida** | Florida Statutes **§501.171(4)(a)**: as expeditiously as practicable, without unreasonable delay, generally **within 30 days after determination/reason to believe**, subject to specified delays/waiver | **§501.171(3)(a)**: **500 or more** Florida individuals, notify Department of Legal Affairs **within 30 days after determination/reason to believe** | [Florida Senate, 2026 §501.171](https://www.flsenate.gov/Laws/Statutes/2026/501.171). Third-party agent has a separate **§501.171(6)** duty |

**Threshold traps:** "more than 500" means 501 or above; "500 or more" includes exactly 500. Texas AG threshold is at least 250, not 500. These thresholds are **not safe harbors for individual notices**. Resident counts must be evaluated for each applicable statute, not summed blindly across states.

## 3. California: resolve the prior source blocker precisely

The previous milestone's archive left §1798.82 currentness **unverified** because California's legislative code website returned an access error. For this milestone, the official **California Department of Real Estate's 2026 code excerpts** were read at printed pp. 107–109 and cross-checked against the California DOJ submission page. The excerpt reflects **SB 446, 2025 Stats. ch. 319**, effective **January 1, 2026**, including the 30-day consumer rule and 15-day post-notice sample requirement.

**Provenance caveat:** This is a state-published *reproduction of statutory text*, not direct access to the California Legislature's dynamic codification page (which remained access-blocked). It resolves the specific previously unverified **statutory text and deadlines** at the stated date, but **not** a complete subsequent-amendments or judicial-history check. Do not treat the DRE publication as an independent statute. [Official CA DOJ reporting guidance](https://oag.ca.gov/privacy/databreach/reporting) confirms the >500 sample submission obligation.

**Processor distinction:** §1798.82(b) requires a data *maintainer* not owning the information to notify the owner/licensee **immediately after discovery** when the covered criteria are met. It is a separate role and notice from the resident's §(a) clock.

## 4. Texas: two different triggers and recipients

Under **§521.053(b)**, the business's resident disclosure clock refers to the date it **determines** that the breach occurred, and is generally capped at 60 days. **§521.053(i)** is a separate AG obligation at ≥250 Texas residents, no later than 30 days after determination. An entity that merely *maintains* covered data not owned by it has an **immediate owner/licensee notice** under §(c). §(h) adds consumer-reporting-agency notification when notifying **more than 10,000 persons at one time**. Review the statute's alternative state-law, investigative and notification-method provisions.

## 5. Illinois and Massachusetts: qualitative timing does not mean optional notice

Illinois §10(a) requires prompt consumer notification; §10(e)(2) makes the AG deadline **no later than** consumer notice when the >500 threshold and conditions are met. The Illinois AG notice includes incident nature, affected resident count and remediation steps, but the resident notice **must not include** the affected Illinois resident count. Under Massachusetts §3(b), AG, Director and residents have parallel duties without a generic fixed day limit; its resident notice has its own prohibited contents, notably the nature of the breach and total affected count, unlike government reporting.

**Do not** use one generic template for Illinois and Massachusetts consumer letters.

## 6. Case exercise (hypothetical)

A SaaS vendor discovers exposed records on November 1, determines on November 5 that qualifying unencrypted records were acquired, and identifies **501 California, 250 Texas, 501 Illinois, 20 Massachusetts, 501 Washington and 499 Florida residents**.

Before computing any dates, record evidence for each state's **trigger**. Conditional notifications may include:
- California **§1798.82(a)** resident notice, and **§(f)** post-resident-notice sample AG filing; the 15-day AG clock is **not** measured from breach discovery.
- Texas resident vs AG **different clocks**; 250 meets Texas's **at least** threshold.
- Illinois AG at **more than 500**, at or before consumer notice.
- Massachusetts AG, Director, and resident without a flat 30-day deadline.
- Washington AG at **more than 500** and consumer notice from discovery, subject to statute's exceptions.
- Florida resident notice may apply even when 499 **does not** meet its 500-person Department threshold.

**Model answer:** An actual notice decision still depends on each state's definition, covered party and data, risk and exemptions, evidence of acquisition/access, lawful delay, sectoral laws, contractual notice duties, and exact historical incident date. The numbers only establish potential threshold differences.

## Evidence receipt / incomplete scope

Checked official source publishers and section numbers on **2026-11-13**: CA DRE official state excerpt with CA DOJ cross-check; TX Texas Legislature; IL General Assembly available codified search extract; MA General Court; WA Revised Code; FL 2026 Florida Senate. **Not** a formal legislative citator, state-by-state survey, claim of every external URL being reachable in CI, or a live incident-response opinion.

See the [normalized obligation register](breach-obligations.csv) and [startup incident textbook](../../textbooks/05-cybersecurity-computer-misuse/03-breach-response.md).