---
name: breach-notification
description: "Drafts legally compliant data breach notification letters to affected consumers under multi-state and federal statutes (HIPAA, GLBA, state AG requirements). Use when drafting breach notices, security incident consumer notifications, or data compromise letters."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/breach-notification
source: https://github.com/casemark/skills/tree/main/skills/legal/breach-notification
---

# Breach Notification

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts legally compliant data breach notification letters to affected consumers under multi-state and federal statutes (HIPAA, GLBA, state AG requirements). Use when drafting breach notices, security incident consumer notifications, or data compromise letters.

## Steps

1. Confirm the task matches this source: Drafts legally compliant data breach notification letters to affected consumers under multi-state and federal statutes (HIPAA, GLBA, state AG requirements). Use when drafting breach notices, security incident consumer no
2. Start with the upstream step: Incident details — discovery date, breach type (unauthorized access, ransomware, inadvertent disclosure), affected timeframe
3. Continue with: Compromised data inventory — exact data elements per affected population segment
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/breach-notification

## Verify

```bash
python scripts/check_skills.py skills/05-domain/breach-notification
```
