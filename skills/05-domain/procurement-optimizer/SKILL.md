---
name: procurement-optimizer
description: "Cut spend on software and suppliers: SaaS audit, category spend review, slow purchasing cycles, supplier consolidation. Use whenever the user asks which tools or vendors to cut, where money goes, or why buying takes so long."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/procurement-optimizer
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/procurement-optimizer
---

# Procurement Optimizer

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Business operations and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/procurement-optimizer
```
