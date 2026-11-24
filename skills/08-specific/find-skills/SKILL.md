---
name: find-skills
description: "Find reusable agent skills by keyword before writing a new skill from scratch."
category: 08-specific
status: referenced
inputs: task or request that matches the upstream skill
outputs: procedure and checkable result
fails_when: the skill is used outside its trigger or the source is not cited
verify: python scripts/check_skills.py skills/08-specific/find-skills
source: https://github.com/vercel-labs/skills
---

# Find Skills

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Find reusable agent skills by keyword before writing a new skill from scratch.

## Steps

1. Run npx skills find with the task keyword.
2. Open the top candidate repositories and read their README and license.
3. Run npx skills add <repo> --list to confirm skill names.
4. Use npx skills use <repo>@<skill> before installing.
5. Write a pointer skill only after verification.

## Hard rules

- Do not bulk-install skills.
- Disable CLI telemetry in automated runs.

## Verify

```bash
python scripts/check_skills.py skills/08-specific/find-skills
```
