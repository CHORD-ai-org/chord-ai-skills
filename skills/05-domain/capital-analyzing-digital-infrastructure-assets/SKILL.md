---
name: capital-analyzing-digital-infrastructure-assets
description: "Evaluates data centers, fiber networks, and tower assets with capacity analysis, tenant credit, and technology obsolescence risk. Use when analyzing digital infrastructure, evaluating tower portfolios, or assessing data center investments."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-digital-infrastructure-assets
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-digital-infrastructure-assets
---

# Capital Analyzing Digital Infrastructure Assets

## Brief info

Evaluates data centers, fiber networks, and tower assets with capacity analysis, tenant credit, and technology obsolescence risk. Use when analyzing digital infrastructure, evaluating tower portfolios, or assessing data center investments. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates data centers, fiber networks, and tower assets with capacity analysis, tenant credit, and technology obsolescence risk. Use when analyzing digital infrastructure, evaluating tower portfolios, or assessing data center investments.

## Steps

1. Confirm the task matches this source: Evaluates data centers, fiber networks, and tower assets with capacity analysis, tenant credit, and technology obsolescence risk. Use when analyzing digital infrastructure, evaluating tower portfolios, or assessing data 
2. Start with the upstream step: Evaluating a data center acquisition or development financing (single-site or portfolio)
3. Continue with: Analyzing a wireless tower portfolio for purchase, sale, or lease-up valuation
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-digital-infrastructure-assets

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-digital-infrastructure-assets
```
