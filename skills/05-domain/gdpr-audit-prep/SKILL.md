---
name: gdpr-audit-prep
description: "Use for /compliance-os:gdpr-audit-prep, or before a GDPR review, post-breach audit or DPA investigation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/gdpr-audit-prep
source: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/gdpr-audit-prep
---

# Gdpr Audit Prep

## Brief info

Use for /compliance-os:gdpr-audit-prep, or before a GDPR review, post-breach audit or DPA investigation. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Use for /compliance-os:gdpr-audit-prep, or before a GDPR review, post-breach audit or DPA investigation.

## Steps

1. Confirm the task matches this source: Use for /compliance-os:gdpr-audit-prep, or before a GDPR review, post-breach audit or DPA investigation.
2. Start with the upstream step: Before annual internal GDPR audit
3. Continue with: Before quarterly Article 30 RoPA refresh
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: compliance-os. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/gdpr-audit-prep

## Verify

```bash
python scripts/check_skills.py skills/05-domain/gdpr-audit-prep
```
