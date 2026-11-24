---
name: case-summary
description: "Produces an attorney-ready memo from a corpus of legal documents supplied by the user. Use when a user shows up with a folder, zip, or vault of case documents and asks for a case summary, case evaluation, litigation package, intake memo, matter overview, or \"can you summarize this case for me.\" The skill ingests the corpus into a searchable index, OCRs anything non-searchable, inventories and diagnoses the practice area, loads the appropriate practice-area playbook module(s) (PI/tort, commercial litigation, IP infringement, or user-authored extensions), iteratively searches the corpus across eight core dimensions plus any module-specific dimensions, defers specialized document clusters (depositions, medical records, discovery, liens) to dedicated sibling skills, and synthesizes a cited memo."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/case-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/case-summary
---

# Case Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/case-summary
```
