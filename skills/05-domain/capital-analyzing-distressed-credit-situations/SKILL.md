---
name: capital-analyzing-distressed-credit-situations
description: "Evaluates distressed debt opportunities with recovery analysis, liquidity assessment, and potential restructuring outcomes. Use when screening distressed situations, analyzing stressed credits, or evaluating workout scenarios."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-distressed-credit-situations
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-distressed-credit-situations
---

# Capital Analyzing Distressed Credit Situations

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates distressed debt opportunities with recovery analysis, liquidity assessment, and potential restructuring outcomes. Use when screening distressed situations, analyzing stressed credits, or evaluating workout scenarios.

## Steps

1. Confirm the task matches this source: Evaluates distressed debt opportunities with recovery analysis, liquidity assessment, and potential restructuring outcomes. Use when screening distressed situations, analyzing stressed credits, or evaluating workout scen
2. Start with the upstream step: Screening a new distressed or stressed credit for potential investment
3. Continue with: Evaluating recovery prospects across tranches in an overleveraged capital structure
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-distressed-credit-situations

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-distressed-credit-situations
```
