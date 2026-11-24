---
name: finance-analyzing-correlation-trading
description: "Structures correlation analysis with index vs. tranche pricing and correlation skew assessment. Use when analyzing correlation products, pricing tranches, or evaluating dispersion trades."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-correlation-trading
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-correlation-trading
---

# Finance Analyzing Correlation Trading

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures correlation analysis with index vs. tranche pricing and correlation skew assessment. Use when analyzing correlation products, pricing tranches, or evaluating dispersion trades.

## Steps

1. Confirm the task matches this source: Structures correlation analysis with index vs. tranche pricing and correlation skew assessment. Use when analyzing correlation products, pricing tranches, or evaluating dispersion trades.
2. Start with the upstream step: Pricing or relative-value assessment of synthetic CDO tranches (equity, mezzanine, senior)
3. Continue with: Evaluating index vs. single-name basis (e.g., CDX.NA.IG/HY vs. constituent CDS)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-correlation-trading

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-correlation-trading
```
