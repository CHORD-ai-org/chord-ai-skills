---
name: ccpa-policy
description: "Drafts a CCPA/CPRA-compliant privacy policy covering all required statutory disclosures under Cal. Civil Code §§ 1798.100–1798.199. Use when drafting or updating a California privacy policy, CCPA compliance notice, or consumer privacy disclosure for a business meeting CCPA applicability thresholds."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ccpa-policy
source: https://github.com/casemark/skills/tree/main/skills/legal/ccpa-policy
---

# Ccpa Policy

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ccpa-policy
```
