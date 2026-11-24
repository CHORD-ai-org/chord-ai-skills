---
name: bill-summary
description: "Produces neutral, section-pinned U.S. legislative bill summaries translating statutory language into plain terms with identifying data, provisions, fiscal impacts, and controversy. Use when summarizing bills, analyzing proposed legislation, preparing bill briefs, digesting committee reports or fiscal notes, or writing legislative updates."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bill-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/bill-summary
---

# Bill Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces neutral, section-pinned U.S. legislative bill summaries translating statutory language into plain terms with identifying data, provisions, fiscal impacts, and controversy. Use when summarizing bills, analyzing proposed legislation, preparing bill briefs, digesting committee reports or fiscal notes, or writing legislative updates.

## Steps

1. Confirm the task matches this source: Produces neutral, section-pinned U.S. legislative bill summaries translating statutory language into plain terms with identifying data, provisions, fiscal impacts, and controversy. Use when summarizing bills, analyzing p
2. Start with the upstream step: Bill text — full or latest engrossed version
3. Continue with: Metadata — number, title, sponsor(s), chamber, status, amendments
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bill-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bill-summary
```
