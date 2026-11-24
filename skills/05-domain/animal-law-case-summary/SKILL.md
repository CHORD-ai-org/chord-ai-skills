---
name: animal-law-case-summary
description: "Produces litigation-grade case summaries for animal law disputes including cruelty/neglect prosecutions, ownership/custody, dangerous animal designations, veterinary malpractice, and service/assistance animal accommodations. Builds exhibit-cited factual timelines, maps evidence to statutory elements, evaluates expert evidence, and assesses remedies with jurisdiction-specific legal research. Use when summarizing animal law cases, analyzing animal cruelty charges, pet custody disputes, dangerous dog hearings, veterinary malpractice claims, or assistance animal accommodation matters. Also trigger for animal forfeiture, bite liability, wildlife possession, or animal-related court filings."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/animal-law-case-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/animal-law-case-summary
---

# Animal Law Case Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/animal-law-case-summary
```
