---
name: client-advisory-summary
description: "Produces client-ready U.S. regulatory advisory summaries translating legal developments into actionable impacts with effective-date tracking and Bluebook citations. Trigger when the user requests a client advisory, regulatory update, compliance memo, law-change summary, or industry alert."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/client-advisory-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/client-advisory-summary
---

# Client Advisory Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces client-ready U.S. regulatory advisory summaries translating legal developments into actionable impacts with effective-date tracking and Bluebook citations. Trigger when the user requests a client advisory, regulatory update, compliance memo, law-change summary, or industry alert.

## Steps

1. Confirm the task matches this source: Produces client-ready U.S. regulatory advisory summaries translating legal developments into actionable impacts with effective-date tracking and Bluebook citations. Trigger when the user requests a client advisory, regul
2. Start with the upstream step: Client profile — industry, products/services, geography, size/thresholds.
3. Continue with: Jurisdiction & scope — federal, state, agency, or court.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/client-advisory-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/client-advisory-summary
```
