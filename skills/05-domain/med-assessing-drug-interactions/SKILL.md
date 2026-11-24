---
name: med-assessing-drug-interactions
description: "Identifies clinically significant drug-drug, drug-food, and drug-disease interactions with severity grading and management recommendations. Use when checking drug interactions, evaluating polypharmacy risks, or managing medication combinations."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-assessing-drug-interactions
source: https://github.com/casemark/skills/tree/main/skills/med/assessing-drug-interactions
---

# Med Assessing Drug Interactions

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Identifies clinically significant drug-drug, drug-food, and drug-disease interactions with severity grading and management recommendations. Use when checking drug interactions, evaluating polypharmacy risks, or managing medication combinations.

## Steps

1. Confirm the task matches this source: Identifies clinically significant drug-drug, drug-food, and drug-disease interactions with severity grading and management recommendations. Use when checking drug interactions, evaluating polypharmacy risks, or managing 
2. Start with the upstream step: What is the complete active medication list, including OTC, herbals, and supplements? (Default: request MAR or pharmacy profile)
3. Continue with: What is the patient's age, sex, weight, and relevant organ function (hepatic/renal)? (Default: assume normal organ function if unspecified, flag as [VERIFY])
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/assessing-drug-interactions

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-assessing-drug-interactions
```
