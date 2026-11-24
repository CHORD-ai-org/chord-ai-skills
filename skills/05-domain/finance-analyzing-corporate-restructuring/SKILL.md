---
name: finance-analyzing-corporate-restructuring
description: "Evaluates restructuring alternatives with debt-for-equity analysis, 363 sale considerations, and recovery analysis. Use when analyzing restructurings, evaluating Chapter 11 options, or modeling recovery scenarios."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-corporate-restructuring
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-corporate-restructuring
---

# Finance Analyzing Corporate Restructuring

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates restructuring alternatives with debt-for-equity analysis, 363 sale considerations, and recovery analysis. Use when analyzing restructurings, evaluating Chapter 11 options, or modeling recovery scenarios.

## Steps

1. Confirm the task matches this source: Evaluates restructuring alternatives with debt-for-equity analysis, 363 sale considerations, and recovery analysis. Use when analyzing restructurings, evaluating Chapter 11 options, or modeling recovery scenarios.
2. Start with the upstream step: Analyzing a distressed company's restructuring options (out-of-court workout vs. Chapter 11 vs. Chapter 7)
3. Continue with: Modeling recovery waterfalls for secured and unsecured creditors
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-corporate-restructuring

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-corporate-restructuring
```
