---
name: cbp-binding-ruling
description: "Drafts U.S. Customs and Border Protection binding ruling requests under 19 CFR Part 177 for tariff classification, valuation, origin, and marking determinations. Trigger when input mentions \"binding ruling,\" \"CBP ruling request,\" \"19 CFR Part 177,\" \"classification request,\" \"HTSUS analysis,\" \"transaction value,\" \"country of origin,\" or \"marking for import."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/cbp-binding-ruling
source: https://github.com/casemark/skills/tree/main/skills/legal/cbp-binding-ruling
---

# Cbp Binding Ruling

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. Customs and Border Protection binding ruling requests under 19 CFR Part 177 for tariff classification, valuation, origin, and marking determinations. Trigger when input mentions \"binding ruling,\" \"CBP ruling request,\" \"19 CFR Part 177,\" \"classification request,\" \"HTSUS analysis,\" \"transaction value,\" \"country of origin,\" or \"marking for import.

## Steps

1. Confirm the task matches this source: Drafts U.S. Customs and Border Protection binding ruling requests under 19 CFR Part 177 for tariff classification, valuation, origin, and marking determinations. Trigger when input mentions \"binding ruling,\" \"CBP ruli
2. Start with the upstream step: Confirm the matter is a U.S. import treatment determination appropriate for 19 CFR Part 177.
3. Continue with: Identify requesting party's role and authority (importer / prospective importer / foreign manufacturer / authorized representative).
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/cbp-binding-ruling

## Verify

```bash
python scripts/check_skills.py skills/05-domain/cbp-binding-ruling
```
