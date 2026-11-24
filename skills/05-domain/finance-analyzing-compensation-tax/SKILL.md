---
name: finance-analyzing-compensation-tax
description: "Evaluates executive compensation tax with Section 409A, 280G golden parachute, and equity comp treatment. Use when analyzing compensation tax, evaluating 409A compliance, or structuring equity compensation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-compensation-tax
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-compensation-tax
---

# Finance Analyzing Compensation Tax

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates executive compensation tax with Section 409A, 280G golden parachute, and equity comp treatment. Use when analyzing compensation tax, evaluating 409A compliance, or structuring equity compensation.

## Steps

1. Confirm the task matches this source: Evaluates executive compensation tax with Section 409A, 280G golden parachute, and equity comp treatment. Use when analyzing compensation tax, evaluating 409A compliance, or structuring equity compensation.
2. Start with the upstream step: Reviewing or structuring deferred compensation plans for Section 409A compliance
3. Continue with: Analyzing change-in-control scenarios for Section 280G parachute payment exposure
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-compensation-tax

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-compensation-tax
```
