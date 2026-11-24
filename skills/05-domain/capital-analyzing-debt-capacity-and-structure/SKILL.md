---
name: capital-analyzing-debt-capacity-and-structure
description: "Evaluates target leverage capacity with cash flow coverage, stress testing, and optimal debt structure across term loans, revolver, and mezzanine. Use when analyzing debt capacity, structuring acquisition financing, or stress testing leverage."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-debt-capacity-and-structure
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-debt-capacity-and-structure
---

# Capital Analyzing Debt Capacity And Structure

## Brief info

Evaluates target leverage capacity with cash flow coverage, stress testing, and optimal debt structure across term loans, revolver, and mezzanine. Use when analyzing debt capacity, structuring acquisition financing, or stress testing leverage. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates target leverage capacity with cash flow coverage, stress testing, and optimal debt structure across term loans, revolver, and mezzanine. Use when analyzing debt capacity, structuring acquisition financing, or stress testing leverage.

## Steps

1. Confirm the task matches this source: Evaluates target leverage capacity with cash flow coverage, stress testing, and optimal debt structure across term loans, revolver, and mezzanine. Use when analyzing debt capacity, structuring acquisition financing, or s
2. Start with the upstream step: Sizing acquisition debt for an LBO or growth equity recapitalization
3. Continue with: Evaluating how much leverage a target's cash flows can support under base and downside scenarios
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-debt-capacity-and-structure

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-debt-capacity-and-structure
```
