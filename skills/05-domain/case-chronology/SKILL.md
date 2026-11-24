---
name: case-chronology
description: "Produces U.S. litigation case chronologies with dated timelines, executive summaries, source attribution, gap analysis, and investigation recommendations. Use when asked for a chronology, timeline, case summary, or executive summary of a legal matter, or during case intake, deposition prep, or trial prep."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/case-chronology
source: https://github.com/casemark/skills/tree/main/skills/legal/case-chronology
---

# Case Chronology

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/case-chronology
```
