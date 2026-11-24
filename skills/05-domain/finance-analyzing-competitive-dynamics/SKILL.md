---
name: finance-analyzing-competitive-dynamics
description: "Maps competitive landscapes with market share tracking and Porter's Five Forces analysis. Use when analyzing competition, assessing market structure, or evaluating competitive threats."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-competitive-dynamics
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-competitive-dynamics
---

# Finance Analyzing Competitive Dynamics

## Brief info

Maps competitive landscapes with market share tracking and Porter's Five Forces analysis. Use when analyzing competition, assessing market structure, or evaluating competitive threats. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Maps competitive landscapes with market share tracking and Porter's Five Forces analysis. Use when analyzing competition, assessing market structure, or evaluating competitive threats.

## Steps

1. Confirm the task matches this source: Maps competitive landscapes with market share tracking and Porter's Five Forces analysis. Use when analyzing competition, assessing market structure, or evaluating competitive threats.
2. Start with the upstream step: Initiating or updating coverage on a company and need to map its competitive position
3. Continue with: Evaluating a sector for investment allocation where market structure drives returns
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-competitive-dynamics

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-competitive-dynamics
```
