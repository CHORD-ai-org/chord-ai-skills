---
name: bill-of-lading
description: "Drafts a U.S. ocean Bill of Lading (B/L) functioning as receipt, contract of carriage, and document of title under COGSA or Hague-Visby. Covers negotiable and straight B/Ls, cargo description, freight allocation, and core carriage clauses. Use when drafting or reviewing a bill of lading, master/house B/L, ocean shipment documentation, or title transfer. Trigger keywords: bill of lading, B/L, ocean carriage, COGSA, Hague-Visby, negotiable, straight, master bill, house bill."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bill-of-lading
source: https://github.com/casemark/skills/tree/main/skills/legal/bill-of-lading
---

# Bill Of Lading

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bill-of-lading
```
