---
name: med-assessing-suicide-risk
description: ">"
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-assessing-suicide-risk
source: https://github.com/casemark/skills/tree/main/skills/med/assessing-suicide-risk
---

# Med Assessing Suicide Risk

## Brief info

> Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: >

## Steps

1. Confirm the task matches this source: >
2. Start with the upstream step: Draft only. Every output is a draft for a qualified clinician (or, in review mode, for the reviewer and the clinician). It supports and never replaces clinical judgment. Never w...
3. Continue with: Source-review gate. Do not call a screen, note or plan missing until every supplied document has been opened and searched, including scanned and oddly named files. Classify each...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/assessing-suicide-risk

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-assessing-suicide-risk
```
