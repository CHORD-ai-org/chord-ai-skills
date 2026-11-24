---
name: grill-me
description: Ask one question at a time to test a user decision without answering for the user.
category: 06-interaction
status: blocked
inputs: one user decision, question budget
outputs: one question at a time, then a decision record
fails_when: questioning becomes interrogation, or the agent decides for the user
verify: python scripts/check_skills.py skills/06-interaction/grill-me
source: from the start.md
---

# Grill Me

## Brief info

Ask one question at a time to test a user decision without answering for the user. Input: one user decision, question budget. Output: one question at a time, then a decision record. Caveat: questioning becomes interrogation, or the agent decides for the user.


Ask one question at a time. Do not answer for the user.

## Trigger

Use when the user says "grill me", "challenge this decision", or presents a decision they want tested.

## Steps

1. Restate the decision in one sentence.
2. Ask the question most likely to change that decision.
3. Stop after one question. Wait for the answer.
4. Repeat until the user says stop or the question budget runs out.
5. Write the record: decision, questions asked, answers, unchanged or changed.

## Hard rules

- Never give a recommendation.
- Never stack questions.
- Never reuse a question already answered.
- If asked for the answer, say: "I can keep grilling, or hand this back to you."

## Why blocked

This skill depends on Thylas' customizable persistent session state. Without it, the question history lives in the transcript and is lost across sessions. Enable only after Thylas can persist state for this skill.

## Source notes

From `from the start.md`, diary entry 2026-11-23, category 6. The diary names grill-me as a human–agent interaction skill made useful by Thylas' customizable persistent session state.

## Verify

```bash
python scripts/check_skills.py skills/06-interaction/grill-me
```
