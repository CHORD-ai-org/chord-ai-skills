---
name: charity-annual-report
description: "Drafts filing-ready Annual Reports for State Charity Bureaus with certified financials, governance disclosures, and required attachments. Extracts organizational, financial, and programmatic data from uploaded documents, researches state-specific filing requirements, and produces a penalty-of-perjury-certified report. Use when drafting charity bureau annual reports, nonprofit compliance filings, charitable solicitation renewals, or state charity registration renewals."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/charity-annual-report
source: https://github.com/casemark/skills/tree/main/skills/legal/charity-annual-report
---

# Charity Annual Report

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/charity-annual-report
```
