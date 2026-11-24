---
name: blue-sky-filings
description: "Produces a practitioner-grade Blue Sky compliance memorandum and execution plan for U.S. securities offerings. Analyzes NSMIA covered securities preemption, classifies offerings under Regulation D/Rule 506 or alternative federal exemptions, maps state jurisdictional nexus distinguishing offers from sales, and generates a state-by-state filing plan with Form D/EFD workflow, fee schedules, amendment triggers, and renewal calendars. Use this skill when advising on private placement Blue Sky compliance, Reg D notice filings, multi-state offering coordination, state securities registration exemptions, Form D filings, EFD submissions, or state fee budgeting. Also trigger when the user mentions covered securities preemption, NSMIA analysis, or asks about state notice filing requirements. Even if the user just says \"Blue Sky\" or \"state filings for our raise,\" use this skill."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/blue-sky-filings
source: https://github.com/casemark/skills/tree/main/skills/legal/blue-sky-filings
---

# Blue Sky Filings

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces a practitioner-grade Blue Sky compliance memorandum and execution plan for U.S. securities offerings. Analyzes NSMIA covered securities preemption, classifies offerings under Regulation D/Rule 506 or alternative federal exemptions, maps state jurisdictional nexus distinguishing offers from sales, and generates a state-by-state filing plan with Form D/EFD workflow, fee schedules, amendment triggers, and renewal calendars. Use this skill when advising on private placement Blue Sky compliance, Reg D notice filings, multi-state offering coordination, state securities registration exemptions, Form D filings, EFD submissions, or state fee budgeting. Also trigger when the user mentions covered securities preemption, NSMIA analysis, or asks about state notice filing requirements. Even if the user just says \"Blue Sky\" or \"state filings for our raise,\" use this skill.

## Steps

1. Confirm the task matches this source: Produces a practitioner-grade Blue Sky compliance memorandum and execution plan for U.S. securities offerings. Analyzes NSMIA covered securities preemption, classifies offerings under Regulation D/Rule 506 or alternative
2. Start with the upstream step: Offering summary — security type, aggregate amount, price/valuation, planned closing dates, single-close vs. rolling/evergreen
3. Continue with: Federal legal basis — Rule 506(b), 506(c), 504, Section 4(a)(2), Reg S, registered offering, Rule 147/147A, or other
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/blue-sky-filings

## Verify

```bash
python scripts/check_skills.py skills/05-domain/blue-sky-filings
```
