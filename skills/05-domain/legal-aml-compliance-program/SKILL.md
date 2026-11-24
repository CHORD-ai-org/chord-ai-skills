---
name: legal-aml-compliance-program
description: "Drafts and reviews Bank Secrecy Act (BSA) anti-money laundering (AML/CFT) compliance programs and policies for U.S. banks, credit unions, money services businesses, broker-dealers, mutual funds, insurers, loan or finance companies and, from January 1, 2028, investment advisers. Applies the program rule for the actual institution type in 31 C.F.R. Chapter X (1020.210, 1022.210, 1023.210, FINRA Rule 3310) and ties every control to the institution's own risk assessment; tests the BSA officer's authority and resources and the independence of independent testing; sets CIP, KYC, customer due diligence and beneficial ownership procedures under 1010.230 after the Corporate Transparency Act changes; writes SAR, CTR, structuring, SAR confidentiality and recordkeeping procedures with each clock from its own trigger; keeps OFAC sanctions compliance separate. Use for an AML policy, BSA program, gap analysis or board approval package. Routes transaction-level testing and SAR narratives to auditing-aml-transactions."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-aml-compliance-program
source: https://github.com/casemark/skills/tree/main/skills/legal/aml-compliance-program
---

# Legal Aml Compliance Program

## Brief info

Drafts and reviews Bank Secrecy Act (BSA) anti-money laundering (AML/CFT) compliance programs and policies for U.S. banks, credit unions, money services businesses, broker-dealers, mutual funds, insurers, loan or finance companies and, from January 1, 2028, investment advisers. Applies the program rule for the actual institution type in 31 C.F.R. Chapter X (1020.210, 1022.210, 1023.210, FINRA Rule 3310) and ties every control to the institution's own risk assessment; tests the BSA officer's authority and resources and the independence of independent testing; sets CIP, KYC, customer due diligence and beneficial ownership procedures under 1010.230 after the Corporate Transparency Act changes; writes SAR, CTR, structuring, SAR confidentiality and recordkeeping procedures with each clock from its own trigger; keeps OFAC sanctions compliance separate. Use for an AML policy, BSA program, gap analysis or board approval package. Routes transaction-level testing and SAR narratives to auditing-aml-transactions. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts and reviews Bank Secrecy Act (BSA) anti-money laundering (AML/CFT) compliance programs and policies for U.S. banks, credit unions, money services businesses, broker-dealers, mutual funds, insurers, loan or finance companies and, from January 1, 2028, investment advisers. Applies the program rule for the actual institution type in 31 C.F.R. Chapter X (1020.210, 1022.210, 1023.210, FINRA Rule 3310) and ties every control to the institution's own risk assessment; tests the BSA officer's authority and resources and the independence of independent testing; sets CIP, KYC, customer due diligence and beneficial ownership procedures under 1010.230 after the Corporate Transparency Act changes; writes SAR, CTR, structuring, SAR confidentiality and recordkeeping procedures with each clock from its own trigger; keeps OFAC sanctions compliance separate. Use for an AML policy, BSA program, gap analysis or board approval package. Routes transaction-level testing and SAR narratives to auditing-aml-transactions.

## Steps

1. Confirm the task matches this source: Drafts and reviews Bank Secrecy Act (BSA) anti-money laundering (AML/CFT) compliance programs and policies for U.S. banks, credit unions, money services businesses, broker-dealers, mutual funds, insurers, loan or finance
2. Start with the upstream step: Draft only. Nothing is filed, adopted or sent. Every output is a draft for counsel and BSA/AML officer review and is never called final or approved.
3. Continue with: Source-review gate. Never call a document missing until the inventory has been checked and the file opened, with OCR or extraction tried. Classify every open item as one of four...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/aml-compliance-program

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-aml-compliance-program
```
