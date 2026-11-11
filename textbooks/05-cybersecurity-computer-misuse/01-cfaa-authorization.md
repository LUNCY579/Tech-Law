# Chapter 1 — The CFAA: unauthorized access versus improper purpose

## Rule structure
[18 U.S.C. §1030](https://uscode.house.gov/us/usc/119-120/t18/s1030/) contains **distinct offenses**, including specified unauthorized access, obtaining certain information, fraud, damage, password trafficking and extortion scenarios. Do not collapse them into the proposition “breaking a website's Terms of Service is always a federal hacking crime.”

To analyze §1030(a)(2), identify: the accused person's conduct, whether access was without authorization or exceeded authorization, whether information was obtained, what category of computer/information is implicated, and the relevant jurisdictional and mental-state requirements. Other subsections have different elements. Civil remedies under §1030(g) require their own statutory conditions.

## Verified Supreme Court case: *Van Buren v. United States*
[Official opinion](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf); [official Supreme Court docket No. 19-783](https://www.supremecourt.gov/docket/docketfiles/html/public/19-783.html). On June 3, 2021, the Court reversed and remanded; Justice Barrett wrote the majority opinion, with Justice Thomas dissenting, joined by Chief Justice Roberts and Justice Alito.

**Relevant facts:** A police officer used valid credentials to look up license-plate information for an impermissible purpose. **Question:** Did a purpose restriction turn access to permitted information into “exceeding authorized access”? **Holding:** Not under the government's proposed interpretation; §1030(e)(6) addresses information in computer areas not accessible to the person, rather than all misuse of information one is allowed to see. **Limitation:** No general permission to bypass tenant controls, access systems without permission, scrape unlawfully, violate separate privacy law or breach contracts.

## Engineering examples
- **Case A:** Employee accesses a database row they are authorized to view but sells the information. *Van Buren* limits one CFAA argument; other legal remedies may still apply.
- **Case B:** Recruiter changes an API ID and obtains a row outside the authorization scope. The “gates” factual analysis is materially different; test the precise authorization boundary and applicable CFAA provision.
- **Case C:** Security student attempts to scan a commercial platform without a written testing authorization. A public bug bounty may permit defined tests, not arbitrary attacks outside its scope.

## Exercise
Write a 700-word comparative IRAC analyzing cases A–C under §1030(a)(2) and §1030(e)(6), separating facts known from missing authorization details. Include a **permissioned test plan** but do not conduct unauthorized probing.

**Model answer outline:** identify the specific data gate, actual grants, person and scope, purpose versus entitlement, other statutory elements and independent contractual/privacy duties. The Court's 2021 holding does not decide every hypothetical automatically.
