---
name: finance-analyzing-bond-structures
description: "Deconstructs bond indenture terms including covenants, call provisions, and credit support features. Use when analyzing bond structures, reviewing indentures, or evaluating bond terms."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-bond-structures
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-bond-structures
---

# Finance Analyzing Bond Structures

## Brief info

Deconstructs bond indenture terms including covenants, call provisions, and credit support features. Use when analyzing bond structures, reviewing indentures, or evaluating bond terms. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Deconstructs bond indenture terms including covenants, call provisions, and credit support features. Use when analyzing bond structures, reviewing indentures, or evaluating bond terms.

## Steps

1. Confirm the task matches this source: Deconstructs bond indenture terms including covenants, call provisions, and credit support features. Use when analyzing bond structures, reviewing indentures, or evaluating bond terms.
2. Start with the upstream step: Reviewing a bond indenture or offering document to extract key structural terms
3. Continue with: Comparing covenant packages across issuers or tranches in a capital structure
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-bond-structures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-bond-structures
```
