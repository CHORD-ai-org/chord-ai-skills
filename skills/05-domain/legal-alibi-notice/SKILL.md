---
name: legal-alibi-notice
description: "Drafts a Notice of Alibi Defense under Fed. R. Crim. P. 12.1 or state equivalents. Triggers on alibi notice drafting, alibi defense filing, Rule 12.1 disclosure, or pre-trial criminal defense notice tasks."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-alibi-notice
source: https://github.com/casemark/skills/tree/main/skills/legal/alibi-notice
---

# Legal Alibi Notice

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Notice of Alibi Defense under Fed. R. Crim. P. 12.1 or state equivalents. Triggers on alibi notice drafting, alibi defense filing, Rule 12.1 disclosure, or pre-trial criminal defense notice tasks.

## Steps

1. Confirm the task matches this source: Drafts a Notice of Alibi Defense under Fed. R. Crim. P. 12.1 or state equivalents. Triggers on alibi notice drafting, alibi defense filing, Rule 12.1 disclosure, or pre-trial criminal defense notice tasks.
2. Start with the upstream step: Charging documents — indictment/information with dates, times, location of alleged offense
3. Continue with: Alibi details — defendant's actual location(s) with full addresses during relevant period
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/alibi-notice

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-alibi-notice
```
