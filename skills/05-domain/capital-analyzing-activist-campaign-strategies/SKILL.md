---
name: capital-analyzing-activist-campaign-strategies
description: "Evaluates activist investor campaigns with thesis assessment, proposed changes, and likely outcome analysis. Use when analyzing activist situations, evaluating campaign theses, or assessing activist track records."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-activist-campaign-strategies
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-activist-campaign-strategies
---

# Capital Analyzing Activist Campaign Strategies

## Brief info

Evaluates activist investor campaigns with thesis assessment, proposed changes, and likely outcome analysis. Use when analyzing activist situations, evaluating campaign theses, or assessing activist track records. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates activist investor campaigns with thesis assessment, proposed changes, and likely outcome analysis. Use when analyzing activist situations, evaluating campaign theses, or assessing activist track records.

## Steps

1. Confirm the task matches this source: Evaluates activist investor campaigns with thesis assessment, proposed changes, and likely outcome analysis. Use when analyzing activist situations, evaluating campaign theses, or assessing activist track records.
2. Start with the upstream step: An activist investor has filed a 13D or issued a public letter, and you need to evaluate the campaign thesis and probable outcomes
3. Continue with: Assessing whether an activist's proposed operational, financial, or governance changes would create shareholder value
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-activist-campaign-strategies

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-activist-campaign-strategies
```
