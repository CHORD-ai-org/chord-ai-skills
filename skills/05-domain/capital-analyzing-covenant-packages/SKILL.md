---
name: capital-analyzing-covenant-packages
description: "Evaluates financial and incurrence covenant packages with headroom analysis, definition review, and covenant-lite comparison. Use when analyzing loan covenants, negotiating covenant levels, or assessing borrower flexibility."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-covenant-packages
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-covenant-packages
---

# Capital Analyzing Covenant Packages

## Brief info

Evaluates financial and incurrence covenant packages with headroom analysis, definition review, and covenant-lite comparison. Use when analyzing loan covenants, negotiating covenant levels, or assessing borrower flexibility. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates financial and incurrence covenant packages with headroom analysis, definition review, and covenant-lite comparison. Use when analyzing loan covenants, negotiating covenant levels, or assessing borrower flexibility.

## Steps

1. Confirm the task matches this source: Evaluates financial and incurrence covenant packages with headroom analysis, definition review, and covenant-lite comparison. Use when analyzing loan covenants, negotiating covenant levels, or assessing borrower flexibil
2. Start with the upstream step: Reviewing a credit agreement or term sheet to assess borrower flexibility and lender protections
3. Continue with: Comparing covenant packages across competing deal proposals or precedent transactions
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-covenant-packages

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-covenant-packages
```
