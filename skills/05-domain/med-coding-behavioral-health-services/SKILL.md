---
name: med-coding-behavioral-health-services
description: "Assigns behavioral health procedure codes with time-based requirements and modifier application. Use when coding therapy sessions, applying psychiatric codes, or documenting behavioral health services."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-behavioral-health-services
source: https://github.com/casemark/skills/tree/main/skills/med/coding-behavioral-health-services
---

# Med Coding Behavioral Health Services

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns behavioral health procedure codes with time-based requirements and modifier application. Use when coding therapy sessions, applying psychiatric codes, or documenting behavioral health services.

## Steps

1. Confirm the task matches this source: Assigns behavioral health procedure codes with time-based requirements and modifier application. Use when coding therapy sessions, applying psychiatric codes, or documenting behavioral health services.
2. Start with the upstream step: What type of behavioral health service was provided? (evaluation, psychotherapy, testing, crisis intervention, medication management)
3. Continue with: What is the provider's credential? (MD/DO psychiatrist, PhD psychologist, LCSW, LPC, LMFT, NP)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-behavioral-health-services

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-behavioral-health-services
```
