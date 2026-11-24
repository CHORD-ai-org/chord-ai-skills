---
name: access-indemnity-agreement
description: "Drafts U.S. commercial real estate access and indemnity (right-of-entry) agreements for pre-closing due diligence. Covers license grants, non-invasive vs invasive testing gates, insurance/endorsement requirements, indemnity with discovery carve-outs, restoration and lien remedies, confidentiality, and anti-indemnity guardrails. Trigger: access agreement, right of entry, due diligence access, Phase I/II, invasive testing, pre-PSA site inspection."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/access-indemnity-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/access-indemnity-agreement
---

# Access Indemnity Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/access-indemnity-agreement
```
