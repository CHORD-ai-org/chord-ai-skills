---
name: assignment-and-assumption-of-leases
description: "Drafts an Assignment and Assumption of Leases transferring tenant leases from seller (Assignor) to buyer (Assignee) as a closing document to a commercial property PSA. Trigger when closing a commercial property sale with existing tenant leases or when a user needs lease assignment/assumption language for a real estate transaction."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/assignment-and-assumption-of-leases
source: https://github.com/casemark/skills/tree/main/skills/legal/assignment-and-assumption-of-leases
---

# Assignment And Assumption Of Leases

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/assignment-and-assumption-of-leases
```
