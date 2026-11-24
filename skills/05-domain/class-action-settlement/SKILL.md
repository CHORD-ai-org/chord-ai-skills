---
name: class-action-settlement
description: "Drafts and reviews federal class action settlement agreements and Rule 23(e) approval papers so the court can find the deal fair, reasonable and adequate. Compares settlement class and release with the complaint (identical factual predicate, released parties, other pending actions), reconciles gross fund to expected payout with a sourced claims rate, tests reversion, clear-sailing and kicker clauses, cy pres, Rule 23(h) fees against actual class recovery, service or incentive awards by circuit (Johnson v. NPAS), coupon settlements under 28 U.S.C. 1712, and builds a clocks table for CAFA notice under 28 U.S.C. 1715, notice date, opt-out, objection, fee motion and fairness hearing. Identifies side agreements and blow provisions under Rule 23(e)(3) and objector payments under 23(e)(5)(B), and declines to conceal them from the court. Use for settlement agreement drafting, preliminary or final approval review. Routes notices, claim forms, fee and approval motions to sibling skills."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/class-action-settlement
source: https://github.com/casemark/skills/tree/main/skills/legal/class-action-settlement
---

# Class Action Settlement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/class-action-settlement
```
