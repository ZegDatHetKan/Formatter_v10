---
paths:
  - "**/*.py"
---

# Python Rules

- Use clear, small functions with explicit inputs and outputs.
- Prefer deterministic parsing and formatting over AI calls.
- Keep file writes explicit and easy to audit.
- Do not overwrite historical corpus files.
- Return structured results for classifier and formatter internals.
- Produce human-readable reports for formatter runs.
- If a rule is uncertain, emit a warning or `needs_review` instead of guessing silently.
