---
name: finance-analyzing-credit-ratings
description: "Interprets and anticipates credit rating actions with methodology analysis and surveillance monitoring. Use when analyzing credit ratings, predicting rating changes, or understanding rating methodology."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-credit-ratings
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-credit-ratings
---

# Finance Analyzing Credit Ratings

## Brief info

Interprets and anticipates credit rating actions with methodology analysis and surveillance monitoring. Use when analyzing credit ratings, predicting rating changes, or understanding rating methodology. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Interprets and anticipates credit rating actions with methodology analysis and surveillance monitoring. Use when analyzing credit ratings, predicting rating changes, or understanding rating methodology.

## Steps

1. Confirm the task matches this source: Interprets and anticipates credit rating actions with methodology analysis and surveillance monitoring. Use when analyzing credit ratings, predicting rating changes, or understanding rating methodology.
2. Start with the upstream step: Evaluating an issuer's current credit rating relative to fundamental performance and peer positioning
3. Continue with: Predicting potential rating upgrades, downgrades, or outlook changes before official agency action
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-credit-ratings

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-credit-ratings
```
