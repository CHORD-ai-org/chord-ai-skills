---
name: finance-analyzing-deal-financing-alternatives
description: "Compares financing alternatives including debt, equity, convertibles, and hybrid instruments for transactions. Use when evaluating financing options, comparing capital structure alternatives, or optimizing deal funding."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-deal-financing-alternatives
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-deal-financing-alternatives
---

# Finance Analyzing Deal Financing Alternatives

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Compares financing alternatives including debt, equity, convertibles, and hybrid instruments for transactions. Use when evaluating financing options, comparing capital structure alternatives, or optimizing deal funding.

## Steps

1. Confirm the task matches this source: Compares financing alternatives including debt, equity, convertibles, and hybrid instruments for transactions. Use when evaluating financing options, comparing capital structure alternatives, or optimizing deal funding.
2. Start with the upstream step: Evaluating how to fund an M&A transaction, leveraged buyout, or recapitalization
3. Continue with: Comparing debt vs. equity vs. hybrid instruments for a specific deal
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-deal-financing-alternatives

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-deal-financing-alternatives
```
