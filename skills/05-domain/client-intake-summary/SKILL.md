---
name: client-intake-summary
description: "Produces a structured corporate-client intake brief from intake forms, consultation notes, and initial communications. Use when onboarding a new corporate matter, processing an intake packet, summarizing consult notes, running a conflict check, or triaging deadlines for a corporate governance matter."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/client-intake-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/client-intake-summary
---

# Client Intake Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/client-intake-summary
```
