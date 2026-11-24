---
name: legal-30b6-deposition
description: ">-"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-30b6-deposition
source: https://github.com/casemark/skills/tree/main/skills/legal/30b6-deposition
---

# Legal 30B6 Deposition

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >-

## Steps

1. Confirm the task matches this source: >-
2. Start with the upstream step: Determine role: taking or defending
3. Continue with: If taking → draft topic list (Part A), then build examination outline
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/30b6-deposition

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-30b6-deposition
```
