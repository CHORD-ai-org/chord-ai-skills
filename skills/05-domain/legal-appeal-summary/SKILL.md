---
name: legal-appeal-summary
description: "Generates structured analytical summaries of appellate documents covering procedural posture, issues on appeal, standards of review, and strategic assessment. Use when onboarding to an appeal, preparing for oral argument, evaluating appellate risk, or summarizing the appellate record."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-appeal-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/appeal-summary
---

# Legal Appeal Summary

## Brief info

Generates structured analytical summaries of appellate documents covering procedural posture, issues on appeal, standards of review, and strategic assessment. Use when onboarding to an appeal, preparing for oral argument, evaluating appellate risk, or summarizing the appellate record. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Generates structured analytical summaries of appellate documents covering procedural posture, issues on appeal, standards of review, and strategic assessment. Use when onboarding to an appeal, preparing for oral argument, evaluating appellate risk, or summarizing the appellate record.

## Steps

1. Confirm the task matches this source: Generates structured analytical summaries of appellate documents covering procedural posture, issues on appeal, standards of review, and strategic assessment. Use when onboarding to an appeal, preparing for oral argument
2. Start with the upstream step: [ ] Timeliness of notice of appeal
3. Continue with: [ ] Proper record designation and transmission status
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/appeal-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-appeal-summary
```
