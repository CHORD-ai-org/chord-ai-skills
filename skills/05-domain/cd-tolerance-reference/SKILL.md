---
name: cd-tolerance-reference
description: "Guides the agent through TRID tolerance compliance under 12 CFR § 1026.19(e)(3), comparing Closing Disclosure fees to Loan Estimate fees across zero, 10% cumulative, and unlimited tolerance categories. Use when reviewing a CD for tolerance variances, determining whether a revised LE is permitted, calculating cure amounts, or resolving post-closing tolerance violations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/cd-tolerance-reference
source: https://github.com/casemark/skills/tree/main/skills/legal/cd-tolerance-reference
---

# Cd Tolerance Reference

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cd-tolerance-reference
```
