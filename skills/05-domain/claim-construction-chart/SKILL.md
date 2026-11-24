---
name: claim-construction-chart
description: "Drafts Joint Claim Construction Charts for patent litigation Markman hearings in US federal courts. Organizes disputed claim terms with competing party constructions, intrinsic/extrinsic evidence citations, and agreement status. Use when preparing claim construction charts, Markman hearing exhibits, or joint prehearing statements in IP litigation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/claim-construction-chart
source: https://github.com/casemark/skills/tree/main/skills/legal/claim-construction-chart
---

# Claim Construction Chart

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts Joint Claim Construction Charts for patent litigation Markman hearings in US federal courts. Organizes disputed claim terms with competing party constructions, intrinsic/extrinsic evidence citations, and agreement status. Use when preparing claim construction charts, Markman hearing exhibits, or joint prehearing statements in IP litigation.

## Steps

1. Confirm the task matches this source: Drafts Joint Claim Construction Charts for patent litigation Markman hearings in US federal courts. Organizes disputed claim terms with competing party constructions, intrinsic/extrinsic evidence citations, and agreement
2. Start with the upstream step: Asserted patent(s): number, title, issue date, inventors, full claim text
3. Continue with: Case caption: party names, court/division, civil action number
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/claim-construction-chart

## Verify

```bash
python scripts/check_skills.py skills/05-domain/claim-construction-chart
```
