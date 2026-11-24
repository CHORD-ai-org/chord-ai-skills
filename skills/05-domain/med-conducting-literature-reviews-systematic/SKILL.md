---
name: med-conducting-literature-reviews-systematic
description: "Performs systematic literature review following PRISMA guidelines with search strategy documentation. Use when conducting systematic reviews, documenting search strategies, or performing PRISMA analyses."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-literature-reviews-systematic
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-literature-reviews-systematic
---

# Med Conducting Literature Reviews Systematic

## Brief info

Performs systematic literature review following PRISMA guidelines with search strategy documentation. Use when conducting systematic reviews, documenting search strategies, or performing PRISMA analyses. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Performs systematic literature review following PRISMA guidelines with search strategy documentation. Use when conducting systematic reviews, documenting search strategies, or performing PRISMA analyses.

## Steps

1. Confirm the task matches this source: Performs systematic literature review following PRISMA guidelines with search strategy documentation. Use when conducting systematic reviews, documenting search strategies, or performing PRISMA analyses.
2. Start with the upstream step: What is the review question structured using PICOS (Population, Intervention, Comparator, Outcomes, Study design)?
3. Continue with: Is this review for a regulatory submission (NDA/BLA clinical overview), HTA dossier, clinical guideline, or publication?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-literature-reviews-systematic

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-literature-reviews-systematic
```
