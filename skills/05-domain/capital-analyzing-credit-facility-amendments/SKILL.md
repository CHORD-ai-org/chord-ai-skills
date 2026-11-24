---
name: capital-analyzing-credit-facility-amendments
description: "Evaluates amendment and waiver requests with consent requirements, fee structures, and modified term impact analysis. Use when analyzing amendments, structuring consent solicitations, or evaluating covenant relief requests."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-facility-amendments
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-facility-amendments
---

# Capital Analyzing Credit Facility Amendments

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates amendment and waiver requests with consent requirements, fee structures, and modified term impact analysis. Use when analyzing amendments, structuring consent solicitations, or evaluating covenant relief requests.

## Steps

1. Confirm the task matches this source: Evaluates amendment and waiver requests with consent requirements, fee structures, and modified term impact analysis. Use when analyzing amendments, structuring consent solicitations, or evaluating covenant relief reques
2. Start with the upstream step: Borrower or sponsor requests a covenant waiver, amendment, or consent under an existing credit agreement
3. Continue with: Evaluating whether a proposed amendment requires Required Lender, Super-Majority, or unanimous lender consent
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-facility-amendments

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-facility-amendments
```
