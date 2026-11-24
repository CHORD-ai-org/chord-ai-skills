---
name: capital-analyzing-alternative-data-signals
description: "Evaluates alternative data sources including satellite, NLP sentiment, web scraping, and geolocation for alpha signal generation. Use when analyzing alt data, evaluating new data sources, or integrating non-traditional signals."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/capital-analyzing-alternative-data-signals
source: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-alternative-data-signals
---

# Capital Analyzing Alternative Data Signals

## Brief info

Evaluates alternative data sources including satellite, NLP sentiment, web scraping, and geolocation for alpha signal generation. Use when analyzing alt data, evaluating new data sources, or integrating non-traditional signals. Input: a domain question, document, or decision to review. Output: structured expert-field review with caveats. Caveat: output gives professional advice without human expert review.


Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Evaluates alternative data sources including satellite, NLP sentiment, web scraping, and geolocation for alpha signal generation. Use when analyzing alt data, evaluating new data sources, or integrating non-traditional signals.

## Steps

1. Confirm the task matches this source: Evaluates alternative data sources including satellite, NLP sentiment, web scraping, and geolocation for alpha signal generation. Use when analyzing alt data, evaluating new data sources, or integrating non-traditional s
2. Start with the upstream step: Evaluating a new alternative data vendor or dataset for potential alpha generation
3. Continue with: Assessing signal strength, decay, and capacity of non-traditional data sources (satellite imagery, credit card transactions, web traffic, app usage, geolocation, NLP sentiment, ...
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: capital. Upstream: https://github.com/casemark/skills/tree/main/skills/capital/analyzing-alternative-data-signals

## Verify

```bash
python scripts/check_skills.py skills/05-domain/capital-analyzing-alternative-data-signals
```
