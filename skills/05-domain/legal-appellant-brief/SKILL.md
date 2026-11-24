---
name: legal-appellant-brief
description: ">-"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-appellant-brief
source: https://github.com/casemark/skills/tree/main/skills/legal/appellant-brief
---

# Legal Appellant Brief

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >-

## Steps

1. Confirm the task matches this source: >-
2. Start with the upstream step: Lower court decision — opinion, order, or judgment being appealed
3. Continue with: Trial record — transcripts, exhibits, motions, and orders
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/appellant-brief

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-appellant-brief
```
