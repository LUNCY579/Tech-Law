# Casebook II — Software interfaces, creative adaptation, and fair use

## 1. Read the legal statute before the opinions

[17 U.S.C. §102](https://www.govinfo.gov/link/uscode/17/102): protected subject matter, including the expression/idea distinction under subsection (b).  
[17 U.S.C. §106](https://www.govinfo.gov/link/uscode/17/106): exclusive rights, including reproduction and preparation of derivative works.  
[17 U.S.C. §107](https://www.govinfo.gov/link/uscode/17/107): fair use, evaluated under four statutory factors and the purpose-specific facts.

**Method:** Identify the work; rights holder; allegedly copied expression; licensing scope; potential statutory exception; and facts supporting *all four* fair-use factors. “I changed it,” “it is for research,” or “it was online” are not automatic defenses.

## 2. Case brief — *Google LLC v. Oracle America, Inc.*

**Citation:** 593 U.S. 1 (2021), No. 18-956. [Official Supreme Court opinion](https://www.supremecourt.gov/opinions/20pdf/18-956_new_0e04.pdf).  
**Posture:** Federal Circuit held relevant declaring code copyrightable and later rejected a jury fair-use verdict; Supreme Court reversed the fair-use conclusion and remanded.  
**Facts:** In developing Android, Google copied approximately 11,500 lines of Java API declaring code enabling developers to call familiar routines.  
**Question:** Was that particular copying fair use, assuming the code could be protected?  
**Holding:** Yes on the specific record. The Court **assumed without deciding copyrightability**; it did not hold all APIs unprotected. Majority opinion begins following the syllabus (consult majority pp. 1–36 in the slip opinion).  
**Reasoning:** The functional nature of declaring code, programmers' investment and use in a distinct new platform informed the four-factor balance. The Court assessed the particular copied portion and its role in enabling programmers' existing skills.  
**Opposing view:** Justice Thomas dissented, joined by Justice Alito, arguing against the majority's fair-use result. Read dissent rather than pretending the decision was unanimous.  
**Limit:** Not a blanket fair-use exemption for training large models, copying app UI, redistributing weights or commercializing game assets.

### Analogy drill
A startup copies 9,000 lines of a proprietary API specification so established applications can integrate with a new platform. Compare purpose, degree of functional need, amount, licensing markets and alternative implementations to the Court's actual facts. Do **not** assert the same outcome just because both examples involve APIs.

## 3. Case brief — *Andy Warhol Foundation v. Goldsmith*

**Citation:** No. 21-869, slip op. (U.S. May 18, 2023). [Official Supreme Court opinion](https://www.supremecourt.gov/opinions/22pdf/21-869_87ad.pdf).  
**Posture:** District court favored Warhol Foundation on fair use; Second Circuit reversed; Supreme Court affirmed on the **specific first-factor issue** presented.  
**Facts:** A portrait of Prince based on photographer Lynn Goldsmith's work was later licensed by the foundation for a magazine cover; the original photo was commercially licensed as well.  
**Question:** Does the **purpose and character** factor favor the Foundation's commercial licensing of Orange Prince to a magazine?  
**Holding:** It does not. The Court assessed the challenged **use**, not whether Warhol's art was intrinsically original or transformative in an abstract sense. See syllabus pp. 1–3 and majority's factor-one analysis; do not cite the syllabus as the binding opinion.  
**Opposing view:** Justice Kagan dissented, joined by Chief Justice Roberts; Justice Gorsuch concurred, joined by Justice Jackson.  
**Limit:** The Court did **not** decide whether every possible display of a Prince Series image infringes. Nor did it decide every fair-use factor as a fresh, complete dispute.

### Combined interpretation
*Google* recognizes fair use in a specific new technological context; *Warhol* warns that simply adding meaning/message to an existing work does not guarantee factor one when licensing purpose overlaps. The **particular use, alternatives, market and factual record** matter more than an AI-vs-human label.

## 4. Founder scenarios

**Scenario 1 — Pixel-art library:** Code is MIT, but bundled sprite images have untracked owners. **Answer:** audit each asset; an MIT notice on the repository does not independently prove the art was licensed by its rightful owner.

**Scenario 2 — LLM training set:** Training corpus contains copyrighted articles. **Answer:** determine acquisition and licensing facts, acts of reproduction, applicable exceptions and current litigation; do not treat either *Google* or *Warhol* as resolving all training cases.

**Scenario 3 — Prompt-generated illustration:** A vendor says commercial use is permitted. **Answer:** distinguish vendor contract permission, output copyrightability/human authorship, and possible similarity or third-party infringement. They are three different legal questions.

## 5. Four-factor research worksheet

| Factor | Evidence to collect | Incorrect shortcut |
|---|---|---|
| Purpose/character | Intended use, market role, commercial licensing, new purpose | “Different style means fair use” |
| Nature | Functional/creative aspects, publication status | “Code never has copyright” |
| Amount | Quantity, qualitative centrality, alternatives | “Under 10% is safe” |
| Market effect | Existing/expected licenses, substitution evidence | “No direct sale, so no harm” |

### Independent exam (30 points)
Propose a model developer's ingestion and output reuse policy. Identify **at least six source-rights categories**, apply §107 to one specific copy/use, evaluate both *Google* and *Warhol* on analogous and distinguishable facts, and include a reasoned contrary argument. Score 10 for authority, 10 for factor-specific facts, 5 for limits, 5 for implementation evidence.
