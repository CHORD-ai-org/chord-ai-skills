---
name: med-analyzing-epidemiological-data
description: "Structures epidemiologic analysis with incidence, prevalence, rate calculations, and statistical inference. Use when calculating disease rates, analyzing epi data, or interpreting population statistics."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-analyzing-epidemiological-data
source: https://github.com/casemark/skills/tree/main/skills/med/analyzing-epidemiological-data
---

# Med Analyzing Epidemiological Data

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures epidemiologic analysis with incidence, prevalence, rate calculations, and statistical inference. Use when calculating disease rates, analyzing epi data, or interpreting population statistics.

## Steps

1. Confirm the task matches this source: Structures epidemiologic analysis with incidence, prevalence, rate calculations, and statistical inference. Use when calculating disease rates, analyzing epi data, or interpreting population statistics.
2. Start with the upstream step: What is the analytic question — disease burden estimation, trend comparison, risk factor association, or program effectiveness?
3. Continue with: What data sources are available — NNDSS, BRFSS, YRBSS, NHANES, vital records, hospital discharge data, claims data, or custom surveillance?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/analyzing-epidemiological-data

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-analyzing-epidemiological-data
```
