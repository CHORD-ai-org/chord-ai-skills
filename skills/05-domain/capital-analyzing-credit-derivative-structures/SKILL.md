---
name: capital-analyzing-credit-derivative-structures
description: "Evaluates CDS, CDX, and bespoke credit derivative structures with spread analysis and credit event mechanics. Use when analyzing credit derivatives, pricing CDS, or evaluating index tranche products."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-derivative-structures
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-derivative-structures
---

# Capital Analyzing Credit Derivative Structures

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates CDS, CDX, and bespoke credit derivative structures with spread analysis and credit event mechanics. Use when analyzing credit derivatives, pricing CDS, or evaluating index tranche products.

## Steps

1. Confirm the task matches this source: Evaluates CDS, CDX, and bespoke credit derivative structures with spread analysis and credit event mechanics. Use when analyzing credit derivatives, pricing CDS, or evaluating index tranche products.
2. Start with the upstream step: Pricing or re-marking single-name CDS contracts on corporate or sovereign reference entities
3. Continue with: Analyzing CDX or iTraxx index positions, including on-the-run vs. off-the-run roll dynamics
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-derivative-structures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-derivative-structures
```
