# Milestone 18A — Oregon 2026 session-law reconciliation

**Reviewed:** November 13, 2026. **Scope:** direct amendments indexed for ORS 646A.570–646A.589, related 2026 privacy/data-broker enactments, and the separately enacted 2025 changes with 2026 operative dates. **Not** a general confirmation that every new uncodified Oregon law or every case-law development was exhausted.

## 1. Resolve the old 403 blocker using a different official publication

Milestone 17B reported that the chapter's linked 2026 amendments table returned a 403 error. The official **Legislative Counsel [2026 ORS update portal](https://www.oregonlegislature.gov/lc/Pages/ORSupdate.aspx)** and the consolidated **[2026 Oregon Laws A&R table](https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2026OrLawAR.pdf)** were subsequently retrieved and the relevant page read as an image.

- **2026 regular session, A&R table RS26-T-4 (PDF page 4):** lists **646A.115**, changed by Oregon Laws 2026 chapter 9 §1 (**HB 4024**), and **646A.694**, changed by chapter 109 §35 (**HB 4040**). It lists **no direct amendment or repeal of ORS 646A.570–646A.589**. This is a finding about *the table's amendment entries*, not every newly enacted related law.
- **[2025 special-session A&R table](https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2025S1OrLawAR.pdf), SS25-T-1 (PDF page 1):** also lists **no ORS 646A.570–646A.589 amendment**.
- **[Legislative Counsel instructions](https://www.oregonlegislature.gov/lc/ORSupdate/instructions.pdf):** explain why the online **2025 ORS** is not a free-standing record of 2025 special-session and 2026 regular-session amendments and why both session-law tables must be consulted.

**Disposition:** the **narrow 2026 direct-amendment-index access issue** is resolved and has a dated official-source receipt. This does **not** prove that no uncodified law, new law added to a chapter, agency rule, referendum, judicial development or later legislation affects a given product. Review [the remaining verification gates](../../quality/MILESTONE18_OREGON_SOURCE_AUDIT_2026-11-13.md).

## 2. Distinguish 2025 legislation that became operative in 2026

The prominent 2026 Oregon privacy obligations largely come from **Oregon Laws 2025, chapter 251, HB 2008** (not an amendment enacted in the 2026 regular session). [Official enrolled-bill overview](https://olis.oregonlegislature.gov/liz/2025r1/Measures/Overview/HB2008) confirms chapter number and scope. The state-published [ORS 646A.578](https://www.oregonlegislature.gov/bills_laws/ors/ors646a.html) records the enrolled changes and current section text.

| Current provision / subject | Targeted statutory point | Implementation distinction |
|---|---|---|
| **ORS 646A.578(1)(d)** | A covered controller offers revocation of consent by a means **at least as easy** as giving it and generally stops covered processing **as soon as practicable, no later than 15 days** after revocation | A consent-revocation deadline is **not** the 45-day response period for some access/rights requests |
| **ORS 646A.578(2)(c)** | Restricts targeted advertising or legally significant profiling when controller has actual knowledge or willfully disregards that consumer is **under 16** | Does **not** describe every ad to every minor; inspect purpose and knowledge trigger |
| **ORS 646A.578(2)(d)(A)** | Restricts **sale** of personal data about a consumer known/willfully disregarded to be under 16 | Distinguish sale from internal processing and other statutory protections |
| **ORS 646A.578(2)(d)(B)** | Restricts sale of covered information capable of identifying present or past location to **within a radius of 1,750 feet**, with statutory exclusions | It is **not** a universal prohibition on all location processing; don't erase exceptions |
| **ORS 646A.578(5)** | Opt-out mechanism allowing a recognized consumer/agent signal, including qualified universal opt-out technology | The signal rules and exceptions differ from a generic account deletion request |

**Temporal discipline:** the 2025 chapter 251 amendments became operative **January 1, 2026**. The **2026 regular-session A&R table** showing no direct amendment to these same OCPA sections does not conflict with earlier law taking effect in 2026.

## 3. A genuinely new 2026 data-broker rule: SB 1587

[**Oregon Laws 2026, chapter 96 (SB 1587), §1**](https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2026orLaw0096.pdf) was read directly and visually inspected (single-page official Oregon Laws PDF). It is **effective June 5, 2026**. It uses the **ORS 646A.593** definition of `data broker` and the ORS 432.005 definition of `personally identifiable information`.

Subject to subsection (3)'s exceptions, **a public body** may not disclose covered personally identifiable information **to a data broker** unless the broker first provides a written attestation that the information will not be sold or transferred to an entity using it to enforce federal immigration law. A public body must reject an attestation it reasonably believes contains material misrepresentations, falsehoods or omissions. Exceptions include certain court-ordered, legally required and generally available information disclosures.

**What this does not say:** This enactment is **not** a blanket ban on every private-to-private data broker sale, a repeal of OCPA, or an amendment to every OCPA controller obligation. The statutory rule's key obligated actor is the **public body**. The broker has an attestation role. It is distinct from the pre-existing data broker registration scheme at **ORS 646A.593**.

## Milestone 19 follow-up: Oregon's separate 2026 ALPR statute

The narrower 2026 A&R index review did **not** capture the separately enacted **[Oregon Laws 2026, chapter 77 (SB 1516)](https://www.oregonlegislature.gov/bills_laws/lawsstatutes/2026orLaw0077.pdf)**, effective March 31, 2026. Sections 3–9 regulate Oregon **law-enforcement agencies'** automated license-plate reader systems, captured data and the **vendors contracting with those agencies**. See the [new sector-specific casebook](12-oregon-alpr-law-and-vendor-contracts.md) and [official source receipt](../../quality/MILESTONE19_OREGON_ALPR_SOURCE_AUDIT.md). This is **not a direct amendment to ORS 646A.570–646A.589**, nor a general ban on ordinary private vehicle telemetry; it confirms why an indexed code section is **not** a complete search of new or uncodified law.

## 4. Founder and engineering scenarios (synthetic)

**Game analytics:** An SDK captures a user's exact location. Apply OCPA threshold and controller/processor facts first, then ask whether data are sold, whether they locate within the statutory radius, whether the SDK receives a universal opt-out signal, and how consent revocation is enforced. Do not equate a marketing statement (“we do not sell”) with a completed data-flow review.

**Government-data startup:** An API purchases Oregon public-body datasets through a broker. Map the public body's disclosure, the broker's attestation, actual onward transfers and the applicability of statutory subsection (3) exceptions. A sale from another private actor may involve different laws; chapter 96 alone does not resolve it.

**AI hiring assessment:** Employment-context exclusions and other employment statutes remain relevant. An Oregon resident's ZIP code is not automatically equivalent to a covered precise location dataset, and neither OCPA thresholds nor use-purpose classification can be assumed from the service's title.

## 5. Evidence status

| Item | Source read | Result | Unresolved |
|---|---|---|---|
| 2026 amendment status for **existing** ORS 646A.570–.589 | Official 2026 A&R table, image-checked RS26-T-4 | No direct changes to those numbered sections listed | New/uncodified enactments must be checked separately |
| 2025 special-session direct changes to those sections | Official 2025 S1 A&R table, image-checked SS25-T-1 | No entries | General session-law scope still matters |
| 2026 changes traceable to **2025** HB 2008 | State-published ORS 646A.578, official enrolled bill overview and DOJ | Operative provisions identified separately from enactment year | Product-specific applicability and all exceptions |
| 2026 chapter 96 | Official enacted one-page statute, image-checked | Independent data-broker/public-body rule effective June 5, 2026 | Enforcement history, additional sectoral law |

No wholesale statute reproductions, attorney opinion, external source licensing assumption or legal compliance certification is included.
