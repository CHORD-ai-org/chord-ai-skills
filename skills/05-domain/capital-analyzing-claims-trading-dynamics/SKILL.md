---
name: capital-analyzing-claims-trading-dynamics
description: "Evaluates claims trading market with trading levels, holder identification, and blocking position analysis. Use when analyzing claims markets, tracking distressed debt trading, or evaluating ad hoc group dynamics."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-claims-trading-dynamics
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-claims-trading-dynamics
---

# Capital Analyzing Claims Trading Dynamics

## Brief info

Evaluates claims trading market with trading levels, holder identification, and blocking position analysis. Use when analyzing claims markets, tracking distressed debt trading, or evaluating ad hoc group dynamics. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates claims trading market with trading levels, holder identification, and blocking position analysis. Use when analyzing claims markets, tracking distressed debt trading, or evaluating ad hoc group dynamics.

## Steps

1. Confirm the task matches this source: Evaluates claims trading market with trading levels, holder identification, and blocking position analysis. Use when analyzing claims markets, tracking distressed debt trading, or evaluating ad hoc group dynamics.
2. Start with the upstream step: Mapping the secondary market for claims against a debtor in or approaching Chapter 11
3. Continue with: Identifying whether an ad hoc group or single holder is building a blocking position in a particular class
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-claims-trading-dynamics

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-claims-trading-dynamics
```
