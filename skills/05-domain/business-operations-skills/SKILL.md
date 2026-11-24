---
name: business-operations-skills
description: "Route internal operations requests to the right BizOps skill: process, vendors, capacity, internal comms, SOPs, procurement. Use whenever the user asks where the bottleneck is or about vendor health."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/business-operations-skills
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/business-operations-skills
---

# Business Operations Skills

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Route internal operations requests to the right BizOps skill: process, vendors, capacity, internal comms, SOPs, procurement. Use whenever the user asks where the bottleneck is or about vendor health.

## Steps

1. Confirm the task matches this source: Route internal operations requests to the right BizOps skill: process, vendors, capacity, internal comms, SOPs, procurement. Use whenever the user asks where the bottleneck is or about vendor health.
2. Start with the upstream step: Does the user's working directory already contain a process map, vendor catalog, SOP, or org chart we can grep?
3. Continue with: Does the inquiry already disambiguate the lane (e.g., "vendor SLA review" — that's vendor-management, no question needed)?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: business-operations. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/business-operations-skills

## Verify

```bash
python scripts/check_skills.py skills/05-domain/business-operations-skills
```
