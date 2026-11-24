---
name: articles-of-dissolution
description: "Drafts Articles of Dissolution (Certificate of Dissolution) for U.S. corporations to terminate legal existence via state filing. Reviews articles of incorporation, bylaws, board resolutions, and shareholder consents for jurisdiction-specific compliance. Use when preparing dissolution filings, terminating a corporation, or drafting dissolution certificates for Secretary of State submission."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/articles-of-dissolution
source: https://github.com/casemark/skills/tree/main/skills/legal/articles-of-dissolution
---

# Articles Of Dissolution

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts Articles of Dissolution (Certificate of Dissolution) for U.S. corporations to terminate legal existence via state filing. Reviews articles of incorporation, bylaws, board resolutions, and shareholder consents for jurisdiction-specific compliance. Use when preparing dissolution filings, terminating a corporation, or drafting dissolution certificates for Secretary of State submission.

## Steps

1. Confirm the task matches this source: Drafts Articles of Dissolution (Certificate of Dissolution) for U.S. corporations to terminate legal existence via state filing. Reviews articles of incorporation, bylaws, board resolutions, and shareholder consents for 
2. Start with the upstream step: Articles of Incorporation — exact legal name, incorporation date, state file/ID number
3. Continue with: Bylaws — voting thresholds, notice requirements, officer authority
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/articles-of-dissolution

## Verify

```bash
python scripts/check_skills.py skills/05-domain/articles-of-dissolution
```
