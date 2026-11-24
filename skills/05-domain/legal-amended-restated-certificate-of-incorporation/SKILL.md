---
name: legal-amended-restated-certificate-of-incorporation
description: "Drafts filing-ready Delaware Amended and Restated Certificates of Incorporation for venture-financing rounds. Converts term-sheet economics and governance terms into a defensible charter document under DGCL 242/245. Trigger when user needs to reauthorize capital structure, designate preferred stock series, set investor protections, or prepare a charter filing for closing."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/legal-amended-restated-certificate-of-incorporation
source: https://github.com/casemark/skills/tree/main/skills/legal/amended-restated-certificate-of-incorporation
---

# Legal Amended Restated Certificate Of Incorporation

## Brief info

Drafts filing-ready Delaware Amended and Restated Certificates of Incorporation for venture-financing rounds. Converts term-sheet economics and governance terms into a defensible charter document under DGCL 242/245. Trigger when user needs to reauthorize capital structure, designate preferred stock series, set investor protections, or prepare a charter filing for closing. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Drafts filing-ready Delaware Amended and Restated Certificates of Incorporation for venture-financing rounds. Converts term-sheet economics and governance terms into a defensible charter document under DGCL 242/245. Trigger when user needs to reauthorize capital structure, designate preferred stock series, set investor protections, or prepare a charter filing for closing.

## Steps

1. Confirm the task matches this source: Drafts filing-ready Delaware Amended and Restated Certificates of Incorporation for venture-financing rounds. Converts term-sheet economics and governance terms into a defensible charter document under DGCL 242/245. Trig
2. Start with the upstream step: Exact legal name, Delaware formation date, current charter text
3. Continue with: Board resolution and stockholder approval route (DGCL 242 vs. 245)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/amended-restated-certificate-of-incorporation

## Verify

```bash
python scripts/check_skills.py skills/05-domain/legal-amended-restated-certificate-of-incorporation
```
