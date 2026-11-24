---
name: bank-account-resolution
description: "Drafts U.S. corporate board resolutions authorizing bank account opening, signatory designation, transaction limits, and related banking documents with ratification, supersession, and secretary certification language. Use when preparing board resolutions, written consents, bank account opening packets, signatory authority letters, or banking authorization documents. Trigger keywords: bank account resolution, banking resolution, board consent, signatory authority, account opening, ACH, wire, signature card."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bank-account-resolution
source: https://github.com/casemark/skills/tree/main/skills/legal/bank-account-resolution
---

# Bank Account Resolution

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. corporate board resolutions authorizing bank account opening, signatory designation, transaction limits, and related banking documents with ratification, supersession, and secretary certification language. Use when preparing board resolutions, written consents, bank account opening packets, signatory authority letters, or banking authorization documents. Trigger keywords: bank account resolution, banking resolution, board consent, signatory authority, account opening, ACH, wire, signature card.

## Steps

1. Confirm the task matches this source: Drafts U.S. corporate board resolutions authorizing bank account opening, signatory designation, transaction limits, and related banking documents with ratification, supersession, and secretary certification language. Us
2. Start with the upstream step: Corporate legal name and state of incorporation (from charter)
3. Continue with: Bylaws provisions on board action, quorum, notice, written consent
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bank-account-resolution

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bank-account-resolution
```
