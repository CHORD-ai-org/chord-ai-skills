---
name: finance-analyzing-embedded-finance
description: "Evaluates embedded finance opportunities with distribution economics and regulatory framework analysis. Use when analyzing embedded finance, evaluating BaaS models, or assessing embedded lending/insurance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-embedded-finance
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-embedded-finance
---

# Finance Analyzing Embedded Finance

## Brief info

Evaluates embedded finance opportunities with distribution economics and regulatory framework analysis. Use when analyzing embedded finance, evaluating BaaS models, or assessing embedded lending/insurance. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates embedded finance opportunities with distribution economics and regulatory framework analysis. Use when analyzing embedded finance, evaluating BaaS models, or assessing embedded lending/insurance.

## Steps

1. Confirm the task matches this source: Evaluates embedded finance opportunities with distribution economics and regulatory framework analysis. Use when analyzing embedded finance, evaluating BaaS models, or assessing embedded lending/insurance.
2. Start with the upstream step: Assessing a platform's viability for embedding payments, lending, insurance, or deposit products
3. Continue with: Evaluating BaaS (Banking-as-a-Service) provider relationships and sponsor bank dependencies
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-embedded-finance

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-embedded-finance
```
