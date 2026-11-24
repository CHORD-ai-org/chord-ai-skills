---
name: customer-success-manager
description: "Use when reviewing customer accounts for health, churn risk or expansion. Scores health with health_score_calculator.py, churn with churn_risk_analyzer.py and upsell with expansion_opportunity_scorer.py."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/customer-success-manager
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/customer-success-manager
---

# Customer Success Manager

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Business growth and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/customer-success-manager
```
