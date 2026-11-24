---
name: capital-analyzing-activist-investor-vulnerabilities
description: "Evaluates corporate vulnerability to shareholder activism with governance assessment, valuation gaps, and operational improvement opportunities. Use when assessing activist risk, identifying vulnerabilities, or preparing defensive analyses."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-activist-investor-vulnerabilities
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-activist-investor-vulnerabilities
---

# Capital Analyzing Activist Investor Vulnerabilities

## Brief info

Evaluates corporate vulnerability to shareholder activism with governance assessment, valuation gaps, and operational improvement opportunities. Use when assessing activist risk, identifying vulnerabilities, or preparing defensive analyses. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates corporate vulnerability to shareholder activism with governance assessment, valuation gaps, and operational improvement opportunities. Use when assessing activist risk, identifying vulnerabilities, or preparing defensive analyses.

## Steps

1. Confirm the task matches this source: Evaluates corporate vulnerability to shareholder activism with governance assessment, valuation gaps, and operational improvement opportunities. Use when assessing activist risk, identifying vulnerabilities, or preparing
2. Start with the upstream step: Assessing a public company's exposure to activist campaigns before or after 13D/13F filings signal interest
3. Continue with: Preparing a board-level vulnerability review ahead of proxy season or annual meeting
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-activist-investor-vulnerabilities

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-activist-investor-vulnerabilities
```
