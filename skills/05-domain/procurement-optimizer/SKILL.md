---
name: procurement-optimizer
description: "Cut spend on software and suppliers: SaaS audit, category spend review, slow purchasing cycles, supplier consolidation. Use whenever the user asks which tools or vendors to cut, where money goes, or why buying takes so long."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/procurement-optimizer
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/procurement-optimizer
---

# Procurement Optimizer

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Cut spend on software and suppliers: SaaS audit, category spend review, slow purchasing cycles, supplier consolidation. Use whenever the user asks which tools or vendors to cut, where money goes, or why buying takes so long.

## Steps

1. Confirm the task matches this source: Cut spend on software and suppliers: SaaS audit, category spend review, slow purchasing cycles, supplier consolidation. Use whenever the user asks which tools or vendors to cut, where money goes, or why buying takes so l
2. Start with the upstream step: Software spend up 40% YoY with no single owner who can name the top growth categories.
3. Continue with: 3 monitoring tools, 2 expense platforms, 4 email-marketing tools — duplicate-function clusters that nobody consolidated because no one had the data to defend the recommendation.
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: domain. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/procurement-optimizer

## Verify

```bash
python scripts/check_skills.py skills/05-domain/procurement-optimizer
```
