# Chapter 2 — Open-source, copyleft and AI-model licensing

## 1. Public availability is not a license
An internet-visible repository may still be protected by copyright even if it has no explicit license. Check the **actual commit's** LICENSE/NOTICE, individual files, contributor ownership, bundled third-party materials, any additional commercial terms, and distribution obligations. An SPDX identifier is useful metadata, not dispositive permission or chain-of-title proof.

## 2. License families — read the words
| Family | Typical rights and recurring duties | Critical nuance |
|---|---|---|
| MIT | Broad permission, retain copyright and license notice | Only covers material licensors can license |
| Apache-2.0 | Broad copyright license, express patent provisions, notices and changes | Patent termination and NOTICE handling matter |
| GPLv3 | Copyleft conditions on conveying covered works, source availability under specified circumstances | Whether combined work is covered is fact dependent |
| AGPLv3 | GPL-like duties plus specified source-access duty for modified programs serving users over a network | “Any SaaS using AGPL code must publish all its code” is overbroad |
| Proprietary / custom | Rights can restrict usage, redistribution, fields of use, training, outputs, or support | “Open weights” does not necessarily mean OSI open source |

**Publisher references:** [Apache Foundation license texts](https://www.apache.org/licenses/); [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html); [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html); [Open Source Initiative MIT page](https://opensource.org/license/mit). These are first-party rightsholder or license-steward texts, not government laws. Verify the license version actually shipped with each component.

## 3. How to analyze a combined application
1. Inventory files, modules, binaries, assets and dynamic dependencies.
2. Label **development only**, **distributed**, or **network offered**; map modifications separately.
3. Identify direct/indirect copyright holders, exact text and version.
4. Analyze whether combination/derivative-work provisions apply in the relevant jurisdiction.
5. Record attribution, source-offer, patent, notice and redistribution requirements.
6. Preserve compliant release artifacts (LICENSE/NOTICE/source archive) and distribution receipts.

**Worked hypothetical:** A game uses an MIT engine plugin, AGPL server component, Apache image processing code and paid font. The MIT code usually permits commercial usage with notice; the AGPL server demands a separate detailed analysis of modifications/network interaction; Apache's patent grant/NOTICE can matter; the paid font needs its own EULA. A blanket “all open source is free commercially” conclusion is ungrounded.

## 4. AI model and dataset rights are separate
A foundation-model repository may have a code license, distinct weight license, usage policy and dataset statements. A permissive model weight license does **not** legalize all training data, eliminate privacy duties or transfer ownership of third-party trademarks. Similarly, an open dataset description may omit rights held by the original creators of examples.

**Exercise:** Create `license-bom.csv` with source, exact commit, file/asset, licensor, license evidence, modification, commercial rights, export/distribution, attribution, patent, network terms, uncertainties and reviewer.

### Model answer rubric
Correctly distinguish **copyright grant**, **contractual obligations**, **patent rights**, **distribution trigger**, and **source provenance** (20 points each). Do not declare a complex combined work definitively compliant on a filename scan alone.
