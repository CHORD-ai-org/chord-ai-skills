---
name: med-conducting-cognitive-assessments
description: "Administers and interprets cognitive screening tools (MoCA, MMSE, SLUMS) with dementia evaluation. Use when screening for cognitive impairment, administering MoCA/MMSE, or evaluating dementia."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-cognitive-assessments
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-cognitive-assessments
---

# Med Conducting Cognitive Assessments

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Administers and interprets cognitive screening tools (MoCA, MMSE, SLUMS) with dementia evaluation. Use when screening for cognitive impairment, administering MoCA/MMSE, or evaluating dementia.

## Steps

1. Confirm the task matches this source: Administers and interprets cognitive screening tools (MoCA, MMSE, SLUMS) with dementia evaluation. Use when screening for cognitive impairment, administering MoCA/MMSE, or evaluating dementia.
2. Start with the upstream step: What is the referral question? (cognitive screening, dementia evaluation, capacity assessment, medication-induced cognitive concerns, post-delirium cognitive assessment) — defau...
3. Continue with: What is the patient's age and educational level? (critical for score interpretation) — default: obtain at intake
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-cognitive-assessments

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-cognitive-assessments
```
