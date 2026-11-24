---
name: certificate-of-incumbency
description: "Drafts a Certificate of Incumbency certifying current officers, directors, and signing authority for a U.S. corporation. Covers exact legal name matching, incumbency tables with specimen signatures, board resolution certification, authority limitations, reliance language, and execution formalities. Use when banks, lenders, investors, or counterparties require verification of corporate authority for closings, financings, or transactions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/certificate-of-incumbency
source: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-incumbency
---

# Certificate Of Incumbency

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-incumbency
```
