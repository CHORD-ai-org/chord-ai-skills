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

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cafa-notice-of-removal
```
