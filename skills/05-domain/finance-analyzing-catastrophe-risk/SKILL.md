---
name: finance-analyzing-catastrophe-risk
description: "Structures catastrophe risk assessment with model output interpretation and accumulation monitoring. Use when analyzing cat risk, interpreting cat model results, or managing cat exposure."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-catastrophe-risk
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-catastrophe-risk
---

# Finance Analyzing Catastrophe Risk

## Brief info

Structures catastrophe risk assessment with model output interpretation and accumulation monitoring. Use when analyzing cat risk, interpreting cat model results, or managing cat exposure. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures catastrophe risk assessment with model output interpretation and accumulation monitoring. Use when analyzing cat risk, interpreting cat model results, or managing cat exposure.

## Steps

1. Confirm the task matches this source: Structures catastrophe risk assessment with model output interpretation and accumulation monitoring. Use when analyzing cat risk, interpreting cat model results, or managing cat exposure.
2. Start with the upstream step: Evaluating portfolio exposure to natural catastrophe perils (hurricane, earthquake, flood, wildfire, severe convective storm)
3. Continue with: Interpreting output from vendor cat models (AIR, RMS, CoreLogic) for underwriting or reinsurance placement decisions
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-catastrophe-risk

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-catastrophe-risk
```
