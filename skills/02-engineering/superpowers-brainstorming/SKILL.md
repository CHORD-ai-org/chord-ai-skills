---
name: superpowers-brainstorming
description: "Draw out what the user actually wants and why before building, then hand off to a written implementation plan."
category: 02-engineering
status: referenced
inputs: task or request that matches the upstream skill
outputs: procedure and checkable result
fails_when: the skill is used outside its trigger or the source is not cited
verify: python scripts/check_skills.py skills/02-engineering/superpowers-brainstorming
source: https://github.com/obra/superpowers/tree/main/skills/brainstorming
---

# Superpowers Brainstorming

## Brief info

Draw out what the user actually wants and why before building, then hand off to a written implementation plan. Input: task or request that matches the upstream skill. Output: procedure and checkable result. Caveat: the skill is used outside its trigger or the source is not cited.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Draw out what the user actually wants and why before building, then hand off to a written implementation plan.

## Steps

1. Read the request and state what is already known.
2. Lay out approaches in a separate message and ask the user to pick one.
3. Write a short or full design document.
4. Get approval before implementation.
5. Hand off to the writing-plans skill.

## Hard rules

- Do not start implementation before design approval.
- Do not ask questions already answered by the project or context.

## Verify

```bash
python scripts/check_skills.py skills/02-engineering/superpowers-brainstorming
```
