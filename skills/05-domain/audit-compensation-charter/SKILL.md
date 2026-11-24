---
name: audit-compensation-charter
description: "Drafts board-adopted charters establishing Audit and Compensation Committees for U.S. corporations, covering composition, independence, delegated powers, meeting protocol, reporting, and annual review. Adapts for public (SEC/SOX/exchange) or private governance regimes. Use when creating or refreshing committee charters, preparing for IPO governance readiness, onboarding directors, or conducting governance cleanup. Trigger keywords: audit committee charter, compensation committee charter, board governance, SOX compliance, Rule 10A-3, exchange-standard committees."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/audit-compensation-charter
source: https://github.com/casemark/skills/tree/main/skills/legal/audit-compensation-charter
---

# Audit Compensation Charter

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/audit-compensation-charter
```
