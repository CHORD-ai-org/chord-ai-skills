---
name: med-analyzing-clinical-trial-data
description: "Structures clinical trial data analysis with primary endpoint evaluation and safety reporting. Use when analyzing trial results, evaluating endpoints, or preparing statistical reports."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/med-analyzing-clinical-trial-data
source: https://github.com/casemark/skills/tree/main/skills/med/analyzing-clinical-trial-data
---

# Med Analyzing Clinical Trial Data

## Brief info

Structures clinical trial data analysis with primary endpoint evaluation and safety reporting. Use when analyzing trial results, evaluating endpoints, or preparing statistical reports. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Structures clinical trial data analysis with primary endpoint evaluation and safety reporting. Use when analyzing trial results, evaluating endpoints, or preparing statistical reports.

## Steps

1. Confirm the task matches this source: Structures clinical trial data analysis with primary endpoint evaluation and safety reporting. Use when analyzing trial results, evaluating endpoints, or preparing statistical reports.
2. Start with the upstream step: What is the study phase (I–IV) and therapeutic area?
3. Continue with: What are the primary, secondary, and exploratory endpoints as defined in the protocol?
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: med. Upstream: https://github.com/casemark/skills/tree/main/skills/med/analyzing-clinical-trial-data

## Verify

```bash
python scripts/check_skills.py skills/05-domain/med-analyzing-clinical-trial-data
```
