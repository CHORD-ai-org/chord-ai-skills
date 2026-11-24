---
name: 30b6-deposition
description: "Guides taking and defending Rule 30(b)(6) corporate representative depositions. Drafts topic lists with reasonable particularity, builds examination outlines for binding corporate admissions, analyzes noticed topics for objections, and prepares designees. Use when drafting 30(b)(6) notices, preparing corporate deposition topics, selecting or preparing designees, or defending corporate representative depositions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/30b6-deposition
source: https://github.com/casemark/skills/tree/main/skills/legal/30b6-deposition
---

# 30B6 Deposition

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/30b6-deposition
```
