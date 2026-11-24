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

Use when the task matches this source: Generates appellate-filing-ready Tables of Contents, Tables of Authorities, and Certificates of Compliance under FRAP 32(g) and related rules. Produces defensible word-count calculations with transparent exclusions and anti-hallucination guardrails for pagination and citations. Covers federal circuits, state appellate courts, and U.S. Supreme Court variations. Use when building TOC, TOA, compliance certificates, formatting briefs for filing, or when the user mentions word count calculation, FRAP 32 compliance, appellate brief assembly, or page numbering.

## Steps

1. Confirm the task matches this source: Generates appellate-filing-ready Tables of Contents, Tables of Authorities, and Certificates of Compliance under FRAP 32(g) and related rules. Produces defensible word-count calculations with transparent exclusions and a
2. Start with the upstream step: Brief text — final or near-final; label output "DRAFT" if still revising
3. Continue with: Forum/case metadata — court, circuit/state, case number, caption, brief type
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/appellate-formatting

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appellate-formatting
```
