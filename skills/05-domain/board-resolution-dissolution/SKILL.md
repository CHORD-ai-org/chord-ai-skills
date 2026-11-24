---
name: board-resolution-dissolution
description: "Drafts a board resolution authorizing voluntary corporate dissolution via unanimous written consent of directors. Covers Plan of Complete Liquidation adoption, shareholder approval directive, officer authorizations, and execution provisions. Use when initiating voluntary dissolution, preparing corporate wind-down records, or drafting pre-shareholder dissolution authority under state corporation law."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/board-resolution-dissolution
source: https://github.com/casemark/skills/tree/main/skills/legal/board-resolution-dissolution
---

# Board Resolution Dissolution

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a board resolution authorizing voluntary corporate dissolution via unanimous written consent of directors. Covers Plan of Complete Liquidation adoption, shareholder approval directive, officer authorizations, and execution provisions. Use when initiating voluntary dissolution, preparing corporate wind-down records, or drafting pre-shareholder dissolution authority under state corporation law.

## Steps

1. Confirm the task matches this source: Drafts a board resolution authorizing voluntary corporate dissolution via unanimous written consent of directors. Covers Plan of Complete Liquidation adoption, shareholder approval directive, officer authorizations, and 
2. Start with the upstream step: Corporation details — legal name (per articles), state of incorporation, formation date
3. Continue with: Director roster — full names of all current directors (unanimous consent requires all)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/board-resolution-dissolution

## Verify

```bash
python scripts/check_skills.py skills/05-domain/board-resolution-dissolution
```
