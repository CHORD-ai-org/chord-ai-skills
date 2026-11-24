---
name: bill-of-sale
description: "Drafts a U.S. Bill of Sale for transferring personal property ownership from seller to buyer. Covers vehicles, equipment, watercraft, firearms, business assets, and general personal property. Enforces party identification, property description, consideration, condition representations, title warranty, lien disclosure, and jurisdiction-specific execution requirements. Use when drafting a bill of sale, asset transfer document, or ownership transfer instrument."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bill-of-sale
source: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-sale
---

# Bill Of Sale

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a U.S. Bill of Sale for transferring personal property ownership from seller to buyer. Covers vehicles, equipment, watercraft, firearms, business assets, and general personal property. Enforces party identification, property description, consideration, condition representations, title warranty, lien disclosure, and jurisdiction-specific execution requirements. Use when drafting a bill of sale, asset transfer document, or ownership transfer instrument.

## Steps

1. Confirm the task matches this source: Drafts a U.S. Bill of Sale for transferring personal property ownership from seller to buyer. Covers vehicles, equipment, watercraft, firearms, business assets, and general personal property. Enforces party identificatio
2. Start with the upstream step: Property — type, make, model, year, serial/VIN/HIN, condition, mileage (vehicles)
3. Continue with: Parties — full legal names, addresses, capacity (individual or entity)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-sale

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bill-of-sale
```
