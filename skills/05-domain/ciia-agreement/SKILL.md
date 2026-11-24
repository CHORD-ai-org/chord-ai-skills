---
name: ciia-agreement
description: "Drafts Confidentiality and Invention Assignment Agreements (CIIAs) for U.S. companies with jurisdiction-specific invention carve-outs, DTSA whistleblower notices, and restrictive covenants. Use when drafting employee confidentiality agreements, invention assignment agreements, proprietary information agreements, or IP assignment provisions for onboarding, corporate formation, or employment contexts."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ciia-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/ciia-agreement
---

# Ciia Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ciia-agreement
```
