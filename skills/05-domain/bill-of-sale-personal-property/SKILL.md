---
name: bill-of-sale-personal-property
description: "Drafts a U.S. CRE personal property Bill of Sale transferring equipment, fixtures, FF&E, inventory, and other tangible assets. Handles inclusion/exclusion schedules, price allocation, tax responsibility, and risk of loss. Trigger when the user needs a bill of sale, asset schedule, equipment transfer document, or personal property conveyance tied to a CRE closing."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bill-of-sale-personal-property
source: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-sale-personal-property
---

# Bill Of Sale Personal Property

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a U.S. CRE personal property Bill of Sale transferring equipment, fixtures, FF&E, inventory, and other tangible assets. Handles inclusion/exclusion schedules, price allocation, tax responsibility, and risk of loss. Trigger when the user needs a bill of sale, asset schedule, equipment transfer document, or personal property conveyance tied to a CRE closing.

## Steps

1. Confirm the task matches this source: Drafts a U.S. CRE personal property Bill of Sale transferring equipment, fixtures, FF&E, inventory, and other tangible assets. Handles inclusion/exclusion schedules, price allocation, tax responsibility, and risk of loss
2. Start with the upstream step: Mirror PSA terms. Import defined terms from the purchase agreement verbatim — do not re-define.
3. Continue with: Insert parties. Full legal names, entity types, formation states, authority language.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-sale-personal-property

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bill-of-sale-personal-property
```
