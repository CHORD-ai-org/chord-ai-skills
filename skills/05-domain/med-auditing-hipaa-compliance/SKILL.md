---
name: med-auditing-hipaa-compliance
description: "Conducts HIPAA compliance assessments with Privacy Rule, Security Rule, and Breach Notification analysis. Use when auditing HIPAA compliance, assessing privacy practices, or reviewing security controls. Incident-level breach determinations, risk assessments and notice clocks go to managing-privacy-breach-response."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-auditing-hipaa-compliance
source: https://github.com/casemark/skills/tree/main/skills/med/auditing-hipaa-compliance
---

# Med Auditing Hipaa Compliance

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Conducts HIPAA compliance assessments with Privacy Rule, Security Rule, and Breach Notification analysis. Use when auditing HIPAA compliance, assessing privacy practices, or reviewing security controls. Incident-level breach determinations, risk assessments and notice clocks go to managing-privacy-breach-response.

## Steps

1. Confirm the task matches this source: Conducts HIPAA compliance assessments with Privacy Rule, Security Rule, and Breach Notification analysis. Use when auditing HIPAA compliance, assessing privacy practices, or reviewing security controls. Incident-level br
2. Start with the upstream step: Is the entity a covered entity (health plan, clearinghouse, provider with electronic transactions) or a business associate?
3. Continue with: What HIPAA rules are in scope—Privacy only, Security only, Breach Notification only, or comprehensive?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/auditing-hipaa-compliance

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-auditing-hipaa-compliance
```
