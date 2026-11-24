---
name: capital-analyzing-credit-agreement-terms
description: "Evaluates credit agreement provisions with borrower flexibility, lender protections, and documentation comparison analysis. Use when reviewing credit agreements, analyzing doc terms, or comparing loan documentation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-agreement-terms
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-agreement-terms
---

# Capital Analyzing Credit Agreement Terms

## Brief info

Evaluates credit agreement provisions with borrower flexibility, lender protections, and documentation comparison analysis. Use when reviewing credit agreements, analyzing doc terms, or comparing loan documentation. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates credit agreement provisions with borrower flexibility, lender protections, and documentation comparison analysis. Use when reviewing credit agreements, analyzing doc terms, or comparing loan documentation.

## Steps

1. Confirm the task matches this source: Evaluates credit agreement provisions with borrower flexibility, lender protections, and documentation comparison analysis. Use when reviewing credit agreements, analyzing doc terms, or comparing loan documentation.
2. Start with the upstream step: Reviewing a new credit agreement or amendment for key risk provisions
3. Continue with: Comparing a proposed credit agreement against a precedent deal or market-standard terms (e.g., LSTA model credit agreement)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-agreement-terms

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-agreement-terms
```
