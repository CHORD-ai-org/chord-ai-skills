---
name: charitable-solicitation-registration
description: "Prepares jurisdiction-specific charitable solicitation registration packages for U.S. nonprofits. Covers multi-state nexus analysis, exemption eligibility, URS filing strategy, financial disclosures, and professional fundraiser documentation. Use when a nonprofit plans fundraising campaigns, online donation drives, direct mail, telephone solicitation, or any cross-state charitable solicitation."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/charitable-solicitation-registration
source: https://github.com/casemark/skills/tree/main/skills/legal/charitable-solicitation-registration
---

# Charitable Solicitation Registration

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Prepares jurisdiction-specific charitable solicitation registration packages for U.S. nonprofits. Covers multi-state nexus analysis, exemption eligibility, URS filing strategy, financial disclosures, and professional fundraiser documentation. Use when a nonprofit plans fundraising campaigns, online donation drives, direct mail, telephone solicitation, or any cross-state charitable solicitation.

## Steps

1. Confirm the task matches this source: Prepares jurisdiction-specific charitable solicitation registration packages for U.S. nonprofits. Covers multi-state nexus analysis, exemption eligibility, URS filing strategy, financial disclosures, and professional fun
2. Start with the upstream step: Organization basics — legal name (per IRS determination letter), EIN, formation state/date, entity type
3. Continue with: IRS determination letter — 501(c)(3) or other exemption, effective date
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/charitable-solicitation-registration

## Verify

```bash
python scripts/check_skills.py skills/05-domain/charitable-solicitation-registration
```
