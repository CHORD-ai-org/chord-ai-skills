---
name: support-ops
description: "Use for any customer support operations question - SLA attainment and breaches (first response, resolution, business hours, weekends, tickets about to breach), how many agents to schedule per hour for a phone, chat or email queue and where the roster is short (Erlang C, service level, handle time, shrinkage, occupancy, backlog), or which ticket topics to deflect with help-center articles, automate with macros or fix as product bugs. Works from a helpdesk ticket export with stdlib scripts."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/support-ops
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/support-ops
---

# Support Ops

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Use for any customer support operations question - SLA attainment and breaches (first response, resolution, business hours, weekends, tickets about to breach), how many agents to schedule per hour for a phone, chat or email queue and where the roster is short (Erlang C, service level, handle time, shrinkage, occupancy, backlog), or which ticket topics to deflect with help-center articles, automate with macros or fix as product bugs. Works from a helpdesk ticket export with stdlib scripts.

## Steps

1. Confirm the task matches this source: Use for any customer support operations question - SLA attainment and breaches (first response, resolution, business hours, weekends, tickets about to breach), how many agents to schedule per hour for a phone, chat or em
2. Start with the upstream step: Ask which clock the SLA runs on (business or calendar, timezone, holidays) before reporting attainment. Never assume.
3. Continue with: Open breaches count. Never report attainment on closed tickets only.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: business-growth. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/support-ops

## Verify

```bash
python scripts/check_skills.py skills/05-domain/support-ops
```
