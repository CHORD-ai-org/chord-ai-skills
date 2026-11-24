---
name: amicus-coalition-management
description: "Manages multi-organization appellate amicus briefs with single-pen drafting, coalition sign-offs, conflict triage, and compliant disclosures. Use when coordinating a coalition amicus brief, managing amicus sign-on, handling FRAP 29 or Supreme Court Rule 37.6 disclosures, or preparing cover and interest sections for multiple amici."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/amicus-coalition-management
source: https://github.com/casemark/skills/tree/main/skills/legal/amicus-coalition-management
---

# Amicus Coalition Management

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/amicus-coalition-management
```
