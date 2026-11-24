---
name: certificate-of-trust
description: "Drafts a Certificate of Trust (Abstract/Memorandum of Trust) that verifies trustee authority for third-party reliance without disclosing full trust terms. Use when preparing trust certificates for real estate closings, bank account openings, business transactions, or any context requiring trustee authority verification with UTC-compliant, privacy-preserving disclosure."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/certificate-of-trust
source: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-trust
---

# Certificate Of Trust

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts a Certificate of Trust (Abstract/Memorandum of Trust) that verifies trustee authority for third-party reliance without disclosing full trust terms. Use when preparing trust certificates for real estate closings, bank account openings, business transactions, or any context requiring trustee authority verification with UTC-compliant, privacy-preserving disclosure.

## Steps

1. Confirm the task matches this source: Drafts a Certificate of Trust (Abstract/Memorandum of Trust) that verifies trustee authority for third-party reliance without disclosing full trust terms. Use when preparing trust certificates for real estate closings, b
2. Start with the upstream step: Trust instrument — executed agreement with all amendments/restatements
3. Continue with: Trustee identification — full legal names, capacities, current acting status
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/certificate-of-trust

## Verify

```bash
python scripts/check_skills.py skills/05-domain/certificate-of-trust
```
