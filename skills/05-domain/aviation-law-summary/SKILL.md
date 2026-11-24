---
name: aviation-law-summary
description: "Produces structured aviation law summaries with Bluebook citations covering U.S. and international regulatory frameworks, treaties, and case law. Use when drafting an aviation law summary, FAA/DOT/TSA compliance overview, Montreal/Warsaw Convention liability analysis, air service agreement review, accident liability synopsis, or aviation regulatory research memo."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/aviation-law-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/aviation-law-summary
---

# Aviation Law Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/aviation-law-summary
```
