---
name: finance-analyzing-cryptocurrency-tax
description: "Structures cryptocurrency tax analysis with cost basis tracking, gain classification, and reporting requirements. Use when analyzing crypto tax, tracking digital asset basis, or classifying crypto transactions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-cryptocurrency-tax
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-cryptocurrency-tax
---

# Finance Analyzing Cryptocurrency Tax

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures cryptocurrency tax analysis with cost basis tracking, gain classification, and reporting requirements. Use when analyzing crypto tax, tracking digital asset basis, or classifying crypto transactions.

## Steps

1. Confirm the task matches this source: Structures cryptocurrency tax analysis with cost basis tracking, gain classification, and reporting requirements. Use when analyzing crypto tax, tracking digital asset basis, or classifying crypto transactions.
2. Start with the upstream step: Analyzing taxable events from cryptocurrency trading, staking, lending, or mining activity
3. Continue with: Determining cost basis methodology and gain/loss classification for digital asset dispositions
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-cryptocurrency-tax

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-cryptocurrency-tax
```
