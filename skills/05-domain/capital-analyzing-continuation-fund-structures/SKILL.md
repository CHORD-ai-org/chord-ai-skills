---
name: capital-analyzing-continuation-fund-structures
description: "Evaluates GP-led continuation vehicle structures with existing LP options, pricing methodology, and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-continuation-fund-structures
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-continuation-fund-structures
---

# Capital Analyzing Continuation Fund Structures

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates GP-led continuation vehicle structures with existing LP options, pricing methodology, and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers.

## Steps

1. Confirm the task matches this source: Evaluates GP-led continuation vehicle structures with existing LP options, pricing methodology, and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offe
2. Start with the upstream step: Evaluating a GP-led secondary transaction where portfolio assets roll into a new continuation vehicle (CV)
3. Continue with: Assessing LP election options (rollover, cash-out, partial liquidity) in a tender offer or stapled secondary
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-continuation-fund-structures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-continuation-fund-structures
```
