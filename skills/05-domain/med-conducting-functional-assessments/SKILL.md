---
name: med-conducting-functional-assessments
description: "Structures functional capacity evaluation with standardized measures and activity limitation documentation. Use when assessing functional status, measuring mobility, or documenting activity levels."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-functional-assessments
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-functional-assessments
---

# Med Conducting Functional Assessments

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures functional capacity evaluation with standardized measures and activity limitation documentation. Use when assessing functional status, measuring mobility, or documenting activity levels.

## Steps

1. Confirm the task matches this source: Structures functional capacity evaluation with standardized measures and activity limitation documentation. Use when assessing functional status, measuring mobility, or documenting activity levels.
2. Start with the upstream step: What is the referral diagnosis and date of onset/surgery?
3. Continue with: What is the patient's prior level of function (PLOF) before the current episode?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-functional-assessments

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-functional-assessments
```
