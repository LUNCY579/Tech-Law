# Security incident law: determine the trigger before calculating a deadline

**As of:** 2026-11-13. This is a selective follow-up to the uploaded Milestone 15 breach module. No universal U.S. notice clock exists.

## Decision tree

Investigate: (1) which entity owns/licenses versus processes the data; (2) affected residents and countries; (3) legally defined personal information; (4) acquisition/access, encryption and compromise; (5) harm and statutory exceptions; (6) trigger timestamp; (7) residents versus regulators versus consumer-reporting agencies; (8) sectoral overlays, law-enforcement delay and permissible extensions.

**Do not count from an arbitrary incident-monitoring alert if the statute triggers on a later legal determination; also do not wait for an internal meeting when the statute triggers on discovery.**

## Verified examples from official law

| State | Individual notice | Government / regulator notice | Source |
|---|---|---|---|
| Washington | RCW 19.255.010(8): expeditiously without unreasonable delay; not more than 30 calendar days after discovery, subject to specified delays | Under (7), **more than 500** Washington residents: Attorney General no more than 30 days after discovery | [RCW 19.255.010](https://app.leg.wa.gov/RCW/default.aspx?cite=19.255.010) |
| Florida | Fla. Stat. §501.171(4): generally within 30 days of determination or reason to believe a covered breach occurred, subject to extensions/waiver and other conditions | §501.171(3): covered breach involving **500 or more** Florida individuals, Department of Legal Affairs within 30 days | [2026 statute](https://www.flsenate.gov/Laws/Statutes/2026/501.171) |

Washington also provides a distinct immediate notification obligation for data maintainers to the owner/licensee under RCW 19.255.010(2). Florida has a separate rule for third-party agents in §501.171(6); this note is not a complete substitute for reading it.

## Additional jurisdiction research, NOT signed off here

- **California:** The uploaded Milestone 15 handoff proposes a 30-day resident deadline and a post-resident-notice Attorney General sample period under California Civil Code §1798.82. Its own source audit recorded an official-legislative-text access failure. Do **not** calculate a legal deadline from the archive alone. Recheck the [California Legislature](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.82.&lawCode=CIV) and [California DOJ reporting page](https://oag.ca.gov/privacy/databreach/reporting).
- **Texas:** The handoff distinguishes individual and AG clocks under [Business and Commerce Code §521.053](https://statutes.capitol.texas.gov/?artSec=521.053&chapter=BC.521&code=BC&tab=1). Current codified subsections and any amendment after the handoff still require targeted confirmation before actual deadlines are asserted here.
- **Illinois and Massachusetts:** Locate operative 815 ILCS 530/10 and Mass. Gen. Laws ch. 93H and their exceptions. Do not generalize one state's notice limit to both.

## Applied exercise

A hypothetical incident affects 600 Washington residents and 490 Florida residents. Incident response discovered suspicious database access November 1 and formed a reasonable belief of unauthorized personal-data access November 5. The precise trigger and affected information are not yet fully established.

**Model analysis:** Establish discovery and statutory definitions separately. Washington's conditional 30-day regime and AG threshold require assessment of whether personal information was acquired or reasonably believed acquired and risk-of-harm exceptions. Florida's individual clock depends on a statutory determination/reason-to-believe trigger; 490 affected Florida people do not automatically meet its 500-person department threshold. Law enforcement, extensions, processors and sectoral rules may change the result.

## Product artifacts

Maintain a UTC incident timeline, affected-resident matrix, data categories, encryption/key evidence, counsel decision log, owner/processor contacts, jurisdiction-specific obligations, notice content versions, draft approvals, post-notice supplements and preservation requirements. This is an engineering evidence framework, **not** a statement that any particular incident is reportable.

**Status:** Washington/Florida provisions directly checked; California/Texas/Illinois/Massachusetts retained as source-specific research tasks, not certified clocks.