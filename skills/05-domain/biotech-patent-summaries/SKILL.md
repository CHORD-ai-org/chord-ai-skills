---
name: biotech-patent-summaries
description: "Summarizes biotech patent families and disputes into litigation-ready intelligence briefs. Trigger when the user provides patent applications, issued patents, PTAB filings, prosecution histories, licensing materials, or litigation documents in biotechnology domains and requests a summary, risk assessment, or FTO analysis."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/biotech-patent-summaries
source: https://github.com/casemark/skills/tree/main/skills/legal/biotech-patent-summaries
---

# Biotech Patent Summaries

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Summarizes biotech patent families and disputes into litigation-ready intelligence briefs. Trigger when the user provides patent applications, issued patents, PTAB filings, prosecution histories, licensing materials, or litigation documents in biotechnology domains and requests a summary, risk assessment, or FTO analysis.

## Steps

1. Confirm the task matches this source: Summarizes biotech patent families and disputes into litigation-ready intelligence briefs. Trigger when the user provides patent applications, issued patents, PTAB filings, prosecution histories, licensing materials, or 
2. Start with the upstream step: Collect inputs: patent corpus, dispute materials, parties/products map, jurisdiction scope, and clear objective (litigation exposure, licensing, design-around, or FTO).
3. Continue with: Run the core workflow below.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/biotech-patent-summaries

## Verify

```bash
python scripts/check_skills.py skills/05-domain/biotech-patent-summaries
```
