---
name: claim-construction-order
description: "Drafts a U.S. federal court Claim Construction Order (Markman order) applying the Phillips v. AWH Corp. intrinsic/extrinsic evidence hierarchy to construe disputed patent claim terms. Use when drafting Markman orders, claim construction memoranda, or disputed-term rulings in U.S. patent litigation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/claim-construction-order
source: https://github.com/casemark/skills/tree/main/skills/legal/claim-construction-order
---

# Claim Construction Order

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/claim-construction-order
```
