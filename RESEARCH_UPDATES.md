# November 2026 research updates

The seven-textbook [Tech-Law curriculum](README.md) is supplemented by [a source-linked, qualified research tranche](research/2026-11-13/README.md) reconciling the uploaded later-milestone archive with current official legal sources.

**New subjects:** Colorado's 2026 ADMT replacement statute; Illinois employment AI and NYC AEDT requirements; California's phased ADMT regulations; the enacted EU 2026 AI Act amendment; Washington/Florida data-breach notification; Illinois BIPA and Texas 2026 biometric AI conditions; ROSCA and the vacated FTC amendment; withdrawn CFPB employment-screening guidance; and TAKE IT DOWN Act coverage.

**Evidence and limits:** [Source register](research/2026-11-13/source-register.csv), [archive reconciliation](research/2026-11-13/ARCHIVE_RECONCILIATION.md), and [quality gate](quality/RESEARCH_RECONCILIATION_2026-11-13.md). The original uploaded archive is preserved as the source handoff; the research chapter is a curated selection, not a full ingestion of all 128 staged entries. This does **not** establish an exhaustive 50-state survey, legal advice or compliance certification.

**Milestone 16 (November 13):** The prior open source check on California Civil Code §1798.82 was resolved for the specified deadline propositions using the California Department of Real Estate's 2026 statutory excerpts and state DOJ guidance; the [six-state breach chapter](research/2026-11-13/03-breach-notifications.md), [timing casebook](research/2026-11-13/07-breach-timeline-casebook.md), [recipient matrix](research/2026-11-13/breach-obligations.csv) and [audit receipt](quality/MILESTONE16_BREACH_SOURCE_AUDIT_2026-11-13.md) add exact triggers and distinctions for CA, TX, IL, MA, WA and FL. A full current legislative/case history and 50-state review remain open.


**Milestone 16B data-quality gate:** [Source register policy](quality/SOURCE_REGISTER_POLICY.md) and an [offline metadata checker](scripts/audit_source_register.py) now validate authority status, official HTTPS URL hosts, IDs, dates and cross-references; they do not claim to test external legal truth or predict incident deadlines.


**Milestone 17A (historical cases):** The [case provenance and later-history clinic](casebook/2026-11-13-historic-opinion-source-clinic.md) analyzes *Specht* and *Smith v. Van Gorkom* against available reproduced texts and **official later court opinions**. Neither original issuing-court copy was authenticated, so both remain flagged pending; the 2017/2024 Delaware court discussion narrows *Gantler*'s change to ratification terminology rather than discarding the entire historic case.


**Milestone 17B (Maryland and Oregon privacy):** [New state privacy research](research/2026-11-13/08-maryland-oregon-privacy.md) and [applied exercises](research/2026-11-13/09-state-privacy-implementation-exercises.md) add exact count/revenue thresholds, separate government vs private Maryland statutes and significant 2026 Oregon consumer privacy guidance. The [source audit](quality/MILESTONE17_STATE_PRIVACY_AUDIT_2026-11-13.md) retains a documented **403 access blocker for Oregon's 2026 amendments table**, so the findings are not full amendment-verified current-law advice.


**Milestone 18A (Oregon amended-law reconciliation):** An accessible [official consolidated 2026 A&R table](https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2026OrLawAR.pdf) resolves the prior 403 **for the direct-amendment index**: no direct 2026 changes listed for **ORS 646A.570–646A.589**. This does not erase **2025** privacy amendments that began **January 2026**, nor [2026 Oregon Laws chapter 96](https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2026orLaw0096.pdf), a separate **public-body/data-broker attestation** law. See [the research and case exercises](research/2026-11-13/10-oregon-session-law-reconciliation.md) and [verification receipt](quality/MILESTONE18_OREGON_SOURCE_AUDIT_2026-11-13.md). Other new/uncodified enactments and case history remain to be reviewed.


