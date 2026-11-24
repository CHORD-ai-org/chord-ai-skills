---
name: legal-amicus-coalition-management
description: "Manages multi-organization appellate amicus briefs with single-pen drafting, coalition sign-offs, conflict triage, and compliant disclosures. Use when coordinating a coalition amicus brief, managing amicus sign-on, handling FRAP 29 or Supreme Court Rule 37.6 disclosures, or preparing cover and interest sections for multiple amici."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-amicus-coalition-management
source: https://github.com/casemark/skills/tree/main/skills/legal/amicus-coalition-management
---

# Legal Amicus Coalition Management

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Manages multi-organization appellate amicus briefs with single-pen drafting, coalition sign-offs, conflict triage, and compliant disclosures. Use when coordinating a coalition amicus brief, managing amicus sign-on, handling FRAP 29 or Supreme Court Rule 37.6 disclosures, or preparing cover and interest sections for multiple amici.

## Steps

1. Confirm the task matches this source: Manages multi-organization appellate amicus briefs with single-pen drafting, coalition sign-offs, conflict triage, and compliant disclosures. Use when coordinating a coalition amicus brief, managing amicus sign-on, handl
2. Start with the upstream step: Court, case number, caption, and all amicus deadlines
3. Continue with: Party briefs and key orders (issues and timing)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/amicus-coalition-management

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-amicus-coalition-management
```
