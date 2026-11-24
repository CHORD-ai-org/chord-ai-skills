---
name: chart-audit-protocol
description: "Drafts healthcare chart audit protocols covering clinical documentation review, coding accuracy, and billing compliance. Aligns with Medicare CoPs, OIG Compliance Program Guidance, RAC preparedness, federal sentencing guidelines, and the 60-day overpayment rule. Use when drafting routine periodic audits, targeted risk reviews, proactive compliance measures, or post-regulatory-update assessments."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/chart-audit-protocol
source: https://github.com/casemark/skills/tree/main/skills/legal/chart-audit-protocol
---

# Chart Audit Protocol

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/chart-audit-protocol
```
