---
name: antitrust-investigation-summary
description: "Drafts privilege-protective, board-ready executive summary memoranda of internal antitrust investigation findings for US federal law. Covers monopolization, vertical restraints, acquisitions, FTC Act Section 5, tech-platform conduct, risk assessment, and remediation. Use when drafting antitrust investigation summaries, board memos on competition risk, or internal compliance investigation reports."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/antitrust-investigation-summary
source: https://github.com/casemark/skills/tree/main/skills/legal/antitrust-investigation-summary
---

# Antitrust Investigation Summary

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task falls under Law and the upstream skill matches the request.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Verify

```bash
python scripts/check_skills.py skills/05-domain/antitrust-investigation-summary
```
