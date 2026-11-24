---
name: case-briefs
description: "Generates structured case briefs from judicial opinions. Use when the user provides a court opinion and needs a case brief, case summary, or distillation of a judicial decision for legal research."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/case-briefs
source: https://github.com/casemark/skills/tree/main/skills/legal/case-briefs
---

# Case Briefs

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Generates structured case briefs from judicial opinions. Use when the user provides a court opinion and needs a case brief, case summary, or distillation of a judicial decision for legal research.

## Steps

1. Confirm the task matches this source: Generates structured case briefs from judicial opinions. Use when the user provides a court opinion and needs a case brief, case summary, or distillation of a judicial decision for legal research.
2. Start with the upstream step: Caption & Procedural Posture — full case name, court, date, citation; how the case reached this court; lower court decision and basis for review
3. Continue with: Statement of Facts — material facts chronologically; distinguish background, operative, and procedural facts; include only facts the court deemed relevant
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/case-briefs

## Verify

```bash
python scripts/check_skills.py skills/05-domain/case-briefs
```
