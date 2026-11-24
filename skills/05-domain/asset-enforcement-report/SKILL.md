---
name: asset-enforcement-report
description: "Generates a post-judgment asset and enforcement report synthesizing debtor asset investigations, exemption analysis, fraudulent transfer assessment, and prioritized collection strategies. Use when preparing judgment enforcement plans, debtor asset profiles, collection status reports, or post-trial recovery analysis."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/asset-enforcement-report
source: https://github.com/casemark/skills/tree/main/skills/legal/asset-enforcement-report
---

# Asset Enforcement Report

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Generates a post-judgment asset and enforcement report synthesizing debtor asset investigations, exemption analysis, fraudulent transfer assessment, and prioritized collection strategies. Use when preparing judgment enforcement plans, debtor asset profiles, collection status reports, or post-trial recovery analysis.

## Steps

1. Confirm the task matches this source: Generates a post-judgment asset and enforcement report synthesizing debtor asset investigations, exemption analysis, fraudulent transfer assessment, and prioritized collection strategies. Use when preparing judgment enfo
2. Start with the upstream step: Judgment documents — order text, amount (principal, interest, costs, fees), case caption, court, entry date
3. Continue with: Post-judgment discovery — debtor examination transcripts, interrogatory responses, document production, third-party subpoena returns
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/asset-enforcement-report

## Verify

```bash
python scripts/check_skills.py skills/05-domain/asset-enforcement-report
```
