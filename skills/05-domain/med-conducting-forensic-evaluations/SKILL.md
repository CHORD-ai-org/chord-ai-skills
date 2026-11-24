---
name: med-conducting-forensic-evaluations
description: "Structures forensic psychiatric evaluations for competency, insanity, and civil commitment proceedings. Use when performing forensic evaluations, assessing competency, or documenting forensic opinions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-forensic-evaluations
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-forensic-evaluations
---

# Med Conducting Forensic Evaluations

## Brief info

Structures forensic psychiatric evaluations for competency, insanity, and civil commitment proceedings. Use when performing forensic evaluations, assessing competency, or documenting forensic opinions. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures forensic psychiatric evaluations for competency, insanity, and civil commitment proceedings. Use when performing forensic evaluations, assessing competency, or documenting forensic opinions.

## Steps

1. Confirm the task matches this source: Structures forensic psychiatric evaluations for competency, insanity, and civil commitment proceedings. Use when performing forensic evaluations, assessing competency, or documenting forensic opinions.
2. Start with the upstream step: What is the specific legal question? (competency to stand trial, criminal responsibility/insanity, civil commitment, personal injury, disability, child custody, testamentary cap...
3. Continue with: Who retained the evaluator? (defense, prosecution, court, plaintiff, defendant, guardian ad litem) — default: identify retaining party
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-forensic-evaluations

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-forensic-evaluations
```
