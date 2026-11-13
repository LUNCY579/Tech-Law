# Source register governance and offline integrity checks (Milestone 16B)

**As of 2026-11-13.** This is editorial data governance for an educational repository. The checker does **not** consult a court citator, establish a legal obligation, access government websites or approve commercial reuse.

## Two research artifacts

- [Primary source register](../research/2026-11-13/source-register.csv): one row per authority or selected official explanatory publication, with `id`, jurisdiction, authority type, **status**, relevant `date`, official URL and claim-limiting caveat.
- [Breach notice obligations](../research/2026-11-13/breach-obligations.csv): one row per **jurisdiction + recipient + cited section** recording the trigger, clock anchor, timing phrase, exact threshold wording and related source ID.

A single state can yield multiple independently triggered obligations. A registration row is **not** an assertion that a particular event is legally reportable or that an alert can be assigned an automated deadline.

## Status values

| Status | Meaning | Appropriate claim |
|---|---|---|
| `ENACTED_AND_APPLICABLE` | Operative primary-law provision at the stated date, subject to factual scope and amendments | "The cited statute says X"; **not** "product Y is certified" |
| `ENACTED_FUTURE` | Enacted law with an operative duty or phase scheduled for a later date | Explain future condition, transition and status |
| `OFFICIAL_GUIDANCE` | Published agency explanation, not independently an enacted statute | Identify agency role and limits |
| `WITHDRAWN` / `VACATED` | Historical agency action or rule without current operative force in the stated sense | Never call it current binding text |
| `REQUIRES_FURTHER_REVIEW` | Specific current provision or amendment not adequately authenticated | Maintain as research lead only |

For the **six-state breach obligation matrix**, only a source row with `ENACTED_AND_APPLICABLE` may be referenced. This is a **minimum editorial gate**, not a guarantee that the statutory interpretation is correct.

## What the static checker catches

Run:

```bash
python3 scripts/audit_source_register.py
python3 -m unittest discover -s tests -v
python3 scripts/audit_curriculum.py
```

It verifies CSV headers, no blank required metadata, unique IDs, syntactically valid ISO dates, HTTPS governmental publisher hostnames, consistent state labels, source ID existence, matching source URLs and absence of *pending/withdrawn* sources behind published obligation rows.

**Legacy official hostname exception (Milestone 17):** Oregon's Department of Justice officially publishes consumer privacy guidance at the HTTPS host **www.doj.state.or.us**. The URL validator now allows that **exact vetted host** alongside government and EU domains; it deliberately rejects an arbitrary *.or.us domain or a lookalike suffix. Hostname checks remain metadata hygiene, not a legal-authenticity or live-site security guarantee.

**What it cannot catch:** silently amended law, a government HTML endpoint displaying a superseded version, unsupported pinpoint interpretation, omitted exceptions, unreviewed court subsequent history, broken HTTP responses, or a real-world factual trigger.

## Verification workflow for future contributors

1. Record the **exact operative provision**, official publisher and relevant version/date, plus the actor and jurisdiction. An official government document may contain non-binding guidance, legislative proposals or historical text.
2. Document a **tight paraphrase** with a citation and at least one consequential caveat. Do not reproduce third-party protected text.
3. Apply source-status labels and keep research-pending propositions out of the normalized obligation matrix.
4. Add or modify a small, deterministic offline regression test for a new schema or invariant; run GitHub Actions.
5. Record a review receipt: date, source actually opened, source access failures, verified claims and unresolved subsequent history.
6. Require updated attorney review and current statute check before deploying to a real-world breach, regulated assessment, or financing transaction.

## Revision policy

Do not erase a prior milestone's dated uncertainty; append a **new** dated verification receipt and reference it. Distinguish the statute from the agency's explanatory website; a 403 error on one version of the publisher does not mean no law exists. Preserve records of contradictory sources and unresolved questions.

**Source-specific illustration:** [Milestone 16 source audit](MILESTONE16_BREACH_SOURCE_AUDIT_2026-11-13.md) documents California §1798.82 from state-published 2026 excerpts after the Legislature's HTML page returned 403, without claiming every subsequent amendment has been checked.
