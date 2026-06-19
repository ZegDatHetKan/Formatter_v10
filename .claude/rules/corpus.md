---
paths:
  - "previous_works/**"
  - "docs/previous_works_plan.md"
---

# Corpus Rules

- `previous_works/` is a benchmark corpus, not a working output directory.
- Historical outputs are references and must not be modified.
- IDs are stable once assigned.
- Preserve original filenames and source job paths in `manifest.json`.
- Put user feedback in manifest fields, not by editing reference documents.
- Mark classification uncertainty as `needs_review`.
