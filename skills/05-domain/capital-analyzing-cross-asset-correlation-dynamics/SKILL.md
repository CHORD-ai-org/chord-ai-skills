---
name: capital-analyzing-cross-asset-correlation-dynamics
description: "Monitors cross-asset correlation patterns with regime-dependent analysis and diversification effectiveness assessment. Use when analyzing correlations, assessing diversification, or evaluating cross-asset relationships."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-asset-correlation-dynamics
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-asset-correlation-dynamics
---

# Capital Analyzing Cross Asset Correlation Dynamics

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Monitors cross-asset correlation patterns with regime-dependent analysis and diversification effectiveness assessment. Use when analyzing correlations, assessing diversification, or evaluating cross-asset relationships.

## Steps

1. Confirm the task matches this source: Monitors cross-asset correlation patterns with regime-dependent analysis and diversification effectiveness assessment. Use when analyzing correlations, assessing diversification, or evaluating cross-asset relationships.
2. Start with the upstream step: Evaluating portfolio diversification effectiveness across equities, fixed income, commodities, FX, and alternatives
3. Continue with: Detecting correlation regime shifts (e.g., crisis convergence where historically uncorrelated assets move together)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-asset-correlation-dynamics

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-asset-correlation-dynamics
```
