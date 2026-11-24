---
name: body-camera-incident-summary
description: "Transforms police body camera transcripts into structured 10-section legal summaries with timestamp-cited verbatim statements, constitutional issue spotting, evidence inventory, and probable cause articulation. Maintains strict neutrality for all parties. Use when analyzing BWC footage for discovery, pre-trial prep, or trial. Trigger: body camera, BWC, body worn camera, officer footage, use of force review, incident summary."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/body-camera-incident-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/body-camera-incident-summary
---

# Body Camera Incident Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/body-camera-incident-summary
```
