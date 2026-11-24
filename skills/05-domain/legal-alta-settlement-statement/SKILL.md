---
name: legal-alta-settlement-statement
description: ">-"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-alta-settlement-statement
source: https://github.com/casemark/skills/tree/main/skills/legal/alta-settlement-statement
---

# Legal Alta Settlement Statement

## Brief info

>- Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >-

## Steps

1. Confirm the task matches this source: >-
2. Start with the upstream step: Purchase and Sale Agreement — sales price, earnest money, seller concessions, cost allocation.
3. Continue with: Title Commitment — premiums, endorsements, exception items requiring payoff.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/alta-settlement-statement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-alta-settlement-statement
```
