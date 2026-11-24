---
name: finance-analyzing-corporate-tax-structures
description: ">"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-corporate-tax-structures
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-corporate-tax-structures
---

# Finance Analyzing Corporate Tax Structures

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >

## Steps

1. Confirm the task matches this source: >
2. Start with the upstream step: Draft only. Every comparison, status conclusion and recommendation is a draft for review by a qualified tax adviser. Never call a conclusion final, an opinion, or confirmed for ...
3. Continue with: Source-review gate. Never call a document missing until the inventory has been checked and each file opened, including exhibits, side letters and spreadsheet tabs. Classify ever...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-corporate-tax-structures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-corporate-tax-structures
```
