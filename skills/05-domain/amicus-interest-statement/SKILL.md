---
name: amicus-interest-statement
description: "Drafts the \"Interest of Amicus Curiae\" section of an amicus brief. Establishes institutional credibility, tethers the amicus's interest to the specific legal question, articulates non-party impacts, and embeds disclosure guardrails under FRAP 29 and Supreme Court Rule 37. Trigger when drafting amicus briefs, friend-of-the-court filings, interest statements, amicus disclosures, or when the user asks why an organization belongs in a case."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/amicus-interest-statement
source: https://github.com/casemark/skills/tree/main/skills/legal/amicus-interest-statement
---

# Amicus Interest Statement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts the \"Interest of Amicus Curiae\" section of an amicus brief. Establishes institutional credibility, tethers the amicus's interest to the specific legal question, articulates non-party impacts, and embeds disclosure guardrails under FRAP 29 and Supreme Court Rule 37. Trigger when drafting amicus briefs, friend-of-the-court filings, interest statements, amicus disclosures, or when the user asks why an organization belongs in a case.

## Steps

1. Confirm the task matches this source: Drafts the \"Interest of Amicus Curiae\" section of an amicus brief. Establishes institutional credibility, tethers the amicus's interest to the specific legal question, articulates non-party impacts, and embeds disclosu
2. Start with the upstream step: Case context — caption, court, docket number, stage, questions presented, decision below
3. Continue with: Amicus identity — legal name, entity type, founding year, membership size/scope, coalition status
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/amicus-interest-statement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/amicus-interest-statement
```
