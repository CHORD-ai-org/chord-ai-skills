---
name: finance-analyzing-development-feasibility
description: "Evaluates real estate development projects with cost analysis, return projections, and risk assessment. Use when analyzing development deals, projecting development returns, or assessing feasibility."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-development-feasibility
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-development-feasibility
---

# Finance Analyzing Development Feasibility

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates real estate development projects with cost analysis, return projections, and risk assessment. Use when analyzing development deals, projecting development returns, or assessing feasibility.

## Steps

1. Confirm the task matches this source: Evaluates real estate development projects with cost analysis, return projections, and risk assessment. Use when analyzing development deals, projecting development returns, or assessing feasibility.
2. Start with the upstream step: Sponsor or LP requests underwriting of a proposed ground-up development or major redevelopment
3. Continue with: Comparing multiple development sites or project configurations for capital allocation
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-development-feasibility

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-development-feasibility
```
