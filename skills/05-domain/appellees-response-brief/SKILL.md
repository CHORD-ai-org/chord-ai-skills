---
name: appellees-response-brief
description: "Drafts an Appellee's Response Brief defending the trial court's judgment and arguing for affirmance. Covers standard of review analysis, record-based rebuttal, authority distinction, and procedural compliance. Trigger when drafting appellee briefs, response briefs, answering briefs, or defending trial court judgments on appeal."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/appellees-response-brief
source: https://github.com/casemark/skills/tree/main/skills/legal/appellees-response-brief
---

# Appellees Response Brief

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts an Appellee's Response Brief defending the trial court's judgment and arguing for affirmance. Covers standard of review analysis, record-based rebuttal, authority distinction, and procedural compliance. Trigger when drafting appellee briefs, response briefs, answering briefs, or defending trial court judgments on appeal.

## Steps

1. Confirm the task matches this source: Drafts an Appellee's Response Brief defending the trial court's judgment and arguing for affirmance. Covers standard of review analysis, record-based rebuttal, authority distinction, and procedural compliance. Trigger wh
2. Start with the upstream step: Appellant's opening brief — issues raised, authorities cited, claimed standards of review
3. Continue with: Trial court's judgment/order — decision, ruling transcripts, findings of fact and conclusions of law
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/appellees-response-brief

## Verify

```bash
python scripts/check_skills.py skills/05-domain/appellees-response-brief
```
