# Milestone 16 casebook: incident-response timing and role separation

**Educational lab / as-of November 13, 2026.** Facts are fictional. Check [six-state statute review](03-breach-notifications.md) and [obligation matrix](breach-obligations.csv) for source links and statutory exceptions. Nothing here is an operational incident notice or legal advice.

## The three-clock problem

A vendor detects a possible leak on **November 1**, a forensics team confirms covered records were acquired on **November 5**, and resident notices are approved on **November 18**. A staff member proposes setting every state filing date to **December 1** ("30 days from discovery").

That proposal is not legally sufficient:
1. **Washington** generally uses discovery for its 30-calendar-day resident notice and AG clocks; check possible scope/security-restoration and law-enforcement delays.
2. **Texas** distinguishes generally 60 days after breach determination for resident disclosure from 30 days after determination for AG when at least 250 Texas residents are involved.
3. **California** generally uses discovery/notification for resident notices, but its >500-resident **redacted sample to AG** is due within **15 calendar days after residents are notified**, not 30 days after detection.
4. **Illinois** gives no universal 30-day resident period in §530/10(a); required AG notice for >500 residents is due **no later than** consumer notice.
5. **Massachusetts** uses reasonable-practicability timing for residents, Attorney General and Director, without a universal 30-day cap in ch. 93H §3(b).
6. **Florida** uses determination/reason to believe for its two 30-day tracks; the Department trigger is **500 or more** individuals, not California's/Illinois's "more than 500."

The timeline cannot be finalized from these dates alone; each statute defines covered event, data, party, exceptions and the legal meaning of the clock trigger.

## Worked example: exactly 500 residents

A breach affects **500 California residents**, **500 Illinois residents**, **500 Florida individuals**, **250 Texas residents** and **501 Washington residents**. Assume *solely for the threshold comparison* that an applicable resident notice is required under each respective statute.

| Notice recipient | Threshold result | Explanation |
|---|---|---|
| California AG | Not met for this §1798.82(f) sample rule | Text says **more than 500** California residents |
| Illinois AG | Not met for this §530/10(e)(2) rule | Text says **more than 500** Illinois residents |
| Florida Department of Legal Affairs | Met | Text says **500 or more** Florida individuals |
| Texas AG | Met | Text says **at least 250** Texas residents |
| Washington AG | Met | Text says **more than 500** Washington residents |

**Important:** Missing the regulator threshold never means a covered individual is entitled to no notice.

## Worked example: who must notify whom?

A payroll SaaS vendor stores employee records for an employer. A compromised vendor account exposes data affecting several state residents.

- **Texas §521.053(c)**: a maintainer not owning the data may have an *immediate* owner/licensee notice duty; the employer/owner has separate resident obligations if the statute applies.
- **California §1798.82(b)**: a maintainer not owning the data may have a distinct immediate notice to the owner/licensee.
- **Illinois §530/10(b)**: a maintainer that does not own or license the covered data must notify the owner/licensee immediately when the statute's acquisition condition is met.
- **Massachusetts ch. 93H §3(a)**: a maintainer not owning or licensing personal information notifies the owner or licensor as soon as practicable and without unreasonable delay when the prescribed conditions exist.
- **Other requirements**: a SaaS DPA could require a separate, shorter contract notice that does not substitute for statutory reporting.

## Drafting trap: different resident-notice contents

- **Illinois** §530/10(a) says the individual notification must **not include the number of Illinois residents affected**.
- **Massachusetts** ch. 93H §3(b) says the resident notice must not include the nature of the breach or number of affected Massachusetts residents, even though AG/Director notices require incident information.
- **California** §1798.82(d) specifies notice format and required content; its sample for AG must exclude personally identifiable information.

A reusable notification template needs state-specific clauses and separate versions for regulator and residents.

## Student assignment (100 points)

- **20:** Distinguish owner/licensee from maintainer and third-party agent for each contract.
- **20:** Explain legal trigger, record facts unknown and reason about encryption/keys.
- **25:** Build distinct resident/regulator timelines without collapsing discovery and determination.
- **20:** Apply exact numeric thresholds; test **250, 500 and 501**.
- **15:** Draft separate regulator vs resident notice checklists, without including prohibited content.

**Verification receipt:** US state-published laws reviewed November 13, 2026; see [source register](source-register.csv). Legal conclusions for a real incident require the then-current operative text, evidence and counsel.