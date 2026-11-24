---
name: client-advisory
description: "Drafts client advisory memoranda translating legal developments into actionable guidance with impact analysis, Bluebook citations, and compliance recommendations. Use when preparing client alerts, regulatory updates, legal bulletins, or proactive advisory summaries."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/client-advisory
source: https://github.com/casemark/skills/tree/main/skills/legal/client-advisory
---

# Client Advisory

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts client advisory memoranda translating legal developments into actionable guidance with impact analysis, Bluebook citations, and compliance recommendations. Use when preparing client alerts, regulatory updates, legal bulletins, or proactive advisory summaries.

## Steps

1. Confirm the task matches this source: Drafts client advisory memoranda translating legal developments into actionable guidance with impact analysis, Bluebook citations, and compliance recommendations. Use when preparing client alerts, regulatory updates, leg
2. Start with the upstream step: Legal development(s) — case law, statutory amendments, regulatory updates, agency guidance, or pending legislation
3. Continue with: Client profile — industry, jurisdiction(s), operations, and specific legal concerns
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/client-advisory

## Verify

```bash
python scripts/check_skills.py skills/05-domain/client-advisory
```
