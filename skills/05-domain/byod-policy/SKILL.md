---
name: byod-policy
description: "Drafts a Bring Your Own Device (BYOD) policy for U.S. employers governing personal device access to company systems. Covers MDM enrollment, encryption, remote wipe authority, privacy expectations, data classification, and regulatory overlays (HIPAA, GLBA, SOX, GDPR). Use when creating or updating BYOD policies, mobile device security policies, or personal device programs."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/byod-policy
source: https://github.com/casemark/skills/tree/main/skills/legal/byod-policy
---

# Byod Policy

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Bring Your Own Device (BYOD) policy for U.S. employers governing personal device access to company systems. Covers MDM enrollment, encryption, remote wipe authority, privacy expectations, data classification, and regulatory overlays (HIPAA, GLBA, SOX, GDPR). Use when creating or updating BYOD policies, mobile device security policies, or personal device programs.

## Steps

1. Confirm the task matches this source: Drafts a Bring Your Own Device (BYOD) policy for U.S. employers governing personal device access to company systems. Covers MDM enrollment, encryption, remote wipe authority, privacy expectations, data classification, an
2. Start with the upstream step: Organization profile — industry, size, applicable regulations (HIPAA, GLBA, SOX, GDPR, CCPA)
3. Continue with: Device scope — smartphones, tablets, laptops, wearables
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/byod-policy

## Verify

```bash
python scripts/check_skills.py skills/05-domain/byod-policy
```
