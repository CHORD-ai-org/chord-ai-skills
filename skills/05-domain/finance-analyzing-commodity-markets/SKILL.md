---
name: finance-analyzing-commodity-markets
description: "Structures commodity market analysis with supply/demand balances, inventory dynamics, and price driver attribution. Use when analyzing commodities, evaluating supply/demand, or forecasting commodity prices."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-commodity-markets
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-commodity-markets
---

# Finance Analyzing Commodity Markets

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures commodity market analysis with supply/demand balances, inventory dynamics, and price driver attribution. Use when analyzing commodities, evaluating supply/demand, or forecasting commodity prices.

## Steps

1. Confirm the task matches this source: Structures commodity market analysis with supply/demand balances, inventory dynamics, and price driver attribution. Use when analyzing commodities, evaluating supply/demand, or forecasting commodity prices.
2. Start with the upstream step: Building a supply/demand balance for a specific commodity (e.g., crude oil, copper, wheat, natural gas)
3. Continue with: Attributing recent price moves to fundamental, technical, or macro drivers
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-commodity-markets

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-commodity-markets
```
