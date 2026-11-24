---
name: asbestos-abatement-plan
description: "Drafts an asbestos abatement plan compliant with OSHA 29 CFR 1926.1101 and EPA NESHAP 40 CFR 61 Subpart M. Extracts facility details from uploaded surveys and contractor documents to produce a regulatory filing and operational guide. Use when preparing pre-abatement regulatory submissions, contractor work plans, or facility owner compliance documentation for asbestos removal projects."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/asbestos-abatement-plan
source: https://github.com/casemark/skills/tree/main/skills/legal/asbestos-abatement-plan
---

# Asbestos Abatement Plan

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/asbestos-abatement-plan
```
