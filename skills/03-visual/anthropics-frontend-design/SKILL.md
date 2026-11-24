---
name: anthropics-frontend-design
description: "Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one, with anti-generic design rules."
category: 03-visual
status: referenced
inputs: task or request that matches the upstream skill
outputs: procedure and checkable result
fails_when: the skill is used outside its trigger or the source is not cited
verify: python scripts/check_skills.py skills/03-visual/anthropics-frontend-design
source: https://github.com/anthropics/skills/tree/main/skills/frontend-design
---

# Anthropics Frontend Design

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one, with anti-generic design rules.

## Steps

1. Identify the subject, audience, and primary job of the page.
2. Write a compact token system for color, type, layout, and principles.
3. Review the plan against generic AI design defaults and revise.
4. Build the page, then critique and remove one unnecessary accessory.

## Hard rules

- Do not reuse default typography or SaaS-card patterns without justification.
- Respect reduced motion and keyboard focus.

## Verify

```bash
python scripts/check_skills.py skills/03-visual/anthropics-frontend-design
```
