---
name: articles-of-incorporation-nonprofit
description: "Drafts filing-ready Articles of Incorporation for U.S. non-profit corporations satisfying state corporate law and the IRS organizational test under IRC § 501(c)(3). Enforces mandatory exempt-purpose language, private inurement prohibition, dissolution clause, and political activity limitations. Use when forming a new non-profit, charitable corporation, or tax-exempt entity seeking 501(c)(3) recognition."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/articles-of-incorporation-nonprofit
source: https://github.com/casemark/skills/tree/main/skills/legal/articles-of-incorporation-nonprofit
---

# Articles Of Incorporation Nonprofit

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/articles-of-incorporation-nonprofit
```
