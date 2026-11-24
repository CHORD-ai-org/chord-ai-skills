---
name: finance-analyzing-credit-default-swaps
description: "Interprets CDS markets with basis analysis, curve dynamics, and credit event monitoring. Use when analyzing CDS spreads, monitoring credit events, or evaluating CDS basis."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-credit-default-swaps
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-credit-default-swaps
---

# Finance Analyzing Credit Default Swaps

## Brief info

Interprets CDS markets with basis analysis, curve dynamics, and credit event monitoring. Use when analyzing CDS spreads, monitoring credit events, or evaluating CDS basis. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Interprets CDS markets with basis analysis, curve dynamics, and credit event monitoring. Use when analyzing CDS spreads, monitoring credit events, or evaluating CDS basis.

## Steps

1. Confirm the task matches this source: Interprets CDS markets with basis analysis, curve dynamics, and credit event monitoring. Use when analyzing CDS spreads, monitoring credit events, or evaluating CDS basis.
2. Start with the upstream step: Evaluating single-name or index CDS spreads for relative value or directional views
3. Continue with: Monitoring credit events (failure to pay, restructuring, bankruptcy) and their settlement implications
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-credit-default-swaps

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-credit-default-swaps
```
