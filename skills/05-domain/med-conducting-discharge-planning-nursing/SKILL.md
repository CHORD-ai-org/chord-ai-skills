---
name: med-conducting-discharge-planning-nursing
description: "Coordinates nursing discharge planning with medication teaching, follow-up scheduling, and resource coordination. Use when planning discharge, coordinating post-discharge care, or documenting discharge teaching."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-discharge-planning-nursing
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-discharge-planning-nursing
---

# Med Conducting Discharge Planning Nursing

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Coordinates nursing discharge planning with medication teaching, follow-up scheduling, and resource coordination. Use when planning discharge, coordinating post-discharge care, or documenting discharge teaching.

## Steps

1. Confirm the task matches this source: Coordinates nursing discharge planning with medication teaching, follow-up scheduling, and resource coordination. Use when planning discharge, coordinating post-discharge care, or documenting discharge teaching.
2. Start with the upstream step: [ ] Current medical diagnoses and problem list
3. Continue with: [ ] Current functional status: mobility, ADL independence, cognitive function
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-discharge-planning-nursing

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-discharge-planning-nursing
```
