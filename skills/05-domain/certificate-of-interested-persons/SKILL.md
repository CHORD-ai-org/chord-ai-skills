---
name: certificate-of-interested-persons
description: "Drafts a FRAP 26.1-compliant Certificate of Interested Persons identifying all parties, entities, and affiliates with financial or legal interests in a federal appeal. Adapts to circuit-specific local rules. Use when filing appeals, corporate disclosure statements, or conflict-of-interest certificates in U.S. Courts of Appeals."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/certificate-of-interested-persons
source: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-interested-persons
---

# Certificate Of Interested Persons

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-interested-persons
```
