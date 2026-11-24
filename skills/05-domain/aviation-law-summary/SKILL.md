---
name: aviation-law-summary
description: "Produces structured aviation law summaries with Bluebook citations covering U.S. and international regulatory frameworks, treaties, and case law. Use when drafting an aviation law summary, FAA/DOT/TSA compliance overview, Montreal/Warsaw Convention liability analysis, air service agreement review, accident liability synopsis, or aviation regulatory research memo."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/aviation-law-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/aviation-law-summary
---

# Aviation Law Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces structured aviation law summaries with Bluebook citations covering U.S. and international regulatory frameworks, treaties, and case law. Use when drafting an aviation law summary, FAA/DOT/TSA compliance overview, Montreal/Warsaw Convention liability analysis, air service agreement review, accident liability synopsis, or aviation regulatory research memo.

## Steps

1. Confirm the task matches this source: Produces structured aviation law summaries with Bluebook citations covering U.S. and international regulatory frameworks, treaties, and case law. Use when drafting an aviation law summary, FAA/DOT/TSA compliance overview
2. Start with the upstream step: Topic scope — precise issue (e.g., accident liability, slot allocation, UAS operations, air service agreements)
3. Continue with: Jurisdiction — U.S. federal, international, or mixed; list relevant countries
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/aviation-law-summary

## Verify

```bash
python scripts/check_skills.py skills/05-domain/aviation-law-summary
```
