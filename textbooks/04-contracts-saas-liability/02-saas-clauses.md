# Chapter 2 — SaaS and AI contract anatomy

## 1. Read a business deal as allocated risk
A typical SaaS commercial stack may include an **MSA**, order form, SLA, DPA, acceptable-use policy, product-specific AI terms and vendor subprocessor terms. Every document can have different parties, versions, jurisdiction and precedence. The goal is not to paste boilerplate; it is to align legal representations with actual architecture.

| Clause | Questions | Evidence |
|---|---|---|
| Service description | What functionality and human oversight promised? | Versioned product scope |
| Payment and renewal | Billing triggers, tax, notices, refunds and termination? | Checkout / billing tests |
| Security/availability | Express warranties, SLOs and exclusions? | Incident history and measured metrics |
| Data processing | Controller/processor roles, vendors, purpose, transfers? | DPA and data flow map |
| Customer content | Who owns inputs, processing license, generated results? | Rights inventory |
| AI behavior | Model changes, prohibited uses, output review and residual risks? | Version logs, evaluations |
| Indemnity | What third-party claims; who defends and controls settlement? | Specific clause and exceptions |
| Liability limits | Cap baseline, exclusions, special carveouts? | Pricing and financial exposure |
| Termination | Export, deletion/retention, backup lifecycle? | Tested workflow |
| Precedence | MSA vs order vs promotion vs DPA conflicts? | Signed versions |

## 2. Disclaimers are not immunities
A contract saying “all AI results are guaranteed correct” may create substantial exposure if unsupported. A contract saying “we have no responsibility whatsoever” cannot automatically override statutory consumer remedies, privacy laws, fraud principles, or all contract-law restrictions. The real enforceability depends on exact language, governing law and the type of harm.

## 3. Model provider subcontracting
Example: A SaaS product says “customer content stays in the U.S.” but routes AI prompts and observability logs internationally. Check **all** downstream data recipients, the meaning of “stay,” subprocessors and provider configurations. A DPA with a misleading architecture diagram may not solve the contradiction.

## 4. Limitation of liability math
If an MSA caps ordinary contractual damages to “fees paid in prior 12 months,” a $100/month customer paying 12 months might suggest $1,200 cap **only for claims actually governed by that clause**. Whether the cap applies to personal-data leakage, IP claims or gross negligence depends on exceptions, statutory rules and judicial enforceability. Never treat a sample arithmetic cap as a prediction of ultimate liability.

## Practical assignment
Draft a **contract-to-implementation traceability matrix** with 20 promises and a software test or audit artifact per promise. Flag “not measured” instead of claiming success.

**Legal anchors:** [FTC §5](https://www.govinfo.gov/link/uscode/15/45), [GDPR Art. 28](https://eur-lex.europa.eu/eli/reg/2016/679/oj) when applicable, [Coinbase opinion](https://www.supremecourt.gov/opinions/23pdf/23-3_879d.pdf). These are distinct legal sources with different scopes.
