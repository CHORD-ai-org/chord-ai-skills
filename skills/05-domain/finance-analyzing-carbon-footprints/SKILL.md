---
name: finance-analyzing-carbon-footprints
description: "Structures carbon footprint analysis with Scope 1/2/3 measurement and intensity benchmarking. Use when measuring carbon emissions, analyzing Scope 3, or benchmarking carbon intensity."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-carbon-footprints
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-carbon-footprints
---

# Finance Analyzing Carbon Footprints

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures carbon footprint analysis with Scope 1/2/3 measurement and intensity benchmarking. Use when measuring carbon emissions, analyzing Scope 3, or benchmarking carbon intensity.

## Steps

1. Confirm the task matches this source: Structures carbon footprint analysis with Scope 1/2/3 measurement and intensity benchmarking. Use when measuring carbon emissions, analyzing Scope 3, or benchmarking carbon intensity.
2. Start with the upstream step: Measuring a company's or portfolio's greenhouse gas (GHG) emissions across Scope 1, 2, and 3
3. Continue with: Benchmarking carbon intensity (tCO2e per $M revenue, per unit produced, or per square foot)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-carbon-footprints

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-carbon-footprints
```
