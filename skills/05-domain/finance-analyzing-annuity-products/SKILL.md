---
name: finance-analyzing-annuity-products
description: "Evaluates annuity structures with guaranteed benefit analysis, fee comparison, and surrender value modeling. Use when analyzing annuities, comparing guaranteed benefits, or evaluating annuity products."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-annuity-products
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-annuity-products
---

# Finance Analyzing Annuity Products

## Brief info

Evaluates annuity structures with guaranteed benefit analysis, fee comparison, and surrender value modeling. Use when analyzing annuities, comparing guaranteed benefits, or evaluating annuity products. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates annuity structures with guaranteed benefit analysis, fee comparison, and surrender value modeling. Use when analyzing annuities, comparing guaranteed benefits, or evaluating annuity products.

## Steps

1. Confirm the task matches this source: Evaluates annuity structures with guaranteed benefit analysis, fee comparison, and surrender value modeling. Use when analyzing annuities, comparing guaranteed benefits, or evaluating annuity products.
2. Start with the upstream step: Comparing fixed, variable, fixed-indexed, or registered index-linked annuity (RILA) products
3. Continue with: Evaluating guaranteed living benefit riders (GLWB, GMIB, GMAB, GMWB)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-annuity-products

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-annuity-products
```
