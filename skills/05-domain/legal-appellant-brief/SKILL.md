---
name: legal-appellant-brief
description: "Drafts the appellant's opening brief challenging a lower court decision in federal or state appellate courts. Covers issue selection, standard of review framing, record citation, argument structure, and procedural compliance under FRAP 28/32 or state equivalents. Use when preparing an appellant's opening brief, selecting appellate issues, structuring appellate arguments, or demonstrating reversible error on appeal."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-appellant-brief
source: https://github.com/casemark/skills/tree/main/skills/legal/appellant-brief
---

# Legal Appellant Brief

## Brief info

Drafts the appellant's opening brief challenging a lower court decision in federal or state appellate courts. Covers issue selection, standard of review framing, record citation, argument structure, and procedural compliance under FRAP 28/32 or state equivalents. Use when preparing an appellant's opening brief, selecting appellate issues, structuring appellate arguments, or demonstrating reversible error on appeal. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts the appellant's opening brief challenging a lower court decision in federal or state appellate courts. Covers issue selection, standard of review framing, record citation, argument structure, and procedural compliance under FRAP 28/32 or state equivalents. Use when preparing an appellant's opening brief, selecting appellate issues, structuring appellate arguments, or demonstrating reversible error on appeal.

## Steps

1. Confirm the task matches this source: Drafts the appellant's opening brief challenging a lower court decision in federal or state appellate courts. Covers issue selection, standard of review framing, record citation, argument structure, and procedural compli
2. Start with the upstream step: Lower court decision — opinion, order, or judgment being appealed
3. Continue with: Trial record — transcripts, exhibits, motions, and orders
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/appellant-brief

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-appellant-brief
```
