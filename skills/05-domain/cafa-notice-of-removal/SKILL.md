---
name: cafa-notice-of-removal
description: "Drafts a Notice of Removal under the Class Action Fairness Act (CAFA), 28 U.S.C. § 1332(d), transferring a state court class action to federal court. Covers minimal diversity, aggregate amount in controversy exceeding $5 million, 100+ class members, CAFA exceptions, unanimity, timeliness, and required exhibits. Use when a defendant needs to remove a state-filed class action to federal court within 30 days of service."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/cafa-notice-of-removal
source: https://github.com/casemark/skills/tree/main/skills/legal/cafa-notice-of-removal
---

# Cafa Notice Of Removal

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Notice of Removal under the Class Action Fairness Act (CAFA), 28 U.S.C. § 1332(d), transferring a state court class action to federal court. Covers minimal diversity, aggregate amount in controversy exceeding $5 million, 100+ class members, CAFA exceptions, unanimity, timeliness, and required exhibits. Use when a defendant needs to remove a state-filed class action to federal court within 30 days of service.

## Steps

1. Confirm the task matches this source: Drafts a Notice of Removal under the Class Action Fairness Act (CAFA), 28 U.S.C. § 1332(d), transferring a state court class action to federal court. Covers minimal diversity, aggregate amount in controversy exceeding $5
2. Start with the upstream step: State court complaint with all exhibits and filing date
3. Continue with: Service documents — date and method of service on each defendant
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/cafa-notice-of-removal

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cafa-notice-of-removal
```
