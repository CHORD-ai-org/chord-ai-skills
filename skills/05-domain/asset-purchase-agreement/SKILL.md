---
name: asset-purchase-agreement
description: "Drafts a U.S. Asset Purchase Agreement for deals where a buyer acquires specified business assets while avoiding unwanted liabilities. Enforces itemized asset/liability schedules, purchase price mechanics with working capital true-ups, IRS Form 8594 tax allocation, seller and buyer reps and warranties with disclosure schedules, pre- and post-closing covenants, closing conditions and deliveries, and indemnification with basket/cap limits. Use when drafting an asset purchase agreement, APA, asset acquisition, purchase and sale of assets, asset deal, or excluded liabilities agreement."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/asset-purchase-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/asset-purchase-agreement
---

# Asset Purchase Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a U.S. Asset Purchase Agreement for deals where a buyer acquires specified business assets while avoiding unwanted liabilities. Enforces itemized asset/liability schedules, purchase price mechanics with working capital true-ups, IRS Form 8594 tax allocation, seller and buyer reps and warranties with disclosure schedules, pre- and post-closing covenants, closing conditions and deliveries, and indemnification with basket/cap limits. Use when drafting an asset purchase agreement, APA, asset acquisition, purchase and sale of assets, asset deal, or excluded liabilities agreement.

## Steps

1. Confirm the task matches this source: Drafts a U.S. Asset Purchase Agreement for deals where a buyer acquires specified business assets while avoiding unwanted liabilities. Enforces itemized asset/liability schedules, purchase price mechanics with working ca
2. Start with the upstream step: Parties and structure — legal names, entity types, jurisdictions, signing authority, deal structure
3. Continue with: Asset and liability inventory — preliminary lists for Purchased Assets, Excluded Assets, Assumed Liabilities, Excluded Liabilities
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/asset-purchase-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/asset-purchase-agreement
```
