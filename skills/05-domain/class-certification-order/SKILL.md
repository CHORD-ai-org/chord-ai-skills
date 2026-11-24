---
name: class-certification-order
description: "Drafts a federal or state court order certifying a class action under Rule 23. Triggers when formalizing class certification after a granted motion, drafting certification orders, or preparing rulings for appellate review. Covers Rule 23(a) findings, Rule 23(b) analysis, class definition, counsel appointment under Rule 23(g), and notice provisions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-certification-order
source: https://github.com/casemark/skills/tree/main/skills/legal/class-certification-order
---

# Class Certification Order

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a federal or state court order certifying a class action under Rule 23. Triggers when formalizing class certification after a granted motion, drafting certification orders, or preparing rulings for appellate review. Covers Rule 23(a) findings, Rule 23(b) analysis, class definition, counsel appointment under Rule 23(g), and notice provisions.

## Steps

1. Confirm the task matches this source: Drafts a federal or state court order certifying a class action under Rule 23. Triggers when formalizing class certification after a granted motion, drafting certification orders, or preparing rulings for appellate revie
2. Start with the upstream step: Granted certification motion — docket number, filing date, briefing history
3. Continue with: Class definition — proposed class, any subclasses, class period dates
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/class-certification-order

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-certification-order
```
