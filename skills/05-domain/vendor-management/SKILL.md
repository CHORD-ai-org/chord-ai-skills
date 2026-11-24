---
name: vendor-management
description: "Use when scoring or auditing vendors: scorecards, SLA compliance and service credits, third-party risk tier or a tier-1 vendor review. Runs vendor_scorer.py, sla_compliance_tracker.py and vendor_risk_classifier.py."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/vendor-management
source: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/vendor-management
---

# Vendor Management

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Use when scoring or auditing vendors: scorecards, SLA compliance and service credits, third-party risk tier or a tier-1 vendor review. Runs vendor_scorer.py, sla_compliance_tracker.py and vendor_risk_classifier.py.

## Steps

1. Confirm the task matches this source: Use when scoring or auditing vendors: scorecards, SLA compliance and service credits, third-party risk tier or a tier-1 vendor review. Runs vendor_scorer.py, sla_compliance_tracker.py and vendor_risk_classifier.py.
2. Start with the upstream step: The VMO or IT director needs to prepare a quarterly vendor scorecard for the leadership team
3. Continue with: A tier-1 vendor (e.g., your identity provider, your data warehouse) has had recurring incidents and you need to quantify the SLA gap
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: business-operations. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/business-operations/skills/vendor-management

## Verify

```bash
python scripts/check_skills.py skills/05-domain/vendor-management
```
