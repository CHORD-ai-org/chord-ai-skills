---
name: med-conducting-capacity-evaluations
description: "Assesses medical decision-making capacity with Appelbaum criteria documentation. Use when evaluating decision-making capacity, documenting capacity assessments, or determining informed consent ability."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-capacity-evaluations
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-capacity-evaluations
---

# Med Conducting Capacity Evaluations

## Brief info

Assesses medical decision-making capacity with Appelbaum criteria documentation. Use when evaluating decision-making capacity, documenting capacity assessments, or determining informed consent ability. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Assesses medical decision-making capacity with Appelbaum criteria documentation. Use when evaluating decision-making capacity, documenting capacity assessments, or determining informed consent ability.

## Steps

1. Confirm the task matches this source: Assesses medical decision-making capacity with Appelbaum criteria documentation. Use when evaluating decision-making capacity, documenting capacity assessments, or determining informed consent ability.
2. Start with the upstream step: What specific medical decision is at issue? (surgery consent, medication consent, discharge against medical advice, refusal of life-sustaining treatment, enrollment in research,...
3. Continue with: Who requested the capacity evaluation? (attending physician, nurse, patient advocate, ethics committee, family) — default: identify requesting party and trigger
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-capacity-evaluations

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-capacity-evaluations
```
