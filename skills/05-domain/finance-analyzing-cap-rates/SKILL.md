---
name: finance-analyzing-cap-rates
description: "Structures capitalization rate analysis with market comparison, risk premium decomposition, and trend assessment. Use when analyzing cap rates, comparing market yields, or assessing pricing trends."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-cap-rates
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-cap-rates
---

# Finance Analyzing Cap Rates

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures capitalization rate analysis with market comparison, risk premium decomposition, and trend assessment. Use when analyzing cap rates, comparing market yields, or assessing pricing trends.

## Steps

1. Confirm the task matches this source: Structures capitalization rate analysis with market comparison, risk premium decomposition, and trend assessment. Use when analyzing cap rates, comparing market yields, or assessing pricing trends.
2. Start with the upstream step: Evaluating acquisition pricing against market benchmarks for a specific property or portfolio
3. Continue with: Comparing yields across property types, geographies, or vintages
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-cap-rates

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-cap-rates
```
