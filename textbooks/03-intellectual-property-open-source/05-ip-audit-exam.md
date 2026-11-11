# Chapter 5 — Intellectual-property compliance laboratory

## Assignment: audit an AI-powered indie game
Assume the game ships: MIT particle FX code, Apache-2.0 image processor, AGPL web service modified in house, paid personal-use-only font, public-domain-claimed music of unknown provenance, a model with custom commercial restrictions, and AI-generated portraits.

### Step-by-step method
1. Freeze exact build and repository SHAs.
2. Generate a component/asset manifest with rightsholders and license evidence.
3. Separate software code from bundled art, fonts, sound, training data and weights.
4. Identify **copied expression** and specific acts of distribution/network service.
5. Apply license obligations, notices, code/offer obligations, patent provisions and exceptions.
6. Examine AI output authorship and similarity for each commercial asset.
7. Conduct trademark clearance before release.
8. Decide: cleared / conditional / blocked / counsel required; attach evidence.

### Example findings
| ID | Finding | Severity | Resolution |
|---|---|---|---|
| IP-1 | Font permits personal use only | P0 for commercial distribution | Buy license or replace |
| IP-2 | Unknown audio author | P0 until provenance | Locate rights or replace |
| IP-3 | AGPL modified web component | Needs analysis | Assess network/source duties and separated architecture |
| IP-4 | Apache component NOTICE missing | Conditional remediation | Inspect license/NOTICE and include required notices |
| IP-5 | Generated portraits sold as “exclusive copyrighted art” | Material claims risk | Review human authorship, terms and claims |

## Graded exercises (100)
**A — 25:** Brief *Google v. Oracle* and *Warhol* including facts, legal issue, holding, dissent, differences.  
**B — 25:** Build a 12-entry license BOM. Distinguish rights-holder assertions from verified documents.  
**C — 20:** Analyze one possible copyright claim under §§102, 106, 107, 501.  
**D — 15:** Research a potentially similar trademark using USPTO search guidance, including classes and related services.  
**E — 15:** Draft a release decision memo that makes uncertainty and evidence visible.

**Answer rubric:** Valid statutory elements (30), case distinction (20), asset provenance (20), concrete mitigation (20), limits/permissions (10). **No score constitutes legal clearance or a legal certification.**

## Sources and republication
Link to [Copyright Office](https://www.copyright.gov/ai/), [US Code](https://www.govinfo.gov/link/uscode/17/107), [USPTO](https://www.uspto.gov/trademarks/search/likelihood-confusion), and relevant license publisher texts; do not paste full third-party works into the repository without verifying rights.
