---
name: legal-adr-outcomes-summary
description: "Generates structured summaries of mediation and arbitration proceedings, extracting outcomes, settlement terms, monetary amounts, obligations, releases, and enforcement steps. Trigger when the user needs to document mediation settlements, arbitration awards, or partial ADR resolutions from transcripts, agreements, mediator reports, or awards."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-adr-outcomes-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/adr-outcomes-summary
---

# Legal Adr Outcomes Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Generates structured summaries of mediation and arbitration proceedings, extracting outcomes, settlement terms, monetary amounts, obligations, releases, and enforcement steps. Trigger when the user needs to document mediation settlements, arbitration awards, or partial ADR resolutions from transcripts, agreements, mediator reports, or awards.

## Steps

1. Confirm the task matches this source: Generates structured summaries of mediation and arbitration proceedings, extracting outcomes, settlement terms, monetary amounts, obligations, releases, and enforcement steps. Trigger when the user needs to document medi
2. Start with the upstream step: Source document — transcript, settlement agreement, MOU, mediator report, or arbitration award
3. Continue with: Party names and representatives
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/adr-outcomes-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-adr-outcomes-summary
```
