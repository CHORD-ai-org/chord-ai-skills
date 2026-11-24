---
name: bad-actor-disqualification-review
description: "Produces a Rule 506(d) bad actor disqualification review for private securities offerings, including a covered persons register, tailored questionnaires mapping to each disqualifying event category, a documented reasonable-care diligence record, and classification analysis of flagged events with remediation or disclosure recommendations. Use this skill when conducting Rule 506(d) diligence, identifying covered persons for a Regulation D offering, drafting bad actor questionnaires, or analyzing potential disqualifying events involving criminal convictions, SEC orders, SRO sanctions, or state regulatory actions. Also trigger when the user mentions bad actor screening, covered persons analysis, Rule 506(d) questionnaire, disqualification waiver, or reasonable care defense. Even if the user just says \"bad actor check\" or \"506(d) diligence,\" use this skill."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bad-actor-disqualification-review
source: https://github.com/casemark/skills/tree/main/skills/legal/bad-actor-disqualification-review
---

# Bad Actor Disqualification Review

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces a Rule 506(d) bad actor disqualification review for private securities offerings, including a covered persons register, tailored questionnaires mapping to each disqualifying event category, a documented reasonable-care diligence record, and classification analysis of flagged events with remediation or disclosure recommendations. Use this skill when conducting Rule 506(d) diligence, identifying covered persons for a Regulation D offering, drafting bad actor questionnaires, or analyzing potential disqualifying events involving criminal convictions, SEC orders, SRO sanctions, or state regulatory actions. Also trigger when the user mentions bad actor screening, covered persons analysis, Rule 506(d) questionnaire, disqualification waiver, or reasonable care defense. Even if the user just says \"bad actor check\" or \"506(d) diligence,\" use this skill.

## Steps

1. Confirm the task matches this source: Produces a Rule 506(d) bad actor disqualification review for private securities offerings, including a covered persons register, tailored questionnaires mapping to each disqualifying event category, a documented reasonab
2. Start with the upstream step: Offering perimeter — Rule 506(b) vs. 506(c), expected sale date(s), staged closing schedule
3. Continue with: Cap table — full beneficial ownership chains, voting agreements, convertible instruments, super-voting stock; sufficient to calculate voting power (not just equity %)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bad-actor-disqualification-review

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bad-actor-disqualification-review
```
