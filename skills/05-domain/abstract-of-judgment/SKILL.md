---
name: abstract-of-judgment
description: "Drafts a recordable Abstract of Judgment to create a judgment lien on a debtor's real property. Extracts party names, monetary components, and judgment details from case documents, then applies jurisdiction-specific formatting and certification requirements. Use post-judgment in commercial litigation when enforcing monetary awards, perfecting judgment liens, or preparing lien filings with the county recorder."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/abstract-of-judgment
source: https://github.com/casemark/skills/tree/main/skills/legal/abstract-of-judgment
---

# Abstract Of Judgment

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/abstract-of-judgment
```
