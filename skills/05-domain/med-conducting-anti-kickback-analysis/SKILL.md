---
name: med-conducting-anti-kickback-analysis
description: "Evaluates payment arrangements against Anti-Kickback Statute safe harbors with documentation. Use when analyzing AKS compliance, evaluating compensation arrangements, or documenting safe harbor applicability. Counsel's AKS intent analysis and opinions go to stark-law-aks-compliance; FCA exposure and overpayment sizing go to conducting-false-claims-analysis."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-conducting-anti-kickback-analysis
source: https://github.com/casemark/skills/tree/main/skills/med/conducting-anti-kickback-analysis
---

# Med Conducting Anti Kickback Analysis

## Brief info

Evaluates payment arrangements against Anti-Kickback Statute safe harbors with documentation. Use when analyzing AKS compliance, evaluating compensation arrangements, or documenting safe harbor applicability. Counsel's AKS intent analysis and opinions go to stark-law-aks-compliance; FCA exposure and overpayment sizing go to conducting-false-claims-analysis. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates payment arrangements against Anti-Kickback Statute safe harbors with documentation. Use when analyzing AKS compliance, evaluating compensation arrangements, or documenting safe harbor applicability. Counsel's AKS intent analysis and opinions go to stark-law-aks-compliance; FCA exposure and overpayment sizing go to conducting-false-claims-analysis.

## Steps

1. Confirm the task matches this source: Evaluates payment arrangements against Anti-Kickback Statute safe harbors with documentation. Use when analyzing AKS compliance, evaluating compensation arrangements, or documenting safe harbor applicability. Counsel's A
2. Start with the upstream step: What is the nature of the arrangement—referral fee, consulting agreement, lease, equipment purchase, joint venture, management services, personal services, discount/rebate, inve...
3. Continue with: Who are the parties, and does either party generate referrals for items or services reimbursable by Medicare, Medicaid, TRICARE, or other federal healthcare programs?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/conducting-anti-kickback-analysis

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-conducting-anti-kickback-analysis
```
