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

Use when the task matches this source: Drafts a BSA/AML Risk Assessment for U.S. financial institutions per FinCEN, FFIEC, and OCC standards. Evaluates inherent risks (customer, product, geographic, transaction, third-party), control adequacy, and residual risk. Use when preparing annual BSA compliance assessments, post-acquisition integration reviews, or when business changes trigger reassessment under 31 U.S.C. § 5318(h).

## Steps

1. Confirm the task matches this source: Drafts a BSA/AML Risk Assessment for U.S. financial institutions per FinCEN, FFIEC, and OCC standards. Evaluates inherent risks (customer, product, geographic, transaction, third-party), control adequacy, and residual ri
2. Start with the upstream step: Institution profile — entity type, charter/regulator, total assets, branch footprint, international relationships
3. Continue with: Products & services — inventory with volumes for high-risk products (wires, monetary instruments, prepaid, trade finance, crypto on/off ramps)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bsa-risk-assessment

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bsa-risk-assessment
```
