---
name: appeal-summary
description: "Generates structured analytical summaries of appellate documents covering procedural posture, issues on appeal, standards of review, and strategic assessment. Use when onboarding to an appeal, preparing for oral argument, evaluating appellate risk, or summarizing the appellate record."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appeal-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/appeal-summary
---

# Appeal Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appeal-summary
```
