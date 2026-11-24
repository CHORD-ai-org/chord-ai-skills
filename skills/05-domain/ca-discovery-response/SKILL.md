---
name: ca-discovery-response
description: "Drafts code-compliant California responses to Requests for Production (CCP § 2031.010 et seq.) for Superior Court. Use when the user mentions California RFP responses, CCP 2031, discovery objections, compliance statements, inability to comply, privilege objections, Bates numbering, verification requirements, or responding to document requests in California state court. California Superior Court only — not for federal court without substantial modification."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ca-discovery-response
source: https://github.com/casemark/skills/tree/main/skills/legal/ca-discovery-response
---

# Ca Discovery Response

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ca-discovery-response
```
