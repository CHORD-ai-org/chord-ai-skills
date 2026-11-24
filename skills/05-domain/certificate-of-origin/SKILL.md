---
name: certificate-of-origin
description: "Drafts USMCA/NAFTA Certificates of Origin for preferential tariff treatment on US-Mexico-Canada goods. Verifies origin criteria, HS classifications, and regional value content. Use when preparing trade certificates, customs origin documentation, duty preference claims, or cross-border shipment certifications."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/certificate-of-origin
source: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-origin
---

# Certificate Of Origin

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-origin
```
