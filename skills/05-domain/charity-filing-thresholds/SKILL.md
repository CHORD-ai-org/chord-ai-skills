---
name: charity-filing-thresholds
description: "Researches state-specific charitable solicitation filing requirements keyed to gross revenue, producing a citation-backed state-by-state compliance matrix of audit thresholds, financial-statement tiers, filing fees, and due dates. Use when building charity compliance matrices, researching nonprofit filing thresholds, charitable solicitation registration renewals, comparing state audit requirements for 501(c)(3) organizations, or when the user mentions audit threshold, review threshold, compilation requirement, charity filing deadline, or multi-state nonprofit compliance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/charity-filing-thresholds
source: https://github.com/casemark/skills/tree/main/skills/legal/charity-filing-thresholds
---

# Charity Filing Thresholds

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/charity-filing-thresholds
```
