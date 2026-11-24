---
name: legal-abstract-of-judgment
description: "Drafts a recordable Abstract of Judgment to create a judgment lien on a debtor's real property. Extracts party names, monetary components, and judgment details from case documents, then applies jurisdiction-specific formatting and certification requirements. Use post-judgment in commercial litigation when enforcing monetary awards, perfecting judgment liens, or preparing lien filings with the county recorder."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-abstract-of-judgment
source: https://github.com/casemark/skills/tree/main/skills/legal/abstract-of-judgment
---

# Legal Abstract Of Judgment

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a recordable Abstract of Judgment to create a judgment lien on a debtor's real property. Extracts party names, monetary components, and judgment details from case documents, then applies jurisdiction-specific formatting and certification requirements. Use post-judgment in commercial litigation when enforcing monetary awards, perfecting judgment liens, or preparing lien filings with the county recorder.

## Steps

1. Confirm the task matches this source: Drafts a recordable Abstract of Judgment to create a judgment lien on a debtor's real property. Extracts party names, monetary components, and judgment details from case documents, then applies jurisdiction-specific form
2. Start with the upstream step: Judgment order — final judgment with entry date, relief granted, and any amendments
3. Continue with: Case filing documents — complaint, caption, case number
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/abstract-of-judgment

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-abstract-of-judgment
```
