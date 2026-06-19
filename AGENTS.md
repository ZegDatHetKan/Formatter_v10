# Agent Operating Guide

## Mission

Convert the current AI-heavy legal document formatter into a Python-first pipeline.

The system should use deterministic scripts for known document families and reserve AI for classification, ambiguity handling, fallback formatting, and controlled script generation.

For specialized formatters, AI extracts semantic blocks. Python formats.

Do not ask AI to reproduce visual formatting when a deterministic formatter exists.

## Working Rules

- Inspect before editing.
- Preserve historical input/output files.
- Keep changes incremental and easy to review.
- Update documentation when behavior or assumptions change.
- Every script must produce a report explaining what it did.
- Every classifier decision must be traceable to document evidence.
- If a rule is stable across examples, encode it in Python.
- If a rule is uncertain, record it as feedback or a known issue before automating it.
- Treat specialized formatter scripts as the source of truth for layout and styles.

## Corpus Rules

- Create `previous_works/` from the historical job archive.
- Number files with stable 3-digit IDs: `001`, `002`, `003`.
- Keep original names in `manifest.json`.
- Do not rename IDs after they are assigned.
- Do not overwrite reference outputs.

## Formatter Rules

- Start with `letters`.
- Do not implement `acts` yet.
- Generate output files outside the historical reference set.
- Compare generated outputs against historical outputs using text, paragraph structure, styles, margins, alignment, and reports.
- Prefer explicit failure or `needs_review` over silent incorrect formatting.
- The AI layer may map input content into semantic blocks, but it must not choose fonts, sizes, margins, or ad hoc paragraph styling for specialized modes.
- If a known document type contains an extra section, use a deterministic `extra_section` rule only if defined. Otherwise mark `needs_review` or use `generic_fallback`.

## Agent Communication

- Use compact English prompts for agent instructions.
- Include context, task, constraints, and output format.
- Avoid vague phrases such as "help me", "improve this", or "make it better".
- For long tasks, work in iterations: inspect, summarize, implement, verify, report.
