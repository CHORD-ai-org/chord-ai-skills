---
name: med-conducting-health-impact-assessments
description: "Structures health impact assessment with exposure evaluation and risk characterization. Use when assessing health impacts, evaluating environmental exposures, or characterizing population risk."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-health-impact-assessments
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-health-impact-assessments
---

# Med Conducting Health Impact Assessments

## Brief info

Structures health impact assessment with exposure evaluation and risk characterization. Use when assessing health impacts, evaluating environmental exposures, or characterizing population risk. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures health impact assessment with exposure evaluation and risk characterization. Use when assessing health impacts, evaluating environmental exposures, or characterizing population risk.

## Steps

1. Confirm the task matches this source: Structures health impact assessment with exposure evaluation and risk characterization. Use when assessing health impacts, evaluating environmental exposures, or characterizing population risk.
2. Start with the upstream step: What is the proposed decision (policy, project, or plan) being assessed?
3. Continue with: Who is the decision-maker and what is the decision timeline?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-health-impact-assessments

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-health-impact-assessments
```
