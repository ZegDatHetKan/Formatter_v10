# Letters Formatter — First Slice Run Report

Date: 2026-06-19. Engine: `formatters/letters.py` (deterministic, python-docx).
Structure inferred only from letter outputs + `assets/Template_Vuoto.docx`.

## Status

Working first deterministic slice. Runs on all 15 letters without errors.

## What it does

- Uses `Template_Vuoto.docx` as base → letterhead (logo + header/footer) and
  margins (5.91 / 4.54 / 2.0 / 2.0 cm) preserved, never recreated.
- Reads input as plain text (handles real paragraphs and single-paragraph `\n`).
- Strips duplicated typed letterhead at the top.
- Normalizes dashes (`–`/`—` → `-`), nbsp, zero-width, multi-spaces; drops empties.
- Classifies blocks around the OGGETTO anchor: delivery, date (RIGHT), recipient
  (`left_indent 8.5 cm`), OGGETTO (16 pt), opening, body (JUSTIFY 12 pt), center
  sections (16 pt), left subsections (14 pt), numbered/enum/bullet lists, closing
  + signature (RIGHT, name bold), attachments.
- Forces Times New Roman + explicit size on every run.
- Placeholders `[…]` → bold + `needs_review`.

## Test results (15/15 letters)

- No crashes.
- Text preserved on every letter (token counts identical; the only removed tokens
  are stripped studio letterhead in 003/025/027/028/029 — no letter content lost).
- `needs_review = true` for 13/15 — all and only the letters containing `[DA INSERIRE]`
  placeholders. 004 and 005 (no placeholders) correctly not flagged.
- Verified on 032 / 005 / 003: letterhead, margins, logo (`image1.jpg`) all intact.

Outputs in `out/output_*.docx` (+ per-file `*_report.md`). Historical references in
`previous_works/` untouched.

## Known gaps

- Implicit (marker-less) lists only partially detected.
- Opening greeting kept JUSTIFY/not-bold; some refs use LEFT/bold.
- List indent fixed 0.5 cm (some refs 0.75 cm).
- Signature role/company lines may be over-bolded.
- Inline semantic bold inside body not reproduced (only labels/numbers/placeholders).

## Next steps

- Side-by-side compare `out/` vs `previous_works/output_*` (the planned comparison).
- Tune opening / list indent / signature bold from those diffs.
- Refactor shared page/run helpers into `common/` per spec.
