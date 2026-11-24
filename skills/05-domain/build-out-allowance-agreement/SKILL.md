---
name: build-out-allowance-agreement
description: "Drafts a Build-Out Allowance Agreement as a commercial lease addendum governing landlord-provided TI allowance terms. Use when structuring TI allowance financing, negotiating landlord work letters, or documenting tenant improvement funds at lease execution."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/build-out-allowance-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/build-out-allowance-agreement
---

# Build Out Allowance Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Build-Out Allowance Agreement as a commercial lease addendum governing landlord-provided TI allowance terms. Use when structuring TI allowance financing, negotiating landlord work letters, or documenting tenant improvement funds at lease execution.

## Steps

1. Confirm the task matches this source: Drafts a Build-Out Allowance Agreement as a commercial lease addendum governing landlord-provided TI allowance terms. Use when structuring TI allowance financing, negotiating landlord work letters, or documenting tenant 
2. Start with the upstream step: Executed lease (or near-final draft) with premises address, suite/unit, commencement date, SF
3. Continue with: Allowance amount — lump sum or per-SF rate; disposition of unused funds (forfeit vs. rent credit)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/build-out-allowance-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/build-out-allowance-agreement
```
