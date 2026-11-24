---
name: vercel-web-design-guidelines
description: "Review UI code against Web Interface Guidelines for accessibility, performance, UX, typography, and interaction rules."
category: 03-visual
status: referenced
inputs: task or request that matches the upstream skill
outputs: procedure and checkable result
fails_when: the skill is used outside its trigger or the source is not cited
verify: python scripts/check_skills.py skills/03-visual/vercel-web-design-guidelines
source: https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines
---

# Vercel Web Design Guidelines

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Review UI code against Web Interface Guidelines for accessibility, performance, UX, typography, and interaction rules.

## Steps

1. Read the bundled references/command.md file.
2. Read the files or pattern the user provides.
3. Check every rule in the bundled guidelines.
4. Output findings in terse file:line format.

## Hard rules

- Do not fetch rules from the network.
- Report findings only; do not silently rewrite code.

## Verify

```bash
python scripts/check_skills.py skills/03-visual/vercel-web-design-guidelines
```
