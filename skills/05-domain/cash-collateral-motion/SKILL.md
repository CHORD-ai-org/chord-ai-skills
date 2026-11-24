---
name: cash-collateral-motion
description: "Drafts motions to use cash collateral under 11 U.S.C. § 363. Use when a debtor-in-possession needs court authorization to use cash collateral, typically as a first-day pleading."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/cash-collateral-motion
source: https://github.com/casemark/skills/tree/main/skills/legal/cash-collateral-motion
---

# Cash Collateral Motion

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts motions to use cash collateral under 11 U.S.C. § 363. Use when a debtor-in-possession needs court authorization to use cash collateral, typically as a first-day pleading.

## Steps

1. Confirm the task matches this source: Drafts motions to use cash collateral under 11 U.S.C. § 363. Use when a debtor-in-possession needs court authorization to use cash collateral, typically as a first-day pleading.
2. Start with the upstream step: Case info — debtor name, case number, chapter, court, judge
3. Continue with: Prepetition debt — secured creditor(s), loan docs, amounts, collateral descriptions
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/cash-collateral-motion

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cash-collateral-motion
```
