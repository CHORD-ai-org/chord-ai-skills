---
name: legal-30b6-corporate-rep
description: ">-"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-30b6-corporate-rep
source: https://github.com/casemark/skills/tree/main/skills/legal/30b6-corporate-rep
---

# Legal 30B6 Corporate Rep

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >-

## Steps

1. Confirm the task matches this source: >-
2. Start with the upstream step: Governing law — FRCP 30(b)(6) or state analog (e.g., Cal. CCP § 2025.230 [VERIFY]), local rules, protective orders
3. Continue with: Case theory — claims, defenses, relief sought
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/30b6-corporate-rep

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-30b6-corporate-rep
```
