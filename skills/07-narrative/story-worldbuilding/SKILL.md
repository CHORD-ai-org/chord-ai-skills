---
name: story-worldbuilding
description: "Create and manage locations, systems, factions, artifacts, routes, and glossary terms for a story project."
category: 07-narrative
status: referenced
inputs: task or request that matches the upstream skill
outputs: procedure and checkable result
fails_when: the skill is used outside its trigger or the source is not cited
verify: python scripts/check_skills.py skills/07-narrative/story-worldbuilding
source: https://github.com/danjdewhurst/story-skills/tree/main/skills/worldbuilding
---

# Story Worldbuilding

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Create and manage locations, systems, factions, artifacts, routes, and glossary terms for a story project.

## Steps

1. Confirm the story project exists by checking story.md.
2. Read worldbuilding/_index.md and existing cross-references.
3. Build the location or system through conversation.
4. Write the entity file from the upstream template.
5. Run story reindex, wordcount, and check when the CLI is available.

## Hard rules

- Do not hand-edit index tables that belong to story reindex.
- Do not invent facts that the story bible already answers.

## Verify

```bash
python scripts/check_skills.py skills/07-narrative/story-worldbuilding
```
