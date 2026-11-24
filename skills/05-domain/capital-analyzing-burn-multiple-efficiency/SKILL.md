---
name: capital-analyzing-burn-multiple-efficiency
description: "Evaluates capital efficiency with burn multiple, net new ARR per dollar burned, and path to profitability analysis. Use when analyzing burn efficiency, assessing capital needs, or modeling runway scenarios."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-burn-multiple-efficiency
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-burn-multiple-efficiency
---

# Capital Analyzing Burn Multiple Efficiency

## Brief info

Evaluates capital efficiency with burn multiple, net new ARR per dollar burned, and path to profitability analysis. Use when analyzing burn efficiency, assessing capital needs, or modeling runway scenarios. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates capital efficiency with burn multiple, net new ARR per dollar burned, and path to profitability analysis. Use when analyzing burn efficiency, assessing capital needs, or modeling runway scenarios.

## Steps

1. Confirm the task matches this source: Evaluates capital efficiency with burn multiple, net new ARR per dollar burned, and path to profitability analysis. Use when analyzing burn efficiency, assessing capital needs, or modeling runway scenarios.
2. Start with the upstream step: Evaluating a growth-stage company's capital efficiency before committing to a new round
3. Continue with: Benchmarking portfolio companies against peer cohorts on cash-to-growth conversion
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-burn-multiple-efficiency

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-burn-multiple-efficiency
```
