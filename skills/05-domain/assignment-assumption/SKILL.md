---
name: assignment-assumption
description: "Drafts Assignment and Assumption Agreements transferring contractual rights and obligations from assignor to assignee in asset purchase transactions. Covers assignment mechanics, liability assumption with temporal cutoff, third-party consent handling, reps and warranties, indemnification, and Exhibit A contract schedule. Trigger keywords: \"assignment and assumption\", \"contract transfer\", \"assign contracts\", \"assume obligations\", \"asset purchase closing document\", \"assignor assignee agreement\"."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/assignment-assumption
source: https://github.com/casemark/skills/tree/main/skills/legal/assignment-assumption
---

# Assignment Assumption

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/assignment-assumption
```
