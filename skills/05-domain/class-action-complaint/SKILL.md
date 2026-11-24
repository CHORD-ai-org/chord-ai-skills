---
name: class-action-complaint
description: "Drafts federal or state class action complaints satisfying FRCP Rule 23 certification prerequisites. Use when filing class actions, representative plaintiff complaints, Rule 23 certification pleadings, or multi-party consumer/securities/antitrust actions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-action-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/class-action-complaint
---

# Class Action Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts federal or state class action complaints satisfying FRCP Rule 23 certification prerequisites. Use when filing class actions, representative plaintiff complaints, Rule 23 certification pleadings, or multi-party consumer/securities/antitrust actions.

## Steps

1. Confirm the task matches this source: Drafts federal or state class action complaints satisfying FRCP Rule 23 certification prerequisites. Use when filing class actions, representative plaintiff complaints, Rule 23 certification pleadings, or multi-party con
2. Start with the upstream step: Named plaintiff facts — individual harm, standing, timeline, no conflicts with putative class
3. Continue with: Defendant identification — corporate structure, registered agents, principal place of business
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/class-action-complaint

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-action-complaint
```
