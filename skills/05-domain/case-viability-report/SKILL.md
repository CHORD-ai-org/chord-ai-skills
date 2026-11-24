---
name: case-viability-report
description: "Produces internal case viability and conflict check memos for personal injury litigation intake. Screens conflicts, assesses liability and damages, checks statute of limitations, and outputs an accept/decline recommendation. Use when evaluating new PI intake, running conflict checks, assessing case merit pre-filing, or preparing acceptance memos."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/case-viability-report
source: https://github.com/casemark/skills/tree/main/skills/legal/case-viability-report
---

# Case Viability Report

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces internal case viability and conflict check memos for personal injury litigation intake. Screens conflicts, assesses liability and damages, checks statute of limitations, and outputs an accept/decline recommendation. Use when evaluating new PI intake, running conflict checks, assessing case merit pre-filing, or preparing acceptance memos.

## Steps

1. Confirm the task matches this source: Produces internal case viability and conflict check memos for personal injury litigation intake. Screens conflicts, assesses liability and damages, checks statute of limitations, and outputs an accept/decline recommendat
2. Start with the upstream step: Intake summary — client name, adverse parties, incident date, injuries, objectives
3. Continue with: Supporting documents — police reports, medical records, photos, insurance info
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/case-viability-report

## Verify

```bash
python scripts/check_skills.py skills/05-domain/case-viability-report
```
