---
name: advisory-summary
description: "Drafts U.S. regulatory client advisory summaries translating legal developments into actionable risk and compliance guidance. Use when a client needs a proactive memo, client alert, or legal-update brief for a new law, case, rulemaking, agency guidance, or pending reform. Trigger on requests for \"client advisory,\" \"regulatory update,\" \"legal alert,\" \"compliance briefing,\" \"new law summary,\" or \"quarterly advisory."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/advisory-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/advisory-summary
---

# Advisory Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/advisory-summary
```
