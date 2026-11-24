---
name: ca-privilege-log
description: "Generates California-compliant privilege logs for withheld or redacted discovery materials under CCP 2031.240. Use when the user mentions privilege log drafting, California privilege log, CCP 2031.240, attorney-client privilege logging, work product designation, Evid. Code 952/954, CCP 2018.030, redaction logging, meet-and-confer privilege disputes, waiver analysis, common interest doctrine, or asks for help documenting withheld documents. Also trigger on references to Hernandez v. Superior Court, Costco Wholesale, or Wellpoint."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ca-privilege-log
source: https://github.com/casemark/skills/tree/main/skills/legal/ca-privilege-log
---

# Ca Privilege Log

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ca-privilege-log
```
