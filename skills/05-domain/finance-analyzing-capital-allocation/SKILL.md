---
name: finance-analyzing-capital-allocation
description: "Evaluates management capital allocation decisions across M&A, buybacks, dividends, and reinvestment. Use when assessing capital allocation, analyzing ROIC, or evaluating shareholder return strategies."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-capital-allocation
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-capital-allocation
---

# Finance Analyzing Capital Allocation

## Brief info

Evaluates management capital allocation decisions across M&A, buybacks, dividends, and reinvestment. Use when assessing capital allocation, analyzing ROIC, or evaluating shareholder return strategies. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates management capital allocation decisions across M&A, buybacks, dividends, and reinvestment. Use when assessing capital allocation, analyzing ROIC, or evaluating shareholder return strategies.

## Steps

1. Confirm the task matches this source: Evaluates management capital allocation decisions across M&A, buybacks, dividends, and reinvestment. Use when assessing capital allocation, analyzing ROIC, or evaluating shareholder return strategies.
2. Start with the upstream step: Evaluating how management deploys free cash flow across competing uses (M&A, buybacks, dividends, organic reinvestment, debt paydown)
3. Continue with: Scoring management quality for equity research or investment committee memos
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-capital-allocation

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-capital-allocation
```
