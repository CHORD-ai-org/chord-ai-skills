---
name: compliance-os
description: "Use when running several compliance frameworks at once: which apply, where controls overlap, a mock audit or one evidence checklist. Runs framework_selector.py, cross_framework_mapper.py, audit_simulator.py and evidence_pool_generator.py."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/compliance-os
source: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/compliance-os
---

# Compliance Os

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Compliance and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/compliance-os
```
