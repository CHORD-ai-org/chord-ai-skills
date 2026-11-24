---
name: class-action-notice
description: "Drafts Rule 23-compliant class action notices to absent class members for certification or settlement. Agent uses this skill when drafting class action notices, class member notifications, settlement notices, opt-out notices, or fairness hearing notices."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-action-notice
source: https://github.com/casemark/skills/tree/main/skills/legal/class-action-notice
---

# Class Action Notice

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts Rule 23-compliant class action notices to absent class members for certification or settlement. Agent uses this skill when drafting class action notices, class member notifications, settlement notices, opt-out notices, or fairness hearing notices.

## Steps

1. Confirm the task matches this source: Drafts Rule 23-compliant class action notices to absent class members for certification or settlement. Agent uses this skill when drafting class action notices, class member notifications, settlement notices, opt-out not
2. Start with the upstream step: Complaint — factual allegations, legal claims, named parties
3. Continue with: Class certification order — exact class definition, court-specified notice requirements
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/class-action-notice

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-action-notice
```
