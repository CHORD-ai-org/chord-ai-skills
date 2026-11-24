---
name: capital-analyzing-add-on-acquisition-candidates
description: "Evaluates bolt-on acquisitions for existing platforms with strategic fit, synergy quantification, and return contribution analysis. Use when screening add-on targets, building platform acquisition strategies, or modeling tuck-in economics."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-add-on-acquisition-candidates
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-add-on-acquisition-candidates
---

# Capital Analyzing Add On Acquisition Candidates

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates bolt-on acquisitions for existing platforms with strategic fit, synergy quantification, and return contribution analysis. Use when screening add-on targets, building platform acquisition strategies, or modeling tuck-in economics.

## Steps

1. Confirm the task matches this source: Evaluates bolt-on acquisitions for existing platforms with strategic fit, synergy quantification, and return contribution analysis. Use when screening add-on targets, building platform acquisition strategies, or modeling
2. Start with the upstream step: Screening potential tuck-in or bolt-on targets against an existing portfolio company (platform)
3. Continue with: Building a systematic add-on acquisition pipeline for a buy-and-build thesis
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-add-on-acquisition-candidates

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-add-on-acquisition-candidates
```
