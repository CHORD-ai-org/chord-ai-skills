---
name: charitable-remainder-trust
description: "Drafts IRC 664–compliant Charitable Remainder Trust agreements (CRAT/CRUT), covering payout math, remainder qualification, trustee powers, and tax compliance. Use when drafting a CRT, CRAT, CRUT, unitrust, annuity trust, or charitable remainder planning document, or when ensuring IRC 664 compliance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/charitable-remainder-trust
source: https://github.com/casemark/skills/tree/main/skills/legal/charitable-remainder-trust
---

# Charitable Remainder Trust

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/charitable-remainder-trust
```
