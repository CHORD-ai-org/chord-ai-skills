---
name: bates-citation-verification
description: "Citation format and verification protocol for legal documents that draw on Bates-stamped source records. Defines the bracket citation format, multi-source citation rules, quotation handling, the verification pass that runs before output, and the [UNVERIFIED] flag protocol. Use this skill any time another skill produces a legal work product that cites Bates-stamped pages, including medical chronologies, deposition summaries, demand letters, case briefs, and discovery responses. Also use any time the user asks how to format a citation or verify that a claim is supported by the source."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bates-citation-verification
source: https://github.com/casemark/skills/tree/main/skills/legal/bates-citation-verification
---

# Bates Citation Verification

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Citation format and verification protocol for legal documents that draw on Bates-stamped source records. Defines the bracket citation format, multi-source citation rules, quotation handling, the verification pass that runs before output, and the [UNVERIFIED] flag protocol. Use this skill any time another skill produces a legal work product that cites Bates-stamped pages, including medical chronologies, deposition summaries, demand letters, case briefs, and discovery responses. Also use any time the user asks how to format a citation or verify that a claim is supported by the source.

## Steps

1. Confirm the task matches this source: Citation format and verification protocol for legal documents that draw on Bates-stamped source records. Defines the bracket citation format, multi-source citation rules, quotation handling, the verification pass that ru
2. Start with the upstream step: Source chunk was retrieved during initial drafting but cannot be re-retrieved during the verification pass (RAG flakiness)
3. Continue with: The claim is a high-level summary that aggregates content across many pages and no single citation suffices
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bates-citation-verification

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bates-citation-verification
```
