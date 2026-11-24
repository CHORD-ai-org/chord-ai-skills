---
name: capital-analyzing-credit-fund-performance
description: "Evaluates credit fund returns with yield attribution, mark-to-market dynamics, and performance comparison across credit strategies. Use when analyzing credit fund performance, decomposing returns, or benchmarking credit strategies."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-fund-performance
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-fund-performance
---

# Capital Analyzing Credit Fund Performance

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates credit fund returns with yield attribution, mark-to-market dynamics, and performance comparison across credit strategies. Use when analyzing credit fund performance, decomposing returns, or benchmarking credit strategies.

## Steps

1. Confirm the task matches this source: Evaluates credit fund returns with yield attribution, mark-to-market dynamics, and performance comparison across credit strategies. Use when analyzing credit fund performance, decomposing returns, or benchmarking credit 
2. Start with the upstream step: Decomposing credit fund total returns into yield income, spread movement, and credit migration components
3. Continue with: Benchmarking a credit strategy (direct lending, broadly syndicated loans, CLO equity, distressed) against peers or indices
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-fund-performance

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-fund-performance
```
