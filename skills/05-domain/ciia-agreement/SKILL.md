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

Use when the task matches this source: Drafts Confidentiality and Invention Assignment Agreements (CIIAs) for U.S. companies with jurisdiction-specific invention carve-outs, DTSA whistleblower notices, and restrictive covenants. Use when drafting employee confidentiality agreements, invention assignment agreements, proprietary information agreements, or IP assignment provisions for onboarding, corporate formation, or employment contexts.

## Steps

1. Confirm the task matches this source: Drafts Confidentiality and Invention Assignment Agreements (CIIAs) for U.S. companies with jurisdiction-specific invention carve-outs, DTSA whistleblower notices, and restrictive covenants. Use when drafting employee con
2. Start with the upstream step: Company info — legal entity name, state of incorporation, address
3. Continue with: Employee/contractor info — full name, address, role, start date
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/ciia-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ciia-agreement
```
