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

Use when the task matches this source: Drafts USMCA/NAFTA Certificates of Origin for preferential tariff treatment on US-Mexico-Canada goods. Verifies origin criteria, HS classifications, and regional value content. Use when preparing trade certificates, customs origin documentation, duty preference claims, or cross-border shipment certifications.

## Steps

1. Confirm the task matches this source: Drafts USMCA/NAFTA Certificates of Origin for preferential tariff treatment on US-Mexico-Canada goods. Verifies origin criteria, HS classifications, and regional value content. Use when preparing trade certificates, cust
2. Start with the upstream step: Commercial invoices and bills of materials for goods being certified
3. Continue with: Production records (material sourcing, manufacturing location, supplier docs)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-origin

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-origin
```
