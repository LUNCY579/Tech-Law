# Casebook III — Security authorization, data representations, and AI employment tools

## 1. *Van Buren v. United States* — authorization gates

**Citation:** 593 U.S. 374 (2021), No. 19-783. [Official opinion](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf).  
**Relevant statute:** [18 U.S.C. §1030(a)(2), (e)(6)](https://www.govinfo.gov/link/uscode/18/1030).  
**Facts:** An officer used valid credentials to look up a license plate for an improper, non-police purpose.  
**Procedural history:** Jury conviction, Eleventh Circuit affirmed under its broader reading; Supreme Court reversed and remanded.  
**Issue:** Does violating a use-policy restriction while accessing data a person is otherwise authorized to view constitute exceeding authorized access?  
**Holding:** Not on that theory. The statutory phrase targets gaining information from areas (files/folders/databases) off limits to the user, not merely the improper purpose of otherwise permitted access. See majority opinion, especially discussion of §1030(e)(6).  
**Opposing view:** Justice Thomas dissented, joined by Chief Justice Roberts and Justice Alito.  
**Boundary:** The decision does not immunize access without authorization, bypassed access controls, breach of contract, privacy violations, or unethical use. State and federal laws can independently apply.

**Product thought experiment:** Recruiter A legitimately sees Candidate A's résumé but sells that information. Recruiter A may violate policy/contract/other law without *necessarily* “exceeding authorized access” on that factual theory. By contrast, bypassing tenant authorization to retrieve Candidate B's restricted data presents a different statutory analysis.

## 2. *In re Everalbum* — privacy promises and settlement status

**Agency docket:** FTC File No. 192-3172; administrative Docket C-4743. [Official FTC case docket](https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter); [official complaint](https://www.ftc.gov/system/files/documents/cases/1923172_-_everalbum_complaint_final.pdf).  
**Procedure:** FTC alleged that a photo storage app misrepresented aspects of facial recognition and user-deletion practices. The matter resolved through a **final consent order in 2021**. **It is neither a litigated federal court liability holding nor proof each allegation was found true.**  
**Read carefully:** Identify which paragraphs are allegations (complaint) and which duties are operative obligations binding the respondent (decision and order). A consent order's specific model/data deletion requirements should not be generalized into a universal rule that every company must destroy every derived model whenever someone deletes an account.
**Product implication:** Couple user-facing retention statements to actual object stores, model-training pipelines, embeddings, logs, backups and vendor processing.

**Assignment:** Draft a claim-to-control table for “no facial recognition,” “photos deleted on request,” and “we never train on your documents.” Include tests, processor terms, remaining exceptions and an owner.

## 3. *Bostock v. Clayton County* — employment decision rules

**Citation:** 590 U.S. 644 (2020), No. 17-1618. [Official Supreme Court opinion](https://www.supremecourt.gov/opinions/19pdf/17-1618_hfci.pdf).  
**Relevant statute:** [42 U.S.C. §2000e-2(a)(1)](https://www.govinfo.gov/link/uscode/42/2000e-2).  
**Facts:** Consolidated employment cases involved alleged discharge because employees were gay or transgender.  
**Posture:** Circuit decisions differed; Supreme Court resolved the statutory interpretation issue.  
**Holding:** Discharging an employee merely for being gay or transgender is discrimination because of sex under Title VII. The Court grounded its analysis in statutory text and causation.  
**Opposing views:** Justices Alito and Kavanaugh authored separate dissents (Thomas joined Alito's).  
**Boundary:** This case does not establish that every AI scoring system or disparate-impact claim is invalid or valid. The case principally concerns discriminatory treatment; adverse-impact claims require distinct elements and proof.

**AI-product application:** An automated ranking system that deliberately applies a protected characteristic as a disadvantage presents a disparate-treatment question. A facially neutral assessment with unequal outcomes calls for a separate statistical and legal investigation; causation, selection procedures, job relatedness and available alternatives matter. Do not equate statistical subgroup disparities with automatically proven illegality.

## 4. Comparative issue-spotting problem

A recruitment platform uses API vendor V, announces “no retention,” sends CVs for training, and allows employers to export candidate data they are not authorized to view. Its model ranks candidates and the interface claims “scientifically validated.” Analyze:

1. **FTC representations:** What exact statements may be deceptive and what supporting evidence is needed?
2. **Privacy rights:** Which laws govern the data subjects, and what jurisdictional/threshold facts are missing?
3. **Authorization:** What access is expressly allowed? Where do *Van Buren*'s limits matter, and what other causes of action may remain?
4. **Employment discrimination:** Is there intentional differential treatment or a potential adverse-impact issue? What validation evidence exists?
5. **Security remediation:** Which server-side access checks, tenant-isolation tests and vendor controls are immediate priority?

### Model issue map
High-risk facts are untrue retention promises, missing tenant authorization and unsupported validation claims. These need evidence, mitigations, and qualified review; none alone conclusively establishes every element of a particular legal claim. Use *Everalbum* for agency settlement risk, *Van Buren* for narrow CFAA interpretation and *Bostock* for text-based Title VII coverage. Do not substitute one source for another.

## 5. Recommended exam rubric
Legal issue spotting 25; legal elements 25; case distinctions 20; missing facts 15; product controls 15. Minimum passing memo: one official statute, two authenticated opinions and specific product evidence.
