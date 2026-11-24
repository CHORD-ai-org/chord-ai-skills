---
name: alta-settlement-statement
description: "Drafts a mathematically balanced ALTA Settlement Statement for U.S. real estate closings, allocating debits and credits between buyer and seller with prorations, payoffs, lender fees, title charges, and transfer taxes. Enforces balance verification (seller credits minus debits equals cash to seller; buyer debits minus credits equals cash from buyer) and cross-references title commitment, loan documents, and purchase agreement. Use when preparing closing financials, settlement statements, HUD-equivalent documents, or real estate closing allocations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/alta-settlement-statement
source: https://github.com/casemark/skills/tree/main/skills/legal/alta-settlement-statement
---

# Alta Settlement Statement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/alta-settlement-statement
```
