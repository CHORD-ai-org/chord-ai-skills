---
name: chapter-11-reorg-plan
description: "Drafts a Chapter 11 Plan of Reorganization under 11 U.S.C. §§ 1121–1129 with claim classification, treatment provisions, distribution mechanics, executory contract determinations, and confirmation compliance. Use when preparing reorganization plans, restructuring debts, classifying claims, drafting Chapter 11 plans, or helping debtors emerge from bankruptcy. Trigger keywords: reorganization plan, Chapter 11, plan of reorganization, debt restructuring, cramdown, claim classification, confirmation order."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/chapter-11-reorg-plan
source: https://github.com/casemark/skills/tree/main/skills/legal/chapter-11-reorg-plan
---

# Chapter 11 Reorg Plan

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/chapter-11-reorg-plan
```
