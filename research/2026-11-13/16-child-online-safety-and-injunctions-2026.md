# Milestone 21B — children's online-safety law: text, replacement and judicial posture

**As-of:** November 13, 2026. **Scope:** two carefully distinguished legal histories: California's Age-Appropriate Design Code (AADC) and its enacted 2026 replacement, and Texas's SCOPE Act / 2026 Fifth Circuit litigation. This is an educational **issue-spotting** casebook, not a statement that an entire state statute is enforceable or unenforceable against any particular business.

## 1. Start with three independently dated sources

1. **Statute:** What was enacted, what provisions and actors it actually covers, and which version is operative on the relevant day?
2. **Judicial order:** What *court*, *docket*, *date*, *procedural posture*, *parties* and *specific provisions* are affected by an injunction, appeal or vacatur?
3. **Subsequent law/order:** Has a legislature replaced the statutory text, or has an appellate court vacated its own prior panel opinion? An old litigation summary may have become materially stale overnight.

In particular, **an appellate panel opinion vacated for en banc rehearing is not a current controlling panel precedent**. Nor does vacating a panel opinion, *by itself*, establish that every district-court injunction below is automatically dissolved. Follow the separate operative injunction, stay and mandate records.

## 2. California: *NetChoice v. Bonta* concerns the original 2022 law

The Ninth Circuit's **March 12, 2026** opinion in [*NetChoice, LLC v. Bonta*, No. **25-2366**](https://cdn.ca9.uscourts.gov/datastore/opinions/2026/03/12/25-2366.pdf) was issued in an **interlocutory preliminary-injunction appeal** concerning the **2022 California Age-Appropriate Design Code Act**, then codified at Civil Code §§1798.99.28–1798.99.40. The court **affirmed** the preliminary injunction against the challenged **data-use restrictions**, former **§1798.99.31(b)(1)–(4)**, and **dark-pattern restriction**, former **§1798.99.31(b)(7)**, on the described vagueness record. The court **vacated** broad whole-act preliminary relief and the separate injunction against the former **age-estimation requirement**, **§1798.99.31(a)(5)**, and remanded. The prior appeal had also addressed the risk-assessment/mitigation requirement and the question of severability.

**Precise lesson:** This was not a final merits judgment permanently invalidating all of the California AADC, and a court vacating one injunction does not itself certify that the provision is legally valid in every application. The **court's summary is explicitly not part of its opinion**; use the majority analysis and procedural disposition for citations. Official PDF pp. 3, 6–7 and 27–29 were inspected, including the printed opinion summary's limits.

### Then California enacted a replacement

California **AB 2246, Chapter 187 (2026)** was **signed September 10, 2026**. The [Governor's official September 10 announcement](https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/) independently confirms signature of AB 2246. The **chaptered bill** is available as a [third-party reproduction of the chaptered text](https://legiscan.com/CA/text/AB2246/id/3458541/California-2025-AB2246-Chaptered.html); the [California Legislature's bill portal](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB2246) returned **403**, so **the official hosted chaptered text was not directly authenticated** in this pass.

The signed bill's first two operative sections **repeal and add** Civil Code Title 1.81.47. Its replacement chapter continues to concern services likely accessed by **children under 18** and addresses age estimation or child-level protections, privacy defaults, disclosures, collection/profiling, geolocation, dark patterns, harm prevention, contract voidability and public enforcement, subject to the exact chaptered limitations and exceptions. The enacted measure has **no urgency clause shown in the chaptered copy**. Under the general California statutory-effective-date framework, the replacement is reported to take effect **January 1, 2027**, not retroactively in March 2026; this timing needs a live official-code check before product deployment.

**Crucial version warning:** The 2026 statutory **replacement** reuses the Title 1.81.47 numbering, but its **subsection numbers and language differ** from the 2022 AADC. Do **not** transpose a March 2026 injunction against the old **§1798.99.31(b)** to the newly enacted text, where **§1798.99.31** concerns a **child's ability to void certain contractual provisions**. A future-effective replacement does not erase the need to separately examine the historical statute and court orders for conduct occurring before 2027.

**Example:** A game studio in California preparing a January 2027 launch should review **the replacement AB 2246 chapter** as a prospective product requirement **and** the actual operative statute as of the launch date. It must not use a March 2026 injunction summary as proof that every future California child-safety duty disappeared.

