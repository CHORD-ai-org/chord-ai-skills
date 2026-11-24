---
name: med-classifying-imaging-findings
description: "Applies standardized classification systems (BI-RADS, LI-RADS, TI-RADS, Lung-RADS, PI-RADS) to imaging findings. Use when categorizing imaging findings, applying RADS classifications, or determining follow-up recommendations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-classifying-imaging-findings
source: https://github.com/casemark/skills/tree/main/skills/med/classifying-imaging-findings
---

# Med Classifying Imaging Findings

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Applies standardized classification systems (BI-RADS, LI-RADS, TI-RADS, Lung-RADS, PI-RADS) to imaging findings. Use when categorizing imaging findings, applying RADS classifications, or determining follow-up recommendations.

## Steps

1. Confirm the task matches this source: Applies standardized classification systems (BI-RADS, LI-RADS, TI-RADS, Lung-RADS, PI-RADS) to imaging findings. Use when categorizing imaging findings, applying RADS classifications, or determining follow-up recommendat
2. Start with the upstream step: Which classification system is required? (Default: Determine from organ system and modality)
3. Continue with: What imaging modality was used? (Default: Identify — CT, MRI, US, mammography, PET/CT)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/classifying-imaging-findings

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-classifying-imaging-findings
```
