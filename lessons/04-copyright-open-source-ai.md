# Lesson 04 — Copyright, open-source licenses and AI artifacts

**Goal:** Trace the rights needed to ship code, games, model weights, datasets and generated assets.

## 1. Copyright protects expression, not every idea
[Law] 17 U.S.C. §102(a) protects original works of authorship fixed in a tangible medium; §102(b) excludes protection for ideas, procedures, processes, systems, methods of operation, concepts, principles, or discoveries *as such*. [Official §102](https://www.govinfo.gov/link/uscode/17/102).

Ask four separate questions: (1) is there protected expression? (2) who owns it? (3) what exclusive right does your use implicate? (4) what license, exception, or defense applies? A GitHub repository being public does not equal authorization to use it commercially.

## 2. Copying, modification and distribution
[Law] 17 U.S.C. §106 identifies exclusive rights; §107 provides the multi-factor fair-use framework. [§106](https://www.govinfo.gov/link/uscode/17/106), [§107](https://www.govinfo.gov/link/uscode/17/107).

**Case holding:** *Google LLC v. Oracle America, Inc.*, 593 U.S. 1 (2021), held Google's particular copying of Java API declaring code was fair use, assuming copyrightability without deciding it. It did **not** make all API code copying lawful. [Supreme Court opinion (official PDF)](https://www.supremecourt.gov/opinions/20pdf/18-956_new_0e04.pdf).

## 3. Separate layers of the AI stack
- **Source code** has its own copyright and software license.
- **Model weights** may be subject to contractual license restrictions; whether and how copyright applies to particular weights may be disputed.
- **Training data** may carry underlying rights, contractual restrictions, database or privacy considerations.
- **Outputs** raise separate issues of originality, human authorship, third-party rights and terms.
- **Art, font, audio and game assets** require asset-specific review even when generated or bundled with code.

The U.S. Copyright Office's January 2025 Part 2 report concludes that AI assistance does not preclude protection for human-authored material, but mere prompts alone ordinarily do not confer copyright over generated expressive elements. This is agency analysis, not a standalone new statute. [Copyright Office report page](https://www.copyright.gov/ai/).

## 4. Licenses: map obligations to actions
MIT and Apache-2.0 have notice obligations but differ in express patent-grant and termination terms. GPL family licenses contain conditions relevant to distribution of covered/derivative works; AGPL adds a network-interaction source-availability condition in specified circumstances. Do not assume that using a dependency automatically subjects an unrelated entire project to copyleft; analyze the actual license, linkage, modification and distribution facts. Read original licenses at [SPDX license list](https://spdx.org/licenses/) as an index, and validate against the license text shipped with the package; SPDX is a reference index, not legal authority.

## Hypothetical
A game ships copied GitHub particle effects (MIT), a commercial-only font, and a sound file labeled “free for personal use.” The MIT library may be commercially usable subject to attribution/notice, while the font and sound may not be. Inventory each artifact and its actual permissions.

## Exercise
Create a `provenance.csv` with: component, upstream, version/SHA, license text path, copyright notice, modification, bundled/distributed?, attribution, commercial rights, restrictions, unresolved issues. Identify at least five dependencies or assets and categorize each.

## Sources
- [17 U.S.C. §§102, 106, 107](https://uscode.house.gov/browse/prelim@title17&edition=prelim) [law].
- [Google v. Oracle, U.S. Supreme Court](https://www.supremecourt.gov/opinions/20pdf/18-956_new_0e04.pdf) [case holding].
- [Copyright Office AI reports](https://www.copyright.gov/ai/) [agency research/guidance].
- [USPTO trademarks basics](https://www.uspto.gov/trademarks/basics) [official guidance].
**Note:** Link to third-party license texts and official judicial PDFs; do not mirror them here without a separate re-use assessment.

## Advanced seminar — four-factor fair-use practice

### A. Use all four statutory factors under 17 U.S.C. §107
1. **Purpose and character**, including commercial purpose and transformation in context.
2. **Nature** of the copyrighted work.
3. **Amount and substantiality** of what is used, qualitative as well as quantitative.
4. **Effect on the potential market** for the work.

Fair use is not automatically achieved by changing a set percentage or using a small number of lines. It is fact-dependent.

### B. Read *Google v. Oracle* narrowly
**Citation:** 593 U.S. 1 (2021), No. 18-956, opinion issued April 5, 2021. **Facts:** Google reused roughly 11,500 lines of Java API declaring code in Android. **Issue:** Was the particular copying fair use? **Holding:** Yes, assuming without deciding that the copied lines were copyrightable. **Limitation:** The decision does not immunize model-training copying, game art cloning or wholesale proprietary source-code appropriation. Read the Supreme Court majority's reasoning rather than relying only on the syllabus.

### C. Permission inventory with real engineering implications
| Artifact | Typical diligence | Shipping risk |
|---|---|---|
| OSS source | Actual license at exact commit + NOTICE | Failing attribution/source offers |
| AI model | Model card AND binding license plus downstream restrictions | Unauthorized commercial redistribution |
| Dataset | Provenance, collection rights, privacy, license | Infringement/privacy claims |
| Pixel art/font/music | Asset-specific agreement and contributors | Unlicensed bundled binary content |
| Generated image | Provider terms, human authorship, third-party similarities | Misstated exclusivity or infringement |
| Trademark | Clearance and confusing-similarity risk | Branding dispute |

### D. Applied question
An MIT-licensed effects library contains sprite images copied from a separate commercial pack. **Why is the MIT label insufficient?** A licensor cannot grant rights they do not control; evaluate chain of title and each asset. **Deliverable:** a CSV for 20 dependencies/assets with SPDX ID when meaningful, file SHA, upstream license, attribution action, and unresolved owner.
