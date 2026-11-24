---
name: med-coding-radiology-services
description: "Assigns radiology CPT codes with professional/technical component and supervision level documentation. Use when coding imaging studies, applying 26/TC modifiers, or coding interventional procedures."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-radiology-services
source: https://github.com/casemark/skills/tree/main/skills/med/coding-radiology-services
---

# Med Coding Radiology Services

## Brief info

Assigns radiology CPT codes with professional/technical component and supervision level documentation. Use when coding imaging studies, applying 26/TC modifiers, or coding interventional procedures. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns radiology CPT codes with professional/technical component and supervision level documentation. Use when coding imaging studies, applying 26/TC modifiers, or coding interventional procedures.

## Steps

1. Confirm the task matches this source: Assigns radiology CPT codes with professional/technical component and supervision level documentation. Use when coding imaging studies, applying 26/TC modifiers, or coding interventional procedures.
2. Start with the upstream step: What imaging study or procedure was performed?
3. Continue with: What is the billing entity — physician practice, hospital outpatient department, or independent facility?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-radiology-services

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-radiology-services
```
