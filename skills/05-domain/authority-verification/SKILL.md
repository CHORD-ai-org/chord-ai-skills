---
name: authority-verification
description: "Verifies legal citations and retrieves source material using the case.dev Legal Research API and CLI. Use when validating a citation, confirming a case exists, pulling source text, finding related authorities, extracting citations from a brief or opinion, or building a filing-ready authority check without branded citator terminology."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/authority-verification
source: https://github.com/casemark/skills/tree/main/skills/legal/authority-verification
---

# Authority Verification

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/authority-verification
```
