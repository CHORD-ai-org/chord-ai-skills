---
name: brownfields-agreement
description: "Drafts Brownfields Agreements for contaminated-property transactions under CERCLA, EPA brownfields programs, and state voluntary cleanup programs. Structures BFPP liability protections, All Appropriate Inquiries documentation, remediation obligations, institutional controls, cost allocation, and long-term stewardship covenants. Use when drafting brownfields purchase agreements, prospective purchaser agreements, voluntary cleanup MOAs, or environmental covenant frameworks."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/brownfields-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/brownfields-agreement
---

# Brownfields Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/brownfields-agreement
```
