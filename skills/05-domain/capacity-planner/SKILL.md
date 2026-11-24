---
name: capacity-planner
description: "Size an ops or support team and plan headcount: Erlang C queue models, utilization risk, hiring order. Use whenever the user asks how many agents or staff they need, if the team is overloaded, or who to hire first."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capacity-planner
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/capacity-planner
---

# Capacity Planner

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Size an ops or support team and plan headcount: Erlang C queue models, utilization risk, hiring order. Use whenever the user asks how many agents or staff they need, if the team is overloaded, or who to hire first.

## Steps

1. Confirm the task matches this source: Size an ops or support team and plan headcount: Erlang C queue models, utilization risk, hiring order. Use whenever the user asks how many agents or staff they need, if the team is overloaded, or who to hire first.
2. Start with the upstream step: Capacity sizing at 70/80/90% utilization against P50/P90/P99
3. Continue with: Utilization health at the per-member traffic-light level plus a
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: domain. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/capacity-planner

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capacity-planner
```
