---
name: med-coding-telehealth-services
description: "Assigns telehealth-specific codes with place of service, modifier, and technology requirements. Use when coding virtual visits, applying telehealth modifiers, or documenting telemedicine services."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-telehealth-services
source: https://github.com/casemark/skills/tree/main/skills/med/coding-telehealth-services
---

# Med Coding Telehealth Services

## Brief info

Assigns telehealth-specific codes with place of service, modifier, and technology requirements. Use when coding virtual visits, applying telehealth modifiers, or documenting telemedicine services. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns telehealth-specific codes with place of service, modifier, and technology requirements. Use when coding virtual visits, applying telehealth modifiers, or documenting telemedicine services.

## Steps

1. Confirm the task matches this source: Assigns telehealth-specific codes with place of service, modifier, and technology requirements. Use when coding virtual visits, applying telehealth modifiers, or documenting telemedicine services.
2. Start with the upstream step: What type of telehealth service was provided? (synchronous audio-video, audio-only, store-and-forward, remote monitoring)
3. Continue with: What technology platform was used? Is it HIPAA-compliant with real-time audio-video capability?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-telehealth-services

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-telehealth-services
```
