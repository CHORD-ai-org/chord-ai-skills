---
name: breach-purchase-complaint
description: "Drafts a state-court complaint for breach of a real property purchase agreement. Triggers when the user needs to initiate a lawsuit for breach of a real estate purchase contract, purchase agreement breach, or buyer/seller contract dispute. Covers caption, jurisdiction/venue, party allegations, chronological facts, contract elements, damages, and prayer for relief."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/breach-purchase-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/breach-purchase-complaint
---

# Breach Purchase Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a state-court complaint for breach of a real property purchase agreement. Triggers when the user needs to initiate a lawsuit for breach of a real estate purchase contract, purchase agreement breach, or buyer/seller contract dispute. Covers caption, jurisdiction/venue, party allegations, chronological facts, contract elements, damages, and prayer for relief.

## Steps

1. Confirm the task matches this source: Drafts a state-court complaint for breach of a real property purchase agreement. Triggers when the user needs to initiate a lawsuit for breach of a real estate purchase contract, purchase agreement breach, or buyer/selle
2. Start with the upstream step: Executed purchase agreement — all addenda, amendments, exhibits
3. Continue with: Party details — full legal names, entity types, formation states, registered agents, addresses
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/breach-purchase-complaint

## Verify

```bash
python scripts/check_skills.py skills/05-domain/breach-purchase-complaint
```
