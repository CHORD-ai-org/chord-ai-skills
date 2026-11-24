---
name: breach-of-purchase-agreement-complaint
description: "Drafts a filing-ready U.S. complaint for breach of a purchase agreement. Trigger when the user requests a breach-of-contract complaint, forum-selection analysis, or remedy package for a real-estate or asset purchase dispute."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/breach-of-purchase-agreement-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/breach-of-purchase-agreement-complaint
---

# Breach Of Purchase Agreement Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/breach-of-purchase-agreement-complaint
```
