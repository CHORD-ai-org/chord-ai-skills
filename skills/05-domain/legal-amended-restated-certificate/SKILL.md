---
name: legal-amended-restated-certificate
description: "Drafts a Delaware Amended and Restated Certificate of Incorporation implementing VC term sheet economics and governance into DGCL-compliant charter provisions. Use when drafting or revising a Delaware A&R certificate, preferred stock charter terms, Series Seed/A/B financing charter, blank check preferred authority, or implementing cap structure from a term sheet or SPA."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-amended-restated-certificate
source: https://github.com/casemark/skills/tree/main/skills/legal/amended-restated-certificate
---

# Legal Amended Restated Certificate

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Delaware Amended and Restated Certificate of Incorporation implementing VC term sheet economics and governance into DGCL-compliant charter provisions. Use when drafting or revising a Delaware A&R certificate, preferred stock charter terms, Series Seed/A/B financing charter, blank check preferred authority, or implementing cap structure from a term sheet or SPA.

## Steps

1. Confirm the task matches this source: Drafts a Delaware Amended and Restated Certificate of Incorporation implementing VC term sheet economics and governance into DGCL-compliant charter provisions. Use when drafting or revising a Delaware A&R certificate, pr
2. Start with the upstream step: Executed term sheet or SPA exhibits (final economics and governance)
3. Continue with: Current cap table (outstanding, reserved, convertible securities)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/amended-restated-certificate

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-amended-restated-certificate
```
