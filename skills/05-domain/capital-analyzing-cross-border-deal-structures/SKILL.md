---
name: capital-analyzing-cross-border-deal-structures
description: "Evaluates cross-border transaction complexities including tax treaties, currency, regulatory approvals, and cultural factors. Use when structuring international deals, assessing cross-border risk, or navigating multi-jurisdiction closings."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-border-deal-structures
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-border-deal-structures
---

# Capital Analyzing Cross Border Deal Structures

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates cross-border transaction complexities including tax treaties, currency, regulatory approvals, and cultural factors. Use when structuring international deals, assessing cross-border risk, or navigating multi-jurisdiction closings.

## Steps

1. Confirm the task matches this source: Evaluates cross-border transaction complexities including tax treaties, currency, regulatory approvals, and cultural factors. Use when structuring international deals, assessing cross-border risk, or navigating multi-jur
2. Start with the upstream step: Structuring an acquisition, merger, or joint venture involving entities in two or more jurisdictions
3. Continue with: Assessing whether a share purchase vs. asset purchase optimizes tax treaty benefits across borders
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-border-deal-structures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-border-deal-structures
```
