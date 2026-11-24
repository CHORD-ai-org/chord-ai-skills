---
name: client-friendly-tone
description: "Rewrites legal communications in plain-language, client-friendly tone. Triggers when drafting or revising engagement letters, status updates, strategy memos, settlement recommendations, invoice cover letters, or any client-facing correspondence. Replaces jargon, leads with conclusions, and highlights action items."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/client-friendly-tone
source: https://github.com/casemark/skills/tree/main/skills/legal/client-friendly-tone
---

# Client Friendly Tone

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/client-friendly-tone
```
