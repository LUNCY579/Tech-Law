# Citation and claim validation manual

## 1. Source hierarchy, mapped to the *actual* proposition
A federal statute can be binding but not necessarily apply to a Delaware-law contract; a Delaware statute can be binding yet not answer federal securities law; a Supreme Court holding interprets a particular legal question, while an FTC administrative settlement binds identified parties according to the order. An EU consolidated regulation is a useful official reading text, but its authentic amending legal acts govern. **Authority is jurisdiction- and issue-dependent.**

## 2. Source record (mandatory schema)
```yaml
claim_id: IP-FAIRUSE-001
proposition: "Fair use requires consideration of the four statutory factors."
jurisdiction: "United States, federal"
authority_type: statute
citation: "17 U.S.C. § 107 (current edition checked 2026-11-11)"
publisher: "U.S. Government Publishing Office"
url: "https://www.govinfo.gov/link/uscode/17/107"
pinpoint: "§ 107(1)-(4)"
version_date: "verify relevant edition"
checked_at: "2026-11-11"
source_status: "official text"
authority_grade: "B"
later_history: "not applicable to statute; amendments must be checked"
permissions: "link and original paraphrase; no imported full text"
```

Do not copy the sample grade into another proposition; it reflects the stated checks only.

## 3. Citation format
- Statute: **17 U.S.C. § 107(1)–(4)**, pinpoint a subsection for a specific element.
- State law: **Del. Code tit. 8, § 141(a)**, compare current text to company documents.
- Regulation: **Regulation (EU) 2024/1689, art. 6, annex III**, cite the operative consolidated/amending version and application date.
- Judicial opinion: ***Coinbase, Inc. v. Suski*, 602 U.S. 143 (2024)**; when using slip pagination, explicitly mark **slip op. at 4–9** instead of pretending those are U.S. Reports pages.
- Enforcement: ***In re Everalbum*, FTC File No. 192-3172, complaint and final consent order (2021)** — identify complaint **allegations** separately from the enforceable order.
- Guidance: **SEC, “Rule 506(c),” page updated March 17, 2026** — guidance, not the actual rule text.

## 4. Opinion verification checklist
1. Verify issuing court, decision date, docket, caption, vote and the actual opinion PDF.
2. Read **majority** and the operative mandate, not merely the syllabus (a Supreme Court syllabus is not part of the opinion).
3. Separate outcome of trial, appeal, certiorari, remand, later judgments.
4. Quote only short necessary excerpts and give pinpoint; paraphrase in own words.
5. Research later history, including reversals, statutory overrides, circuit splits and context-specific distinctions; **not completed** by a simple link check.
6. A concurrence is not automatically majority reasoning; a dissent is a counterargument, not precedent.
7. For older opinions without authenticated official originals, label the historic reporter citation **PENDING**.

## 5. Example issue tree — *Coinbase* versus *Specht*
**Coinbase:** multiple contracts conflict about who resolves arbitrability; threshold contract conflict is for court. [Official opinion](https://www.supremecourt.gov/opinions/23pdf/23-3_879d.pdf), majority slip pp. 4–9.  
**Specht:** concerns notice and manifestation of assent to downloadable software terms; the original Second Circuit text **is not authenticated in this project**. Do not cite an invented court URL or pinpoint.  
**Difference:** existence of assent versus allocation among conflicting agreements.

## 6. Effective-date trap example
As of the reviewed official [EU AI Act 2026 consolidation](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02024R1689-20260727), some obligations are already operative while specified Annex III high-risk provisions have later application dates. A statute being enacted and a particular obligation being operative are separate facts.

The [FTC 2026 conforming action](https://www.ftc.gov/policy/public-comments/revision-negative-option-rule-withdrawal-cars-rule-removal-non-compete-rule-conform-these-rules-0) records rollback of its vacated 2024 Negative Option Rule amendment; separately, the [federal ROSCA statute](https://www.govinfo.gov/link/uscode/15/8403) remains a distinct enacted obligation.

## 7. Permissions gate
U.S. federal government works may be excluded from copyright under 17 U.S.C. § 105, subject to scope and third-party exceptions; this is not a blanket license for federal websites or state/EU materials. Private OSS licenses are source agreements, not U.S. government grants. **Course rule: original summaries, short properly attributed quotations, outbound links; no mirrored source texts.**
