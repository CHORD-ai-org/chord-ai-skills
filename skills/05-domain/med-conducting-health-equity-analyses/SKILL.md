---
name: med-conducting-health-equity-analyses
description: "Analyzes health disparities with demographic stratification and equity-focused intervention planning. Use when analyzing health disparities, assessing equity, or designing health equity interventions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-health-equity-analyses
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-health-equity-analyses
---

# Med Conducting Health Equity Analyses

## Brief info

Analyzes health disparities with demographic stratification and equity-focused intervention planning. Use when analyzing health disparities, assessing equity, or designing health equity interventions. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Analyzes health disparities with demographic stratification and equity-focused intervention planning. Use when analyzing health disparities, assessing equity, or designing health equity interventions.

## Steps

1. Confirm the task matches this source: Analyzes health disparities with demographic stratification and equity-focused intervention planning. Use when analyzing health disparities, assessing equity, or designing health equity interventions.
2. Start with the upstream step: What health outcome(s) are being assessed for equity — mortality, morbidity, access to care, quality of care, health behaviors, or social determinants?
3. Continue with: What dimensions of equity will be analyzed — race/ethnicity, income/poverty, education, geography (urban/rural, neighborhood), sex/gender, sexual orientation/gender identity, di...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-health-equity-analyses

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-health-equity-analyses
```
