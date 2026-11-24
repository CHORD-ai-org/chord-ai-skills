---
name: capital-analyzing-alpha-signal-decay
description: "Evaluates signal half-life, turnover implications, and capacity constraints for systematic alpha factors. Use when analyzing signal persistence, evaluating factor decay, or estimating strategy capacity."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-alpha-signal-decay
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-alpha-signal-decay
---

# Capital Analyzing Alpha Signal Decay

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates signal half-life, turnover implications, and capacity constraints for systematic alpha factors. Use when analyzing signal persistence, evaluating factor decay, or estimating strategy capacity.

## Steps

1. Confirm the task matches this source: Evaluates signal half-life, turnover implications, and capacity constraints for systematic alpha factors. Use when analyzing signal persistence, evaluating factor decay, or estimating strategy capacity.
2. Start with the upstream step: Evaluating whether an alpha signal retains predictive power across different holding periods
3. Continue with: Determining optimal rebalance frequency by measuring how quickly signal strength deteriorates
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-alpha-signal-decay

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-alpha-signal-decay
```
