---
name: 30b6-corporate-rep
description: "Manages Rule 30(b)(6) corporate representative deposition workflows — drafting notice topics with reasonable particularity, building examination outlines, defending designees, handling objections, and preserving binding admissions for summary judgment or trial. Use when drafting or responding to 30(b)(6) notices, selecting and preparing designees, building topic-by-topic outlines, or triaging scope and privilege disputes. Trigger keywords: 30(b)(6), corporate representative deposition, topic list, designee, notice analysis, deposition objections, corporate admissions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/30b6-corporate-rep
source: https://github.com/casemark/skills/tree/main/skills/legal/30b6-corporate-rep
---

# 30B6 Corporate Rep

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/30b6-corporate-rep
```
