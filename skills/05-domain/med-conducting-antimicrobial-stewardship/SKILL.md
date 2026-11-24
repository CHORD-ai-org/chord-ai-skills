---
name: med-conducting-antimicrobial-stewardship
description: "Reviews antibiotic appropriateness with spectrum optimization, de-escalation, and duration recommendations. Use when reviewing antibiotic use, recommending de-escalation, or conducting antibiotic time-outs."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-antimicrobial-stewardship
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-antimicrobial-stewardship
---

# Med Conducting Antimicrobial Stewardship

## Brief info

Reviews antibiotic appropriateness with spectrum optimization, de-escalation, and duration recommendations. Use when reviewing antibiotic use, recommending de-escalation, or conducting antibiotic time-outs. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Reviews antibiotic appropriateness with spectrum optimization, de-escalation, and duration recommendations. Use when reviewing antibiotic use, recommending de-escalation, or conducting antibiotic time-outs.

## Steps

1. Confirm the task matches this source: Reviews antibiotic appropriateness with spectrum optimization, de-escalation, and duration recommendations. Use when reviewing antibiotic use, recommending de-escalation, or conducting antibiotic time-outs.
2. Start with the upstream step: What is the suspected or confirmed infection site? (Default: request clinical assessment)
3. Continue with: What cultures and sensitivities are available or pending? (Default: review microbiology results)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-antimicrobial-stewardship

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-antimicrobial-stewardship
```
