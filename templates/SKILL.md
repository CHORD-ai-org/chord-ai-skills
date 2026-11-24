---
name: skill-id
description: what the skill does and when to use it
category: 00-category
status: draft
inputs: what the user gives
outputs: what the skill returns
fails_when: condition under which the result is wrong
verify: python scripts/check_skills.py skills/00-category/skill-id
source: URL or diary entry
---

# Skill title

## Trigger

Use when:

- condition one
- condition two

## Steps

1. First action.
2. Second action.
3. Stop condition.

## Hard rules

- Never do X.
- Always show Y.

## Verify

```bash
python scripts/check_skills.py skills/00-category/skill-id
```
