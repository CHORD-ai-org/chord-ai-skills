---
name: appeal-document-summary
description: "Produces structured U.S. appellate document summaries mapping procedural posture, issues on appeal, standards of review, and competing arguments into memo-ready format. Use when summarizing appellate briefs, notices of appeal, records on appeal, or preparing for oral argument. Triggers: appeal, appellate, notice of appeal, standard of review, cross-appeal, appellate brief intake, record on appeal synthesis."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appeal-document-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/appeal-document-summary
---

# Appeal Document Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appeal-document-summary
```
