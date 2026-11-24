---
name: class-claim-form
description: "Drafts U.S. class action settlement claim forms compliant with FRCP 23 and court approval orders. Triggers on claim form drafting, settlement administrator packets, online claim workflows, or class member submission forms."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-claim-form
source: https://github.com/casemark/skills/tree/main/skills/legal/class-claim-form
---

# Class Claim Form

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-claim-form
```
