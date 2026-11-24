---
name: med-assessing-community-health-needs
description: "Conducts community health needs assessment with data collection, analysis, and priority identification. Use when assessing community health, prioritizing health needs, or planning health interventions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-assessing-community-health-needs
source: https://github.com/casemark/skills/tree/main/skills/med/assessing-community-health-needs
---

# Med Assessing Community Health Needs

## Brief info

Conducts community health needs assessment with data collection, analysis, and priority identification. Use when assessing community health, prioritizing health needs, or planning health interventions. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Conducts community health needs assessment with data collection, analysis, and priority identification. Use when assessing community health, prioritizing health needs, or planning health interventions.

## Steps

1. Confirm the task matches this source: Conducts community health needs assessment with data collection, analysis, and priority identification. Use when assessing community health, prioritizing health needs, or planning health interventions.
2. Start with the upstream step: Who is the lead entity — health department, nonprofit hospital, or collaborative? (Determines regulatory framework: PHAB vs. IRS 501(r)(3).)
3. Continue with: What is the geographic scope — county, multi-county region, city, tribal area, or hospital service area?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/assessing-community-health-needs

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-assessing-community-health-needs
```
