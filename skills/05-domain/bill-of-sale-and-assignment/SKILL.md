---
name: bill-of-sale-and-assignment
description: "Drafts a Bill of Sale, Assignment and Assumption Agreement for M&A asset purchase closings. Transfers purchased assets (tangible and intangible) from seller to buyer and memorializes assumption of specified liabilities. Use when drafting closing deliverables for asset purchase transactions, including IP assignments, contract rights transfers, and goodwill conveyances."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bill-of-sale-and-assignment
source: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-sale-and-assignment
---

# Bill Of Sale And Assignment

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Bill of Sale, Assignment and Assumption Agreement for M&A asset purchase closings. Transfers purchased assets (tangible and intangible) from seller to buyer and memorializes assumption of specified liabilities. Use when drafting closing deliverables for asset purchase transactions, including IP assignments, contract rights transfers, and goodwill conveyances.

## Steps

1. Confirm the task matches this source: Drafts a Bill of Sale, Assignment and Assumption Agreement for M&A asset purchase closings. Transfers purchased assets (tangible and intangible) from seller to buyer and memorializes assumption of specified liabilities. 
2. Start with the upstream step: Executed APA with defined terms for Purchased Assets, Assumed Liabilities, Excluded Assets
3. Continue with: Asset schedule — complete list of tangible and intangible assets
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-sale-and-assignment

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bill-of-sale-and-assignment
```
