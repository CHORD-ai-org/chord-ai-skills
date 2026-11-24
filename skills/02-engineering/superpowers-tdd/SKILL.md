---
name: superpowers-tdd
description: "Use when implementing any feature or bugfix, before writing implementation code"
category: 02-engineering
status: referenced
inputs: task or request that matches the upstream skill
outputs: procedure and checkable result
fails_when: the skill is used outside its trigger or the source is not cited
verify: python scripts/check_skills.py skills/02-engineering/superpowers-tdd
source: https://github.com/obra/superpowers/tree/main/skills/test-driven-development
---

# Superpowers Tdd

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Use when implementing any feature or bugfix, before writing implementation code

## Steps

1. Write a failing test for the next behavior.
2. Run the test and confirm it fails for the expected reason.
3. Write the minimal code to make it pass.
4. Run the test again and confirm it passes.
5. Refactor only after the test is green.

## Hard rules

- Delete code written before its test.
- Do not claim completion without a passing test run.

## Verify

```bash
python scripts/check_skills.py skills/02-engineering/superpowers-tdd
```
