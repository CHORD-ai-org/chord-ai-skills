---
name: finance-analyzing-business-cycle-positioning
description: "Structures business cycle analysis with phase identification, leading indicator tracking, and sector implications. Use when identifying cycle phase, tracking business cycles, or assessing cyclical positioning."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-business-cycle-positioning
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-business-cycle-positioning
---

# Finance Analyzing Business Cycle Positioning

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures business cycle analysis with phase identification, leading indicator tracking, and sector implications. Use when identifying cycle phase, tracking business cycles, or assessing cyclical positioning.

## Steps

1. Confirm the task matches this source: Structures business cycle analysis with phase identification, leading indicator tracking, and sector implications. Use when identifying cycle phase, tracking business cycles, or assessing cyclical positioning.
2. Start with the upstream step: Determining which phase of the business cycle an economy currently occupies (expansion, peak, contraction, trough)
3. Continue with: Assessing whether leading indicators signal a regime change or phase transition
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-business-cycle-positioning

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-business-cycle-positioning
```
