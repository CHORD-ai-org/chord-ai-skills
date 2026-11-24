---
name: capital-analyzing-corporate-governance-effectiveness
description: "Evaluates board composition, compensation alignment, and governance practices with proxy advisory and institutional investor standards. Use when analyzing governance, evaluating board effectiveness, or assessing shareholder alignment."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-corporate-governance-effectiveness
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-corporate-governance-effectiveness
---

# Capital Analyzing Corporate Governance Effectiveness

## Brief info

Evaluates board composition, compensation alignment, and governance practices with proxy advisory and institutional investor standards. Use when analyzing governance, evaluating board effectiveness, or assessing shareholder alignment. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates board composition, compensation alignment, and governance practices with proxy advisory and institutional investor standards. Use when analyzing governance, evaluating board effectiveness, or assessing shareholder alignment.

## Steps

1. Confirm the task matches this source: Evaluates board composition, compensation alignment, and governance practices with proxy advisory and institutional investor standards. Use when analyzing governance, evaluating board effectiveness, or assessing sharehol
2. Start with the upstream step: Preparing for or responding to proxy season and say-on-pay votes
3. Continue with: Evaluating a target company's governance profile during M&A due diligence
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-corporate-governance-effectiveness

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-corporate-governance-effectiveness
```
