---
name: scientific-skills-index
description: "Index of 177 scientific and research skills covering biology, chemistry, medicine, physics, engineering, earth science, data analysis, and scientific communication."
category: 04-foundations
status: referenced
inputs: task or request that matches the upstream skill
outputs: procedure and checkable result
fails_when: the skill is used outside its trigger or the source is not cited
verify: python scripts/check_skills.py skills/04-foundations/scientific-skills-index
source: https://github.com/K-Dense-AI/scientific-agent-skills
---

# Scientific Skills Index

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Index of 177 scientific and research skills covering biology, chemistry, medicine, physics, engineering, earth science, data analysis, and scientific communication.

## Steps

1. Identify the scientific domain and the concrete task.
2. Open the upstream repository and select the matching skill.
3. Check the skill prerequisites and package dependencies.
4. Run one documented workflow and record the evidence.

## Hard rules

- Do not copy upstream scripts into this repository.
- Report inference and uncertainty explicitly.

## Verify

```bash
python scripts/check_skills.py skills/04-foundations/scientific-skills-index
```
