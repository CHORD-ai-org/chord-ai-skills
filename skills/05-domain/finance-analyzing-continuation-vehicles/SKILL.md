---
name: finance-analyzing-continuation-vehicles
description: "Evaluates GP-led continuation fund structures with existing LP options and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-continuation-vehicles
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-continuation-vehicles
---

# Finance Analyzing Continuation Vehicles

## Brief info

Evaluates GP-led continuation fund structures with existing LP options and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates GP-led continuation fund structures with existing LP options and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers.

## Steps

1. Confirm the task matches this source: Evaluates GP-led continuation fund structures with existing LP options and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers.
2. Start with the upstream step: A GP proposes transferring one or more portfolio assets from a legacy fund into a new continuation vehicle
3. Continue with: Existing LPs must decide between rolling over, selling at a stated NAV, or a hybrid election
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-continuation-vehicles

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-continuation-vehicles
```
