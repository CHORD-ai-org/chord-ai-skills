---
name: broker-dealer-customer-agreement
description: "Drafts SEC/FINRA-compliant Broker-Dealer Customer Agreements covering account opening, trading, margin, fees, risk disclosures, privacy, arbitration, and execution. Use when drafting or updating customer account agreements, brokerage agreements, or customer documentation for registered broker-dealers."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/broker-dealer-customer-agreement
source: https://github.com/casemark/skills/tree/main/skills/legal/broker-dealer-customer-agreement
---

# Broker Dealer Customer Agreement

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts SEC/FINRA-compliant Broker-Dealer Customer Agreements covering account opening, trading, margin, fees, risk disclosures, privacy, arbitration, and execution. Use when drafting or updating customer account agreements, brokerage agreements, or customer documentation for registered broker-dealers.

## Steps

1. Confirm the task matches this source: Drafts SEC/FINRA-compliant Broker-Dealer Customer Agreements covering account opening, trading, margin, fees, risk disclosures, privacy, arbitration, and execution. Use when drafting or updating customer account agreemen
2. Start with the upstream step: Firm registration — Form BD, FINRA CRD, state registrations, dual-registrant status
3. Continue with: Business model — execution-only vs. full-service, order routing, PFOF, principal trading
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/broker-dealer-customer-agreement

## Verify

```bash
python scripts/check_skills.py skills/05-domain/broker-dealer-customer-agreement
```
