---
name: iso13485-audit-prep
description: "Use for /compliance-os:iso13485-audit-prep, or before an ISO 13485 internal audit or DHF closure."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/iso13485-audit-prep
source: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/iso13485-audit-prep
---

# Iso13485 Audit Prep

## Brief info

Use for /compliance-os:iso13485-audit-prep, or before an ISO 13485 internal audit or DHF closure. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Use for /compliance-os:iso13485-audit-prep, or before an ISO 13485 internal audit or DHF closure.

## Steps

1. Confirm the task matches this source: Use for /compliance-os:iso13485-audit-prep, or before an ISO 13485 internal audit or DHF closure.
2. Start with the upstream step: Before annual Clause 8.2.4 internal audit
3. Continue with: Before MDR / FDA QSR alignment review (substantially harmonized post Feb 2026)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: compliance-os. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/iso13485-audit-prep

## Verify

```bash
python scripts/check_skills.py skills/05-domain/iso13485-audit-prep
```
