---
name: bankruptcy-interest-calculation
description: "Calculates pre-petition interest for bankruptcy proofs of claim and produces a filing-ready worksheet. Covers rate source hierarchy, day-count conventions, simple interest formulas, post-petition rules under 11 U.S.C. § 506(b), and fee inclusion standards. Use when preparing interest components of a proof of claim, calculating creditor claim amounts, or verifying interest calculations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bankruptcy-interest-calculation
source: https://github.com/casemark/skills/tree/main/skills/legal/bankruptcy-interest-calculation
---

# Bankruptcy Interest Calculation

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bankruptcy-interest-calculation
```
