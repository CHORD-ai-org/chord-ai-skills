---
name: bad-faith-demand
description: "Drafts time-limited policy-limits demands, with a readiness memo, that give the insurer a genuine, statute-compliant opportunity to settle within limits. Handles any offer to a liability insurer to settle within limits, and any pre-answer attorney offer on a Georgia motor-vehicle injury claim under O.C.G.A. 9-11-67.1(b). Separates third-party failure-to-settle from first-party claims, tests demands against Georgia 9-11-67.1 (Holt), California CCP 999-999.5, Missouri RSMo 537.058, Florida 624.155 and Texas Stowers, computes the deadline from the correct trigger, builds limits, lien and multiple-claimant matrices, and drafts measurable acceptance, release and payment terms. Use for time-limited, policy limits, Stowers or Holt demands, failure to settle, civil remedy notice, UM/UIM notice, or demand compliance review. Declines bad faith setup letters. Routes general pre-suit demands to demand-letter, liability coverage questions to coverage-opinion, and first-party coverage questions to legal-research."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bad-faith-demand
source: https://github.com/casemark/skills/tree/main/skills/legal/bad-faith-demand
---

# Bad Faith Demand

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts time-limited policy-limits demands, with a readiness memo, that give the insurer a genuine, statute-compliant opportunity to settle within limits. Handles any offer to a liability insurer to settle within limits, and any pre-answer attorney offer on a Georgia motor-vehicle injury claim under O.C.G.A. 9-11-67.1(b). Separates third-party failure-to-settle from first-party claims, tests demands against Georgia 9-11-67.1 (Holt), California CCP 999-999.5, Missouri RSMo 537.058, Florida 624.155 and Texas Stowers, computes the deadline from the correct trigger, builds limits, lien and multiple-claimant matrices, and drafts measurable acceptance, release and payment terms. Use for time-limited, policy limits, Stowers or Holt demands, failure to settle, civil remedy notice, UM/UIM notice, or demand compliance review. Declines bad faith setup letters. Routes general pre-suit demands to demand-letter, liability coverage questions to coverage-opinion, and first-party coverage questions to legal-research.

## Steps

1. Confirm the task matches this source: Drafts time-limited policy-limits demands, with a readiness memo, that give the insurer a genuine, statute-compliant opportunity to settle within limits. Handles any offer to a liability insurer to settle within limits, 
2. Start with the upstream step: Draft only. Nothing is sent, served or filed by this skill. Every output is a draft for attorney review, and the letter is never called ready to send.
3. Continue with: Source-review gate. Never call a document missing until the matter inventory has been checked and the file opened, with OCR or extraction tried. Classify every open item as one...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bad-faith-demand

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bad-faith-demand
```
