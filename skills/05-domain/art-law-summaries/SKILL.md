---
name: art-law-summaries
description: "Generates structured U.S. art law summaries with Bluebook citations, doctrinal analysis, and stakeholder guidance. Use when researching art law precedents, advising on art transactions, preparing for art market litigation, or surveying a doctrine or statute across ownership, provenance, copyright, VARA, NAGPRA, authentication, NFTs, or AI-generated art."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/art-law-summaries
source: https://github.com/casemark/skills/tree/main/skills/legal/art-law-summaries
---

# Art Law Summaries

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/art-law-summaries
```
