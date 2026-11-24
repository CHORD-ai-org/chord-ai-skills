---
name: advance-health-care-directive
description: "Drafts jurisdiction-specific Advance Health Care Directive packages with agent appointment, living will instructions, HIPAA authorization bridge, organ donation preferences, and execution compliance checklists. Trigger when the user mentions advance directive, healthcare proxy, living will, health care agent, HIPAA authorization, medical power of attorney, end-of-life planning, capacity trigger planning, state-specific directive forms, witness/notary requirements for healthcare documents, or cross-state directive portability."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/advance-health-care-directive
source: https://github.com/casemark/skills/tree/main/skills/legal/advance-health-care-directive
---

# Advance Health Care Directive

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/advance-health-care-directive
```
