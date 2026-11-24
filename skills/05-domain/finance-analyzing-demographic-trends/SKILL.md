---
name: finance-analyzing-demographic-trends
description: "Structures demographic analysis with population projections, dependency ratios, and economic impact assessment. Use when analyzing demographics, projecting population trends, or assessing demographic economic impact."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-demographic-trends
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-demographic-trends
---

# Finance Analyzing Demographic Trends

## Brief info

Structures demographic analysis with population projections, dependency ratios, and economic impact assessment. Use when analyzing demographics, projecting population trends, or assessing demographic economic impact. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures demographic analysis with population projections, dependency ratios, and economic impact assessment. Use when analyzing demographics, projecting population trends, or assessing demographic economic impact.

## Steps

1. Confirm the task matches this source: Structures demographic analysis with population projections, dependency ratios, and economic impact assessment. Use when analyzing demographics, projecting population trends, or assessing demographic economic impact.
2. Start with the upstream step: Projecting population size, age distribution, or growth rates for a country, region, or market
3. Continue with: Calculating dependency ratios (youth, old-age, total) and assessing fiscal/labor-market implications
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-demographic-trends

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-demographic-trends
```
