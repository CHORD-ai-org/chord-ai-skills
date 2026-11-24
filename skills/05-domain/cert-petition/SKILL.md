---
name: cert-petition
description: "Drafts a Petition for Writ of Certiorari to the U.S. Supreme Court under Rules 10, 13, 14, and 33. Enforces Rule 10 criteria (circuit splits, precedent conflicts, important federal questions), jurisdictional verification under 28 U.S.C. §§ 1254/1257, timeliness, document structure, and booklet formatting. Use when seeking discretionary Supreme Court review, filing a cert petition, or drafting a writ of certiorari."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/cert-petition
source: https://github.com/casemark/skills/tree/main/skills/legal/cert-petition
---

# Cert Petition

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Petition for Writ of Certiorari to the U.S. Supreme Court under Rules 10, 13, 14, and 33. Enforces Rule 10 criteria (circuit splits, precedent conflicts, important federal questions), jurisdictional verification under 28 U.S.C. §§ 1254/1257, timeliness, document structure, and booklet formatting. Use when seeking discretionary Supreme Court review, filing a cert petition, or drafting a writ of certiorari.

## Steps

1. Confirm the task matches this source: Drafts a Petition for Writ of Certiorari to the U.S. Supreme Court under Rules 10, 13, 14, and 33. Enforces Rule 10 criteria (circuit splits, precedent conflicts, important federal questions), jurisdictional verification
2. Start with the upstream step: Lower court opinions/orders — all decisions including rehearing orders
3. Continue with: Record materials — key pleadings, evidentiary materials for appendix
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/cert-petition

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cert-petition
```
