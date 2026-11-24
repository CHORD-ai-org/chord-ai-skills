---
name: certificate-of-service
description: "Drafts certificates of service (proofs of service) for court filings. Use when a filing must be accompanied by proof that copies were served on all parties or counsel. Covers FRCP Rule 5, state equivalents, ECF/e-service, U.S. mail, hand delivery, and overnight courier methods."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/certificate-of-service
source: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-service
---

# Certificate Of Service

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-service
```
