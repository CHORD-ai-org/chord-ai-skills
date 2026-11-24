---
name: amicus-curiae-brief
description: "Drafts filing-ready U.S. amicus curiae briefs with rule-anchored compliance, additive thesis selection, record-safe fact handling, and verified authority control. Trigger when asked to draft an amicus or friend-of-the-court brief, prepare FRAP 29/32 or Supreme Court Rule 37 amicus filings, draft consent/leave or disclosure language, or handle amicus procedural requirements at any stage."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/amicus-curiae-brief
source: https://github.com/casemark/skills/tree/main/skills/legal/amicus-curiae-brief
---

# Amicus Curiae Brief

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/amicus-curiae-brief
```
