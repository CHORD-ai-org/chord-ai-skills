---
name: finance-analyzing-alternative-investments
description: "Evaluates alternative investment strategies (hedge funds, real assets, private markets) with risk-return and liquidity analysis. Use when analyzing alternatives, evaluating fund strategies, or assessing illiquidity premiums."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-alternative-investments
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-alternative-investments
---

# Finance Analyzing Alternative Investments

## Brief info

Evaluates alternative investment strategies (hedge funds, real assets, private markets) with risk-return and liquidity analysis. Use when analyzing alternatives, evaluating fund strategies, or assessing illiquidity premiums. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates alternative investment strategies (hedge funds, real assets, private markets) with risk-return and liquidity analysis. Use when analyzing alternatives, evaluating fund strategies, or assessing illiquidity premiums.

## Steps

1. Confirm the task matches this source: Evaluates alternative investment strategies (hedge funds, real assets, private markets) with risk-return and liquidity analysis. Use when analyzing alternatives, evaluating fund strategies, or assessing illiquidity premi
2. Start with the upstream step: Evaluating a specific fund or strategy for inclusion in a portfolio
3. Continue with: Comparing alternative strategies against each other or against public-market benchmarks
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-alternative-investments

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-alternative-investments
```
