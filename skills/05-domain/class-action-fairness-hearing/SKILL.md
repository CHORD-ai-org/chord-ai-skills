---
name: class-action-fairness-hearing
description: "Drafts FRCP 23(e)-compliant fairness hearing notices for class action settlements. Covers settlement terms, opt-out rights, objection procedures, and hearing logistics. Use when notifying class members of a proposed settlement pending court approval."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-action-fairness-hearing
source: https://github.com/casemark/skills/tree/main/skills/legal/class-action-fairness-hearing
---

# Class Action Fairness Hearing

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-action-fairness-hearing
```
