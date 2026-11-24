---
name: med-conducting-false-claims-analysis
description: ">"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-false-claims-analysis
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-false-claims-analysis
---

# Med Conducting False Claims Analysis

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >

## Steps

1. Confirm the task matches this source: >
2. Start with the upstream step: Draft only. Nothing is filed, refunded, disclosed or sent to a government agency or contractor by this skill. Every output is labeled a draft for the compliance officer and coun...
3. Continue with: Source-review gate. Do not call a claim, date or document missing until every supplied file has been opened and searched, with OCR or extraction tried. Classify each gap as an *...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-false-claims-analysis

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-false-claims-analysis
```
