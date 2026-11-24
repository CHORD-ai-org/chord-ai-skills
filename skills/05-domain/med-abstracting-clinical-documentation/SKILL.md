---
name: med-abstracting-clinical-documentation
description: "Extracts codeable diagnoses and procedures from clinical notes with specificity capture. Use when abstracting medical records, identifying codeable conditions, or capturing documentation specificity."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-abstracting-clinical-documentation
source: https://github.com/casemark/skills/tree/main/skills/med/abstracting-clinical-documentation
---

# Med Abstracting Clinical Documentation

## Brief info

Extracts codeable diagnoses and procedures from clinical notes with specificity capture. Use when abstracting medical records, identifying codeable conditions, or capturing documentation specificity. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Extracts codeable diagnoses and procedures from clinical notes with specificity capture. Use when abstracting medical records, identifying codeable conditions, or capturing documentation specificity.

## Steps

1. Confirm the task matches this source: Extracts codeable diagnoses and procedures from clinical notes with specificity capture. Use when abstracting medical records, identifying codeable conditions, or capturing documentation specificity.
2. Start with the upstream step: Map all diagnoses to ICD-10-CM descriptors. Do NOT assign codes; capture the
3. Continue with: Map procedures to CPT/HCPCS descriptors where identifiable.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/abstracting-clinical-documentation

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-abstracting-clinical-documentation
```
