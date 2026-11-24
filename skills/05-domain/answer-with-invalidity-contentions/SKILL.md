---
name: answer-with-invalidity-contentions
description: "Drafts a defendant's Answer with Invalidity Contentions responding to a U.S. patent infringement complaint. Covers FRCP 8(b) admissions/denials, affirmative defenses, and PLR 3-3 invalidity contentions with claim charts under 35 U.S.C. §§ 101, 102, 103, 112. Use when representing a defendant in the pleadings phase of federal patent litigation who must respond to an infringement suit and assert prior art, anticipation, obviousness, or § 112 defenses."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/answer-with-invalidity-contentions
source: https://github.com/casemark/skills/tree/main/skills/legal/answer-with-invalidity-contentions
---

# Answer With Invalidity Contentions

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a defendant's Answer with Invalidity Contentions responding to a U.S. patent infringement complaint. Covers FRCP 8(b) admissions/denials, affirmative defenses, and PLR 3-3 invalidity contentions with claim charts under 35 U.S.C. §§ 101, 102, 103, 112. Use when representing a defendant in the pleadings phase of federal patent litigation who must respond to an infringement suit and assert prior art, anticipation, obviousness, or § 112 defenses.

## Steps

1. Confirm the task matches this source: Drafts a defendant's Answer with Invalidity Contentions responding to a U.S. patent infringement complaint. Covers FRCP 8(b) admissions/denials, affirmative defenses, and PLR 3-3 invalidity contentions with claim charts 
2. Start with the upstream step: Complaint — all numbered paragraphs requiring response
3. Continue with: Asserted patent(s) — specification, claims, and prosecution history
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/answer-with-invalidity-contentions

## Verify

```bash
python scripts/check_skills.py skills/05-domain/answer-with-invalidity-contentions
```
