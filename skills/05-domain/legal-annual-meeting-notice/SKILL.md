---
name: legal-annual-meeting-notice
description: "Drafts legally compliant Notice of Annual Shareholders Meeting for US corporations, covering state-specific notice periods, record dates, quorum and voting thresholds, proxy procedures, and SEC Regulation 14A compliance for public companies. Use when preparing annual meeting notices, shareholder meeting notifications, or proxy notice and access mailings."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-annual-meeting-notice
source: https://github.com/casemark/skills/tree/main/skills/legal/annual-meeting-notice
---

# Legal Annual Meeting Notice

## Brief info

Drafts legally compliant Notice of Annual Shareholders Meeting for US corporations, covering state-specific notice periods, record dates, quorum and voting thresholds, proxy procedures, and SEC Regulation 14A compliance for public companies. Use when preparing annual meeting notices, shareholder meeting notifications, or proxy notice and access mailings. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts legally compliant Notice of Annual Shareholders Meeting for US corporations, covering state-specific notice periods, record dates, quorum and voting thresholds, proxy procedures, and SEC Regulation 14A compliance for public companies. Use when preparing annual meeting notices, shareholder meeting notifications, or proxy notice and access mailings.

## Steps

1. Confirm the task matches this source: Drafts legally compliant Notice of Annual Shareholders Meeting for US corporations, covering state-specific notice periods, record dates, quorum and voting thresholds, proxy procedures, and SEC Regulation 14A compliance 
2. Start with the upstream step: Corporate documents — articles of incorporation, current bylaws, prior meeting notices
3. Continue with: State of incorporation — determines applicable business corporation act and notice periods
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/annual-meeting-notice

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-annual-meeting-notice
```
