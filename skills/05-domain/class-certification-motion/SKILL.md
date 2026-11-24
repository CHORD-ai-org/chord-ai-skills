---
name: class-certification-motion
description: "Drafts a Motion for Class Certification under FRCP 23 or state equivalents, arguing numerosity, commonality, typicality, adequacy, predominance, and superiority from case materials. Use when drafting class certification motions, seeking class treatment, or preparing Rule 23 briefing in discovery or pre-trial phases."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-certification-motion
source: https://github.com/casemark/skills/tree/main/skills/legal/class-certification-motion
---

# Class Certification Motion

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Motion for Class Certification under FRCP 23 or state equivalents, arguing numerosity, commonality, typicality, adequacy, predominance, and superiority from case materials. Use when drafting class certification motions, seeking class treatment, or preparing Rule 23 briefing in discovery or pre-trial phases.

## Steps

1. Confirm the task matches this source: Drafts a Motion for Class Certification under FRCP 23 or state equivalents, arguing numerosity, commonality, typicality, adequacy, predominance, and superiority from case materials. Use when drafting class certification 
2. Start with the upstream step: Pleadings — complaint, answer, amended pleadings
3. Continue with: Discovery materials — interrogatories, document productions, RFAs, defendant's business records showing scope of conduct
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/class-certification-motion

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-certification-motion
```
