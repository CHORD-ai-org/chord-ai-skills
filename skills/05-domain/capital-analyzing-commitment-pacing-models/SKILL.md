---
name: capital-analyzing-commitment-pacing-models
description: "Builds LP commitment pacing with deployment curves, distribution assumptions, and NAV projection for portfolio planning. Use when modeling commitment pacing, projecting LP cash flows, or planning new fund allocations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-commitment-pacing-models
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-commitment-pacing-models
---

# Capital Analyzing Commitment Pacing Models

## Brief info

Builds LP commitment pacing with deployment curves, distribution assumptions, and NAV projection for portfolio planning. Use when modeling commitment pacing, projecting LP cash flows, or planning new fund allocations. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Builds LP commitment pacing with deployment curves, distribution assumptions, and NAV projection for portfolio planning. Use when modeling commitment pacing, projecting LP cash flows, or planning new fund allocations.

## Steps

1. Confirm the task matches this source: Builds LP commitment pacing with deployment curves, distribution assumptions, and NAV projection for portfolio planning. Use when modeling commitment pacing, projecting LP cash flows, or planning new fund allocations.
2. Start with the upstream step: Modeling forward commitment schedules against an LP's allocation targets and liquidity constraints
3. Continue with: Projecting net cash flows (capital calls minus distributions) across existing and prospective fund commitments
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-commitment-pacing-models

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-commitment-pacing-models
```
