---
name: board-meeting-minutes
description: "Drafts U.S. corporate board-of-directors meeting minutes into formal, defensible records documenting valid corporate action and governance process. Triggers on board minutes, directors meeting record, board resolutions, quorum validation, motion and vote capture, corporate secretary records, governance drafting. Requires source materials such as agenda, attendance, bylaws, notices, reports, prior minutes, and resolutions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/board-meeting-minutes
source: https://github.com/casemark/skills/tree/main/skills/legal/board-meeting-minutes
---

# Board Meeting Minutes

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. corporate board-of-directors meeting minutes into formal, defensible records documenting valid corporate action and governance process. Triggers on board minutes, directors meeting record, board resolutions, quorum validation, motion and vote capture, corporate secretary records, governance drafting. Requires source materials such as agenda, attendance, bylaws, notices, reports, prior minutes, and resolutions.

## Steps

1. Confirm the task matches this source: Drafts U.S. corporate board-of-directors meeting minutes into formal, defensible records documenting valid corporate action and governance process. Triggers on board minutes, directors meeting record, board resolutions, 
2. Start with the upstream step: Collect: corporation name, governing docs (bylaws, charter), meeting materials (agenda, notice, attendance, reports, prior minutes), director roster, and state of incorporation.
3. Continue with: Map each source to the intake fields below.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/board-meeting-minutes

## Verify

```bash
python scripts/check_skills.py skills/05-domain/board-meeting-minutes
```
