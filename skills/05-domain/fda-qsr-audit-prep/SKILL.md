---
name: fda-qsr-audit-prep
description: "Use for /compliance-os:fda-qsr-audit-prep, or before an FDA inspection, QMSR internal audit or Form 483 response."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/fda-qsr-audit-prep
source: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/fda-qsr-audit-prep
---

# Fda Qsr Audit Prep

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Compliance and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/fda-qsr-audit-prep
```
