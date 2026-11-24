---
name: med-conducting-annual-wellness-visits
description: "Structures Medicare Annual Wellness Visit documentation with HRA, prevention plan, and advance care planning. Use when performing wellness visits, documenting AWVs, or creating personalized prevention plans."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-annual-wellness-visits
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-annual-wellness-visits
---

# Med Conducting Annual Wellness Visits

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures Medicare Annual Wellness Visit documentation with HRA, prevention plan, and advance care planning. Use when performing wellness visits, documenting AWVs, or creating personalized prevention plans.

## Steps

1. Confirm the task matches this source: Structures Medicare Annual Wellness Visit documentation with HRA, prevention plan, and advance care planning. Use when performing wellness visits, documenting AWVs, or creating personalized prevention plans.
2. Start with the upstream step: Is this an Initial AWV (G0438, no prior AWV) or Subsequent AWV (G0439)? Default: G0439
3. Continue with: What is the patient's age, sex assigned at birth, and current gender identity? Default: [REQUIRED]
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-annual-wellness-visits

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-annual-wellness-visits
```
