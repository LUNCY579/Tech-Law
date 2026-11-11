# Lesson 05 — Privacy, consumer protection, retention and deletion

**Goal:** Translate actual data flows into legal issue spotting and engineering controls.

## 1. Start with what the system does, not the privacy policy
A real data map should include: data field; subject; source; purpose; storage location; processor; access roles; retention; deletion mechanism; data transfer; legal justification (where applicable); and evidence of consent or other legal basis.

## 2. U.S. FTC deception and unfairness
[Law] FTC Act §5, 15 U.S.C. §45(a)(1), addresses deceptive and unfair acts/practices in commerce. §45(n) sets statutory parameters for unfairness. [Official U.S. Code](https://www.govinfo.gov/link/uscode/15/45).

**Real regulatory proceeding:** *In re Everalbum, Inc.*, FTC File No. 192-3172. The FTC alleged misrepresentations about face recognition and deletion after deactivation; settlement obligations included deletion measures affecting models developed from the relevant data. **A settlement resolves allegations; do not present it as a litigated judicial finding.** [FTC docket with complaint and order](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter).

## 3. State and international privacy are conditional
California CCPA/CPRA: evaluate whether the organization qualifies as a regulated business, whether data is personal information, what consumer rights apply, exemptions, notice requirements, service-provider restrictions, verification, and exceptions. See [California Civil Code §1798.100 et seq.](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5) and [CPPA regulations](https://cppa.ca.gov/regulations/).

EU GDPR: read Article 3 (territorial scope), Article 5 (principles), Article 6 (lawfulness), Articles 12–23 (rights), Article 28 (processors), Article 32 (security), and Articles 33–34 (breach notifications). These provisions **are not interchangeable**, and rights have exceptions. [Official EUR-Lex GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## 4. Children's data
[Law] COPPA, 15 U.S.C. §6502, applies to covered child-directed operators and certain other operators with actual knowledge of collection from children under 13; it is not correctly summarized as “every app needs age consent.” [Official statute](https://www.govinfo.gov/link/uscode/15/6502). Check the current FTC COPPA Rule and amendments for details.

## 5. Design and verification
Build deletion as an auditable workflow: authenticated request → eligible data scope → exception check → primary records → indexes/embeddings → subprocessors → backups under documented lifecycle → confirmation. “Delete account” is not a substitute for a tested system-wide deletion mechanism.

## Hypothetical
A resume-processing AI retains candidate PDFs indefinitely for training but the UI says “processed for this job only.” Analyze actual representations, vendor pipelines, employment context, rights requests and deletion propagation.

## Exercise
Classify these as legal requirements, context-specific obligations, or engineering best practices: cookie banner on every page; encryption at rest; access controls; data inventory; one-click deletion; documented breach response.

**Answer:** None can be universally asserted without facts. Encryption, access controls, inventories and response plans are often prudent and may support compliance with applicable legal standards; exact duties depend on jurisdiction, data, contract and industry. Cookie consent, deletion mechanisms and response deadlines vary by regime.

## Sources
- [FTC Act §5](https://www.govinfo.gov/link/uscode/15/45) [law].
- [FTC Start with Security](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) [guidance based on enforcement matters].
- [FTC Everalbum case](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter) [settlement].
- [California CCPA statute](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5) [law].
- [GDPR official text](https://eur-lex.europa.eu/eli/reg/2016/679/oj) [law].

## Advanced seminar — data-subject rights and implementation

### A. Read applicability first
California privacy law requires assessing the entity's covered-business status and exceptions, not simply whether any California resident visits a site. The CPPA publishes **CCPA regulations effective January 1, 2026** and related current threshold information. Check the currently effective text, not 2023-era summaries. For the GDPR, Article 3's territorial criteria precede Articles 5 and 6 compliance analysis.

### B. Separate privacy concepts
- **Notice**: accurate explanation of collection, use, sharing and rights.
- **Consent**: one possible legal basis, not universally the only one (GDPR Article 6).
- **Access/deletion**: context-specific rights with exceptions, verification and scope limitations.
- **Processor/controller**: determine role from actual purposes and means rather than an arbitrary label.
- **Breach response**: applicability, awareness, risk, deadlines and notification actors vary.

### C. *Everalbum* mini brief
**FTC file:** 192-3172. **Complaint:** alleged deceptive representations regarding face recognition and retained user photos/videos. **Resolution:** 2021 final consent order; do not describe allegations as judicially proven findings. **Engineering translation:** maintain a feature-level use inventory and test deletion propagation through learned artifacts where order, contract or law so requires.

### D. Example deletion trace
Request ID → verification proof → identity scope → legal exceptions → application DB → vector index → object store → processor notification → backup expiration → final evidence entry. Never log unnecessary sensitive content in the deletion audit itself.

### E. Practice scenario
A candidate requests deletion during an active employment dispute. How do you handle competing obligations? **Answer framework:** identify governing right, lawful exceptions/retention duties, actual records and processors, preservation obligations and documented rationale; avoid automatic blanket deletion or indefinite retention.
