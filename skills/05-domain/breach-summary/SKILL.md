---
name: breach-summary
description: "Summarizes cybersecurity breach incidents into structured legal and compliance records. Trigger when synthesizing incident reports, forensics, logs, or notifications into a defensible chronology, scope-impact analysis, response ledger, or regulatory-risk assessment. Keywords: data breach, incident response, unauthorized access, ransomware, exfiltration, GDPR, CCPA, HIPAA."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/breach-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/breach-summary
---

# Breach Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/breach-summary
```
