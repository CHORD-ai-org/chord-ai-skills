---
name: ada-failure-to-accommodate-complaint
description: "Drafts a court-ready ADA failure-to-accommodate complaint under Title I (employment, 42 U.S.C. § 12112) or Title III (public accommodations, 42 U.S.C. § 12182). Structures jurisdiction, EEOC exhaustion, factual allegations, causes of action, and relief. Use when drafting ADA disability discrimination complaints, reasonable accommodation pleadings, or civil rights complaints for plaintiffs with disabilities."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ada-failure-to-accommodate-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/ada-failure-to-accommodate-complaint
---

# Ada Failure To Accommodate Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ada-failure-to-accommodate-complaint
```
