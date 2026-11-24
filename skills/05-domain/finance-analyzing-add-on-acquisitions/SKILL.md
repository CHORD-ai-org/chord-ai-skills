---
name: finance-analyzing-add-on-acquisitions
description: "Evaluates platform add-on opportunities with strategic fit, synergy potential, and return contribution. Use when analyzing add-on M&A, evaluating bolt-on targets, or building platform acquisition strategies."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/finance-analyzing-add-on-acquisitions
source: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-add-on-acquisitions
---

# Finance Analyzing Add On Acquisitions

## Brief info

Evaluates platform add-on opportunities with strategic fit, synergy potential, and return contribution. Use when analyzing add-on M&A, evaluating bolt-on targets, or building platform acquisition strategies. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates platform add-on opportunities with strategic fit, synergy potential, and return contribution. Use when analyzing add-on M&A, evaluating bolt-on targets, or building platform acquisition strategies.

## Steps

1. Confirm the task matches this source: Evaluates platform add-on opportunities with strategic fit, synergy potential, and return contribution. Use when analyzing add-on M&A, evaluating bolt-on targets, or building platform acquisition strategies.
2. Start with the upstream step: Evaluating a specific bolt-on target against an existing platform company
3. Continue with: Screening multiple add-on candidates to prioritize pipeline
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: finance. Upstream: https://github.com/casemark/skills/tree/main/skills/finance/analyzing-add-on-acquisitions

## Verify

```bash
python scripts/check_skills.py skills/05-domain/finance-analyzing-add-on-acquisitions
```
