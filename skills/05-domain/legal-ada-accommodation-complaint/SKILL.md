---
name: legal-ada-accommodation-complaint
description: "Drafts an ADA failure-to-accommodate complaint for federal or state court filing. Covers Title I employment (42 U.S.C. § 12112) and Title III public accommodations (42 U.S.C. § 12182), including EEOC exhaustion, interactive process failures, and prayer for relief. Use when drafting an ADA complaint, disability discrimination pleading, failure-to-accommodate lawsuit, or right-to-sue complaint."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-ada-accommodation-complaint
source: https://github.com/casemark/skills/tree/main/skills/legal/ada-accommodation-complaint
---

# Legal Ada Accommodation Complaint

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts an ADA failure-to-accommodate complaint for federal or state court filing. Covers Title I employment (42 U.S.C. § 12112) and Title III public accommodations (42 U.S.C. § 12182), including EEOC exhaustion, interactive process failures, and prayer for relief. Use when drafting an ADA complaint, disability discrimination pleading, failure-to-accommodate lawsuit, or right-to-sue complaint.

## Steps

1. Confirm the task matches this source: Drafts an ADA failure-to-accommodate complaint for federal or state court filing. Covers Title I employment (42 U.S.C. § 12112) and Title III public accommodations (42 U.S.C. § 12182), including EEOC exhaustion, interact
2. Start with the upstream step: [ ] Plaintiff name, state of residence
3. Continue with: [ ] Disability: diagnosis, functional limitations, treating provider
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/ada-accommodation-complaint

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-ada-accommodation-complaint
```
