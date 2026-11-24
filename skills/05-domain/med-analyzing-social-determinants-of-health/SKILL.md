---
name: med-analyzing-social-determinants-of-health
description: "Maps social determinants affecting health outcomes with intervention strategy development. Use when analyzing SDOH, mapping community resources, or designing social health interventions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-analyzing-social-determinants-of-health
source: https://github.com/casemark/skills/tree/main/skills/med/analyzing-social-determinants-of-health
---

# Med Analyzing Social Determinants Of Health

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Maps social determinants affecting health outcomes with intervention strategy development. Use when analyzing SDOH, mapping community resources, or designing social health interventions.

## Steps

1. Confirm the task matches this source: Maps social determinants affecting health outcomes with intervention strategy development. Use when analyzing SDOH, mapping community resources, or designing social health interventions.
2. Start with the upstream step: What is the analytic purpose — community health assessment, grant application, intervention design, policy brief, or health equity evaluation?
3. Continue with: What is the geographic unit of analysis — state, county, census tract, zip code, or neighborhood?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/analyzing-social-determinants-of-health

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-analyzing-social-determinants-of-health
```
