---
name: adverse-possession-claim
description: "Drafts adverse possession complaints and quiet title pleadings. Structures jurisdictional foundations, legal property descriptions, and element-by-element proof of actual, open, continuous, exclusive, and hostile possession. Use when filing adverse possession claims, quiet title actions, or prescriptive ownership pleadings."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/adverse-possession-claim
source: https://github.com/casemark/skills/tree/main/skills/legal/adverse-possession-claim
---

# Adverse Possession Claim

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/adverse-possession-claim
```
