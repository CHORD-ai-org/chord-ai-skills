---
name: capital-analyzing-customer-cohort-economics
description: "Deconstructs customer cohort behavior with retention curves, LTV progression, and vintage-over-vintage comparison analysis. Use when analyzing cohort data, assessing customer quality, or modeling lifetime value trajectories."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-customer-cohort-economics
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-customer-cohort-economics
---

# Capital Analyzing Customer Cohort Economics

## Brief info

Deconstructs customer cohort behavior with retention curves, LTV progression, and vintage-over-vintage comparison analysis. Use when analyzing cohort data, assessing customer quality, or modeling lifetime value trajectories. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Deconstructs customer cohort behavior with retention curves, LTV progression, and vintage-over-vintage comparison analysis. Use when analyzing cohort data, assessing customer quality, or modeling lifetime value trajectories.

## Steps

1. Confirm the task matches this source: Deconstructs customer cohort behavior with retention curves, LTV progression, and vintage-over-vintage comparison analysis. Use when analyzing cohort data, assessing customer quality, or modeling lifetime value trajector
2. Start with the upstream step: Evaluating a SaaS or subscription company's customer quality during investment diligence
3. Continue with: Assessing whether net revenue retention is improving, stable, or deteriorating across vintages
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-customer-cohort-economics

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-customer-cohort-economics
```
