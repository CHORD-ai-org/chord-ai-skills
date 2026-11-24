---
name: auth-packet-summary
description: "Validates and summarizes the four required authorization forms in a personal injury matter (retainer, HIPAA release, insurance authorization, employment record release). Confirms signatures, dates, scope, and completeness to determine readiness for the investigation phase. Use when reviewing client onboarding packets, verifying authorization forms before discovery, or checking HIPAA and record-release compliance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/auth-packet-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/auth-packet-summary
---

# Auth Packet Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Validates and summarizes the four required authorization forms in a personal injury matter (retainer, HIPAA release, insurance authorization, employment record release). Confirms signatures, dates, scope, and completeness to determine readiness for the investigation phase. Use when reviewing client onboarding packets, verifying authorization forms before discovery, or checking HIPAA and record-release compliance.

## Steps

1. Confirm the task matches this source: Validates and summarizes the four required authorization forms in a personal injury matter (retainer, HIPAA release, insurance authorization, employment record release). Confirms signatures, dates, scope, and completenes
2. Start with the upstream step: All client-signed authorization forms uploaded to the matter
3. Continue with: Client full legal name and case/matter number
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/auth-packet-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/auth-packet-summary
```
