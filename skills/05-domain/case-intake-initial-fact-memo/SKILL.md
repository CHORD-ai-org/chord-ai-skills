---
name: case-intake-initial-fact-memo
description: "Generates a structured attorney work product memorandum from an initial client consultation for commercial litigation. Extracts verifiable facts from uploaded documents, builds a chronological narrative, identifies parties and contracts, flags preliminary legal claims and defenses, and produces a prioritized action plan. Triggers at matter intake when a business client needs a foundational case evaluation document for a pre-filing commercial dispute."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/case-intake-initial-fact-memo
source: https://github.com/casemark/skills/tree/main/skills/legal/case-intake-initial-fact-memo
---

# Case Intake Initial Fact Memo

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/case-intake-initial-fact-memo
```
