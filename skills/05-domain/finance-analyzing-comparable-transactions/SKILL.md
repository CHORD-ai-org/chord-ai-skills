---
name: finance-analyzing-comparable-transactions
description: "Structures precedent transaction analysis with deal multiples, premium calculation, and transaction characteristic comparison. Use when analyzing M&A precedents, calculating transaction multiples, or benchmarking deal terms."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-comparable-transactions
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-comparable-transactions
---

# Finance Analyzing Comparable Transactions

## Brief info

Structures precedent transaction analysis with deal multiples, premium calculation, and transaction characteristic comparison. Use when analyzing M&A precedents, calculating transaction multiples, or benchmarking deal terms. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures precedent transaction analysis with deal multiples, premium calculation, and transaction characteristic comparison. Use when analyzing M&A precedents, calculating transaction multiples, or benchmarking deal terms.

## Steps

1. Confirm the task matches this source: Structures precedent transaction analysis with deal multiples, premium calculation, and transaction characteristic comparison. Use when analyzing M&A precedents, calculating transaction multiples, or benchmarking deal te
2. Start with the upstream step: Building a precedent transactions analysis for a sell-side or buy-side pitch book
3. Continue with: Benchmarking a proposed offer price or premium against historical M&A deals
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-comparable-transactions

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-comparable-transactions
```
