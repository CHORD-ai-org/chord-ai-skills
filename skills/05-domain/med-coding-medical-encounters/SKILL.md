---
name: med-coding-medical-encounters
description: "Assigns ICD-10-CM diagnosis codes and CPT/HCPCS procedure codes with supporting documentation validation. Use when coding medical visits, selecting diagnosis codes, or assigning procedure codes."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-medical-encounters
source: https://github.com/casemark/skills/tree/main/skills/med/coding-medical-encounters
---

# Med Coding Medical Encounters

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns ICD-10-CM diagnosis codes and CPT/HCPCS procedure codes with supporting documentation validation. Use when coding medical visits, selecting diagnosis codes, or assigning procedure codes.

## Steps

1. Confirm the task matches this source: Assigns ICD-10-CM diagnosis codes and CPT/HCPCS procedure codes with supporting documentation validation. Use when coding medical visits, selecting diagnosis codes, or assigning procedure codes.
2. Start with the upstream step: Revenue — incorrect codes cause denials, underpayment, or overpayment
3. Continue with: Compliance — upcoding and unbundling trigger OIG audits and False Claims Act liability
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-medical-encounters

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-medical-encounters
```
