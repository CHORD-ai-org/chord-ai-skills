---
name: legal-adoption-petition
description: "Drafts a Petition for Adoption for U.S. family law courts (stepparent, relative, agency, independent). Use when drafting adoption petitions, initiating adoption proceedings, or preparing pre-filing adoption pleadings."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-adoption-petition
source: https://github.com/casemark/skills/tree/main/skills/legal/adoption-petition
---

# Legal Adoption Petition

## Brief info

Drafts a Petition for Adoption for U.S. family law courts (stepparent, relative, agency, independent). Use when drafting adoption petitions, initiating adoption proceedings, or preparing pre-filing adoption pleadings. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Petition for Adoption for U.S. family law courts (stepparent, relative, agency, independent). Use when drafting adoption petitions, initiating adoption proceedings, or preparing pre-filing adoption pleadings.

## Steps

1. Confirm the task matches this source: Drafts a Petition for Adoption for U.S. family law courts (stepparent, relative, agency, independent). Use when drafting adoption petitions, initiating adoption proceedings, or preparing pre-filing adoption pleadings.
2. Start with the upstream step: Classify adoption type (stepparent / relative / agency / independent) — this drives consent rules, waiting periods, and eligibility
3. Continue with: Collect party information: full legal names, DOBs, addresses for petitioner(s), child, biological parents
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/adoption-petition

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-adoption-petition
```
