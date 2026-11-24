---
name: bill-of-costs-on-appeal
description: "Drafts a verified U.S. appellate Bill of Costs itemizing taxable costs under FRAP 39 or state analogs. Trigger when the user needs to prepare, file, or tax appellate costs after judgment, or references FRAP 39, bill of costs on appeal, or appellate cost taxation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bill-of-costs-on-appeal
source: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-costs-on-appeal
---

# Bill Of Costs On Appeal

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a verified U.S. appellate Bill of Costs itemizing taxable costs under FRAP 39 or state analogs. Trigger when the user needs to prepare, file, or tax appellate costs after judgment, or references FRAP 39, bill of costs on appeal, or appellate cost taxation.

## Steps

1. Confirm the task matches this source: Drafts a verified U.S. appellate Bill of Costs itemizing taxable costs under FRAP 39 or state analogs. Trigger when the user needs to prepare, file, or tax appellate costs after judgment, or references FRAP 39, bill of c
2. Start with the upstream step: Appellate judgment/order with entry date and prevailing-party designation
3. Continue with: Applicable appellate rules, local rules, deadline, required form, and taxing court
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-costs-on-appeal

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bill-of-costs-on-appeal
```
