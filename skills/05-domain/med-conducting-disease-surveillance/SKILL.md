---
name: med-conducting-disease-surveillance
description: "Structures disease surveillance systems with case definitions, reporting requirements, and trend analysis. Use when monitoring disease trends, managing surveillance data, or analyzing reportable conditions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-disease-surveillance
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-disease-surveillance
---

# Med Conducting Disease Surveillance

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures disease surveillance systems with case definitions, reporting requirements, and trend analysis. Use when monitoring disease trends, managing surveillance data, or analyzing reportable conditions.

## Steps

1. Confirm the task matches this source: Structures disease surveillance systems with case definitions, reporting requirements, and trend analysis. Use when monitoring disease trends, managing surveillance data, or analyzing reportable conditions.
2. Start with the upstream step: What condition(s) or syndrome(s) are under surveillance? List ICD-10-CM codes if available.
3. Continue with: Is this passive surveillance (provider-reported), active surveillance (health department–initiated), sentinel surveillance, or syndromic surveillance?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-disease-surveillance

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-disease-surveillance
```
