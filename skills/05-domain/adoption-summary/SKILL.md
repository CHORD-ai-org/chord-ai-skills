---
name: adoption-summary
description: "Produces structured U.S. adoption-law summaries for litigation and client-facing use. Use when asked to summarize adoption law, draft pre-filing research briefs, create jurisdiction-specific issue memoranda, or prepare client education documents. Triggers: adoption summary, domestic adoption, intercountry adoption, Hague adoption, foster care adoption, TPR in adoption, stepparent/relative adoption, post-adoption rights."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/adoption-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/adoption-summary
---

# Adoption Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces structured U.S. adoption-law summaries for litigation and client-facing use. Use when asked to summarize adoption law, draft pre-filing research briefs, create jurisdiction-specific issue memoranda, or prepare client education documents. Triggers: adoption summary, domestic adoption, intercountry adoption, Hague adoption, foster care adoption, TPR in adoption, stepparent/relative adoption, post-adoption rights.

## Steps

1. Confirm the task matches this source: Produces structured U.S. adoption-law summaries for litigation and client-facing use. Use when asked to summarize adoption law, draft pre-filing research briefs, create jurisdiction-specific issue memoranda, or prepare c
2. Start with the upstream step: Identify jurisdiction (U.S. state + foreign country if intercountry).
3. Continue with: Confirm adoption type: domestic (agency/private/stepparent/relative), intercountry, foster care, or mixed.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/adoption-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/adoption-summary
```
