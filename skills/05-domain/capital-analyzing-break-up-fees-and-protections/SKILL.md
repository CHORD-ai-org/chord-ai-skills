---
name: capital-analyzing-break-up-fees-and-protections
description: "Evaluates deal protection mechanisms including break-up fees, no-shop clauses, matching rights, and force-the-vote provisions. Use when analyzing deal protections, negotiating break fees, or assessing termination provisions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-break-up-fees-and-protections
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-break-up-fees-and-protections
---

# Capital Analyzing Break Up Fees And Protections

## Brief info

Evaluates deal protection mechanisms including break-up fees, no-shop clauses, matching rights, and force-the-vote provisions. Use when analyzing deal protections, negotiating break fees, or assessing termination provisions. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates deal protection mechanisms including break-up fees, no-shop clauses, matching rights, and force-the-vote provisions. Use when analyzing deal protections, negotiating break fees, or assessing termination provisions.

## Steps

1. Confirm the task matches this source: Evaluates deal protection mechanisms including break-up fees, no-shop clauses, matching rights, and force-the-vote provisions. Use when analyzing deal protections, negotiating break fees, or assessing termination provisi
2. Start with the upstream step: Reviewing a signed or draft merger agreement to assess the full suite of deal protections
3. Continue with: Advising a target board on whether proposed break-up fee and no-shop terms satisfy fiduciary obligations
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-break-up-fees-and-protections

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-break-up-fees-and-protections
```