## 3. Texas: the July 24 panel result was expressly VACATED on October 28

The [Texas Business & Commerce Code Chapter 509](https://tcss.legis.texas.gov/resources/BC/htm/BC.509.htm), enacted by **HB 18 (2023)** and generally effective **September 1, 2024**, contains the **SCOPE Act** restrictions on certain providers of digital services used by **known minors under 18**. Under **§509.002**, covered services typically combine social interaction, account profiles and posting/viewing user-generated content; the statute contains enumerated exceptions. **§509.057** has distinct application language and must be examined independently rather than assuming every provision shares the same coverage gate.

**The judicial chronology matters:**

| Date | Source | Exact procedure and status |
|---|---|---|
| **Aug. 30, 2024; Feb. 7, 2025** | Western District of Texas orders in two distinct pre-enforcement actions | Various **preliminary injunctions** were entered against specified restrictions; identify the parties and provision separately |
| **July 24, 2026** | [Fifth Circuit panel opinion, Nos. **24-50721/25-50096**](https://www.ca5.uscourts.gov/opinions/pub/25/25-50096-CV0.pdf) | The panel addressed Section 230 preemption, constitutional and standing issues and altered some injunction results; this is **historical only after Oct. 28** |
| **October 28, 2026** | [Official Fifth Circuit **en banc** order, Doc. 224-1](https://www.ca5.uscourts.gov/opinions/pub/25/25-50096-CV1.pdf), p. 2 | Court **granted rehearing en banc and expressly VACATED the July 24, 2026 panel opinion** under Fifth Circuit Rule 41.3. This is the later verified order as of Nov. 13 |

The **October 28 order** does not decide the underlying First Amendment or preemption merits and does not itself specify a comprehensive final enforceability map of each district injunction. Therefore **do not cite the July 24 panel's affirmance/reversal as binding appellate law in November 2026** and **do not infer all of HB18 is enjoined, invalid, or freely enforceable** from the two-page rehearing order. A service-specific, provision-by-provision injunction/stay, affected party, and later docket check remains necessary.

### Texas actor/applicability exercise

A multiplayer platform has an account profile, game chat and community-created content, but its main function is playing games. Does Chapter 509 cover it? The analysis begins at **§509.002** and its exemptions, the intended content and social features, purpose/control of data, the known-minor definition and the specific legal duty in question. A **mere incidental chat feature** may implicate a statutory exception; another service designed primarily around social posting may be classified differently. The vacated panel opinion is **not** a legal safe harbor.

## 4. Explicit litigation-status matrix

| Question | California AADC | Texas SCOPE Act |
|---|---|---|
| Law version | 2022 law litigated in **March 2026**; enacted **AB2246/Ch187 (2026)** replaces Title 1.81.47 for the next legal period | 2023 **HB18**, Chapter 509 (generally Sept. 2024) |
| Primary appellate event | **March 12, 2026 Ninth Circuit** narrowed/altered preliminary injunction; remand, **not final merits** | **October 28, 2026 Fifth Circuit** granted **en banc** rehearing and **VACATED** July panel opinion |
| What remains uncertain | Specific 2026 district-court proceedings, effect on historical conduct, version and effective date of replacement, future injunctions | Current district-court injunction scope by plaintiff/provision, any later appellate stay/en banc judgment, actual operator coverage |
| Error to avoid | Citing former **§1798.99.31(b)** as the 2027 replacement's same subsection | Calling the **vacated July 24 panel opinion** controlling precedent |

## 5. Founder exercise (100 points)

Build an online youth community product with user-created profiles, location-based discovery and a game/chat feature. Prepare a decision memo with **20 points** each for (a) statutory actor and age coverage, (b) the **exact time-versioned** California 2022 vs 2026 text, (c) Ninth Circuit procedural and provision-specific scope, (d) the Fifth Circuit **en banc vacatur** vs underlying district injunction status, and (e) engineering evidence and mandatory legal unknowns.

**Research controls:** preserve official court PDF references, order date and exact affected sections. Preserve official government enactment confirmation separately from the **unverified direct California Legislature bill-viewer access**. Do not reproduce full court texts, do not claim complete Shepard's/KeyCite review and do not turn an editorial source ledger into an automated legal-compliance approval.

[Milestone 21 court/source audit](../../quality/MILESTONE21_CHILD_SAFETY_LITIGATION_AUDIT_2026-11-13.md).