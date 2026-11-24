---
name: asset-purchase-loi
description: "Drafts a U.S. asset purchase letter of intent (LOI) separating binding from non-binding terms and capturing deal points, diligence, exclusivity, and closing path. Trigger on \"letter of intent\", \"LOI\", \"asset purchase\", \"M&A LOI\", \"no-shop\", \"exclusivity\", \"purchase price\", \"due diligence\"."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/asset-purchase-loi
source: https://github.com/casemark/skills/tree/main/skills/legal/asset-purchase-loi
---

# Asset Purchase Loi

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/asset-purchase-loi
```
