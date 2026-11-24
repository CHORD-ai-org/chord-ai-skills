---
name: bylaw-amendment-resolution
description: "Drafts a formal Bylaw Amendment Resolution for U.S. corporations, LLCs, or non-profits. Invoke when a board, shareholders, or members approve bylaw changes and need an auditable WHEREAS/RESOLVED record with amendment text, vote tallies, effective date, and secretary certification for minute books, bank submissions, or state filings."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bylaw-amendment-resolution
source: https://github.com/casemark/skills/tree/main/skills/legal/bylaw-amendment-resolution
---

# Bylaw Amendment Resolution

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bylaw-amendment-resolution
```
