---
name: finance-analyzing-banking-system-health
description: "Structures banking system assessment with capital adequacy, asset quality, and systemic risk evaluation. Use when analyzing banking systems, assessing financial stability, or evaluating systemic risk."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-banking-system-health
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-banking-system-health
---

# Finance Analyzing Banking System Health

## Brief info

Structures banking system assessment with capital adequacy, asset quality, and systemic risk evaluation. Use when analyzing banking systems, assessing financial stability, or evaluating systemic risk. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures banking system assessment with capital adequacy, asset quality, and systemic risk evaluation. Use when analyzing banking systems, assessing financial stability, or evaluating systemic risk.

## Steps

1. Confirm the task matches this source: Structures banking system assessment with capital adequacy, asset quality, and systemic risk evaluation. Use when analyzing banking systems, assessing financial stability, or evaluating systemic risk.
2. Start with the upstream step: Evaluating a country's or region's banking sector stability for policy research or investment analysis
3. Continue with: Assessing systemic risk buildup across a group of financial institutions
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-banking-system-health

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-banking-system-health
```
