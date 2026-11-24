---
name: api-license-agreement
description: "Drafts a clickwrap-ready US API License Agreement for companies licensing proprietary APIs to third-party developers. Use when drafting API terms of service, developer agreements, API access agreements, or click-through license terms. Produces full agreement (17 sections), condensed terms, or developer quick-reference. Cross-references DPA, SLA, AUP, trademark guidelines, and privacy policy modules."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/api-license-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/api-license-agreement
---

# Api License Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/api-license-agreement
```
