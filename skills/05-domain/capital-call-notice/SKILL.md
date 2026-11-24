---
name: capital-call-notice
description: "Drafts U.S. capital call notices for PE, VC, or fund-managed LLCs aligned to LPA/operating agreement procedures and side letters. Use when drafting a capital call notice, drawdown notice, capital contribution demand, unfunded commitment call, or LP/GP capital call letter."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-call-notice
source: https://github.com/casemark/skills/tree/main/skills/legal/capital-call-notice
---

# Capital Call Notice

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-call-notice
```
