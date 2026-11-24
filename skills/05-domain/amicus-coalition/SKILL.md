---
name: amicus-coalition
description: "Manages end-to-end workflow for multi-organization amicus coalition briefs in appellate courts. Covers single-pen drafting governance, position alignment, conflict resolution, documented sign-offs, FRAP 29/Rule 37.6 disclosures, FRAP 26.1 corporate disclosures, cover formatting for multiple amici, and compliant filing. Use when coordinating coalition amicus briefs, managing sign-offs, drafting joint friend-of-court briefs, handling multi-amici filing, or resolving inter-organization conflicts. Triggers on phrases like \"coalition brief,\" \"12 orgs joining this amicus,\" or \"coordinate the amicus."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/amicus-coalition
source: https://github.com/casemark/skills/tree/main/skills/legal/amicus-coalition
---

# Amicus Coalition

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/amicus-coalition
```
