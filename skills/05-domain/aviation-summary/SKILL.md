---
name: aviation-summary
description: "Generates structured U.S. aviation-law summaries by synthesizing FAA, DOT, and TSA rules, treaties, and precedent into actionable legal analysis. Use when briefing on air traffic rights, aircraft operations, airworthiness, carrier liability, or incident/compliance exposure. Trigger: aviation law, FAA, DOT, TSA, 14 CFR, Part 121/125/135, Montreal Convention, Warsaw Convention, ICAO, route authority, code-sharing, slot allocation, accident liability."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/aviation-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/aviation-summary
---

# Aviation Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Generates structured U.S. aviation-law summaries by synthesizing FAA, DOT, and TSA rules, treaties, and precedent into actionable legal analysis. Use when briefing on air traffic rights, aircraft operations, airworthiness, carrier liability, or incident/compliance exposure. Trigger: aviation law, FAA, DOT, TSA, 14 CFR, Part 121/125/135, Montreal Convention, Warsaw Convention, ICAO, route authority, code-sharing, slot allocation, accident liability.

## Steps

1. Confirm the task matches this source: Generates structured U.S. aviation-law summaries by synthesizing FAA, DOT, and TSA rules, treaties, and precedent into actionable legal analysis. Use when briefing on air traffic rights, aircraft operations, airworthines
2. Start with the upstream step: Issue statement — legal question, party posture, desired depth, decision use (advisory, compliance memo, litigation prep).
3. Continue with: Jurisdiction — U.S. federal at minimum; add foreign states when international carriage is involved.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/aviation-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/aviation-summary
```
