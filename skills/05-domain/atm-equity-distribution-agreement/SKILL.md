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

Use when the task matches this source: Drafts a market-standard At-The-Market (ATM) Equity Distribution Agreement for public issuers conducting continuous shelf offerings under Rule 415(a)(4). Use when establishing or renewing an ATM program under an effective Form S-3, drafting a sales agent agreement, or structuring a continuous equity offering program.

## Steps

1. Confirm the task matches this source: Drafts a market-standard At-The-Market (ATM) Equity Distribution Agreement for public issuers conducting continuous shelf offerings under Rule 415(a)(4). Use when establishing or renewing an ATM program under an effectiv
2. Start with the upstream step: Issuer — legal name, state of incorporation, principal office
3. Continue with: Registration statement — Form S-3 file number, effective date, maximum aggregate offering amount
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/atm-equity-distribution-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/atm-equity-distribution-agreement
```
