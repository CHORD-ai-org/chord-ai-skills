---
name: adverse-event-reporting-policy
description: "Drafts an Adverse Event Reporting Policy compliant with 21 CFR 312.32 (IND safety reporting), 21 CFR 314.80 (postmarketing), and ICH E2A, with multi-jurisdictional overlays (EMA, PMDA, Health Canada). Covers seriousness/causality frameworks, expedited reporting timelines, roles, documentation standards, training mandates, and QA mechanisms. Use when drafting or updating an adverse event reporting policy, pharmacovigilance policy, AE/SAE reporting SOP, or safety reporting framework for a pharmaceutical company, CRO, biotech, or clinical research institution."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/adverse-event-reporting-policy
source: https://github.com/casemark/skills/tree/main/skills/legal/adverse-event-reporting-policy
---

# Adverse Event Reporting Policy

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/adverse-event-reporting-policy
```
