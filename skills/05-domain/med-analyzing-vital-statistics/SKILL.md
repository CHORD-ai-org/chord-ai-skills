---
name: med-analyzing-vital-statistics
description: "Structures vital records analysis with birth, death, and demographic trend reporting. Use when analyzing vital statistics, interpreting mortality data, or reporting demographic trends."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-analyzing-vital-statistics
source: https://github.com/casemark/skills/tree/main/skills/med/analyzing-vital-statistics
---

# Med Analyzing Vital Statistics

## Brief info

Structures vital records analysis with birth, death, and demographic trend reporting. Use when analyzing vital statistics, interpreting mortality data, or reporting demographic trends. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures vital records analysis with birth, death, and demographic trend reporting. Use when analyzing vital statistics, interpreting mortality data, or reporting demographic trends.

## Steps

1. Confirm the task matches this source: Structures vital records analysis with birth, death, and demographic trend reporting. Use when analyzing vital statistics, interpreting mortality data, or reporting demographic trends.
2. Start with the upstream step: What vital records data are being analyzed — births, deaths (all-cause or cause-specific), fetal deaths, linked birth-infant deaths, or a combination?
3. Continue with: What is the time period and geographic scope — single year, multi-year trend, state, county, or sub-county?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/analyzing-vital-statistics

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-analyzing-vital-statistics
```
