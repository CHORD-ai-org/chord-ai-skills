---
name: asset-liability-summaries
description: "Produces structured asset and liability summaries from financial documents for legal proceedings. Extracts valuations, ownership classifications, and encumbrances, then outputs net-worth overview, categorized schedules, disputed items, and documentation gaps. Use when preparing financial summaries for divorce/dissolution, estate planning, bankruptcy, business valuation, or settlement negotiations. Trigger on: net worth summary, marital estate, balance sheet, asset schedule, liability schedule, community/separate property."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/asset-liability-summaries
source: https://github.com/casemark/skills/tree/main/skills/legal/asset-liability-summaries
---

# Asset Liability Summaries

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Produces structured asset and liability summaries from financial documents for legal proceedings. Extracts valuations, ownership classifications, and encumbrances, then outputs net-worth overview, categorized schedules, disputed items, and documentation gaps. Use when preparing financial summaries for divorce/dissolution, estate planning, bankruptcy, business valuation, or settlement negotiations. Trigger on: net worth summary, marital estate, balance sheet, asset schedule, liability schedule, community/separate property.

## Steps

1. Confirm the task matches this source: Produces structured asset and liability summaries from financial documents for legal proceedings. Extracts valuations, ownership classifications, and encumbrances, then outputs net-worth overview, categorized schedules, 
2. Start with the upstream step: Source documents — bank/brokerage statements, tax returns, mortgage/loan documents, business financials, appraisals, retirement account statements
3. Continue with: Effective date — valuation date controlling all figures (date of separation, petition date, death date)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/asset-liability-summaries

## Verify

```bash
python scripts/check_skills.py skills/05-domain/asset-liability-summaries
```
