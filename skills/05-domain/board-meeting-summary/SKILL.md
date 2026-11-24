---
name: board-meeting-summary
description: "Produces a structured, objective summary of corporate board meetings covering metadata, quorum, attendance, conflicts, resolutions with vote counts, committee reports, and significant corporate actions. Use when summarizing board minutes, creating a corporate governance record, or preparing a post-meeting recap for officers, shareholders, or regulators."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/board-meeting-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/board-meeting-summary
---

# Board Meeting Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces a structured, objective summary of corporate board meetings covering metadata, quorum, attendance, conflicts, resolutions with vote counts, committee reports, and significant corporate actions. Use when summarizing board minutes, creating a corporate governance record, or preparing a post-meeting recap for officers, shareholders, or regulators.

## Steps

1. Confirm the task matches this source: Produces a structured, objective summary of corporate board meetings covering metadata, quorum, attendance, conflicts, resolutions with vote counts, committee reports, and significant corporate actions. Use when summariz
2. Start with the upstream step: Collect inputs: agenda, minutes/notes, attendance list, resolutions, committee reports.
3. Continue with: Populate every section below. Mark missing information as UNKNOWN and flag it in the Issues checklist.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/board-meeting-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/board-meeting-summary
```
