---
name: audit-summary
description: "Produces structured U.S. legal audit summaries that distill compliance findings into executive-ready risk prioritization and remediation plans, covering likelihood/impact scoring, consequence analysis, and corrective actions with timelines and owners. Use for legal audits, compliance audits, regulatory audits, compliance gap analyses, risk assessments, audit report summaries, or remediation roadmaps. Trigger keywords: audit summary, compliance findings, audit report, risk prioritization, remediation plan, regulatory exposure, corrective action plan."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/audit-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/audit-summary
---

# Audit Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/audit-summary
```
