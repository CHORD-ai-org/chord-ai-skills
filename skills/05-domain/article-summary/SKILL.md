---
name: article-summary
description: "Generates structured 500-800 word summaries of legal articles distilling thesis, methodology, arguments, authorities, conclusions, and significance. Triggers when summarizing legal scholarship, reviewing law review articles, preparing literature reviews, or triaging articles for full reading."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/article-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/article-summary
---

# Article Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/article-summary
```
