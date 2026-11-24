---
name: med-coding-anesthesia-services
description: "Assigns anesthesia codes with time documentation, base/time unit calculation, and physical status modifiers. Use when coding anesthesia, calculating anesthesia units, or applying physical status modifiers."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-anesthesia-services
source: https://github.com/casemark/skills/tree/main/skills/med/coding-anesthesia-services
---

# Med Coding Anesthesia Services

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns anesthesia codes with time documentation, base/time unit calculation, and physical status modifiers. Use when coding anesthesia, calculating anesthesia units, or applying physical status modifiers.

## Steps

1. Confirm the task matches this source: Assigns anesthesia codes with time documentation, base/time unit calculation, and physical status modifiers. Use when coding anesthesia, calculating anesthesia units, or applying physical status modifiers.
2. Start with the upstream step: What surgical procedure was performed under anesthesia?
3. Continue with: What type of anesthesia was administered? (general, regional, MAC, combined)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-anesthesia-services

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-anesthesia-services
```
