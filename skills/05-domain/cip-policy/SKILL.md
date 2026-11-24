---
name: cip-policy
description: "Drafts a U.S. Customer Identification Program (CIP) policy compliant with USA PATRIOT Act Section 326 and 31 CFR 1020.220. Covers identity collection, verification, OFAC screening, CDD/beneficial ownership, recordkeeping, and governance. Trigger when the user needs to create or update a CIP policy, AML onboarding procedures, or exam-ready Section 326 documentation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/cip-policy
source: https://github.com/casemark/skills/tree/main/skills/legal/cip-policy
---

# Cip Policy

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cip-policy
```
