---
name: amicus-brief
description: "Drafts and analyzes U.S. appellate amicus curiae briefs for non-parties with Rule 29/Rule 37 compliance, unique perspective development, and Bluebook-ready citations. Use when asked to draft or review an amicus brief, friend-of-the-court brief, non-party brief, or anything involving FRAP 29, Supreme Court Rule 37, or appellate amicus practice."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/amicus-brief
source: https://github.com/casemark/skills/tree/main/skills/legal/amicus-brief
---

# Amicus Brief

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts and analyzes U.S. appellate amicus curiae briefs for non-parties with Rule 29/Rule 37 compliance, unique perspective development, and Bluebook-ready citations. Use when asked to draft or review an amicus brief, friend-of-the-court brief, non-party brief, or anything involving FRAP 29, Supreme Court Rule 37, or appellate amicus practice.

## Steps

1. Confirm the task matches this source: Drafts and analyzes U.S. appellate amicus curiae briefs for non-parties with Rule 29/Rule 37 compliance, unique perspective development, and Bluebook-ready citations. Use when asked to draft or review an amicus brief, fr
2. Start with the upstream step: Case posture, issues presented, and parties' arguments or briefs
3. Continue with: Amicus identity, constituency, and concrete stake in outcome
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/amicus-brief

## Verify

```bash
python scripts/check_skills.py skills/05-domain/amicus-brief
```
