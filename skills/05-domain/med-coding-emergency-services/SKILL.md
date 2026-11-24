---
name: med-coding-emergency-services
description: "Assigns ED-specific E/M codes with critical care time documentation and procedure coding. Use when coding ED visits, documenting critical care, or coding ED procedures."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-coding-emergency-services
source: https://github.com/casemark/skills/tree/main/skills/med/coding-emergency-services
---

# Med Coding Emergency Services

## Brief info

Assigns ED-specific E/M codes with critical care time documentation and procedure coding. Use when coding ED visits, documenting critical care, or coding ED procedures. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assigns ED-specific E/M codes with critical care time documentation and procedure coding. Use when coding ED visits, documenting critical care, or coding ED procedures.

## Steps

1. Confirm the task matches this source: Assigns ED-specific E/M codes with critical care time documentation and procedure coding. Use when coding ED visits, documenting critical care, or coding ED procedures.
2. Start with the upstream step: What type of ED encounter is this? (straightforward visit, critical care, observation, trauma activation)
3. Continue with: Is this facility (UB-04) or professional (CMS-1500) coding?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/coding-emergency-services

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-coding-emergency-services
```
