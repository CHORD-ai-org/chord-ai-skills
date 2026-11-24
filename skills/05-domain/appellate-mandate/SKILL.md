---
name: appellate-mandate
description: "Drafts formal appellate mandates that conclude the appeal process and direct trial courts to implement appellate decisions. Extracts disposition language, remand directives, and procedural history from appellate records to construct jurisdiction-specific mandate orders. Use when preparing mandate orders, returning jurisdiction to lower courts, or formalizing appellate dispositions after ruling."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appellate-mandate
source: https://github.com/casemark/skills/tree/main/skills/legal/appellate-mandate
---

# Appellate Mandate

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts formal appellate mandates that conclude the appeal process and direct trial courts to implement appellate decisions. Extracts disposition language, remand directives, and procedural history from appellate records to construct jurisdiction-specific mandate orders. Use when preparing mandate orders, returning jurisdiction to lower courts, or formalizing appellate dispositions after ruling.

## Steps

1. Confirm the task matches this source: Drafts formal appellate mandates that conclude the appeal process and direct trial courts to implement appellate decisions. Extracts disposition language, remand directives, and procedural history from appellate records 
2. Start with the upstream step: Appellate opinion/judgment — final decision with exact disposition language
3. Continue with: Case caption — all party names and designations as they appear in the appellate record
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/appellate-mandate

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appellate-mandate
```
