---
name: legal-aml-compliance-program
description: ">-"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-aml-compliance-program
source: https://github.com/casemark/skills/tree/main/skills/legal/aml-compliance-program
---

# Legal Aml Compliance Program

## Brief info

>- Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >-

## Steps

1. Confirm the task matches this source: >-
2. Start with the upstream step: Draft only. Nothing is filed, adopted or sent. Every output is a draft for counsel and BSA/AML officer review and is never called final or approved.
3. Continue with: Source-review gate. Never call a document missing until the inventory has been checked and the file opened, with OCR or extraction tried. Classify every open item as one of four...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/aml-compliance-program

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-aml-compliance-program
```
