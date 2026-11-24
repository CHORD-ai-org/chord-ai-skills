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

Use when the task matches this source: Produces structured U.S. class action lawsuit summaries covering claims, class definition, Rule 23 analysis, procedural history, and outcomes. Use when summarizing class actions, class certification rulings, MDL proceedings, or settlement approvals for litigation evaluation, due diligence, or compliance monitoring.

## Steps

1. Confirm the task matches this source: Produces structured U.S. class action lawsuit summaries covering claims, class definition, Rule 23 analysis, procedural history, and outcomes. Use when summarizing class actions, class certification rulings, MDL proceedi
2. Start with the upstream step: Operative complaint (and amendments).
3. Continue with: Docket report with key dates and ECF numbers.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/class-action-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-action-summary
```
