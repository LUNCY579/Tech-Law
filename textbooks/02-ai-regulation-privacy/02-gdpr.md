# Chapter 2 — GDPR: scope, legal basis, privacy rights and AI decision-making

## 2.1 Does the GDPR apply?
**Article 2:** assess material scope. **Article 3:** territorial reach includes processing in the context of a Union establishment and, under conditions, offering goods/services to or monitoring behavior of people in the Union. Mere global accessibility of a web page is not the same as satisfying Article 3.

**Primary:** [GDPR official EUR-Lex text](https://eur-lex.europa.eu/eli/reg/2016/679/oj), Arts. 2–3.

## 2.2 Who controls purposes and means?
**Article 4:** personal data can include identifiers, online IDs and information relating to identifiable individuals. Controller determines purposes and means; processor acts on controller's behalf. Roles must be evaluated per activity, not assigned solely from the contract heading.

**Example:** A customer uploads a CV to an agentic workspace. The workspace processes it for storage/analysis; its provider may act in different roles for core customer instructions, fraud prevention analytics and independent model training. Analyze each processing purpose separately.

## 2.3 Six bases—not “consent for everything”
**Article 6(1)** includes consent; contract necessity; legal obligation; vital interests; public interest/official authority; and legitimate interests subject to conditions. The choice must reflect the actual processing and applicable special-category rules. Blanket consent is not a universal safe harbor. Read Article 9 when special-category personal data are involved.

## 2.4 Fundamental principles
**Article 5(1):** lawfulness, fairness and transparency; purpose limitation; data minimization; accuracy; storage limitation; integrity/confidentiality. **Article 5(2):** accountability. The operational question is whether the *actual architecture* proves those principles for a specific purpose.

## 2.5 Rights and exceptions
**Articles 12–23** include transparency and rights to access, rectify, erase, restrict, portability, object and safeguards against certain automated decisions. **Article 17** erasure is conditional, not absolute; check competing legal obligations and lawful exceptions. **Article 22** concerns decisions based *solely* on automated processing with legal/similarly significant effects, subject to exceptions and safeguards. A superficial “human in the loop” checkbox may be inadequate to demonstrate meaningful human involvement.

## 2.6 Processors and security
**Article 28:** processor requirements and contracts. **Article 32:** security appropriate to risk. **Articles 33–34:** distinct controller-to-authority and data-subject breach notification frameworks. Article 33's qualified 72-hour notification reference does not apply universally to every breach or every company in the world.

## 2.7 Worked exercise
An employment assessment app ingests a candidate's CV, infers traits, sends data to a U.S. API vendor and rejects candidates automatically.

**Analysis sequence:** applicability under Arts. 2–3; roles; Art. 6 legal basis; Art. 9 if relevant; Arts. 13–14 notice; Art. 22 significant solely automated decision question; Art. 28 vendor agreement; Chapter V transfer basis where relevant; Arts. 5 and 32 safeguards; retention and rights workflows.

**Engineering output:** processing register with purposes/legal basis; model and provider version; data-flow map; retention/deletion tasks; access control; transfer risk; appeal and decision record.

### Self-check
**Q:** Can a company choose consent as the basis for all data uses without distinguishing them?  
**A:** No sound conclusion. Consent must meet legal requirements, and some purposes are incompatible or require other obligations; choose the genuine applicable basis on the facts.

**Source:** [GDPR original regulation and articles](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
