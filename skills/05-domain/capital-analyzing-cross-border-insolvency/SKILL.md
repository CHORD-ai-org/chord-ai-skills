---
name: capital-analyzing-cross-border-insolvency
description: "Evaluates multi-jurisdictional restructuring with Chapter 15 recognition, COMI analysis, and parallel proceeding coordination. Use when analyzing cross-border insolvency, assessing jurisdiction selection, or coordinating multi-country restructurings."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-border-insolvency
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-border-insolvency
---

# Capital Analyzing Cross Border Insolvency

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates multi-jurisdictional restructuring with Chapter 15 recognition, COMI analysis, and parallel proceeding coordination. Use when analyzing cross-border insolvency, assessing jurisdiction selection, or coordinating multi-country restructurings.

## Steps

1. Confirm the task matches this source: Evaluates multi-jurisdictional restructuring with Chapter 15 recognition, COMI analysis, and parallel proceeding coordination. Use when analyzing cross-border insolvency, assessing jurisdiction selection, or coordinating
2. Start with the upstream step: A debtor entity has assets, creditors, or operations in more than one country and a restructuring or liquidation is underway or anticipated.
3. Continue with: A foreign representative seeks Chapter 15 recognition of a foreign proceeding in the United States.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-border-insolvency

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-border-insolvency
```
