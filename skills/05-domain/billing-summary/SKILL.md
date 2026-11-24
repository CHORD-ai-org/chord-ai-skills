---
name: billing-summary
description: "Produces privilege-safe U.S. corporate legal billing summaries from time and expense data. Converts entries into client-friendly narratives with categorized hours, rates, expenses, and milestones while enforcing engagement-letter rules and ethical billing safeguards. Use when asked to create a billing summary, invoice narrative, timekeeper breakdown, expense summary, or fee narrative."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/billing-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/billing-summary
---

# Billing Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/billing-summary
```
