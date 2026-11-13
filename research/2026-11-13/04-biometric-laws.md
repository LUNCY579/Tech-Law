# Biometrics: collection-stage rules, current damages and AI exceptions

**As of:** 2026-11-13. Adapted and corrected from the uploaded Milestone 15 discussion. A photograph, video, face-geometry template and identity-matching embedding must be classified separately using the statute and actual use.

## Illinois BIPA

[740 ILCS 14/10](https://ilga.gov/legislation/ilcs/fulltext?DocName=074000140K10) defines biometric identifier and information, with explicit exclusions. [Section 15](https://www.ilga.gov/legislation/ilcs/fulltext?DocName=074000140K15) addresses retention/destruction policy, notice and written release before covered collection, restrictions on profit/disclosure and care in storage/transmission. Section 20 provides private enforcement subject to its terms.

**Important amendment:** [Public Act 103-769](https://www.ilga.gov/Legislation/publicacts/view/103-0769), effective August 2, 2024, updated the written-release definition to recognize electronic signatures and modified recovery for repeated same-person/same-method captures or disclosures. Old summaries assuming an independent recovery for every scan should not be quoted as current law without analyzing §20(b)–(c).

**Hypothetical:** An online identity-assessment service stores a student's face-geometry template alongside webcam recordings. First classify the template and company, then evaluate whether §15 notice/release, purpose, retention and third-party disclosure rules apply. A broad general website privacy notice is not a substitute for a documented analysis of the BIPA release requirement.

## Texas commercial biometric collection and the 2026 AI amendment

[Texas Business & Commerce Code §503.001](https://statutes.capitol.texas.gov/?artSec=503.001&chapter=BC.503&code=BC&tab=1) generally addresses notice and consent for capture of covered biometric identifiers for commercial purposes, permitted disclosures, protection and destruction. Its current text reflects **H.B. 149 (2025), effective January 1, 2026**, which adds AI-related provisions and exceptions.

In particular, **§503.001(e)(2)** creates an exception for certain model/system development, training, evaluation and related activity unless a system is used or deployed to uniquely identify a specific person. Other listed exceptions include specified security/fraud purposes. Under **§503.001(f)**, subsequent commercial use outside the referenced exception can trigger possession/destruction obligations and penalties. These exceptions are carefully conditioned; neither "all AI training is exempt" nor "every model embedding requires consent" is legally defensible shorthand.

Texas enforcement (including Attorney General civil penalties) should not be conflated with Illinois BIPA's private-right-of-action structure.

## Washington: commercial-purpose enrollment, not a universal BIPA rule

[RCW 19.375.010–.040](https://app.leg.wa.gov/RCW/default.aspx?cite=19.375.020) is materially different from Illinois and Texas. Its definition of **commercial purpose** concerns identifier sale/disclosure to a third party for unrelated marketing, and **enrollment** refers to a qualifying reference-template database. **§19.375.020(1)** provides alternatives of notice, consent **or** a mechanism preventing subsequent covered commercial use. **§19.375.020(7)** has a security-purpose exception, and **§19.375.030(2)** provides Attorney-General-only enforcement. Definitions and photograph/audio/video exclusions must be checked precisely. Read the [full Washington/Illinois/Texas comparison and exercises](15-washington-biometric-privacy.md) before assigning the same legal obligations to all three states.

## Comparative exercise

A research team trains a general-purpose model from lawfully obtained images. Later, a customer enables identification of a named person from a face embedding, while another customer uses the model solely to detect fraudulent login attempts.

Ask: what identifier or data is collected; by whom; which state and commercial purpose; whether the AI exception still applies after redeployment; whether use uniquely identifies someone; what consent, retention, sharing and processor evidence exists? The answer differs between development, fraud prevention and identification products.

## Implementation evidence

Create inventory rows for raw media, templates/embeddings, intended purposes, controllers/vendors, retention schedules, notice and electronic release versions, deletion propagation, security safeguards, risk assessment and any exemption analysis. Do not reuse a biometric consent proof for an unrelated secondary purpose without renewed legal analysis.

**Source quality:** Illinois current code and 2024 public act, plus Texas current official statute directly reviewed. Legal definitions, exceptions and case history still require project-specific review.