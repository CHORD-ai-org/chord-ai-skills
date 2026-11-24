---
name: class-settlement-preliminary-approval
description: "Drafts a Motion for Preliminary Approval of Class Action Settlement under Rule 23(e), covering settlement class certification, notice plan, claims administration, fairness analysis, and proposed scheduling order. Use when drafting preliminary approval motions, class action settlement filings, or Rule 23(e) submissions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-settlement-preliminary-approval
source: https://github.com/casemark/skills/tree/main/skills/legal/class-settlement-preliminary-approval
---

# Class Settlement Preliminary Approval

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-settlement-preliminary-approval
```
