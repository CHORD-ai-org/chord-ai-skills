---
name: capital-analyzing-counterparty-netting-efficiency
description: "Evaluates netting benefits across derivative portfolios with bilateral vs cleared netting, portfolio compression, and capital savings. Use when analyzing netting efficiency, evaluating compression opportunities, or optimizing counterparty exposure."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-counterparty-netting-efficiency
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-counterparty-netting-efficiency
---

# Capital Analyzing Counterparty Netting Efficiency

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates netting benefits across derivative portfolios with bilateral vs cleared netting, portfolio compression, and capital savings. Use when analyzing netting efficiency, evaluating compression opportunities, or optimizing counterparty exposure.

## Steps

1. Confirm the task matches this source: Evaluates netting benefits across derivative portfolios with bilateral vs cleared netting, portfolio compression, and capital savings. Use when analyzing netting efficiency, evaluating compression opportunities, or optim
2. Start with the upstream step: Assessing gross-to-net exposure ratios across counterparties to identify optimization targets
3. Continue with: Evaluating whether bilateral OTC trades should migrate to central clearing for netting benefit
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-counterparty-netting-efficiency

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-counterparty-netting-efficiency
```
