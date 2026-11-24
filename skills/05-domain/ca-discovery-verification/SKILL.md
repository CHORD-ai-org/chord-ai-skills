---
name: ca-discovery-verification
description: "Drafts California Superior Court discovery verification pages under CCP §§ 2030.250 and 2031.250 with proper CCP § 2015.5 perjury declarations. Trigger when the user needs a verification page for interrogatory or inspection/RPD responses, mentions California discovery verification, party vs. attorney signing, information-and-belief clauses, or fixing unverified responses. CA Superior Court only — not federal."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ca-discovery-verification
source: https://github.com/casemark/skills/tree/main/skills/legal/ca-discovery-verification
---

# Ca Discovery Verification

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts California Superior Court discovery verification pages under CCP §§ 2030.250 and 2031.250 with proper CCP § 2015.5 perjury declarations. Trigger when the user needs a verification page for interrogatory or inspection/RPD responses, mentions California discovery verification, party vs. attorney signing, information-and-belief clauses, or fixing unverified responses. CA Superior Court only — not federal.

## Steps

1. Confirm the task matches this source: Drafts California Superior Court discovery verification pages under CCP §§ 2030.250 and 2031.250 with proper CCP § 2015.5 perjury declarations. Trigger when the user needs a verification page for interrogatory or inspect
2. Start with the upstream step: Gather intake details (see Pre-Draft Intake)
3. Continue with: Select verification type by discovery device
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/ca-discovery-verification

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ca-discovery-verification
```
