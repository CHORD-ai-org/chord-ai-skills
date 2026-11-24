---
name: capital-analyzing-commodity-price-risk
description: "Evaluates commodity price exposure with forward curve analysis, hedging strategies, and break-even price sensitivity. Use when analyzing commodity risk, designing hedging programs, or stress testing price assumptions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-commodity-price-risk
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-commodity-price-risk
---

# Capital Analyzing Commodity Price Risk

## Brief info

Evaluates commodity price exposure with forward curve analysis, hedging strategies, and break-even price sensitivity. Use when analyzing commodity risk, designing hedging programs, or stress testing price assumptions. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates commodity price exposure with forward curve analysis, hedging strategies, and break-even price sensitivity. Use when analyzing commodity risk, designing hedging programs, or stress testing price assumptions.

## Steps

1. Confirm the task matches this source: Evaluates commodity price exposure with forward curve analysis, hedging strategies, and break-even price sensitivity. Use when analyzing commodity risk, designing hedging programs, or stress testing price assumptions.
2. Start with the upstream step: Assessing a portfolio's or project's exposure to commodity price movements (crude oil, natural gas, metals, agricultural products)
3. Continue with: Designing or reviewing a hedging program for a producer, refiner, or offtaker
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-commodity-price-risk

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-commodity-price-risk
```
