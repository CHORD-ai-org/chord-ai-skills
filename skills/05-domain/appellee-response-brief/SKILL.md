---
name: appellee-response-brief
description: "Drafts appellee response briefs for federal and state appellate courts, exploiting standards of review and record evidence to defend trial court decisions. Trigger when the user needs to respond to an appellant's opening brief or defend a favorable lower court ruling on appeal."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appellee-response-brief
source: https://github.com/casemark/skills/tree/main/skills/legal/appellee-response-brief
---

# Appellee Response Brief

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appellee-response-brief
```
