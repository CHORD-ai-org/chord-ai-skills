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

Use when the task matches this source: Use when documenting an end-to-end business process (procurement, onboarding, handoffs) and finding where work waits. Maps it with process_documenter.py, measures stages with cycle_time_analyzer.py and finds bottlenecks with bottleneck_detector.py.

## Steps

1. Confirm the task matches this source: Use when documenting an end-to-end business process (procurement, onboarding, handoffs) and finding where work waits. Maps it with process_documenter.py, measures stages with cycle_time_analyzer.py and finds bottlenecks 
2. Start with the upstream step: Implicit process — the steps exist only in tribal knowledge, so handoffs drop and onboarding takes weeks.
3. Continue with: Invisible waiting — most of the elapsed time on any business process is queue / wait / approval time, not actual work; teams optimize the wrong stage.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: business-operations. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/process-mapper

## Verify

```bash
python scripts/check_skills.py skills/05-domain/process-mapper
```
