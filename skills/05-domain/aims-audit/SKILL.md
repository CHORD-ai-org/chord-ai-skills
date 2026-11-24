---
name: aims-audit
description: "ISO 42001 AI readiness check. Use before a stage 1 or internal audit, or /compliance-os:aims-audit."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/aims-audit
source: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/aims-audit
---

# Aims Audit

## Brief info

ISO 42001 AI readiness check. Use before a stage 1 or internal audit, or /compliance-os:aims-audit. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: ISO 42001 AI readiness check. Use before a stage 1 or internal audit, or /compliance-os:aims-audit.

## Steps

1. Confirm the task matches this source: ISO 42001 AI readiness check. Use before a stage 1 or internal audit, or /compliance-os:aims-audit.
2. Start with the upstream step: Before stage 1 ISO 42001 certification audit
3. Continue with: Before annual internal audit cycle (Clause 9.2)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: compliance-os. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/aims-audit

## Verify

```bash
python scripts/check_skills.py skills/05-domain/aims-audit
```
