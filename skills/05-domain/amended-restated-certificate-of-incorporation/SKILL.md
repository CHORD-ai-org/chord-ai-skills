---
name: amended-restated-certificate-of-incorporation
description: "Drafts filing-ready Delaware Amended and Restated Certificates of Incorporation for venture-financing rounds. Converts term-sheet economics and governance terms into a defensible charter document under DGCL 242/245. Trigger when user needs to reauthorize capital structure, designate preferred stock series, set investor protections, or prepare a charter filing for closing."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/amended-restated-certificate-of-incorporation
source: https://github.com/casemark/skills/tree/main/skills/legal/amended-restated-certificate-of-incorporation
---

# Amended Restated Certificate Of Incorporation

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/amended-restated-certificate-of-incorporation
```
