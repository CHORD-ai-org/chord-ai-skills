---
name: med-auditing-coding-accuracy
description: "Reviews coded encounters for accuracy using OIG compliance guidelines and CMS documentation requirements. Use when auditing medical codes, reviewing coding accuracy, or conducting compliance audits."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-auditing-coding-accuracy
source: https://github.com/casemark/skills/tree/main/skills/med/auditing-coding-accuracy
---

# Med Auditing Coding Accuracy

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Reviews coded encounters for accuracy using OIG compliance guidelines and CMS documentation requirements. Use when auditing medical codes, reviewing coding accuracy, or conducting compliance audits.

## Steps

1. Confirm the task matches this source: Reviews coded encounters for accuracy using OIG compliance guidelines and CMS documentation requirements. Use when auditing medical codes, reviewing coding accuracy, or conducting compliance audits.
2. Start with the upstream step: What is the audit scope? (prospective pre-bill, retrospective post-payment, focused, or random)
3. Continue with: Which service lines or provider specialties are included?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/auditing-coding-accuracy

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-auditing-coding-accuracy
```
