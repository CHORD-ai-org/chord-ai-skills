---
name: legal-advisory-summary
description: "Drafts U.S. regulatory client advisory summaries translating legal developments into actionable risk and compliance guidance. Use when a client needs a proactive memo, client alert, or legal-update brief for a new law, case, rulemaking, agency guidance, or pending reform. Trigger on requests for \"client advisory,\" \"regulatory update,\" \"legal alert,\" \"compliance briefing,\" \"new law summary,\" or \"quarterly advisory."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-advisory-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/advisory-summary
---

# Legal Advisory Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts U.S. regulatory client advisory summaries translating legal developments into actionable risk and compliance guidance. Use when a client needs a proactive memo, client alert, or legal-update brief for a new law, case, rulemaking, agency guidance, or pending reform. Trigger on requests for "client advisory," "regulatory update," "legal alert," "compliance briefing," "new law summary," or "quarterly advisory.

## Steps

1. Confirm the task matches this source: Drafts U.S. regulatory client advisory summaries translating legal developments into actionable risk and compliance guidance. Use when a client needs a proactive memo, client alert, or legal-update brief for a new law, c
2. Start with the upstream step: Confirm jurisdiction (US federal/state/agency) and client industry.
3. Continue with: Identify the legal development(s) and research scope (date range, source types).
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/advisory-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-advisory-summary
```
