# Milestone 17B — Maryland and Oregon consumer privacy law

**Research cutoff:** November 13, 2026. **Scope:** targeted official-source comparison, not an exhaustive 50-state or amendment/case-law citator review, product-specific legal advice, or a compliance certification.

## Source hierarchy and currentness

The Maryland source chain is [**Chapter 454 (2024), original MODPA enactment**](https://mgaleg.maryland.gov/2024rs/chapters_noln/ch_454_hb0567e.pdf) plus the [Maryland Attorney General's business guidance](https://oag.maryland.gov/Resources-Info/Pages/data-privacy.aspx). The Oregon chain is [**ORS 646A.570–646A.589**](https://www.oregonlegislature.gov/bills_laws/ors/ors646a.html), [Oregon DOJ overview](https://www.doj.state.or.us/consumer-protection/id-theft-data-breaches/privacy/) and [DOJ FAQ](https://www.doj.state.or.us/consumer-protection/id-theft-data-breaches/privacy/privacy-law-faqs-for-consumers/). Regulator FAQs are **guidance**, not an independent binding statute.

**Milestone 18 follow-up (November 13):** Oregon's 2025-code page does omit later sessions. The earlier 403 was resolved using the Legislature's official **2026 consolidated amendment table**, which shows **no direct amendments** to OCPA **ORS 646A.570–646A.589** in the 2026 regular session; the 2025 special-session index also has no entries for this range. The 2026 regular-session table does list changes elsewhere in Chapter 646A, and **2026 Oregon Laws chapter 96** adds a **distinct public-body/data-broker attestation rule**. The [separate research note](10-oregon-session-law-reconciliation.md) provides exact citations and exceptions. This targeted check is not an exhaustive new-law/case citator.

### Milestone 19 Maryland source-currentness correction

**Current Maryland statute citations are Commercial Law §§14-4701–14-4714**, not the original 2024 chapter's §§14-4601–14-4614. **2026 HB 711 / Chapter 874, effective July 1, 2026** further changed definitions and specified governmental data-transfer rules. The 2026 bill already references §14-47xx in the **2025 Replacement Volume**; do **not** teach the 2026 bill as the sole source of recodification. Read [Milestone 19's current-law chapter](11-maryland-modpa-2026-amendments.md) and [source receipt](../../quality/MILESTONE19_MARYLAND_2026_AUDIT.md).

## 1. Coverage and thresholds

| Question | Maryland MODPA | Oregon OCPA |
|---|---|---|
| Primary law | Current Commercial Law **§§14-4701–14-4714** (original 2024 Ch. 454 numbered §§14-4601–14-4614) | **ORS 646A.570–646A.589**, relevant amendments |
| Date | Main effective date **Oct. 1, 2025**; distinct §14-4612 prospectivity described below | For-profits **July 1, 2024**, nonprofits **July 1, 2025** (DOJ) |
| General quantitative threshold | During previous calendar year, **at least 35,000** Maryland consumers **OR** **at least 10,000** plus **more than 20%** of gross revenue from data sale | **100,000 or more** Oregon consumers (except payment-only data) **OR** **25,000 or more** plus **25% or more** annual gross revenue from data sale |
| Actor and exclusions | Covered controller/processor; consumer excludes employment or commercial context; see **§14-4603** and definitions | Controller/processor roles; ORS **646A.572** excludes certain employment-context information and includes other exclusions and special vehicle-manufacturer coverage |
| Enforcer | Maryland Attorney General | Oregon Attorney General |

**Threshold lesson:** Maryland's “more than 20%” is not Oregon's “25% or more.” These are *general statutory coverage tests*, not immunity from every other privacy, hiring or consumer law.

## 2. Maryland: don't confuse two dates or two statutes

Maryland **MODPA Chapter 454** is an enacted consumer privacy statute effective **October 1, 2025**. Current **§14-4702** provides the general thresholds; **§14-4701** definitions and **§14-4703** exemptions must be applied before deciding coverage.

**Crucial nuance:** **Section 2 of Chapter 454** says the **originally enacted §14-4612** (now **§14-4712**) is prospective and is not to be applied to processing activities **before April 1, 2026**. This is a qualification for that named section, **not** a universal statement that MODPA began in April 2026. It was checked on the signed chapter's **printed p. 38**.

