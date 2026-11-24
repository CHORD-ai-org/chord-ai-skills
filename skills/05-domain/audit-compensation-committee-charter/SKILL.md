---
name: audit-compensation-committee-charter
description: "Drafts a combined Audit and Compensation Committee charter for U.S. boards, tailored for public or private companies with listing-standard compliance, independence criteria, and SOX readiness. Triggers when the user needs a board committee charter, audit committee charter, compensation committee charter, or governance mandate for SEC/NYSE/NASDAQ compliance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/audit-compensation-committee-charter
source: https://github.com/casemark/skills/tree/main/skills/legal/audit-compensation-committee-charter
---

# Audit Compensation Committee Charter

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/audit-compensation-committee-charter
```
