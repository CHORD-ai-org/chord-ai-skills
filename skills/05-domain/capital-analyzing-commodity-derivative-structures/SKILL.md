---
name: capital-analyzing-commodity-derivative-structures
description: "Evaluates commodity swaps, options, and exotic structures with seasonality, convenience yield, and storage cost analysis. Use when pricing commodity derivatives, analyzing energy structures, or evaluating commodity hedging."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-commodity-derivative-structures
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-commodity-derivative-structures
---

# Capital Analyzing Commodity Derivative Structures

## Brief info

Evaluates commodity swaps, options, and exotic structures with seasonality, convenience yield, and storage cost analysis. Use when pricing commodity derivatives, analyzing energy structures, or evaluating commodity hedging. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates commodity swaps, options, and exotic structures with seasonality, convenience yield, and storage cost analysis. Use when pricing commodity derivatives, analyzing energy structures, or evaluating commodity hedging.

## Steps

1. Confirm the task matches this source: Evaluates commodity swaps, options, and exotic structures with seasonality, convenience yield, and storage cost analysis. Use when pricing commodity derivatives, analyzing energy structures, or evaluating commodity hedgi
2. Start with the upstream step: Pricing or re-pricing commodity swaps (fixed-for-floating, basis swaps, calendar spreads)
3. Continue with: Valuing commodity options — vanillas, Asian (average-price), spread options, barrier/knock-in/knock-out structures
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-commodity-derivative-structures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-commodity-derivative-structures
```
