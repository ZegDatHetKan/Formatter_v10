# Letters Formatter Design

Structure inferred **only** from the historical letter outputs (`previous_works/output_*.docx`
for `document_type = letters`) and the empty letterhead template
(`assets/Template_Vuoto.docx`). Pre-existing rule files were intentionally not used.

Implementation: `formatters/letters.py` (CLI: `format_document.py --mode letters`).

## Responsibility split

The `letters` formatter must be a deterministic Python composer.

AI is allowed to:

- Extract content from messy input.
- Map content into semantic blocks.
- Flag uncertain or unsupported structure.
- Suggest future rule candidates from feedback.

AI is not allowed to:

- Choose fonts, sizes, margins, alignment, indentation, or spacing.
- Invent a one-off layout for a document that should use the `letters` formatter.
- Modify legal text while mapping blocks.
- Bypass the Python skeleton unless the run is explicitly using `generic_fallback`.

Target flow:

```text
input.docx / input.txt
  -> extract semantic letter JSON
  -> validate JSON against the letters schema
  -> compose DOCX from Template_Vuoto.docx using hardcoded Python styles
  -> report rules, warnings, needs_review
```

The more paragraph structure and styling we encode in Python, the cheaper and more reliable each run becomes. The AI should spend tokens on understanding the input, not on re-describing the whole layout.

## Semantic input contract

The formatter should accept or internally produce a structure like:

```json
{
  "document_type": "letters",
  "letter_subtype": "diffida|pec|comunicazione|riscontro|recesso|unknown",
  "date_place": "Bergamo, [DA INSERIRE: data]",
  "delivery_method": "A mezzo Raccomandata A/R...",
  "recipient_block": ["..."],
  "subject_line": "...",
  "opening": "...",
  "body_blocks": [
    {"kind": "body_paragraph", "text": "..."},
    {"kind": "section_heading", "text": "..."},
    {"kind": "numbered", "text": "..."},
    {"kind": "extra_section", "title": "...", "items": []}
  ],
  "closing": "...",
  "signature_block": ["..."],
  "attachments": [],
  "placeholders": [],
  "needs_review": false,
  "warnings": []
}
```

This JSON describes semantic roles only. Styling is entirely owned by Python.

## Page / letterhead (from template, never recreated)

- Base = `Template_Vuoto.docx`. The formatter opens it, clears the empty body
  paragraph, and appends the formatted body. Header/footer/margins are inherited.
- A4 portrait. Margins: top `5.91 cm`, bottom `4.54 cm`, left `2.0 cm`, right `2.0 cm`,
  header `1.3 cm`, footer `0.6 cm`.
- **Letterhead lives in the header/footer**: logo (`word/media/image1.jpg`) + studio
  identity (`BERGAMO LEGAL`, `Società tra Avvocati s.r.l.`, partners) in the header;
  R.E.A., C.F./P.IVA, recapiti, indirizzi in the footer. The body must not duplicate it.
- Font: `Times New Roman`, explicit name + size on every run.

## Input shape

- Inputs are essentially **plain text**, already split into logical lines — either as
  real paragraphs or as one paragraph with `\n` separators (both handled).
- Some inputs carry a **manually typed letterhead block at the top** (studio name /
  `[Indirizzo Studio]` / `[pec studio]`); the reference outputs remove it because the
  template supplies the letterhead.

## Block grammar (positional, anchored on OGGETTO)

The OGGETTO line splits the letter into *preamble* and *body*.

| Block | Detection | Style |
|---|---|---|
| `letterhead` (strip) | leading studio-identity lines **+ trailing partner `Avv.` lines** until first real line | removed (bottom signature kept) |
| `delivery_method` | `^(trasmessa\|a mezzo\|raccomandata\|via pec\|anticipata…)` | RIGHT, italic, 12 pt |
| `date_place` | `Luogo, lì <data/placeholder>` (`< 40` chars) | RIGHT, 12 pt |
| `recipient_block` | preamble lines not delivery/date (isolated honorific merged with the name line) | `left_indent 8.5 cm`, LEFT, 12 pt; honorific/name lines bold |
| `subject_line` | `^oggetto:` | label `Oggetto:` 16 pt bold + content 12 pt bold, **JUSTIFY**, single paragraph, keep_with_next |
| `opening` | first body line, greeting ending with `,` | JUSTIFY, 12 pt |
| `section_center` | ritual title set or short ALL-CAPS line | CENTER, 16 pt bold, keep_with_next/together |
| `section_left` | short title-case heading (`Fatto`, `Diritto`…) | LEFT, 14 pt bold, keep_with_next |
| `numbered` | `^N.` / `^N.N` | JUSTIFY, 12 pt, number prefix bold |
| `enum_item` | `^(i)`, `^(a)` | JUSTIFY, `left_indent 0.5 cm` |
| `bullet_item` | `^[•-*]` | JUSTIFY, `left_indent 0.5 cm` |
| `closing_signature` | `cordiali/distinti saluti`, `con osservanza`, `in attesa…riscontro`, then trailing lines | RIGHT, 12 pt; firmatario name bold; `in attesa…` italic |
| `attachments` | `^allegati:` then `All. N` | label LEFT bold; items `left_indent 0.5 cm` |
| `body` (default) | anything else | JUSTIFY, 12 pt, space_after 6 pt |

## Extra section policy

Letters may contain unusual but valid sections. The specialized formatter should handle them only through controlled rules:

- If the section maps to an existing block type, use that block type.
- If it is clearly an extra section but still part of a letter, render it with a predefined `extra_section` style and set a warning.
- If the structure changes the document shape enough that the skeleton is no longer trustworthy, set `needs_review` or route to `generic_fallback`.

Do not let AI create custom styling for that one document inside `letters` mode. That would reintroduce the expensive AI-heavy path and make results inconsistent.

## Normalization (deterministic)

- `–`/`—`/`−` → `-`; `&nbsp;` → space; collapse multiple spaces; strip zero-width/BOM.
- Drop empty paragraphs.
- `[DA INSERIRE: …]` / `[…]` placeholders → kept verbatim, rendered **bold**, and the
  document is flagged `needs_review`.

## First-slice status

Runs on representative letters **032** (comunicazione), **005** (list-heavy),
**003** (duplicated letterhead). Letterhead/margins/logo preserved; text preserved
(only stripped letterhead removed); dashes normalized; OGGETTO/recipient/closing/
signature correctly placed.

## Known gaps (not hidden)

- **Implicit lists** (enumerations with no bullet/number marker, introduced by a `:`
  lead-in) are only partially detected — depends on `;` line endings. Reference outputs
  are themselves inconsistent here.
- **Opening greeting** is left at JUSTIFY/not-bold; some references use LEFT and/or bold.
- **List indent** fixed at `0.5 cm`; some references use `0.75 cm`.
- **Signature role/company lines** may be over-bolded.
- **Inline semantic bold** inside body paragraphs (AI emphasis) is intentionally not
  reproduced — only number prefixes, labels, and placeholders are bolded.
- `section_left` detection limited to a small known heading set to avoid false positives.

## Next steps

- Run on the remaining 12 letters; collect per-block diffs vs references.
- Tune opening/list-indent/signature once compared against historical outputs.
- Extract page/template + run-styling helpers into `common/` per spec code shape.
