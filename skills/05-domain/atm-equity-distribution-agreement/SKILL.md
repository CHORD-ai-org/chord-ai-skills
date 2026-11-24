---
name: atm-equity-distribution-agreement
description: "Drafts a market-standard At-The-Market (ATM) Equity Distribution Agreement for public issuers conducting continuous shelf offerings under Rule 415(a)(4). Use when establishing or renewing an ATM program under an effective Form S-3, drafting a sales agent agreement, or structuring a continuous equity offering program."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/atm-equity-distribution-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/atm-equity-distribution-agreement
---

# Atm Equity Distribution Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/atm-equity-distribution-agreement
```
