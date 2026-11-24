---
name: capital-analyzing-cross-border-tax-structuring
description: "Evaluates international tax structures with treaty networks, withholding rates, and permanent establishment risk analysis. Use when structuring cross-border tax, analyzing treaty benefits, or evaluating tax-efficient structuring."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-border-tax-structuring
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-border-tax-structuring
---

# Capital Analyzing Cross Border Tax Structuring

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates international tax structures with treaty networks, withholding rates, and permanent establishment risk analysis. Use when structuring cross-border tax, analyzing treaty benefits, or evaluating tax-efficient structuring.

## Steps

1. Confirm the task matches this source: Evaluates international tax structures with treaty networks, withholding rates, and permanent establishment risk analysis. Use when structuring cross-border tax, analyzing treaty benefits, or evaluating tax-efficient str
2. Start with the upstream step: Structuring an investment or operating entity across two or more tax jurisdictions
3. Continue with: Evaluating whether an existing holding structure captures available treaty benefits
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cross-border-tax-structuring

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-cross-border-tax-structuring
```
