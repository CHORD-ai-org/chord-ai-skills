---
name: med-conducting-dental-examinations
description: "Structures comprehensive dental examinations with periodontal charting, caries assessment, and oral cancer screening. Use when performing dental exams, documenting oral findings, or creating dental records."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-dental-examinations
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-dental-examinations
---

# Med Conducting Dental Examinations

## Brief info

Structures comprehensive dental examinations with periodontal charting, caries assessment, and oral cancer screening. Use when performing dental exams, documenting oral findings, or creating dental records. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures comprehensive dental examinations with periodontal charting, caries assessment, and oral cancer screening. Use when performing dental exams, documenting oral findings, or creating dental records.

## Steps

1. Confirm the task matches this source: Structures comprehensive dental examinations with periodontal charting, caries assessment, and oral cancer screening. Use when performing dental exams, documenting oral findings, or creating dental records.
2. Start with the upstream step: Current medical history form (updated within 12 months) with medication list
3. Continue with: Dental history including chief complaint, last dental visit date, and prior treatment summary
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-dental-examinations

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-dental-examinations
```
