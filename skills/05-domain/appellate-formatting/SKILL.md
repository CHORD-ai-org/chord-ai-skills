---
name: appellate-formatting
description: "Generates appellate-filing-ready Tables of Contents, Tables of Authorities, and Certificates of Compliance under FRAP 32(g) and related rules. Produces defensible word-count calculations with transparent exclusions and anti-hallucination guardrails for pagination and citations. Covers federal circuits, state appellate courts, and U.S. Supreme Court variations. Use when building TOC, TOA, compliance certificates, formatting briefs for filing, or when the user mentions word count calculation, FRAP 32 compliance, appellate brief assembly, or page numbering."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appellate-formatting
source: https://github.com/casemark/skills/tree/main/skills/legal/appellate-formatting
---

# Appellate Formatting

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appellate-formatting
```
