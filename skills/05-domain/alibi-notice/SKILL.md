---
name: alibi-notice
description: "Drafts a Notice of Alibi Defense under Fed. R. Crim. P. 12.1 or state equivalents. Triggers on alibi notice drafting, alibi defense filing, Rule 12.1 disclosure, or pre-trial criminal defense notice tasks."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/alibi-notice
source: https://github.com/casemark/skills/tree/main/skills/legal/alibi-notice
---

# Alibi Notice

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/alibi-notice
```
