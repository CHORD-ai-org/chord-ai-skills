---
name: capital-analyzing-corporate-governance-catalysts
description: "Identifies governance-related catalysts with board refreshment, compensation reform, and shareholder proposal analysis. Use when analyzing governance catalysts, evaluating shareholder proposals, or assessing governance improvement potential."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-corporate-governance-catalysts
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-corporate-governance-catalysts
---

# Capital Analyzing Corporate Governance Catalysts

## Brief info

Identifies governance-related catalysts with board refreshment, compensation reform, and shareholder proposal analysis. Use when analyzing governance catalysts, evaluating shareholder proposals, or assessing governance improvement potential. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Identifies governance-related catalysts with board refreshment, compensation reform, and shareholder proposal analysis. Use when analyzing governance catalysts, evaluating shareholder proposals, or assessing governance improvement potential.

## Steps

1. Confirm the task matches this source: Identifies governance-related catalysts with board refreshment, compensation reform, and shareholder proposal analysis. Use when analyzing governance catalysts, evaluating shareholder proposals, or assessing governance i
2. Start with the upstream step: Screening a target company for activist engagement based on governance weaknesses
3. Continue with: Evaluating upcoming shareholder proposals (proxy season prep, vote recommendations)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-corporate-governance-catalysts

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-corporate-governance-catalysts
```
