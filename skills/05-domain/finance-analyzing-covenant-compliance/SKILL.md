---
name: finance-analyzing-covenant-compliance
description: "Reviews financial covenant compliance calculations with cure provisions and default trigger analysis. Use when checking covenant compliance, calculating coverage ratios, or evaluating covenant headroom. Takes stressed-case and surveillance reviews of headroom, cure rights and default triggers for a lender, investor or trading view; the borrower's periodic compliance certificate goes to managing-debt-covenant-compliance."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-covenant-compliance
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-covenant-compliance
---

# Finance Analyzing Covenant Compliance

## Brief info

Reviews financial covenant compliance calculations with cure provisions and default trigger analysis. Use when checking covenant compliance, calculating coverage ratios, or evaluating covenant headroom. Takes stressed-case and surveillance reviews of headroom, cure rights and default triggers for a lender, investor or trading view; the borrower's periodic compliance certificate goes to managing-debt-covenant-compliance. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Reviews financial covenant compliance calculations with cure provisions and default trigger analysis. Use when checking covenant compliance, calculating coverage ratios, or evaluating covenant headroom. Takes stressed-case and surveillance reviews of headroom, cure rights and default triggers for a lender, investor or trading view; the borrower's periodic compliance certificate goes to managing-debt-covenant-compliance.

## Steps

1. Confirm the task matches this source: Reviews financial covenant compliance calculations with cure provisions and default trigger analysis. Use when checking covenant compliance, calculating coverage ratios, or evaluating covenant headroom. Takes stressed-ca
2. Start with the upstream step: Evaluating whether a bond issuer or borrower is in compliance with financial maintenance covenants (leverage ratio, interest coverage, fixed charge coverage, minimum net worth, ...
3. Continue with: Calculating covenant headroom to assess proximity to a potential default trigger
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-covenant-compliance

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-covenant-compliance
```
