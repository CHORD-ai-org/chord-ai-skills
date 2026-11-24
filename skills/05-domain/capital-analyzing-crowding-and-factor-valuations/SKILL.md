---
name: capital-analyzing-crowding-and-factor-valuations
description: "Evaluates factor crowding with positioning analysis, valuation spread monitoring, and unwind risk assessment. Use when analyzing factor crowding, assessing unwind risk, or monitoring factor valuation extremes."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-crowding-and-factor-valuations
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-crowding-and-factor-valuations
---

# Capital Analyzing Crowding And Factor Valuations

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates factor crowding with positioning analysis, valuation spread monitoring, and unwind risk assessment. Use when analyzing factor crowding, assessing unwind risk, or monitoring factor valuation extremes.

## Steps

1. Confirm the task matches this source: Evaluates factor crowding with positioning analysis, valuation spread monitoring, and unwind risk assessment. Use when analyzing factor crowding, assessing unwind risk, or monitoring factor valuation extremes.
2. Start with the upstream step: A factor (value, momentum, quality, low-vol, size, growth) shows abnormal return compression or correlation spikes suggesting crowded positioning
3. Continue with: Portfolio managers need to assess whether current factor tilts carry elevated unwind risk before rebalancing
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-crowding-and-factor-valuations

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-crowding-and-factor-valuations
```
