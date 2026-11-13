# Chapter 1 — Jurisdiction is a product property

## Learning goals
Identify separate sources of territorial scope, distinguishing U.S. incorporation, host location, customer destination, data subjects, downstream decisions, cross-border employees and payment collection.

## 1. Six different connecting factors
**Place of incorporation** determines entity formation law, not the exclusive laws governing product sales. **Business establishment**, **consumer location**, **targeted market**, **location of data processing**, **end-user activity**, and **effects of an automated decision** may trigger distinct rules.

A Delaware corporation hosting in Virginia may have German customer-facing obligations if it provides relevant services in Germany. Conversely, an informational website reachable in France does not automatically meet every European statute's scope test.

### Example: AI hiring assessment product
A U.S. company sells to an EU employer, operates a scoring API in the U.S., receives candidate information in Germany and sells an authenticated score. Analyze separately:
- GDPR **Arts. 2–3** (material/territorial scope), **Arts. 4, 6, 28** (roles, legal bases and processors), **Chapter V** (transfers). [Official GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- AI Act **Arts. 2–3, 6**, **Annex III** (scope, provider/deployer, high-risk category), and transitional effective dates. [Official AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline).
- Contract: governing law, jurisdiction, order of precedence, service-specific terms, data protection addendum and dispute resolution.
- Public claims: “verified score” versus scientifically validated employment predictions.

## 2. Formalize the expansion analysis
Create a jurisdiction table with: customer region, candidates' location, data residency, model vendor and subprocessors, online marketing, operator role, currency, taxes, mandatory consumer rights, employment regulation, and **legal basis/source** for each conclusion.

**Do not assume:** A privacy policy saying “Delaware law governs” eliminates GDPR or EU mandatory consumer laws. Contract governing law and statutory territorial reach are different legal questions.

## 3. Market-entry gate
Decide whether you're selling a general-purpose tool, hosting user-generated content, performing professional/regulated assessments, or making binding high-stakes decisions. Each change can alter the analysis.

### Worked comparison
**Scenario A:** U.S.-only coding IDE with a few EU visitors who do not purchase and are not monitored.  
**Scenario B:** A paid German-language AI screening product sold to German HR departments, receiving German candidates' CVs.  
**Discussion:** B contains stronger evidence of EU market targeting and employment-specific intended purpose. A needs factual analysis rather than a blanket EU-law exemption.

## Exam
Explain in 500 words why a U.S. vendor's Delaware certificate, AWS region, website language, billing country and model-output destination are **five separate facts**. List the laws to check before expanding to the EU.

**Model outline:** Entity status, data-processing scope, product/market scope, contractual obligations, consumer protections, and international tax must be checked independently. Do not conclude applicability solely from one field.

**Source references:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj); [EU AI Act official timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline); [EU Digital Services Act Commission guidance](https://digital-strategy.ec.europa.eu/en/faqs/digital-services-act-questions-and-answers).
