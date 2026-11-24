---
name: class-action-summary
description: "Produces structured U.S. class action lawsuit summaries covering claims, class definition, Rule 23 analysis, procedural history, and outcomes. Use when summarizing class actions, class certification rulings, MDL proceedings, or settlement approvals for litigation evaluation, due diligence, or compliance monitoring."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-action-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/class-action-summary
---

# Class Action Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-action-summary
```
