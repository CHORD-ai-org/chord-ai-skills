---
name: case-summary-report
description: "Synthesizes multiple case summaries into one unified Case Summary Report. Triggers when the user has two or more case summaries, document analyses, or memoranda and needs them consolidated into a single report with patterns, contradictions, and gaps identified."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/case-summary-report
source: https://github.com/casemark/skills/tree/main/skills/legal/case-summary-report
---

# Case Summary Report

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Synthesizes multiple case summaries into one unified Case Summary Report. Triggers when the user has two or more case summaries, document analyses, or memoranda and needs them consolidated into a single report with patterns, contradictions, and gaps identified.

## Steps

1. Confirm the task matches this source: Synthesizes multiple case summaries into one unified Case Summary Report. Triggers when the user has two or more case summaries, document analyses, or memoranda and needs them consolidated into a single report with patte
2. Start with the upstream step: Inventory sources — For each summary, record title, date, author, and scope in a source index table.
3. Continue with: Map overlap — Identify where multiple summaries cover the same events, witnesses, or issues.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/case-summary-report

## Verify

```bash
python scripts/check_skills.py skills/05-domain/case-summary-report
```
