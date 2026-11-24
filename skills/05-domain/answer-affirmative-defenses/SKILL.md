---
name: answer-affirmative-defenses
description: "Drafts U.S. civil litigation Answers with paragraph-by-paragraph admissions/denials, affirmative defenses, and counterclaim triage. Trigger when user needs a responsive pleading to a complaint, mentions affirmative defenses, admit/deny responses, Rule 8, or insufficient knowledge responses."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/answer-affirmative-defenses
source: https://github.com/casemark/skills/tree/main/skills/legal/answer-affirmative-defenses
---

# Answer Affirmative Defenses

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. civil litigation Answers with paragraph-by-paragraph admissions/denials, affirmative defenses, and counterclaim triage. Trigger when user needs a responsive pleading to a complaint, mentions affirmative defenses, admit/deny responses, Rule 8, or insufficient knowledge responses.

## Steps

1. Confirm the task matches this source: Drafts U.S. civil litigation Answers with paragraph-by-paragraph admissions/denials, affirmative defenses, and counterclaim triage. Trigger when user needs a responsive pleading to a complaint, mentions affirmative defen
2. Start with the upstream step: Complaint — filed version with numbered paragraphs and caption
3. Continue with: Service data — date, method, proof of service
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/answer-affirmative-defenses

## Verify

```bash
python scripts/check_skills.py skills/05-domain/answer-affirmative-defenses
```
