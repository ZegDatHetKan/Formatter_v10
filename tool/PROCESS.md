# Format Definition Tool Process

This process is repeatable for any client and any document family.

## 1. Intake

Collect examples for one client and one document family:

- 8-12 approved reference outputs when possible;
- matching raw inputs, if available;
- templates, letterheads, or style guides;
- rejected or problematic outputs, if useful.

Create a stable manifest. Preserve original files and names.

## 2. Measurement

Inspect each reference output for:

- page size and orientation;
- margins, header distance, footer distance;
- header/footer text and media;
- paragraph order;
- style name;
- font family and size;
- bold, italic, underline;
- alignment;
- left/right/first-line indents;
- spacing before/after;
- line spacing;
- keep-with-next and keep-together;
- tables, images, numbering, footnotes, and page breaks.

Use:

```bash
python3 tool/scripts/inspect_docx.py reference_output.docx
```

## 3. Semantic Block Model

Group repeated structures into semantic blocks. Examples:

- `page_setup`
- `template_header`
- `authority_header`
- `act_title`
- `party_block`
- `case_metadata`
- `section_heading`
- `subsection_heading`
- `body_paragraph`
- `numbered_item`
- `quote_block`
- `claims_block`
- `exhibits_block`
- `signature_block`
- `footer`

For each block, record:

- evidence by document ID and paragraph number;
- detection rule;
- deterministic style rule;
- required or optional status;
- allowed repetitions;
- known exceptions;
- `needs_review` cases.

Only stable behavior becomes a rule. One-off behavior remains a question unless
the client confirms it.

## 4. Client Confirmation Artifact

Create or update a profile in `tool/profiles/`, then generate the visual artifact:

```bash
python3 tool/scripts/build_anatomy_html.py tool/profiles/<profile>.json
```

The HTML must show:

- a representative page split into colored blocks;
- a legend;
- deterministic pipeline steps;
- client confirmation questions.

The report must explain what was generated and which assumptions are still open.

## 5. Feedback Loop

Discuss the HTML/PDF with the client.

Update the profile until each block is either:

- confirmed and ready for formatter implementation;
- optional with a deterministic rule;
- explicitly `needs_review`;
- out of scope for this formatter and routed to fallback.

## 6. Formatter Handoff

When confirmed, hand off:

- final profile JSON;
- HTML/PDF anatomy;
- report;
- evidence notes;
- open non-blocking limitations.

Then implement or update `formatters/<family>.py`.

The production formatter must use confirmed rules only. It must not ask AI to
invent formatting decisions for a specialized family.
