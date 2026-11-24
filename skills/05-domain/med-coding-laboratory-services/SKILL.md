---
name: med-coding-laboratory-services
description: "Assigns laboratory CPT codes with panel construction and specimen-specific modifiers. Use when coding lab tests, building lab panels, or applying laboratory modifiers."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-laboratory-services
source: https://github.com/casemark/skills/tree/main/skills/med/coding-laboratory-services
---

# Med Coding Laboratory Services

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns laboratory CPT codes with panel construction and specimen-specific modifiers. Use when coding lab tests, building lab panels, or applying laboratory modifiers.

## Steps

1. Confirm the task matches this source: Assigns laboratory CPT codes with panel construction and specimen-specific modifiers. Use when coding lab tests, building lab panels, or applying laboratory modifiers.
2. Start with the upstream step: What laboratory tests were ordered and performed?
3. Continue with: Where was the test performed? (in-house laboratory, reference laboratory, hospital lab)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-laboratory-services

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-laboratory-services
```
