---
name: finance-analyzing-economic-indicators
description: "Structures economic indicator analysis with leading, coincident, and lagging indicator interpretation. Use when analyzing economic data, interpreting economic releases, or tracking macro indicators."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-economic-indicators
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-economic-indicators
---

# Finance Analyzing Economic Indicators

## Brief info

Structures economic indicator analysis with leading, coincident, and lagging indicator interpretation. Use when analyzing economic data, interpreting economic releases, or tracking macro indicators. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures economic indicator analysis with leading, coincident, and lagging indicator interpretation. Use when analyzing economic data, interpreting economic releases, or tracking macro indicators.

## Steps

1. Confirm the task matches this source: Structures economic indicator analysis with leading, coincident, and lagging indicator interpretation. Use when analyzing economic data, interpreting economic releases, or tracking macro indicators.
2. Start with the upstream step: Interpreting a new economic data release (jobs report, CPI, PMI, GDP, etc.)
3. Continue with: Building a macro outlook by synthesizing multiple indicators across categories
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-economic-indicators

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-economic-indicators
```
