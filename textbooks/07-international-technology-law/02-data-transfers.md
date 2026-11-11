# Chapter 2 — International data transfers, DPF, SCCs and vendors

## 1. Start with GDPR applicability and roles
Before invoking international-transfer mechanisms, determine whether GDPR applies (Arts. 2–3), which organization controls purposes and means (Art. 4), the lawful basis (Art. 6), and whether there is a relevant transfer under Chapter V. Even a lawful transfer **does not independently legalize the underlying processing**.

[GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## 2. Adequacy: Article 45
A Commission adequacy decision permits specified covered data flows without the additional Chapter V safeguard otherwise needed for that destination/organization. The coverage is not always countrywide. For example, the Commission's U.S. decision concerns **participating organizations in the EU–U.S. Data Privacy Framework**. Verify the recipient's active participation and coverage; do not treat any U.S. vendor as automatically adequate.

**Official references:** [European Commission adequacy list](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en); [U.S. DPF program FAQ](https://www.dataprivacyframework.gov/program-articles/FAQs%E2%80%93General).

**Critical distinction:** DPF is a transfer mechanism for eligible certified organizations, **not a general GDPR compliance certification**. Data-minimization, transparency, security, lawful processing and other rules still matter.

## 3. Standard Contractual Clauses: Article 46
The Commission adopted modernized SCCs on **4 June 2021**. The SCCs have modules for controller-to-controller, controller-to-processor, processor-to-processor and processor-to-controller flows. Select the module according to the **actual** exporter/importer roles; complete technical/organizational-measure annexes and onward transfer specifications.

Official [Commission SCC page](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_fr) and [Commission implementation Q&A](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/new-standard-contractual-clauses-questions-and-answers-overview_en).

SCCs require assessment of the destination-country circumstances and possible supplementary measures where applicable. Merely attaching uncompleted clauses to a DPA is not sufficient evidence of compliance. A separate GDPR Article 28 agreement may also be relevant depending on the roles; some SCC modules incorporate Art. 28 duties.

## 4. What the transfer map includes
| Movement | Roles to determine | Evidence needed |
|---|---|---|
| German candidate → EU customer | controller/processor | collection notice, legal basis, contract |
| EU customer → U.S. SaaS | exporter/importer | adequacy or Art. 46 instrument, scope |
| U.S. SaaS → model inference provider | roles and onward transfer | vendor location, retention, contract, region |
| EEA administrator → non-EEA support contractor | remote access/control | access rights, transfer determination, controls |
| Backup replication | actual data recipient and location | keys, replication regions, deletion timeline |

## 5. The *Schrems II* historical anchor
*Data Protection Commissioner v. Facebook Ireland and Schrems*, C-311/18 (CJEU, 16 July 2020), is a foundational decision on international transfers. Read the [official EUR-Lex case page](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62018CJ0311) before quoting. This case concerned an earlier adequacy framework; do **not** assert without current legal research that the 2023 DPF has been automatically invalidated. Subsequent adequacy and court developments must be reviewed separately.

## 6. Hypothetical and model answer
A U.S. startup says “all candidate data stays in the EU” but uses a U.S.-hosted LLM API with logging. **Issue spotting:** truth of geographic claim, vendor access and storage locations, controller/processor role, GDPR Chapter V mechanism, SCC or DPF eligibility, legal basis for inference, Art. 28 arrangements, security and rights. **Mitigation:** map every transfer and subprocess, configure actual regional routing or correct the claim, document contracts and evaluate the precise transfer mechanism.

### Independent assignment
Write a transfer impact assessment outline with facts, source law, transfer frequency, recipients, categories of data, destination-country factors, security measures, contractual promises and review date. **This is a study artifact, not a ready-made compliance certification.**
