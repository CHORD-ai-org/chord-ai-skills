---
name: answer-to-harassment-complaint
description: "Drafts a defendant employer's Answer to a workplace harassment complaint. Responds paragraph-by-paragraph to allegations, asserts Faragher-Ellerth and other affirmative defenses, and follows federal/state civil procedure rules. Use when defending employers at the pleadings phase against Title VII, state FEHA, or other employment harassment claims."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/answer-to-harassment-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/answer-to-harassment-complaint
---

# Answer To Harassment Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a defendant employer's Answer to a workplace harassment complaint. Responds paragraph-by-paragraph to allegations, asserts Faragher-Ellerth and other affirmative defenses, and follows federal/state civil procedure rules. Use when defending employers at the pleadings phase against Title VII, state FEHA, or other employment harassment claims.

## Steps

1. Confirm the task matches this source: Drafts a defendant employer's Answer to a workplace harassment complaint. Responds paragraph-by-paragraph to allegations, asserts Faragher-Ellerth and other affirmative defenses, and follows federal/state civil procedure
2. Start with the upstream step: Complaint — all numbered paragraphs, exhibits, referenced documents
3. Continue with: Anti-harassment policies — written policy, training records, complaint procedures, acknowledgment forms
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/answer-to-harassment-complaint

## Verify

```bash
python scripts/check_skills.py skills/05-domain/answer-to-harassment-complaint
```
