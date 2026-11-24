---
name: finance-analyzing-cross-border-transactions
description: "Evaluates cross-border M&A considerations including currency, tax, regulatory, and cultural factors. Use when analyzing international deals, assessing cross-border risks, or structuring multinational transactions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-cross-border-transactions
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-cross-border-transactions
---

# Finance Analyzing Cross Border Transactions

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates cross-border M&A considerations including currency, tax, regulatory, and cultural factors. Use when analyzing international deals, assessing cross-border risks, or structuring multinational transactions.

## Steps

1. Confirm the task matches this source: Evaluates cross-border M&A considerations including currency, tax, regulatory, and cultural factors. Use when analyzing international deals, assessing cross-border risks, or structuring multinational transactions.
2. Start with the upstream step: Assessing a proposed acquisition or merger involving entities in different jurisdictions
3. Continue with: Evaluating foreign-to-domestic or domestic-to-foreign deal structures (inbound vs. outbound transactions)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-cross-border-transactions

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-cross-border-transactions
```
