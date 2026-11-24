---
name: appellate-formatting-certification
description: "Generates appellate-brief TOC, TOA, and Certificate of Compliance with defensible word-count methodology. Triggers on TOC/TOA rebuilds, certificate of compliance drafting, FRAP 32(g) compliance, word-count certification, or final brief formatting before filing."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appellate-formatting-certification
source: https://github.com/casemark/skills/tree/main/skills/legal/appellate-formatting-certification
---

# Appellate Formatting Certification

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Generates appellate-brief TOC, TOA, and Certificate of Compliance with defensible word-count methodology. Triggers on TOC/TOA rebuilds, certificate of compliance drafting, FRAP 32(g) compliance, word-count certification, or final brief formatting before filing.

## Steps

1. Confirm the task matches this source: Generates appellate-brief TOC, TOA, and Certificate of Compliance with defensible word-count methodology. Triggers on TOC/TOA rebuilds, certificate of compliance drafting, FRAP 32(g) compliance, word-count certification,
2. Start with the upstream step: Confirm rules — Identify governing rules and any court order modifying limits.
3. Continue with: Build heading map — Extract headings from brief; preserve exact text, capitalization, numbering.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/appellate-formatting-certification

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appellate-formatting-certification
```
