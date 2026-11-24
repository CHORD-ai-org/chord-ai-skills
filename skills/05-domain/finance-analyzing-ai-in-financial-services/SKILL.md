---
name: finance-analyzing-ai-in-financial-services
description: "Evaluates AI/ML applications in financial services with model governance, bias assessment, and regulatory considerations. Use when analyzing AI in finance, evaluating ML models, or assessing AI governance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-ai-in-financial-services
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-ai-in-financial-services
---

# Finance Analyzing Ai In Financial Services

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates AI/ML applications in financial services with model governance, bias assessment, and regulatory considerations. Use when analyzing AI in finance, evaluating ML models, or assessing AI governance.

## Steps

1. Confirm the task matches this source: Evaluates AI/ML applications in financial services with model governance, bias assessment, and regulatory considerations. Use when analyzing AI in finance, evaluating ML models, or assessing AI governance.
2. Start with the upstream step: Evaluating an AI/ML model deployed or proposed for credit decisioning, fraud detection, AML/KYC, trading, or customer-facing automation
3. Continue with: Assessing model risk management (MRM) posture against SR 11-7, OCC 2011-12, or equivalent guidance [VERIFY jurisdiction-specific MRM guidance]
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-ai-in-financial-services

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-ai-in-financial-services
```
