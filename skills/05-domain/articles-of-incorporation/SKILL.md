---
name: articles-of-incorporation
description: "Drafts jurisdiction-compliant U.S. Articles of Incorporation for corporate entity formation. Analyzes formation documents, term sheets, and cap tables to produce a filing-ready charter with name, purpose, capital structure, registered agent, and governance provisions. Use when forming a new corporation, drafting a charter document, or structuring equity for venture-backed or closely held companies."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/articles-of-incorporation
source: https://github.com/casemark/skills/tree/main/skills/legal/articles-of-incorporation
---

# Articles Of Incorporation

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/articles-of-incorporation
```
