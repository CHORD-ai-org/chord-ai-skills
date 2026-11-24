---
name: revenue-operations
description: "Check sales pipeline and forecasts: pipeline coverage, forecast accuracy, magic number, CAC payback. Use whenever the user asks if pipeline is enough or how good forecasts are."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/revenue-operations
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/revenue-operations
---

# Revenue Operations

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Check sales pipeline and forecasts: pipeline coverage, forecast accuracy, magic number, CAC payback. Use whenever the user asks if pipeline is enough or how good forecasts are.

## Steps

1. Confirm the task matches this source: Check sales pipeline and forecasts: pipeline coverage, forecast accuracy, magic number, CAC payback. Use whenever the user asks if pipeline is enough or how good forecasts are.
2. Start with the upstream step: Pipeline Coverage Ratio -- Total pipeline value / quota target (healthy: 3-4x)
3. Continue with: Stage Conversion Rates -- Stage-to-stage progression rates
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: business-growth. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/revenue-operations

## Verify

```bash
python scripts/check_skills.py skills/05-domain/revenue-operations
```
