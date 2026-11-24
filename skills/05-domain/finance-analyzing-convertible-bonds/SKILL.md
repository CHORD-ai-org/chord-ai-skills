---
name: finance-analyzing-convertible-bonds
description: "Evaluates convertible bond structures with equity sensitivity, credit floor, and Greeks calculation. Use when analyzing convertibles, calculating conversion premiums, or evaluating hybrid instruments."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-convertible-bonds
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-convertible-bonds
---

# Finance Analyzing Convertible Bonds

## Brief info

Evaluates convertible bond structures with equity sensitivity, credit floor, and Greeks calculation. Use when analyzing convertibles, calculating conversion premiums, or evaluating hybrid instruments. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates convertible bond structures with equity sensitivity, credit floor, and Greeks calculation. Use when analyzing convertibles, calculating conversion premiums, or evaluating hybrid instruments.

## Steps

1. Confirm the task matches this source: Evaluates convertible bond structures with equity sensitivity, credit floor, and Greeks calculation. Use when analyzing convertibles, calculating conversion premiums, or evaluating hybrid instruments.
2. Start with the upstream step: Evaluating a new convertible bond issuance for investment suitability
3. Continue with: Calculating conversion premium, parity, and breakeven horizon for an existing position
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-convertible-bonds

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-convertible-bonds
```
