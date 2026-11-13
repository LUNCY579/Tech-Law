# Chapter 1 — Copyright rights, infringement and fair use

## 1. The statutory building blocks
Under [17 U.S.C. §102(a)](https://www.govinfo.gov/link/uscode/17/102), qualifying original works of authorship fixed in a tangible medium can receive copyright protection. **§102(b)** excludes ideas, procedures, processes, systems, methods of operation, concepts and discoveries as such. The software design idea “a command palette for documents” is not the same legal object as a particular codebase or visual design expression.

[§106](https://www.govinfo.gov/link/uscode/17/106) defines exclusive rights, including reproduction, derivative works, distribution and certain performance/display rights. Under [§501](https://www.govinfo.gov/link/uscode/17/501), violation of a copyright owner's exclusive rights can constitute infringement. **Before concluding infringement:** verify ownership, protected material, the act alleged, applicable licensing and statutory defenses. Some suits have additional registration prerequisites under [§411](https://www.govinfo.gov/link/uscode/17/411). The remedies and eligibility for statutory damages require separate review under §§502–505 and §412.

## 2. Fair use requires all four factors
[17 U.S.C. §107](https://www.govinfo.gov/link/uscode/17/107): (1) purpose and character; (2) nature of the work; (3) amount and substantiality; (4) market impact. No “10% rule.” Commercial use is relevant but not automatically disqualifying. Transformative use is contextual, not a magic label.

### Case A — *Google LLC v. Oracle America, Inc.*, 593 U.S. 1 (2021)
[Official Supreme Court opinion](https://www.supremecourt.gov/opinions/20pdf/18-956_new_0e04.pdf). **Facts:** Google used about 11,500 lines of Java API declaring code in Android to enable familiar programmer calls. **Question:** fair use of this particular material? **Holding:** fair use, *assuming without deciding* copyrightability. **Reasoning:** functional characteristics of declarations, programmer investment, new platform context, amount relative to purpose, and market effects. **Counterview:** Thomas dissent (Alito joined). **Boundary:** not a categorical permission for commercial cloning of all APIs or model training.

### Case B — *Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith*, 598 U.S. 508 (2023)
[Official opinion](https://www.supremecourt.gov/opinions/22pdf/21-869_87ad.pdf). **Facts:** foundation licensed Orange Prince image for magazine use based on Goldsmith portrait. **Question:** does factor one favor that licensing use? **Holding:** no, on that particular use. **Reasoning:** focus on challenged purpose and overlap of licensing markets; new meaning alone insufficient. **Counterview:** Kagan dissent joined by Roberts. **Boundary:** the Court did not decide the legality of every use of the Prince Series.

## 3. Apply to software assets
**Example:** A startup copies 50 lines of a proprietary editor's keybinding code and reimplements commands with its own implementation. First ask whether copied lines are protected expression rather than an unprotectable method, whether license or exception permits copying, and how much functional necessity matters. The exact result cannot be supplied from line count alone.

**Example:** An indie studio imports a sound pack labeled “personal use only” into a commercial game. Even if the game engine is MIT-licensed, that does not license unrelated audio. Different components have separate chains of title.

## 4. Section 1201: protection measures
[17 U.S.C. §1201](https://www.govinfo.gov/link/uscode/17/1201) creates anti-circumvention rules distinct from ordinary infringement analysis, with statutory and triennial exemptions. The [Copyright Office's 2026 proceeding](https://www.copyright.gov/1201/) was still underway as of this edition; **proposed** 2027 exemptions are not already binding. Authorized copying and lawful circumvention are distinct questions.

## Exercise and model reasoning
**Question:** A developer decompiles a game to learn an animation format, then redistributes textures and bypass instructions. Can “interoperability” settle legality?  
**Answer:** No. Analyze copying/reproduction, license, fair use, §1201 anti-circumvention, any relevant reverse-engineering statutory exception, texture ownership, redistribution rights and facts. The purpose of understanding a format does not necessarily authorize distribution of protected art or anti-circumvention tools.

**Reading assignment:** Brief both Supreme Court cases in 500 words each: facts, procedure, issue, holding, limiting rationale, strongest counterargument, and impact on a code/model/art workflow.
