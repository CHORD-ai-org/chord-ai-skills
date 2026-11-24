---
name: annual-report-charity-bureau
description: "Generates a cross-referenced U.S. nonprofit annual filing package for state charity-bureau registration. Produces Full Compliance Package, Form-Field Mode, or Executive Briefing with source citations, disclosure cross-checks, and filing instructions. Trigger when the user drafts annual report submissions, renewal packets, penalty-of-perjury certifications, or charity bureau filings. Also trigger on Form RRF-1, CHAR500, BCO-10, nonprofit annual report, charity registration renewal, or fundraiser disclosure attachments."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/annual-report-charity-bureau
source: https://github.com/casemark/skills/tree/main/skills/legal/annual-report-charity-bureau
---

# Annual Report Charity Bureau

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/annual-report-charity-bureau
```
