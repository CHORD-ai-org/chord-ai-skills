---
name: finance-analyzing-digital-lending-platforms
description: "Evaluates digital lending models with credit model assessment, funding structure, and regulatory analysis. Use when analyzing online lenders, evaluating credit models, or assessing lending platform risk."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-digital-lending-platforms
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-digital-lending-platforms
---

# Finance Analyzing Digital Lending Platforms

## Brief info

Evaluates digital lending models with credit model assessment, funding structure, and regulatory analysis. Use when analyzing online lenders, evaluating credit models, or assessing lending platform risk. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates digital lending models with credit model assessment, funding structure, and regulatory analysis. Use when analyzing online lenders, evaluating credit models, or assessing lending platform risk.

## Steps

1. Confirm the task matches this source: Evaluates digital lending models with credit model assessment, funding structure, and regulatory analysis. Use when analyzing online lenders, evaluating credit models, or assessing lending platform risk.
2. Start with the upstream step: Evaluating an online lending platform as a potential investment, acquisition target, or partnership
3. Continue with: Assessing credit model soundness for a marketplace lender, embedded lending product, or BNPL provider
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-digital-lending-platforms

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-digital-lending-platforms
```
