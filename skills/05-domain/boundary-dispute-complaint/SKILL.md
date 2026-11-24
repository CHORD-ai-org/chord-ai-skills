---
name: boundary-dispute-complaint
description: "Drafts a U.S. state-court complaint to establish the true boundary line between adjoining properties, with optional trespass/encroachment claims. Trigger when a user needs to initiate litigation over conflicting property descriptions, ambiguous deed language, or unauthorized encroachments by an adjoining landowner."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/boundary-dispute-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/boundary-dispute-complaint
---

# Boundary Dispute Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/boundary-dispute-complaint
```
