---
name: process-mapper
description: "Use when documenting an end-to-end business process (procurement, onboarding, handoffs) and finding where work waits. Maps it with process_documenter.py, measures stages with cycle_time_analyzer.py and finds bottlenecks with bottleneck_detector.py."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/process-mapper
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/process-mapper
---

# Process Mapper

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Business operations and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/process-mapper
```
