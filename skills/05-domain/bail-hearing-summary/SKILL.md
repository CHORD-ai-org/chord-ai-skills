---
name: bail-hearing-summary
description: "Generates structured bail hearing summaries from transcripts and case documents, extracting charges, arguments, conditions, and rulings. Use when summarizing bail hearings, pretrial detention decisions, bond hearings, or release condition orders."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bail-hearing-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/bail-hearing-summary
---

# Bail Hearing Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Generates structured bail hearing summaries from transcripts and case documents, extracting charges, arguments, conditions, and rulings. Use when summarizing bail hearings, pretrial detention decisions, bond hearings, or release condition orders.

## Steps

1. Confirm the task matches this source: Generates structured bail hearing summaries from transcripts and case documents, extracting charges, arguments, conditions, and rulings. Use when summarizing bail hearings, pretrial detention decisions, bond hearings, or
2. Start with the upstream step: Charging documents — complaint, indictment, or information with statute citations
3. Continue with: Hearing transcript or recording
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bail-hearing-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bail-hearing-summary
```
