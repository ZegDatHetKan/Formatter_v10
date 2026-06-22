# Rich Letters Anatomy Report

- generated_at: 2026-06-22T14:02:09+00:00
- script: `tool/scripts/build_letters_anatomy_html.py`
- output: `tool/output/html/lettera_anatomia_colori.html`
- purpose: visual confirmation artifact for the documented Bergamo Legal letters process

## Inputs represented

- `previous_works/manifest.json`: 32 historical jobs, 15 letters
- `docs/letters_formatter_design.md`: semantic block grammar and style rules
- `docs/feedback_review_lettere.md`: feedback review and anatomy
- `tests/make_examples.py`: synthetic example letters
- `formatters/letters.py`: deterministic formatter implementation

## What this page shows

- corpus classification summary
- a synthetic diffida letter split into semantic blocks
- a technical legend mapping colors to formatter blocks
- confirmed style/layout rules
- repeatable pipeline for future document families
