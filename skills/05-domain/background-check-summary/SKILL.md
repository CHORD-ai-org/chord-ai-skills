---
name: background-check-summary
description: "Summarizes raw background check data into structured executive reports with risk categorization (GREEN/YELLOW/RED). Use when processing criminal records, court filings, employment/education verification, sanctions screening, or adverse media for pre-employment screening, executive due diligence, or investment-grade investigations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/background-check-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/background-check-summary
---

# Background Check Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/background-check-summary
```
