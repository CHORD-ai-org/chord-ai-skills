---
name: adversary-proceeding-complaint
description: "Drafts adversary proceeding complaints for U.S. Bankruptcy Court under FRBP Rule 7001. Covers dischargeability disputes (§ 523), preference actions (§ 547), fraudulent transfers (§ 548), and stay violations (§ 362). Produces a filing-ready pleading with caption, jurisdictional basis, numbered allegations, count structure, and prayer for relief. Triggers when a trustee, creditor, or party in interest needs to initiate litigation within an existing bankruptcy case."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/adversary-proceeding-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/adversary-proceeding-complaint
---

# Adversary Proceeding Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/adversary-proceeding-complaint
```
