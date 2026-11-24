---
name: finance-analyzing-biodiversity-risk
description: "Structures biodiversity risk assessment with nature-related dependency mapping and TNFD alignment. Use when analyzing biodiversity risk, mapping nature dependencies, or implementing TNFD disclosure."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-biodiversity-risk
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-biodiversity-risk
---

# Finance Analyzing Biodiversity Risk

## Brief info

Structures biodiversity risk assessment with nature-related dependency mapping and TNFD alignment. Use when analyzing biodiversity risk, mapping nature dependencies, or implementing TNFD disclosure. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures biodiversity risk assessment with nature-related dependency mapping and TNFD alignment. Use when analyzing biodiversity risk, mapping nature dependencies, or implementing TNFD disclosure.

## Steps

1. Confirm the task matches this source: Structures biodiversity risk assessment with nature-related dependency mapping and TNFD alignment. Use when analyzing biodiversity risk, mapping nature dependencies, or implementing TNFD disclosure.
2. Start with the upstream step: Evaluating a portfolio company or asset for nature-related financial risks (physical, transition, systemic)
3. Continue with: Mapping dependencies and impacts on ecosystem services for TNFD-aligned disclosure
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-biodiversity-risk

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-biodiversity-risk
```
