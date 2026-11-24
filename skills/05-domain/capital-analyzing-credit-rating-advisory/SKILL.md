---
name: capital-analyzing-credit-rating-advisory
description: "Prepares credit rating agency presentations with methodology alignment, peer positioning, and target rating analysis. Use when advising on credit ratings, preparing rating agency meetings, or analyzing rating methodology impact."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-rating-advisory
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-rating-advisory
---

# Capital Analyzing Credit Rating Advisory

## Brief info

Prepares credit rating agency presentations with methodology alignment, peer positioning, and target rating analysis. Use when advising on credit ratings, preparing rating agency meetings, or analyzing rating methodology impact. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Prepares credit rating agency presentations with methodology alignment, peer positioning, and target rating analysis. Use when advising on credit ratings, preparing rating agency meetings, or analyzing rating methodology impact.

## Steps

1. Confirm the task matches this source: Prepares credit rating agency presentations with methodology alignment, peer positioning, and target rating analysis. Use when advising on credit ratings, preparing rating agency meetings, or analyzing rating methodology
2. Start with the upstream step: Preparing for an initial or annual rating agency meeting (S&P, Moody's, Fitch, KBRA, DBRS)
3. Continue with: Advising an issuer on achieving or maintaining a target credit rating
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-credit-rating-advisory

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-credit-rating-advisory
```
