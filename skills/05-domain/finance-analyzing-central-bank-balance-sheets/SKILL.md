---
name: finance-analyzing-central-bank-balance-sheets
description: "Structures central bank balance sheet analysis with QE/QT impact assessment and reserve management. Use when analyzing central bank operations, evaluating QE effects, or tracking reserve management."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-central-bank-balance-sheets
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-central-bank-balance-sheets
---

# Finance Analyzing Central Bank Balance Sheets

## Brief info

Structures central bank balance sheet analysis with QE/QT impact assessment and reserve management. Use when analyzing central bank operations, evaluating QE effects, or tracking reserve management. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures central bank balance sheet analysis with QE/QT impact assessment and reserve management. Use when analyzing central bank operations, evaluating QE effects, or tracking reserve management.

## Steps

1. Confirm the task matches this source: Structures central bank balance sheet analysis with QE/QT impact assessment and reserve management. Use when analyzing central bank operations, evaluating QE effects, or tracking reserve management.
2. Start with the upstream step: Evaluating the impact of quantitative easing (QE) or quantitative tightening (QT) on asset composition and reserve levels
3. Continue with: Analyzing shifts in a central bank's holdings (treasuries, MBS, corporate bonds, FX reserves) over time
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-central-bank-balance-sheets

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-central-bank-balance-sheets
```
