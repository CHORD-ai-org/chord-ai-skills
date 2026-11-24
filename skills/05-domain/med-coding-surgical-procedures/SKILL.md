---
name: med-coding-surgical-procedures
description: "Assigns CPT surgical codes with modifier selection and bundling/unbundling rules. Use when coding surgeries, applying surgical modifiers, or navigating NCCI edits."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-surgical-procedures
source: https://github.com/casemark/skills/tree/main/skills/med/coding-surgical-procedures
---

# Med Coding Surgical Procedures

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns CPT surgical codes with modifier selection and bundling/unbundling rules. Use when coding surgeries, applying surgical modifiers, or navigating NCCI edits.

## Steps

1. Confirm the task matches this source: Assigns CPT surgical codes with modifier selection and bundling/unbundling rules. Use when coding surgeries, applying surgical modifiers, or navigating NCCI edits.
2. Start with the upstream step: What procedure(s) were performed? Obtain the complete operative report.
3. Continue with: What is the setting? (hospital outpatient, ASC, physician office, inpatient)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-surgical-procedures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-surgical-procedures
```
