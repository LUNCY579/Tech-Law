# State consumer-privacy engineering casebook — Maryland and Oregon

**Educational, synthetic scenarios.** Read the [Milestone 17B research note](08-maryland-oregon-privacy.md). Passing a feature test does **not** establish compliance with a privacy statute.

## Exercise A — distinguish product roles

| Feature | Processing context | Questions |
|---|---|---|
| Employer candidate scoring | Hiring and employment | Who is controller versus processor? Are consumers acting as applicants? Is the information excluded under a particular privacy statute but regulated by other employment laws? |
| Subscription learning site | Household consumer | Is account-holder residency reliable? What personal data is processed? Which controller threshold and exemptions apply? |
| Online game social features | Consumer and possibly child | Does an ad SDK sell/shares data? Do precise geolocation, under-16 and universal opt-out rules apply? |

**Deliverable:** dated source-specific applicability matrix, with correct jurisdiction, role, datasets, revenue, coverage threshold, statutory text, evidence owner and unresolved conditions. Do not show a public “legally certified” badge from this worksheet.

## Exercise B — consent and rights receipt

Create hypothetical test fixtures for: (1) notice displayed, (2) consent given for a *specific* sensitive-data purpose, (3) consent revoked, (4) privacy opt-out received from a browser where legally supported, (5) appropriate propagation to processors, and (6) deletion or retention exception documented.

**Negative example:** a one-time broad Terms of Use click does not conclusively establish consent for unrelated purposes and does not excuse a missing rights process.

## Exercise C — compare statutory thresholds

Hypothetical company holds 40,000 Maryland consumer accounts and 20,000 Oregon consumer accounts and earns 5% of revenue from data sale. Is low sales revenue universally sufficient to escape both statutes?

**Answer:** No. Maryland's **35,000** consumer-count branch may apply independently of sales revenue. Oregon's general 100,000 branch and 25,000/25% combined branch may not both be met in this example, but state-specific actor, activity, temporal and exemption details still need assessment. Other laws remain possible even if OCPA does not apply.

## Exercise D — temporal legal-source receipt

Document law version, official publisher, retrieved date, rule effective date, transition clause, exceptions and alternate agency guidance. The Oregon 2025-code webpage itself warns about 2026 amendments, but its 2026 A&R table was inaccessible during this review: mark **2026 amendment verification pending** rather than assuming unchanged law.

**100-point rubric:** 25 each for statutory coverage, consent/rights, concrete technical evidence and careful effective-date/currentness treatment.

Source note: [research chapter](08-maryland-oregon-privacy.md). These exercises do not activate any production workflow or credential issuance.