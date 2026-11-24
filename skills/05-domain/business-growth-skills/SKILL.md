---
name: business-growth-skills
description: "Use when a growth request needs routing between customer-success-manager, sales-engineer, revenue-operations, contract-and-proposal-writer and support-ops."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/business-growth-skills
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/business-growth-skills
---

# Business Growth Skills

## Brief info

Use when a growth request needs routing between customer-success-manager, sales-engineer, revenue-operations, contract-and-proposal-writer and support-ops. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Use when a growth request needs routing between customer-success-manager, sales-engineer, revenue-operations, contract-and-proposal-writer and support-ops.

## Steps

1. Confirm the task matches this source: Use when a growth request needs routing between customer-success-manager, sales-engineer, revenue-operations, contract-and-proposal-writer and support-ops.
2. Start with the upstream step: Route to exactly one skill, then follow that skill's workflow. This router ships no tools of its own.
3. Continue with: Use the skills' Python scorers for metrics, not manual estimates; deal/contract outputs are drafts for human legal/commercial review.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: business-growth. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-growth/skills/business-growth-skills

## Verify

```bash
python scripts/check_skills.py skills/05-domain/business-growth-skills
```
