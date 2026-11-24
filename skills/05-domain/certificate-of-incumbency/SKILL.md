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

Use when the task matches this source: Drafts a Certificate of Incumbency certifying current officers, directors, and signing authority for a U.S. corporation. Covers exact legal name matching, incumbency tables with specimen signatures, board resolution certification, authority limitations, reliance language, and execution formalities. Use when banks, lenders, investors, or counterparties require verification of corporate authority for closings, financings, or transactions.

## Steps

1. Confirm the task matches this source: Drafts a Certificate of Incumbency certifying current officers, directors, and signing authority for a U.S. corporation. Covers exact legal name matching, incumbency tables with specimen signatures, board resolution cert
2. Start with the upstream step: Formation documents — articles/certificate confirming exact legal entity name with designator (Inc., Corp., Ltd., LLC)
3. Continue with: Bylaws or operating agreement — current, with amendments noted (becomes Exhibit A)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-incumbency

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-incumbency
```
