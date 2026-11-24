---
name: finance-analyzing-commodity-derivatives
description: "Structures commodity derivative pricing with forward curve construction and convenience yield estimation. Use when pricing commodity derivatives, analyzing forward curves, or modeling commodity markets."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-commodity-derivatives
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-commodity-derivatives
---

# Finance Analyzing Commodity Derivatives

## Brief info

Structures commodity derivative pricing with forward curve construction and convenience yield estimation. Use when pricing commodity derivatives, analyzing forward curves, or modeling commodity markets. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures commodity derivative pricing with forward curve construction and convenience yield estimation. Use when pricing commodity derivatives, analyzing forward curves, or modeling commodity markets.

## Steps

1. Confirm the task matches this source: Structures commodity derivative pricing with forward curve construction and convenience yield estimation. Use when pricing commodity derivatives, analyzing forward curves, or modeling commodity markets.
2. Start with the upstream step: Pricing commodity futures, options, or swaps on energy, metals, or agricultural underlyings
3. Continue with: Constructing or validating a forward curve from observed futures prices and basis quotes
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-commodity-derivatives

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-commodity-derivatives
```
