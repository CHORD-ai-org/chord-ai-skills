---
name: attorney-representation-agreement
description: "Drafts U.S. litigation attorney representation agreements for client onboarding, covering scope, fees, retainers, confidentiality, conflicts, duties, withdrawal, and dispute resolution. Use when converting consultations into enforceable engagement terms for civil litigation matters including personal injury. Trigger: engagement letter, litigation retainer, representation agreement, fee contract, conflict disclosure, attorney withdrawal, client acknowledgment."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/attorney-representation-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/attorney-representation-agreement
---

# Attorney Representation Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. litigation attorney representation agreements for client onboarding, covering scope, fees, retainers, confidentiality, conflicts, duties, withdrawal, and dispute resolution. Use when converting consultations into enforceable engagement terms for civil litigation matters including personal injury. Trigger: engagement letter, litigation retainer, representation agreement, fee contract, conflict disclosure, attorney withdrawal, client acknowledgment.

## Steps

1. Confirm the task matches this source: Drafts U.S. litigation attorney representation agreements for client onboarding, covering scope, fees, retainers, confidentiality, conflicts, duties, withdrawal, and dispute resolution. Use when converting consultations 
2. Start with the upstream step: Gather: jurisdiction, attorney/firm identity and bar info, client identity (plus entity authority if applicable).
3. Continue with: Define scope: matter type, claims/defenses, courts, and exclusions.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/attorney-representation-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/attorney-representation-agreement
```
