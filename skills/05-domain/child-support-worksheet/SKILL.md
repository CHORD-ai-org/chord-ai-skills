---
name: child-support-worksheet
description: "Drafts a child support guidelines worksheet by extracting financial data, applying jurisdiction-specific guideline models, and calculating obligations. Triggers when preparing child support calculations, modification filings, or guideline worksheets for court submission."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/child-support-worksheet
source: https://github.com/casemark/skills/tree/main/skills/legal/child-support-worksheet
---

# Child Support Worksheet

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/child-support-worksheet
```
