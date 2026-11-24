---
name: bankruptcy-proof-of-claim
description: "Drafts filing-ready proofs of claim for U.S. bankruptcy proceedings using Official Form B 410 under FRBP 3001. Handles secured, unsecured priority, and general unsecured claims with proper valuation, documentation, and bar date compliance. Use when a creditor needs to file or amend a proof of claim in a bankruptcy case."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bankruptcy-proof-of-claim
source: https://github.com/casemark/skills/tree/main/skills/legal/bankruptcy-proof-of-claim
---

# Bankruptcy Proof Of Claim

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bankruptcy-proof-of-claim
```
