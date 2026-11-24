---
name: knowledge-ops
description: "Use when writing, checking or cleaning up SOPs and runbooks. Generates them with sop_generator.py, checks 5W2H completeness and links with runbook_validator.py and ingests an existing knowledge base with kb_ingester.py."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/knowledge-ops
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/knowledge-ops
---

# Knowledge Ops

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Business operations and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/knowledge-ops
```
