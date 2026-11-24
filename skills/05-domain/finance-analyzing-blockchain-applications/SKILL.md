---
name: finance-analyzing-blockchain-applications
description: "Evaluates blockchain use cases in financial services with DLT assessment and implementation feasibility. Use when analyzing blockchain applications, evaluating DLT solutions, or assessing crypto infrastructure."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-blockchain-applications
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-blockchain-applications
---

# Finance Analyzing Blockchain Applications

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates blockchain use cases in financial services with DLT assessment and implementation feasibility. Use when analyzing blockchain applications, evaluating DLT solutions, or assessing crypto infrastructure.

## Steps

1. Confirm the task matches this source: Evaluates blockchain use cases in financial services with DLT assessment and implementation feasibility. Use when analyzing blockchain applications, evaluating DLT solutions, or assessing crypto infrastructure.
2. Start with the upstream step: Assessing whether a blockchain/DLT solution is appropriate for a specific financial services use case (e.g., cross-border payments, trade finance, tokenized assets)
3. Continue with: Evaluating an existing blockchain implementation for scalability, cost, and regulatory compliance
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-blockchain-applications

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-blockchain-applications
```
