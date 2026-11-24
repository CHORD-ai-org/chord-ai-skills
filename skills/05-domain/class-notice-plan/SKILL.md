---
name: class-notice-plan
description: "Drafts a Rule 23 class notice communication plan for U.S. federal class actions, covering notice content, delivery methods, timelines, budgets, and reporting to satisfy the \"best notice practicable\" standard. Use after class certification or when seeking settlement approval. Trigger when user mentions class notice, notice plan, communication plan, Rule 23(c)(2)(B), claims administrator, or CAFA notice. The CAFA 28 U.S.C. 1715 notice package to officials and its clock go to class-action-settlement."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-notice-plan
source: https://github.com/casemark/skills/tree/main/skills/legal/class-notice-plan
---

# Class Notice Plan

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-notice-plan
```
