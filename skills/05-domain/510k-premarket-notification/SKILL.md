---
name: 510k-premarket-notification
description: "Drafts FDA 510(k) Premarket Notification submissions demonstrating substantial equivalence under 21 CFR Part 807. Supports Traditional, Special, and Abbreviated pathways. Use when preparing Class II medical device regulatory filings, substantial equivalence analyses, or FDA premarket submissions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/510k-premarket-notification
source: https://github.com/casemark/skills/tree/main/skills/legal/510k-premarket-notification
---

# 510K Premarket Notification

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/510k-premarket-notification
```
