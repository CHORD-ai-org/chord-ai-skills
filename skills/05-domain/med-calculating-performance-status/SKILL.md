---
name: med-calculating-performance-status
description: "Documents ECOG and Karnofsky performance status with treatment eligibility implications. Use when assessing performance status, documenting ECOG scores, or evaluating treatment candidacy."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-calculating-performance-status
source: https://github.com/casemark/skills/tree/main/skills/med/calculating-performance-status
---

# Med Calculating Performance Status

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Documents ECOG and Karnofsky performance status with treatment eligibility implications. Use when assessing performance status, documenting ECOG scores, or evaluating treatment candidacy.

## Steps

1. Confirm the task matches this source: Documents ECOG and Karnofsky performance status with treatment eligibility implications. Use when assessing performance status, documenting ECOG scores, or evaluating treatment candidacy.
2. Start with the upstream step: What is the purpose of this assessment (treatment decision, clinical trial screening, hospice eligibility, quality reporting)? (Default: treatment decision)
3. Continue with: When was the last documented performance status, and who assessed it? (Default: assess now)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/calculating-performance-status

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-calculating-performance-status
```
