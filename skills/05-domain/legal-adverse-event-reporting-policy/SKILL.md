---
name: legal-adverse-event-reporting-policy
description: ">"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-adverse-event-reporting-policy
source: https://github.com/casemark/skills/tree/main/skills/legal/adverse-event-reporting-policy
---

# Legal Adverse Event Reporting Policy

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >

## Steps

1. Confirm the task matches this source: >
2. Start with the upstream step: Organization type — pharmaceutical sponsor, CRO, healthcare system, academic medical center, or combination
3. Continue with: Product portfolio — IND products (Phase I–IV), approved drugs, biologics, devices, combination products, REMS-covered products
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/adverse-event-reporting-policy

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-adverse-event-reporting-policy
```
