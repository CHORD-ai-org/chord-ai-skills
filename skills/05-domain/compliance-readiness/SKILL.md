---
name: compliance-readiness
description: "Use for /compliance-os:compliance-readiness, or before adding a framework or planning the annual audit calendar."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/compliance-readiness
source: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/compliance-readiness
---

# Compliance Readiness

## Brief info

Use for /compliance-os:compliance-readiness, or before adding a framework or planning the annual audit calendar. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Use for /compliance-os:compliance-readiness, or before adding a framework or planning the annual audit calendar.

## Steps

1. Confirm the task matches this source: Use for /compliance-os:compliance-readiness, or before adding a framework or planning the annual audit calendar.
2. Start with the upstream step: Before adopting a new compliance framework
3. Continue with: Before annual audit calendar finalization
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: compliance-os. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/compliance-readiness

## Verify

```bash
python scripts/check_skills.py skills/05-domain/compliance-readiness
```
