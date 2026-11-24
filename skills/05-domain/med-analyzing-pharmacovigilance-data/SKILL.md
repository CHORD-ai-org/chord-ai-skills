---
name: med-analyzing-pharmacovigilance-data
description: "Structures post-marketing safety surveillance with signal detection and PSUR reporting. Use when analyzing safety signals, preparing PSURs, or managing pharmacovigilance data."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-analyzing-pharmacovigilance-data
source: https://github.com/casemark/skills/tree/main/skills/med/analyzing-pharmacovigilance-data
---

# Med Analyzing Pharmacovigilance Data

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures post-marketing safety surveillance with signal detection and PSUR reporting. Use when analyzing safety signals, preparing PSURs, or managing pharmacovigilance data.

## Steps

1. Confirm the task matches this source: Structures post-marketing safety surveillance with signal detection and PSUR reporting. Use when analyzing safety signals, preparing PSURs, or managing pharmacovigilance data.
2. Start with the upstream step: What is the marketed product (trade name, INN, formulation, indication)?
3. Continue with: What is the data source (spontaneous reports, EHR data, claims databases, registries, published literature)?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/analyzing-pharmacovigilance-data

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-analyzing-pharmacovigilance-data
```
