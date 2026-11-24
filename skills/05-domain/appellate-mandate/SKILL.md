---
name: appellate-mandate
description: "Drafts formal appellate mandates that conclude the appeal process and direct trial courts to implement appellate decisions. Extracts disposition language, remand directives, and procedural history from appellate records to construct jurisdiction-specific mandate orders. Use when preparing mandate orders, returning jurisdiction to lower courts, or formalizing appellate dispositions after ruling."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appellate-mandate
source: https://github.com/casemark/skills/tree/main/skills/legal/appellate-mandate
---

# Appellate Mandate

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appellate-mandate
```
