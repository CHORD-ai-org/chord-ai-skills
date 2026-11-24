---
name: med-analyzing-clinical-data-warehouses
description: "Structures clinical data warehouse queries for quality measurement, research, and operational analytics. Use when querying clinical data, building analytics reports, or extracting research datasets."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-analyzing-clinical-data-warehouses
source: https://github.com/casemark/skills/tree/main/skills/med/analyzing-clinical-data-warehouses
---

# Med Analyzing Clinical Data Warehouses

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures clinical data warehouse queries for quality measurement, research, and operational analytics. Use when querying clinical data, building analytics reports, or extracting research datasets.

## Steps

1. Confirm the task matches this source: Structures clinical data warehouse queries for quality measurement, research, and operational analytics. Use when querying clinical data, building analytics reports, or extracting research datasets.
2. Start with the upstream step: What is the business or research question in one declarative sentence?
3. Continue with: Which CDW platform and version is the target (Epic Caboodle/Clarity, Cerner HealtheIntent, OMOP v5.4, i2b2, PCORnet CDM v6, custom)?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/analyzing-clinical-data-warehouses

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-analyzing-clinical-data-warehouses
```
