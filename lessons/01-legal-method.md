# Lesson 01 — How to read law like an engineer

**Learning goal:** Identify a rule's authority, jurisdiction, elements, exceptions, and legal status before applying it to a startup. **Jurisdiction:** U.S. federal / state. **Updated:** 2026-11-10.

## 1. Law is not a checklist of slogans

A startup legal question generally follows this chain: **facts → jurisdiction → source of law → legal elements → exceptions/defenses → remedies → operational control**. A webpage's assertion that every startup “must have a cookie banner” misses jurisdiction, technology, audience and exemptions.

### Step 1 — Identify the decision
Example: A Missouri-incorporated SaaS company collects California residents' data and sells AI-assisted recruiting evaluations in the EU. Separate questions arise under state privacy law, U.S. employment law, EU product regulation, contracts, and potentially others. Incorporation in one place does not automatically determine the only applicable law.

### Step 2 — Rank sources by legal authority
- **Constitutions, statutes, regulations:** Text governing the relevant parties within their scope. Check amendments and effective dates.
- **Court opinions:** Holdings govern under applicable precedent principles; distinguish holdings from dicta, trial decisions from appellate precedent, and jurisdictional limits.
- **Agency orders/adjudications:** Read the parties, scope and procedural status. A consent order is not automatically a general judicial holding.
- **Agency guidance:** Useful descriptions or enforcement priorities, but not necessarily legally binding.
- **Blogs, videos, templates:** Starting leads, never final authority.

### Step 3 — Parse a statute using elements
[Law] 15 U.S.C. §45(a)(1) prohibits unfair or deceptive acts or practices in or affecting commerce. §45(n) states conditions for an unfairness determination. Do not treat “unfair” as interchangeable with “deceptive”: they are separate analyses. [Official U.S. Code](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section45&num=0&edition=prelim).

Apply to a fictional AI-app claim “98% accurate”: who made the representation? What precisely does “accuracy” measure? Was it material? What test population and benchmark support it? A marketing statement is not made safe by being inside a terms-of-service document.

### Step 4 — Distinguish outcome types
[Settlement] In *In re Everalbum*, FTC File No. 192-3172, the FTC alleged deceptive face-recognition and retention practices. The resulting consent order imposed obligations on the respondent; it was **not a judicial finding that all photo apps violated the law**. [FTC case docket](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter).

### Step 5 — Record uncertainty
For every legal claim log: exact authority, section/page, date accessed, jurisdiction, regulated actor, legal status, effective date, exceptions, unresolved question, and whether counsel review is needed.

## Worked hypothetical
An agent writes: “The GDPR applies to every U.S. SaaS product.” **Incorrect.** Analyze the GDPR's territorial scope under Article 3 and actual establishment, targeting, or monitoring of individuals in the Union. Merely having a public website that can be accessed from Europe is not necessarily enough. [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## Exercise
A founder adds an “unsubscribe” footer to every transactional password-reset email. Identify (1) the specific U.S. federal law to examine, (2) why message classification matters, and (3) what evidence you need before declaring a violation.

<details><summary>Answer and reasoning</summary>

Check the CAN-SPAM Act, 15 U.S.C. §§7701–7713, especially definitions and obligations tied to commercial electronic mail messages. Examine whether the message is transactional/relationship versus primarily commercial, including subject and body. A password reset is usually transactional, but mixed promotional content can complicate classification. Do not claim every email requires the same opt-out. [Official U.S. Code Title 15](https://uscode.house.gov/browse/prelim@title15/chapter103&edition=prelim).

</details>

## Sources and permissions
- [15 U.S.C. §45 — U.S. House Office of Law Revision Counsel](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section45&num=0&edition=prelim) [law].
- [FTC Everalbum proceeding](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter) [settlement].
- [GDPR official text, Article 3](https://eur-lex.europa.eu/eli/reg/2016/679/oj) [law].
Original summaries only; official publication does not itself grant blanket rights to reproduce every third-party element on government websites.
