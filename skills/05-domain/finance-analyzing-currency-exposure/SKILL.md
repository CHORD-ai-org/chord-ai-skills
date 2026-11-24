---
name: finance-analyzing-currency-exposure
description: "Evaluates and manages portfolio currency risk with hedging strategy analysis and cost assessment. Use when analyzing FX exposure, planning currency hedges, or assessing hedging costs."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-currency-exposure
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-currency-exposure
---

# Finance Analyzing Currency Exposure

## Brief info

Evaluates and manages portfolio currency risk with hedging strategy analysis and cost assessment. Use when analyzing FX exposure, planning currency hedges, or assessing hedging costs. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates and manages portfolio currency risk with hedging strategy analysis and cost assessment. Use when analyzing FX exposure, planning currency hedges, or assessing hedging costs.

## Steps

1. Confirm the task matches this source: Evaluates and manages portfolio currency risk with hedging strategy analysis and cost assessment. Use when analyzing FX exposure, planning currency hedges, or assessing hedging costs.
2. Start with the upstream step: Assessing FX risk across a multi-currency portfolio (equity, fixed income, alternatives)
3. Continue with: Evaluating whether to hedge, partially hedge, or leave currency exposure unhedged
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-currency-exposure

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-currency-exposure
```
