---
name: med-conducting-daily-rounds
description: "Structures systematic rounding documentation with overnight events, assessment, and plan updates. Use when documenting daily rounds, updating inpatient plans, or preparing rounding notes."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-daily-rounds
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-daily-rounds
---

# Med Conducting Daily Rounds

## Brief info

Structures systematic rounding documentation with overnight events, assessment, and plan updates. Use when documenting daily rounds, updating inpatient plans, or preparing rounding notes. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures systematic rounding documentation with overnight events, assessment, and plan updates. Use when documenting daily rounds, updating inpatient plans, or preparing rounding notes.

## Steps

1. Confirm the task matches this source: Structures systematic rounding documentation with overnight events, assessment, and plan updates. Use when documenting daily rounds, updating inpatient plans, or preparing rounding notes.
2. Start with the upstream step: What overnight events occurred — nursing calls, vitals changes, medication requests, falls, code events? *(Default: Review nursing flowsheet and overnight notes)*
3. Continue with: What is the patient's current clinical trajectory — improving, stable, or declining? *(Default: Assess against prior 24h baseline)*
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-daily-rounds

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-daily-rounds
```
