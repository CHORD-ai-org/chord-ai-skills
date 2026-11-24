---
name: bulk-sales-compliance
description: "Drafts U.S. bulk sales compliance packages for asset purchase transactions outside the ordinary course, including UCC Article 6 jurisdictional analysis, creditor schedules, notice of intended bulk sale, seller affidavit, escrow framework, and closing checklist. Use when handling bulk sale, bulk transfer, inventory sale, asset purchase compliance, creditor notice, or successor liability avoidance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bulk-sales-compliance
source: https://github.com/casemark/skills/tree/main/skills/legal/bulk-sales-compliance
---

# Bulk Sales Compliance

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bulk-sales-compliance
```
