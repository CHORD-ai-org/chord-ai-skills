---
name: c-tpat-security-profile
description: "Drafts a U.S. C-TPAT Security Profile for CBP submission covering physical, personnel, procedural, conveyance, and IT security domains. Use when preparing C-TPAT enrollment, certification, validation, or recertification profiles, or assembling a CBP-ready security narrative. Trigger: C-TPAT, CBP security profile, supply chain security, trusted trader, customs validation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/c-tpat-security-profile
source: https://github.com/casemark/skills/tree/main/skills/legal/c-tpat-security-profile
---

# C Tpat Security Profile

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a U.S. C-TPAT Security Profile for CBP submission covering physical, personnel, procedural, conveyance, and IT security domains. Use when preparing C-TPAT enrollment, certification, validation, or recertification profiles, or assembling a CBP-ready security narrative. Trigger: C-TPAT, CBP security profile, supply chain security, trusted trader, customs validation.

## Steps

1. Confirm the task matches this source: Drafts a U.S. C-TPAT Security Profile for CBP submission covering physical, personnel, procedural, conveyance, and IT security domains. Use when preparing C-TPAT enrollment, certification, validation, or recertification 
2. Start with the upstream step: Corporate identifiers — legal name, EIN, DUNS, HQ, facility list, C-TPAT account/tier if enrolled
3. Continue with: Supply chain map — roles (importer/broker/forwarder), trade lanes, origin countries, products, volume
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/c-tpat-security-profile

## Verify

```bash
python scripts/check_skills.py skills/05-domain/c-tpat-security-profile
```
