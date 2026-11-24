---
name: med-analyzing-flow-cytometry
description: "Interprets flow cytometry panels for hematologic malignancy classification and minimal residual disease. Use when analyzing flow cytometry, classifying lymphomas/leukemias, or documenting immunophenotyping."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-analyzing-flow-cytometry
source: https://github.com/casemark/skills/tree/main/skills/med/analyzing-flow-cytometry
---

# Med Analyzing Flow Cytometry

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Interprets flow cytometry panels for hematologic malignancy classification and minimal residual disease. Use when analyzing flow cytometry, classifying lymphomas/leukemias, or documenting immunophenotyping.

## Steps

1. Confirm the task matches this source: Interprets flow cytometry panels for hematologic malignancy classification and minimal residual disease. Use when analyzing flow cytometry, classifying lymphomas/leukemias, or documenting immunophenotyping.
2. Start with the upstream step: Specimen type — Peripheral blood, bone marrow aspirate, lymph node, body fluid, or tissue disaggregate? Default: peripheral blood.
3. Continue with: Clinical indication — New diagnosis, relapse assessment, MRD monitoring, staging, or T-cell subset enumeration? Default: new diagnosis workup.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/analyzing-flow-cytometry

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-analyzing-flow-cytometry
```
