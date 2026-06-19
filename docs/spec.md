# Legal Formatter Python-First Specification

## Goal

Build a lower-cost formatting pipeline for legal documents.

The current formatter uses AI heavily to transform `.txt` or `.docx` input into a correctly formatted `.docx`. It works reasonably well but costs too much. The new pipeline should encode stable formatting behavior in Python scripts and use AI only where it adds value.

## Core Architecture Principle

Specialized formatters are **template composers**, not AI formatting prompts.

For known document families, the division of responsibility is:

- AI or lightweight parsing extracts semantic content blocks from the input.
- Python owns the document skeleton, paragraph order, styles, sizes, margins, alignment, indentation, spacing, template usage, and final `.docx` generation.
- AI must not decide visual formatting when a deterministic formatter exists.

The preferred flow is:

```text
input.docx / input.txt
  -> semantic extraction
  -> normalized JSON blocks
  -> deterministic Python formatter
  -> final.docx + report
```

The extraction JSON should describe what each content piece **is**, not how it should look. Example labels: `date_place`, `delivery_method`, `recipient_block`, `subject_line`, `body_paragraph`, `section_heading`, `closing`, `signature_block`, `attachments`.

Python maps those labels to exact formatting.

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
- Specialized formatter detects a structure outside its supported skeleton.
- User explicitly requests generic fallback.

Extra sections inside a known family should not make the AI invent formatting. The formatter may include a controlled `extra_section` block only if it has a deterministic style rule. Otherwise it must emit `needs_review` or route to `generic_fallback`.

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
- Extract or receive common semantic blocks: date, delivery method, recipient, object, body, section headings, closing, signature.
- Compose the output from a hardcoded letter skeleton.
- Apply deterministic styles for every paragraph type: font, size, margins, alignment, indentation, spacing, keep-with-next where needed.
- Avoid duplicating template header/footer.
- Produce a `.docx` output and a technical report.
- Mark uncertain cases as `needs_review`.

The goal is to hardcode as much repeatable structure as possible. The generic fallback exists for strange documents and last-mile edge cases, not as the default path.

## Success Criteria

- `previous_works/` contains 32 numbered historical examples.
- `manifest.json` preserves original job paths and output names.
- Initial document classification is recorded.
- `letters` formatter runs on representative examples.
- Generated output can be compared against historical output.
- Known differences and feedback are captured, not hidden.
