---
name: board-committee-charter
description: "Drafts board committee charters for Audit and Compensation Committees tailored to public/private status, exchange listing (NYSE/NASDAQ), and governance requirements. Covers composition, independence, authority, meeting procedures, and reporting. Use when creating or updating audit committee charters, compensation committee charters, or corporate oversight committee formations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/board-committee-charter
source: https://github.com/casemark/skills/tree/main/skills/legal/board-committee-charter
---

# Board Committee Charter

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/board-committee-charter
```
