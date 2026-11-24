---
name: change-in-control-agreement
description: "Drafts U.S. executive Change in Control Agreements with double-trigger severance, equity acceleration, and 280G/409A compliance. Use when drafting or negotiating CIC agreements, change in control protections, executive severance in M&A, or golden parachute provisions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/change-in-control-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/change-in-control-agreement
---

# Change In Control Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. executive Change in Control Agreements with double-trigger severance, equity acceleration, and 280G/409A compliance. Use when drafting or negotiating CIC agreements, change in control protections, executive severance in M&A, or golden parachute provisions.

## Steps

1. Confirm the task matches this source: Drafts U.S. executive Change in Control Agreements with double-trigger severance, equity acceleration, and 280G/409A compliance. Use when drafting or negotiating CIC agreements, change in control protections, executive s
2. Start with the upstream step: Executive — name, title, base salary, target bonus, outstanding equity (type, vesting, performance metrics)
3. Continue with: Company — legal name, state of incorporation, entity type, public/private status
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/change-in-control-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/change-in-control-agreement
```
