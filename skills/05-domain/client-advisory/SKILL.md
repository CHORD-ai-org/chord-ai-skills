---
name: client-advisory
description: "Drafts client advisory memoranda translating legal developments into actionable guidance with impact analysis, Bluebook citations, and compliance recommendations. Use when preparing client alerts, regulatory updates, legal bulletins, or proactive advisory summaries."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/client-advisory
source: https://github.com/casemark/skills/tree/main/skills/legal/client-advisory
---

# Client Advisory

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/client-advisory
```
