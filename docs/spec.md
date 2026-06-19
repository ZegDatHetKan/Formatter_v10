# Legal Formatter Python-First Specification

## Goal

Build a lower-cost formatting pipeline for legal documents.

The current formatter uses AI heavily to transform `.txt` or `.docx` input into a correctly formatted `.docx`. It works reasonably well but costs too much. The new pipeline should encode stable formatting behavior in Python scripts and use AI only where it adds value.

## Document Families

The system has three main document families:

- `letters`: letters, communications, PEC messages, diffide, riscontri, recesso, external communications.
- `acts`: ricorsi, istanze, memorie, denunce/querele, court-facing or authority-facing legal acts.
- `other_pending_name`: third family to be renamed after corpus review; currently includes mediation/delegation/exposition-style documents.

## Operating Modes

The pipeline must support these modes:

- `letters`: user manually selected letters formatter.
- `acts`: user manually selected acts formatter.
- `other_pending_name`: user manually selected third formatter.
- `auto`: classifier decides document family, then runs the specialized formatter.
- `generic_fallback`: AI-heavy generic formatter; more expensive and used only when needed.

Fallback triggers:

- Unknown document family.
- Low classifier confidence.
- Specialized formatter failure.
- User explicitly requests generic fallback.

## Target CLI

```bash
python format_document.py --mode letters --input input.docx --output final.docx
python format_document.py --mode auto --input input.docx --output final.docx
python format_document.py --mode generic_fallback --input input.docx --output final.docx
```

## Target Code Shape

```text
format_document.py
classify_document.py
formatters/
  letters.py
  acts.py
  other_pending_name.py
  generic_fallback.py
common/
  docx_io.py
  styles.py
  reporting.py
previous_works/
  manifest.json
```

## First Implementation Target

Implement only `letters` first.

The first letters formatter should:

- Read `.docx` input.
- Detect common blocks: date, delivery method, recipient, object, body, section headings, closing, signature.
- Apply deterministic styles: font, size, margins, alignment, indentation, spacing, keep-with-next where needed.
- Avoid duplicating template header/footer.
- Produce a `.docx` output and a technical report.
- Mark uncertain cases as `needs_review`.

## Success Criteria

- `previous_works/` contains 32 numbered historical examples.
- `manifest.json` preserves original job paths and output names.
- Initial document classification is recorded.
- `letters` formatter runs on representative examples.
- Generated output can be compared against historical output.
- Known differences and feedback are captured, not hidden.
