---
name: area-development-agreement
description: "Drafts Area Development Agreements granting exclusive multi-unit franchise territory rights with phased development schedules. Use when drafting area development agreements, multi-unit franchise expansions, territorial franchise grants, or phased development commitments. Enforces FTC Franchise Rule compliance and state registration requirements."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/area-development-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/area-development-agreement
---

# Area Development Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/area-development-agreement
```
