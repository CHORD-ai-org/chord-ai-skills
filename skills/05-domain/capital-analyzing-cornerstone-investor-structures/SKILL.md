---
name: capital-analyzing-cornerstone-investor-structures
description: "Evaluates cornerstone investment commitments with allocation guarantees, lock-up terms, and signaling value assessment. Use when structuring cornerstone tranches, analyzing anchor investors, or evaluating demand signals."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-cornerstone-investor-structures
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cornerstone-investor-structures
---

# Capital Analyzing Cornerstone Investor Structures

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates cornerstone investment commitments with allocation guarantees, lock-up terms, and signaling value assessment. Use when structuring cornerstone tranches, analyzing anchor investors, or evaluating demand signals.

## Steps

1. Confirm the task matches this source: Evaluates cornerstone investment commitments with allocation guarantees, lock-up terms, and signaling value assessment. Use when structuring cornerstone tranches, analyzing anchor investors, or evaluating demand signals.
2. Start with the upstream step: Structuring a cornerstone tranche for an IPO or follow-on offering and need to evaluate proposed commitment terms
3. Continue with: Assessing whether a prospective anchor investor's participation sends a credible demand signal to the broader book
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-cornerstone-investor-structures

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-cornerstone-investor-structures
```
