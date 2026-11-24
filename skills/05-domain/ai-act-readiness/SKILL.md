---
name: ai-act-readiness
description: "EU AI Act readiness: risk tier, duties, deadlines. Load whenever AI ships in the EU or the user asks if the Act applies."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/ai-act-readiness
source: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/ai-act-readiness
---

# Ai Act Readiness

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: EU AI Act readiness: risk tier, duties, deadlines. Load whenever AI ships in the EU or the user asks if the Act applies.

## Steps

1. Confirm the task matches this source: EU AI Act readiness: risk tier, duties, deadlines. Load whenever AI ships in the EU or the user asks if the Act applies.
2. Start with the upstream step: During AI-system intake review (per new system or material change)
3. Continue with: Before placing an AI system on the EU market
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: compliance-os. Upstream: https://github.com/alirezarezvani/claude-skills/tree/main/compliance-os/skills/ai-act-readiness

## Verify

```bash
python scripts/check_skills.py skills/05-domain/ai-act-readiness
```
