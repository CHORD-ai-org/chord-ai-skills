---
name: bsa-risk-assessment
description: "Drafts a BSA/AML Risk Assessment for U.S. financial institutions per FinCEN, FFIEC, and OCC standards. Evaluates inherent risks (customer, product, geographic, transaction, third-party), control adequacy, and residual risk. Use when preparing annual BSA compliance assessments, post-acquisition integration reviews, or when business changes trigger reassessment under 31 U.S.C. § 5318(h)."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bsa-risk-assessment
source: https://github.com/casemark/skills/tree/main/skills/legal/bsa-risk-assessment
---

# Bsa Risk Assessment

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bsa-risk-assessment
```
