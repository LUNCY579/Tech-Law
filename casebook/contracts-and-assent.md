# Casebook I — SaaS agreements, notice, assent, and conflicts

**Learning objectives:** distinguish contract formation from arbitration scope; identify the operative agreement when multiple contracts conflict; design a reproducible assent record.

## 1. Governing legal anchors

- [9 U.S.C. §2 — Federal Arbitration Act](https://www.govinfo.gov/link/uscode/9/2) (federal statute). Arbitration enforcement presupposes an agreement governed by applicable contract principles.
- [*Coinbase, Inc. v. Suski*, No. 23-3, slip op. (U.S. May 23, 2024)](https://www.supremecourt.gov/opinions/23pdf/23-3_879d.pdf) (official majority opinion).
- [*Specht v. Netscape Communications Corp.*, 306 F.3d 17 (2d Cir. 2002)](2026-11-13-historic-opinion-source-clinic.md): court-formatted opinion and reporter text researched; **original issuing-court-hosted copy remains pending**. A later [federal judicial order (GovInfo)](https://www.govinfo.gov/content/pkg/USCOURTS-mad-1_13-cv-11701/pdf/USCOURTS-mad-1_13-cv-11701-0.pdf) cites the notice standard; not a comprehensive citator.

## 2. Verified case brief — *Coinbase v. Suski*

**Parties / posture:** Coinbase users sued over a sweepstakes. Coinbase sought to compel arbitration. The federal district court denied the motion; Ninth Circuit affirmed; Supreme Court unanimously affirmed on May 23, 2024. Verify details in the opinion's **syllabus pp. 1–3 and majority opinion pp. 4–9**; the syllabus itself is not law.

**Facts:** Users accepted an initial user agreement containing an arbitration clause and delegation provision. Separate sweepstakes official rules said California courts had exclusive jurisdiction over disputes regarding the promotion. The agreements conflicted over who would decide whether the dispute was arbitrable.

**Legal question:** When a delegation clause points to an arbitrator but a second agreement points to courts, who decides which agreement governs the particular dispute?

**Holding:** A court resolves the threshold conflict as to which contract controls, notwithstanding the arbitration delegation in the first. This is **not** a blanket holding that a later agreement always supersedes an earlier one in every setting.

**Reasoning architecture:**
1. Arbitration ultimately turns on party agreement.
2. A delegation clause is one way to allocate a threshold arbitrability question.
3. But a conflict between two agreements requires determining what the parties agreed to concerning that *very threshold* question.
4. That contractual-conflict determination must be made by the court. See majority opinion, pp. 4–9 (slip pagination).

**Concurrence / counterargument:** Justice Gorsuch concurred. The defense's theory emphasized the original delegation clause and severability principles; the Court rejected using those principles to avoid the antecedent two-contract conflict. Distinguish that question from deciding the merits of the sweepstakes claim.

**Founder significance:** Terms of Service, subscription order forms, promotion rules, enterprise MSAs, product-specific addenda and data-processing agreements can conflict. Draft an explicit priority/order-of-precedence provision, but recognize enforceability remains fact- and law-specific.

## 3. Historical comparison — *Specht v. Netscape*

**Third-party opinion reproduction inspected; issuing-court original still pending.** Users could download the **SmartDownload plugin** without adequate notice of its license terms located below the download button. A **separate Communicator browser installation** did use affirmative license acceptance; do not conflate the two agreements. The panel held that users lacked sufficiently communicated terms and unambiguous assent to the SmartDownload arbitration clause, and rejected binding a non-signatory website owner based on the attenuated claimed indirect benefit. Its analysis used California law. See the [pinpoint and provenance memo](2026-11-13-historic-opinion-source-clinic.md), plus *Specht*, 306 F.3d at 20, 28–35 (verify original before formal filing).

**Distinguish the two questions:** *Specht* concerns whether the party agreed at all; *Coinbase* concerns which agreement governs and who resolves competing contract terms. A generic “clickwrap always wins” slogan misstates both.

## 4. Startup example — AI workspace SaaS

**Hypothetical A:** During signup the user accepts Terms v3 containing arbitration in New York. Later the user accepts a paid beta program agreement sending all disputes about beta evaluations to Missouri courts. A complaint concerns the beta.  
**Issue 1:** Did the user assent to each agreement, and are the versions authenticated?  
**Issue 2:** Which text governs the claim, and are arbitration/venue clauses conflicting?  
**Issue 3:** Who decides that threshold issue under *Coinbase* and applicable law?  
**Answer:** Do not assume the old arbitration clause controls simply because it has a delegation clause. First compare scope, integration, priority and assent, then apply *Coinbase*'s threshold principle to the identified conflict. Whether the court ultimately orders arbitration depends on text and facts.

## 5. Product controls

| Risk | Engineering artifact |
|---|---|
| Unclear consent | Accessible affirmative action, displayed terms version, screenshot and UI test |
| Disputed assent | Immutable event with user, timestamp, version/hash and capture context |
| Conflicting documents | Contract registry with effective date, scope, hierarchy and owners |
| New terms by stealth | Material-change notice, retrievable old versions and assent policy |
| AI-provider contradiction | Contract/telemetry comparison and customer disclosure review |

## 6. Problems and model answers

**Q1:** A Terms link appears only below a “Start free trial” button. Is arbitration certain to be enforceable?  
**A1:** No. Investigate applicable state assent rules, interface design, user knowledge, notice evidence and *Specht*-type concerns. No single screen placement determines all outcomes.

**Q2:** An enterprise order form says “disputes in state court,” while the standard MSA says “binding arbitration.” What should counsel investigate?  
**A2:** Integration clause, negotiated precedence, signature/acceptance, effective dates, claim scope, law governing contract formation, and the threshold allocation principle recognized in *Coinbase*.

**Q3:** What is the difference between legal validity and strong logging?  
**A3:** Logging proves what the system recorded; it does not itself create informed assent if notice was inadequate.

### Assignment
Draft an order-of-precedence table for terms, MSA, order forms, DPAs and promotion rules. Test four conflicting-clause fixtures; write one page that separates factual findings from the applicable legal doctrine.

**Copyright/reuse:** Original commentary only. The linked Supreme Court opinion is an official judicial source; we do not reproduce its entire text.