The [Maryland AG](https://oag.maryland.gov/Resources-Info/Pages/data-privacy.aspx) describes consumer data rights (including access, correction, deletion and opt-outs), restrictions around sale of sensitive data, controller/processor contracting, and assessments for heightened consumer-risk processing. These are **official regulatory explanations** and must be read alongside the specific operative sections and exceptions.

**2026-name trap:** Do not confuse the enacted **2026 HB711 / Ch. 874** amendments to private-sector MODPA with [Maryland's separately titled Data Privacy and Protection Act of 2026, Ch. 435/HB 264](https://mgaleg.maryland.gov/2026RS/chapters_noln/Ch_435_hb0264T.pdf) principally concerns **state government** data governance, rather than repealing the private-sector MODPA. Similar legislation names do not establish identical actors.

**Hypothetical:** A hiring credential vendor holds applicant scores for employers and offers a separate practice-test subscription to individuals. Identify which processing is employment vs household use and who decides the purpose. Neither a general employment exemption nor a vendor label alone settles coverage under unrelated federal or state laws.

## 3. Oregon: rights, purpose and 2026 changes

[ORS 646A.572](https://www.oregonlegislature.gov/bills_laws/ors/ors646a.html) governs scope and exceptions. **§646A.578** covers controller duties including stated purposes, relevant collection limits, reasonable security, revocation and restrictions on processing sensitive data; **§§646A.574–.576** address requests, opt-outs, appeals and consumer rights. These are not rules that automatically apply to all user information simply because a customer lives in Oregon.

The [Oregon DOJ](https://www.doj.state.or.us/consumer-protection/id-theft-data-breaches/privacy/) says that from **January 1, 2026**, covered businesses and nonprofits must honor valid **universal opt-out preference signals**. The [DOJ FAQ](https://www.doj.state.or.us/consumer-protection/id-theft-data-breaches/privacy/privacy-law-faqs-for-consumers/) identifies new 2026 restrictions concerning **sale of precise geolocation data** and **selling, profiling or using targeted advertising with data about consumers under 16**. For implementation, identify exact statutory amendment, age/knowledge triggers, exceptions and effective date; the DOJ descriptions are not a substitute for enrolled legal text.

**Hypothetical:** A multiplayer game offers location-based matching, under-16 profiles and targeted advertisements through an SDK. Identify precise location and retention, vendor disclosures and whether compensation is data sale; segment age-related rules from general data rights and authenticate opt-out signals. A site saying “no data sale” does not itself establish lawful practice.

## 4. Technical compliance evidence, not automated legal conclusions

For each product feature, record: (1) business role; (2) whether a resident is a statutory consumer; (3) calendar year and unique resident count, revenue denominator and sales; (4) personal/sensitive data and purposes; (5) privacy notice and requests; (6) controller–processor contracts; (7) children, location and automated-profiling features; (8) precise authority, source version and phase dates; and (9) independent review owner and unknowns.

### Graded exercise

A company processes **36,000 Maryland** consumer accounts, **90,000 Oregon** consumer accounts and earns **10%** gross revenue from data sales. In a separate Oregon scenario it processes **26,000** consumers and earns **30%** gross revenue from sale.

- **Maryland:** 36,000 qualifying resident consumers may satisfy the first threshold, irrespective of the 10% fraction; apply other conditions and exceptions.
- **Oregon first scenario:** 90,000 and 10% alone do not meet either ordinary numerical branch; special actor rules and other laws still need review.
- **Oregon second scenario:** 26,000 and 30% meet the alternative **25,000 and at least 25%** numeric threshold when the other coverage criteria are met.
- **Scoring:** 20 points each for actor/consumer distinctions, thresholds, consent and child/sensitive data, governance/evidence, and source-currentness/unknowns.

**Current review boundary:** the prior Oregon 2026 direct-amendments table access failure is **resolved narrowly** in [Milestone 18](10-oregon-session-law-reconciliation.md); full Maryland 2025–2026 codification diff, comprehensive new/uncodified law inventory, judicial history, product-specific applicability and 50-state scope remain open. No complete government texts or third-party manuals reproduced.