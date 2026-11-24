---
name: capital-analyzing-convertible-instrument-terms
description: "Evaluates SAFE, convertible note, and KISS structures with conversion mechanics, caps, discounts, and MFN provisions. Use when analyzing convertible instruments, comparing SAFE vs note terms, or modeling conversion scenarios."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-convertible-instrument-terms
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-convertible-instrument-terms
---

# Capital Analyzing Convertible Instrument Terms

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates SAFE, convertible note, and KISS structures with conversion mechanics, caps, discounts, and MFN provisions. Use when analyzing convertible instruments, comparing SAFE vs note terms, or modeling conversion scenarios.

## Steps

1. Confirm the task matches this source: Evaluates SAFE, convertible note, and KISS structures with conversion mechanics, caps, discounts, and MFN provisions. Use when analyzing convertible instruments, comparing SAFE vs note terms, or modeling conversion scena
2. Start with the upstream step: Reviewing a SAFE, convertible note, or KISS before a founder signs or an investor commits
3. Continue with: Comparing multiple convertible instruments across a cap table to assess aggregate dilution
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-convertible-instrument-terms

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-convertible-instrument-terms
```
