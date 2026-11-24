---
name: at-will-employment-offer-letter
description: "Drafts a U.S. at-will employment offer letter with unambiguous at-will language, FLSA-compliant compensation terms, benefits disclaimers, and conditions precedent. Use when extending formal job offers, issuing written employment offers, or drafting offer letters for new hires in U.S. jurisdictions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/at-will-employment-offer-letter
source: https://github.com/casemark/skills/tree/main/skills/legal/at-will-employment-offer-letter
---

# At Will Employment Offer Letter

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/at-will-employment-offer-letter
```
