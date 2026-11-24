---
name: finance-analyzing-agency-mortgage-bonds
description: "Evaluates agency MBS with prepayment modeling, OAS analysis, and convexity assessment. Use when analyzing agency MBS, modeling prepayments, or evaluating mortgage bond convexity."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-agency-mortgage-bonds
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-agency-mortgage-bonds
---

# Finance Analyzing Agency Mortgage Bonds

## Brief info

Evaluates agency MBS with prepayment modeling, OAS analysis, and convexity assessment. Use when analyzing agency MBS, modeling prepayments, or evaluating mortgage bond convexity. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates agency MBS with prepayment modeling, OAS analysis, and convexity assessment. Use when analyzing agency MBS, modeling prepayments, or evaluating mortgage bond convexity.

## Steps

1. Confirm the task matches this source: Evaluates agency MBS with prepayment modeling, OAS analysis, and convexity assessment. Use when analyzing agency MBS, modeling prepayments, or evaluating mortgage bond convexity.
2. Start with the upstream step: Screening agency pass-throughs or CMO tranches for portfolio inclusion
3. Continue with: Comparing OAS across coupons, vintages, or specified-pool stories (e.g., low-balance, high-LTV, NY geo)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-agency-mortgage-bonds

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-agency-mortgage-bonds
```
