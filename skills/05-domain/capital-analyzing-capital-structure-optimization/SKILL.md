---
name: capital-analyzing-capital-structure-optimization
description: "Evaluates optimal leverage with WACC minimization, rating impact, and financial flexibility assessment across market conditions. Use when optimizing capital structure, analyzing target leverage, or evaluating rating implications."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-capital-structure-optimization
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-capital-structure-optimization
---

# Capital Analyzing Capital Structure Optimization

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates optimal leverage with WACC minimization, rating impact, and financial flexibility assessment across market conditions. Use when optimizing capital structure, analyzing target leverage, or evaluating rating implications.

## Steps

1. Confirm the task matches this source: Evaluates optimal leverage with WACC minimization, rating impact, and financial flexibility assessment across market conditions. Use when optimizing capital structure, analyzing target leverage, or evaluating rating impl
2. Start with the upstream step: Evaluating whether current leverage is optimal relative to peer benchmarks and rating thresholds
3. Continue with: Modeling target debt/equity mix to minimize weighted average cost of capital (WACC)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-capital-structure-optimization

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-capital-structure-optimization
```
