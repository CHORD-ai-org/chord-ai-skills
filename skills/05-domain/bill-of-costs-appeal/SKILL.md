---
name: bill-of-costs-appeal
description: "Drafts an itemized Bill of Costs on Appeal under FRAP 39 or state equivalent for the prevailing party to recover allowable appellate expenses. Triggers on appellate cost bill drafting, post-judgment cost recovery filings, or prevailing party cost submissions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bill-of-costs-appeal
source: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-costs-appeal
---

# Bill Of Costs Appeal

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bill-of-costs-appeal
```
