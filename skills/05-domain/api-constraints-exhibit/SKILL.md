---
name: api-constraints-exhibit
description: "Extracts technical API constraints from OpenAPI/Swagger specs and developer docs into a contract-ready API Access & Constraints Schedule with source traceability, risk flags, and change-control language. Use when drafting legal exhibits or schedules covering API access scope, rate limits, authentication, data fields, or deprecation terms for MSAs, SOWs, or order forms."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/api-constraints-exhibit
source: https://github.com/casemark/skills/tree/main/skills/legal/api-constraints-exhibit
---

# Api Constraints Exhibit

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/api-constraints-exhibit
```