**Milestone 18B — editorial source-review guardrails:** [claim-level watchlist](quality/legal-change-watchlist.csv), [review policy](quality/LEGAL_CHANGE_REVIEW_POLICY.md) and [offline QA script](scripts/audit_legal_change_watchlist.py) separate **index-checked**, **targeted primary-text-checked**, and **pending** propositions. They record planned *manual* review dates only, not live legal monitoring or legal validation.


**Milestone 19A — material Maryland correction:** [Current Maryland MODPA codification and 2026 HB711 / Ch874](research/2026-11-13/11-maryland-modpa-2026-amendments.md) are now documented with active **§§14-4701–14-4714** citations and linked current official text. The 2024 Ch454 **§14-46xx** numbers remain historical only. Includes expanded inferred-sensitive-data, geolocation, government sales and certain subpoena/cooperation provisions; see [verification receipt](quality/MILESTONE19_MARYLAND_2026_AUDIT.md). This is a targeted source audit, not full statewide subsequent-history certification.


**Milestone 19B — separate Oregon 2026 ALPR statute:** [Oregon Laws 2026 chapter 77 / SB1516](research/2026-11-13/12-oregon-alpr-law-and-vendor-contracts.md), effective March 31, 2026, has independent rules for law-enforcement ALPR use, 30-day default noncase data retention, agency/vendor contracts, audits and vendor remedies. It does **not** amend the OCPA §§646A.570–.589. See the [primary-source audit](quality/MILESTONE19_OREGON_ALPR_SOURCE_AUDIT.md). Actual deployment remains subject to qualifying roles, exceptions, policies and attorney review.


**Milestone 20A — children's data:** [COPPA final-rule and 2026 compliance study](research/2026-11-13/13-coppa-2026-children-and-games.md) covers FTC's enacted 2025 amendments, separate parental consent for certain disclosures, new biometric identifiers, retention and security evidence. A [targeted source audit](quality/MILESTONE20_COPPA_SOURCE_AUDIT_2026-11-13.md) distinguishes effective and compliance dates and unfinalized rule proposals. Applicable operator facts and legal exceptions remain open.


**Milestone 20B — employment AI:** [Illinois video-interview and New York City AEDT law](research/2026-11-13/14-hiring-ai-video-and-aedt-2026.md) now distinguishes video-recording notice/consent and on-request deletion, §42/20 demographic reporting only for solely-AI progression decisions, separate Illinois 2026 AI employment discrimination/notice, and NYC independent bias audits and advance notices. The [official-source audit](quality/MILESTONE20_HIRING_SOURCE_AUDIT_2026-11-13.md) preserves the future Jan. 2027 Illinois statutory-version boundary and vendor/employer role caveats.


**Milestone 21A — biometrics:** [Washington RCW 19.375](research/2026-11-13/15-washington-biometric-privacy.md) is now included with a close comparison to Illinois BIPA and Texas commercial biometric collection. Washington's narrow enrollment/commercial-purpose definitions, **notice OR consent OR prevention** alternatives, security exception and AG-only enforcement materially differ from Illinois. See the [official-subsection source receipt](quality/MILESTONE21_BIOMETRIC_AUDIT_2026-11-13.md). No cross-state biometric legal certification is implied.


**Milestone 21B — court-status and children's online-safety legal versions:** The [California / Texas children’s digital services litigation casebook](research/2026-11-13/16-child-online-safety-and-injunctions-2026.md) examines the March 12 **Ninth Circuit preliminary injunction** (about the **2022 California AADC**), the separately signed **California AB2246 / Ch187 (2026)** replacement, and the October 28 **Fifth Circuit en banc order** that **VACATED its July 24 Texas SCOPE Act panel opinion**. The [court/source receipt](quality/MILESTONE21_CHILD_SAFETY_LITIGATION_AUDIT_2026-11-13.md) distinguishes court-hosted orders from a California chaptered text mirror whose official bill viewer returned 403. This is not an enforceability clearance for any company.
