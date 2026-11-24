---
name: contract-and-proposal-writer
description: "Use when drafting a freelance contract, proposal, SOW, NDA or MSA for US, EU, UK or DACH jurisdictions. Writes structured Markdown with docx conversion steps; not legal advice."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/contract-and-proposal-writer
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/contract-and-proposal-writer
---

# Contract And Proposal Writer

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Business growth and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/contract-and-proposal-writer
```
