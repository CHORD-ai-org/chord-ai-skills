---
name: board-minutes
description: "Drafts corporate board of directors meeting minutes. Triggers on \"board minutes\", \"minutes of board meeting\", \"board of directors meeting minutes\", \"corporate minutes\", \"board resolutions\", or \"bylaws compliance\"."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/board-minutes
source: https://github.com/casemark/skills/tree/main/skills/legal/board-minutes
---

# Board Minutes

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts corporate board of directors meeting minutes. Triggers on \"board minutes\", \"minutes of board meeting\", \"board of directors meeting minutes\", \"corporate minutes\", \"board resolutions\", or \"bylaws compliance\".

## Steps

1. Confirm the task matches this source: Drafts corporate board of directors meeting minutes. Triggers on \"board minutes\", \"minutes of board meeting\", \"board of directors meeting minutes\", \"corporate minutes\", \"board resolutions\", or \"bylaws complian
2. Start with the upstream step: Corporation legal name and jurisdiction of incorporation.
3. Continue with: Meeting date, time, location/virtual platform, and type (regular/special/emergency).
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/board-minutes

## Verify

```bash
python scripts/check_skills.py skills/05-domain/board-minutes
```
