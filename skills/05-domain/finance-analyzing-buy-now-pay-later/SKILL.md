---
name: finance-analyzing-buy-now-pay-later
description: "Evaluates BNPL business models with credit performance, merchant economics, and regulatory treatment. Use when analyzing BNPL, evaluating installment products, or assessing consumer lending innovation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-buy-now-pay-later
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-buy-now-pay-later
---

# Finance Analyzing Buy Now Pay Later

## Brief info

Evaluates BNPL business models with credit performance, merchant economics, and regulatory treatment. Use when analyzing BNPL, evaluating installment products, or assessing consumer lending innovation. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates BNPL business models with credit performance, merchant economics, and regulatory treatment. Use when analyzing BNPL, evaluating installment products, or assessing consumer lending innovation.

## Steps

1. Confirm the task matches this source: Evaluates BNPL business models with credit performance, merchant economics, and regulatory treatment. Use when analyzing BNPL, evaluating installment products, or assessing consumer lending innovation.
2. Start with the upstream step: Evaluating a BNPL provider's business model for investment, partnership, or competitive analysis
3. Continue with: Assessing credit risk and loss performance of installment lending portfolios
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-buy-now-pay-later

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-buy-now-pay-later
```
