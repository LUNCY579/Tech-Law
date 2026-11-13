# Chapter 4 — U.S. export controls and economic sanctions for AI/software founders

**Educational caution:** Export classifications, controlled destinations and sanctions restrictions change quickly. This book does **not** make an export-classification determination for any actual model, weight file, chip, encryption package or inference service.

## 1. EAR is an item-and-transaction analysis
The U.S. Export Administration Regulations (EAR), **15 CFR Parts 730–774**, cover certain exports, reexports, transfers, releases of technology/source code and other transactions. The key questions include:
1. Is the item/activity **subject to the EAR** under Part 734?
2. What **ECCN** or EAR99 classification applies, using the Commerce Control List and facts?
3. What are the destination, end user, end use and any intermediary?
4. Which general prohibitions, restrictions, license requirements or exceptions apply under Part 736 and other applicable parts?
5. Are recordkeeping, screening, reporting or other procedural requirements triggered?

Official [BIS Part 734](https://www.bis.gov/regulations/ear/734), [Part 736](https://www.bis.gov/regulations/ear/736), [Part 740](https://www.bis.gov/regulations/ear/740), [Part 742](https://www.bis.gov/regulations/ear/742).

## 2. Open source and encryption do not automatically mean “no controls”
Some publicly available software or technology may fall outside the EAR under defined conditions; separate encryption provisions, publication/notification, license exceptions and restrictions may matter. [EAR §734.7–§734.17](https://www.bis.gov/regulations/ear/734) require close reading. “We put it on GitHub” is not a valid classification memo.

BIS controls can apply to certain advanced computing chips, associated software, technology and end uses. Do **not** automatically infer the same controls apply to every model weight file or publicly accessible API. Classification and current rule text govern.

## 3. Deemed exports and controlled technology access
Releasing certain controlled technology or source code to foreign persons can raise *deemed export* questions; the individual's current physical location and regulatory definitions matter. Export restrictions do not necessarily prohibit all international collaboration. Determine applicability before granting production-model access or restricted engineering documentation to contractors.

## 4. OFAC sanctions are a separate regime
The U.S. Treasury's Office of Foreign Assets Control administers sanctions programs and restrictions that can concern destinations, blocked persons, ownership, payments and services. A transaction might need **both** EAR analysis and OFAC analysis. Screening a person against one list is not a complete sanctions review.

[OFAC compliance framework](https://ofac.treasury.gov/recent-actions/20190502_33) (2019 official guidance) sets out risk assessment, management commitment, internal controls, testing/auditing and training. It is guidance, not a universal statutory checklist. Check actual program-specific prohibitions and licenses.

## 5. Startup cases (hypothetical)
**A — Global model downloads:** A U.S. company offers downloadable models and encryption features. Capture export scope, exact artifact and version, destination, recipient, license classification, end use and available authorization; don't promise worldwide access by default.  
**B — Restricted customer subscription:** A payment attempt originates from a higher-risk destination. Do not rely only on geolocation/IP; gather sanctions program rules and permissible licensed exceptions, and design a false-positive review pathway.  
**C — Research collaboration:** A U.S. employee proposes sending proprietary controlled engineering documents to an international team. Check Part 734 release rules, classifications and authorization; do not confuse publication of noncontrolled information with permission to export controlled technology.

## Exercise and answer
**Prompt:** “Our AI software is free, therefore U.S. export rules do not apply.”  
**Model answer:** Incorrect. Price is not the determining element. Analyze the item/activity, EAR subject status, classification, destination, end user/end use, any licenses or exceptions, and separate sanctions programs. Free access may matter to factual classification in particular provisions but does not erase all rules.

**Practical deliverable:** An export-control worksheet with fields for exact software/model artifact, relevant ECCN, classification evidence, recipient screening date, destination, end-use statement, sanctions review, license decision owner, legal-review status and release gate.
