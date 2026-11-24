---
name: certificate-of-withdrawal-foreign-corp
description: "Drafts a Certificate of Withdrawal for a foreign corporation surrendering its authority to transact business in a US state. Use when a foreign corporation is withdrawing its certificate of authority, ceasing in-state operations, or completing dissolution in a non-home jurisdiction."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/certificate-of-withdrawal-foreign-corp
source: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-withdrawal-foreign-corp
---

# Certificate Of Withdrawal Foreign Corp

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-withdrawal-foreign-corp
```
