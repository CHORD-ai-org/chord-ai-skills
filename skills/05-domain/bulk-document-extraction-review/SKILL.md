---
name: bulk-document-extraction-review
description: "Extracts structured data from large sets of legal documents into tabular format for review, analysis, and reporting. Processes contracts, agreements, correspondence, filings, and other legal documents in bulk — extracting key terms, dates, parties, obligations, risks, and custom fields into organized tables. Use when conducting due diligence document review, bulk contract extraction, compliance audits across document sets, lease portfolio analysis, employment agreement review, regulatory filing review, or any task requiring structured extraction from multiple documents. Trigger keywords: tabular review, bulk extraction, document review table, data room review, batch document analysis, contract extraction, portfolio review, structured extraction, document comparison table."
category: 05-domain
status: referenced
inputs: a domain question, document, or decision to review
outputs: structured expert-field review with caveats
fails_when: output gives professional advice without human expert review
verify: python scripts/check_skills.py skills/05-domain/bulk-document-extraction-review
source: https://github.com/casemark/skills/tree/main/skills/legal/bulk-document-extraction-review
---

# Bulk Document Extraction Review

Pointer skill. Keep upstream files outside this repository.

## Trigger

Use when the task matches this source: Extracts structured data from large sets of legal documents into tabular format for review, analysis, and reporting. Processes contracts, agreements, correspondence, filings, and other legal documents in bulk — extracting key terms, dates, parties, obligations, risks, and custom fields into organized tables. Use when conducting due diligence document review, bulk contract extraction, compliance audits across document sets, lease portfolio analysis, employment agreement review, regulatory filing review, or any task requiring structured extraction from multiple documents. Trigger keywords: tabular review, bulk extraction, document review table, data room review, batch document analysis, contract extraction, portfolio review, structured extraction, document comparison table.

## Steps

1. Confirm the task matches this source: Extracts structured data from large sets of legal documents into tabular format for review, analysis, and reporting. Processes contracts, agreements, correspondence, filings, and other legal documents in bulk — extractin
2. Start with the upstream step: Document set — the files to analyze (contracts, agreements, correspondence, filings, etc.)
3. Continue with: Extraction questions — what to extract from each document (see Column Design below)
4. Record the result with caveats and human expert review.

## Hard rules

- Advisory only. Require human expert review for legal, medical, finance, or capital decisions.
- Do not copy upstream scripts or reference files into this repository.
- State the upstream source when using the skill.

## Source notes

Field: legal. Upstream: https://github.com/casemark/skills/tree/main/skills/legal/bulk-document-extraction-review

## Verify

```bash
python scripts/check_skills.py skills/05-domain/bulk-document-extraction-review
```
