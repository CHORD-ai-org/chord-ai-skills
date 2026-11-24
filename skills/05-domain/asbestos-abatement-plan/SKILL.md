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

Use when the task matches this source: Drafts an asbestos abatement plan compliant with OSHA 29 CFR 1926.1101 and EPA NESHAP 40 CFR 61 Subpart M. Extracts facility details from uploaded surveys and contractor documents to produce a regulatory filing and operational guide. Use when preparing pre-abatement regulatory submissions, contractor work plans, or facility owner compliance documentation for asbestos removal projects.

## Steps

1. Confirm the task matches this source: Drafts an asbestos abatement plan compliant with OSHA 29 CFR 1926.1101 and EPA NESHAP 40 CFR 61 Subpart M. Extracts facility details from uploaded surveys and contractor documents to produce a regulatory filing and opera
2. Start with the upstream step: Asbestos survey report — inspector name/accreditation, survey date, all ACM locations with material type, condition, friability, mineral type, % content (PLM/TEM), quantities (S...
3. Continue with: Facility ID — legal entity, address, parcel/tax ID, county, owner/authorized rep, tenant info if applicable
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/asbestos-abatement-plan

## Verify

```bash
python scripts/check_skills.py skills/05-domain/asbestos-abatement-plan
```
