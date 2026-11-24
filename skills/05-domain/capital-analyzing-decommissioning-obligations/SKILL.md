---
name: capital-analyzing-decommissioning-obligations
description: "Evaluates asset retirement and decommissioning liabilities with cost estimation, timing analysis, and funding adequacy assessment. Use when analyzing decommissioning costs, evaluating ARO exposure, or assessing abandonment liability."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-decommissioning-obligations
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-decommissioning-obligations
---

# Capital Analyzing Decommissioning Obligations

## Brief info

Evaluates asset retirement and decommissioning liabilities with cost estimation, timing analysis, and funding adequacy assessment. Use when analyzing decommissioning costs, evaluating ARO exposure, or assessing abandonment liability. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates asset retirement and decommissioning liabilities with cost estimation, timing analysis, and funding adequacy assessment. Use when analyzing decommissioning costs, evaluating ARO exposure, or assessing abandonment liability.

## Steps

1. Confirm the task matches this source: Evaluates asset retirement and decommissioning liabilities with cost estimation, timing analysis, and funding adequacy assessment. Use when analyzing decommissioning costs, evaluating ARO exposure, or assessing abandonme
2. Start with the upstream step: Underwriting an acquisition of producing oil & gas properties, mines, or power plants with end-of-life obligations
3. Continue with: Auditing an existing ARO balance sheet provision under ASC 410 / IAS 37 / IFRS 16
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-decommissioning-obligations

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-decommissioning-obligations
```
