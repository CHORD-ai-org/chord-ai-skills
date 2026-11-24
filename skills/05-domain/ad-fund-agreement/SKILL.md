---
name: ad-fund-agreement
description: "Drafts franchise advertising fund contribution agreements or addenda governing franchisee obligations to a centralized marketing fund. Trigger when drafting ad fund agreements, marketing fund addenda, or franchise contribution agreements involving fund administration, contribution calculations, or financial reporting."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ad-fund-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/ad-fund-agreement
---

# Ad Fund Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts franchise advertising fund contribution agreements or addenda governing franchisee obligations to a centralized marketing fund. Trigger when drafting ad fund agreements, marketing fund addenda, or franchise contribution agreements involving fund administration, contribution calculations, or financial reporting.

## Steps

1. Confirm the task matches this source: Drafts franchise advertising fund contribution agreements or addenda governing franchisee obligations to a centralized marketing fund. Trigger when drafting ad fund agreements, marketing fund addenda, or franchise contri
2. Start with the upstream step: Franchise Agreement — executed copy with date, amendment numbers, notice clauses, defined terms (especially "Gross Sales")
3. Continue with: Fund structure — standalone vs. addendum; national vs. regional; separate account vs. accounting mechanism
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/ad-fund-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ad-fund-agreement
```
