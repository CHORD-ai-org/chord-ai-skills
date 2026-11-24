---
name: capital-analyzing-conglomerate-discount-dynamics
description: "Evaluates conglomerate discount with SOTP analysis, segment-level valuation, and separation benefit quantification. Use when analyzing conglomerate value, building SOTP models, or evaluating break-up scenarios."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-conglomerate-discount-dynamics
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-conglomerate-discount-dynamics
---

# Capital Analyzing Conglomerate Discount Dynamics

## Brief info

Evaluates conglomerate discount with SOTP analysis, segment-level valuation, and separation benefit quantification. Use when analyzing conglomerate value, building SOTP models, or evaluating break-up scenarios. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates conglomerate discount with SOTP analysis, segment-level valuation, and separation benefit quantification. Use when analyzing conglomerate value, building SOTP models, or evaluating break-up scenarios.

## Steps

1. Confirm the task matches this source: Evaluates conglomerate discount with SOTP analysis, segment-level valuation, and separation benefit quantification. Use when analyzing conglomerate value, building SOTP models, or evaluating break-up scenarios.
2. Start with the upstream step: Quantifying the implied conglomerate discount for a multi-segment company versus pure-play peers
3. Continue with: Building or auditing a sum-of-the-parts (SOTP) model for board presentations or activist defense
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-conglomerate-discount-dynamics

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-conglomerate-discount-dynamics
```
