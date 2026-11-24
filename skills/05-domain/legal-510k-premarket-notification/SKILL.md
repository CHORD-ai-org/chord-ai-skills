---
name: legal-510k-premarket-notification
description: "Drafts FDA 510(k) Premarket Notification submissions demonstrating substantial equivalence under 21 CFR Part 807. Supports Traditional, Special, and Abbreviated pathways. Use when preparing Class II medical device regulatory filings, substantial equivalence analyses, or FDA premarket submissions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-510k-premarket-notification
source: https://github.com/casemark/skills/tree/main/skills/legal/510k-premarket-notification
---

# Legal 510K Premarket Notification

## Brief info

Drafts FDA 510(k) Premarket Notification submissions demonstrating substantial equivalence under 21 CFR Part 807. Supports Traditional, Special, and Abbreviated pathways. Use when preparing Class II medical device regulatory filings, substantial equivalence analyses, or FDA premarket submissions. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts FDA 510(k) Premarket Notification submissions demonstrating substantial equivalence under 21 CFR Part 807. Supports Traditional, Special, and Abbreviated pathways. Use when preparing Class II medical device regulatory filings, substantial equivalence analyses, or FDA premarket submissions.

## Steps

1. Confirm the task matches this source: Drafts FDA 510(k) Premarket Notification submissions demonstrating substantial equivalence under 21 CFR Part 807. Supports Traditional, Special, and Abbreviated pathways. Use when preparing Class II medical device regula
2. Start with the upstream step: 510(k) type — Traditional, Special, or Abbreviated
3. Continue with: Predicate device — trade name, manufacturer, K-number, clearance date
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/510k-premarket-notification

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-510k-premarket-notification
```
