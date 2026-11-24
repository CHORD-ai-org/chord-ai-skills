---
name: cda-certified-claim
description: "Drafts U.S. Contract Disputes Act (CDA) certified claims for federal government contracts, covering FAR Part 33 compliance, entitlement/quantum sections, certification language, and final-decision demand. Use when preparing a CDA claim, certified claim, or submission to a contracting officer under the Contract Disputes Act."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/cda-certified-claim
source: https://github.com/casemark/skills/tree/main/skills/legal/cda-certified-claim
---

# Cda Certified Claim

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. Contract Disputes Act (CDA) certified claims for federal government contracts, covering FAR Part 33 compliance, entitlement/quantum sections, certification language, and final-decision demand. Use when preparing a CDA claim, certified claim, or submission to a contracting officer under the Contract Disputes Act.

## Steps

1. Confirm the task matches this source: Drafts U.S. Contract Disputes Act (CDA) certified claims for federal government contracts, covering FAR Part 33 compliance, entitlement/quantum sections, certification language, and final-decision demand. Use when prepar
2. Start with the upstream step: Executed contract and all modifications (including disputes/changes clauses)
3. Continue with: Contracting officer name, title, office address, submission method
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/cda-certified-claim

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cda-certified-claim
```
