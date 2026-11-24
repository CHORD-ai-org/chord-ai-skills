---
name: awa-compliance-audit
description: "Produces an enforcement-aware Animal Welfare Act compliance audit for USDA/APHIS-regulated facilities. Maps Form 7002 inspection citations to verified 9 C.F.R. Parts 1-3 requirements, analyzes NCI severity and recurrence patterns, evaluates core compliance programs (PVC, IACUC, housing, records, transport), and outputs a prioritized corrective action plan with proof artifacts. Use when auditing AWA compliance, reviewing USDA inspection reports, preparing for license renewal, conducting diligence, or assessing enforcement risk. Trigger: Animal Welfare Act, AWA, USDA, APHIS, Form 7002, IACUC, PVC, exhibitor, dealer, research facility."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/awa-compliance-audit
source: https://github.com/casemark/skills/tree/main/skills/legal/awa-compliance-audit
---

# Awa Compliance Audit

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces an enforcement-aware Animal Welfare Act compliance audit for USDA/APHIS-regulated facilities. Maps Form 7002 inspection citations to verified 9 C.F.R. Parts 1-3 requirements, analyzes NCI severity and recurrence patterns, evaluates core compliance programs (PVC, IACUC, housing, records, transport), and outputs a prioritized corrective action plan with proof artifacts. Use when auditing AWA compliance, reviewing USDA inspection reports, preparing for license renewal, conducting diligence, or assessing enforcement risk. Trigger: Animal Welfare Act, AWA, USDA, APHIS, Form 7002, IACUC, PVC, exhibitor, dealer, research facility.

## Steps

1. Confirm the task matches this source: Produces an enforcement-aware Animal Welfare Act compliance audit for USDA/APHIS-regulated facilities. Maps Form 7002 inspection citations to verified 9 C.F.R. Parts 1-3 requirements, analyzes NCI severity and recurrence
2. Start with the upstream step: Gather facility records and Form 7002 reports (Checkpoint A)
3. Continue with: Establish regulatory applicability
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/awa-compliance-audit

## Verify

```bash
python scripts/check_skills.py skills/05-domain/awa-compliance-audit
```
