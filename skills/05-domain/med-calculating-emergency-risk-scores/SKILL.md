---
name: med-calculating-emergency-risk-scores
description: "Computes validated risk scores (HEART, PERC, Wells, Ottawa, CURB-65) from clinical data. Use when calculating clinical decision scores, risk-stratifying ED patients, or applying clinical prediction rules."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-calculating-emergency-risk-scores
source: https://github.com/casemark/skills/tree/main/skills/med/calculating-emergency-risk-scores
---

# Med Calculating Emergency Risk Scores

## Brief info

Computes validated risk scores (HEART, PERC, Wells, Ottawa, CURB-65) from clinical data. Use when calculating clinical decision scores, risk-stratifying ED patients, or applying clinical prediction rules. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Computes validated risk scores (HEART, PERC, Wells, Ottawa, CURB-65) from clinical data. Use when calculating clinical decision scores, risk-stratifying ED patients, or applying clinical prediction rules.

## Steps

1. Confirm the task matches this source: Computes validated risk scores (HEART, PERC, Wells, Ottawa, CURB-65) from clinical data. Use when calculating clinical decision scores, risk-stratifying ED patients, or applying clinical prediction rules.
2. Start with the upstream step: What is the clinical question to be answered? (Default: identify primary complaint driving score selection)
3. Continue with: What are the patient's demographics (age, sex)? (Default: required for most scoring systems)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/calculating-emergency-risk-scores

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-calculating-emergency-risk-scores
```
