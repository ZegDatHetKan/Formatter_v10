# Reusable Document Profile Process

This is the process for the **format-definition tool** in `tool/`.

It turns a set of approved example documents into a confirmed formatting profile.
That profile is then used to build or update the runtime formatter in `formatters/`.
The tool and the formatter are deliberately separate.

## Objective

Given N examples of one document family, produce:

- a measured structural analysis of the examples;
- a client-readable colored anatomy page with legend;
- a report of stable rules, uncertain cases, and open questions;
- a confirmed profile for the deterministic Python formatter;
- verification outputs comparing generated documents against historical references.

The AI layer may help classify sections or propose semantic labels, but Python owns final
layout, page setup, margins, fonts, spacing, indentation, and report generation.

## Inputs Required From The User

For each document family and client, collect:

- 8-12 approved reference outputs when possible;
- matching raw inputs, if available;
- the client's template or letterhead file, if the format uses one;
- any written style requirements already known to the client;
- examples of rejected or "bad" outputs, if the client has them.

If fewer examples are available, proceed, but mark confidence lower and avoid hardcoding
rules that appear only once.

## Iteration 1 - Corpus Intake

Create a stable tool workspace:

```text
tool/workspaces/<client_slug>/<family_slug>/
  manifest.json
  input/
  reference_output/
  analysis/
  generated/
  reports/
```

Rules:

- never overwrite reference outputs;
- keep original filenames in `manifest.json`;
- assign stable IDs such as `001`, `002`, `003`;
- record whether each file is input, approved output, template, rejected output, or note.

## Iteration 2 - Measurement

For every approved output, inspect:

- page size and orientation;
- top, bottom, left, right, header, and footer margins;
- header/footer text and media;
- paragraph order and text shape;
- paragraph style name;
- font family and size per run;
- bold, italic, underline, and mixed-run behavior;
- alignment;
- left, right, and first-line indents;
- spacing before/after;
- line spacing;
- keep-with-next and keep-together;
- tables, images, page breaks, footnotes, and numbering when present.

Use `tool/scripts/inspect_docx.py` for detailed inspection. Add a family-specific summarizer
only after seeing the actual examples.

## Iteration 3 - Rule Extraction

Group paragraphs into semantic blocks, for example:

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

For each candidate block, record:

- evidence: which document IDs and paragraph numbers support it;
- detection rule: text pattern, position, style, or semantic role;
- deterministic style: font, size, bold/italic, alignment, indents, spacing;
- required/optional status;
- allowed repetitions;
- uncertainty and known exceptions.

Do not automate a rule just because it appears once. Single-example behavior goes into
`needs_review` unless the client confirms it as a rule.

## Iteration 4 - Client Confirmation Artifact

Create or update a JSON profile in `tool/profiles/`.

Then run:

```bash
python3 tool/scripts/build_anatomy_html.py tool/profiles/<profile>.json
```

The generated HTML must show:

- a representative page divided into colored semantic blocks;
- a legend mapping colors to block names and rules;
- the deterministic pipeline;
- acceptance questions for the client;
- a report explaining what was generated and what still needs confirmation.

When the client wants a PDF, print the HTML to PDF from the browser or add a dedicated
HTML-to-PDF step for that environment. The HTML remains the editable source artifact.

## Iteration 5 - Formatter Handoff

Only after the visual rules are confirmed:

- hand off the confirmed profile JSON;
- hand off the HTML/PDF anatomy and report;
- hand off evidence notes and open limitations;
- then create or update `formatters/<family>.py`.

The formatter should:

- accept semantic JSON or parse input text into semantic blocks;
- compose DOCX from the confirmed skeleton;
- hardcode or load confirmed layout and styles;
- emit a report for every generated document;
- set `needs_review` for missing mandatory blocks, unsupported extra sections, or low confidence.

The formatter must not ask AI to choose ad hoc fonts, margins, sizes, spacing, or paragraph
styles inside a specialized family.

## Iteration 6 - Verification

For each reference example, compare generated output against historical output:

- text preservation;
- paragraph count and block order;
- style labels;
- font family and sizes;
- bold/italic behavior;
- margins and page setup;
- alignment and indentation;
- spacing before/after and line spacing;
- report warnings and `needs_review` flags.

Record differences as:

- accepted difference;
- bug to fix;
- client decision needed;
- outside current family, use fallback.

## Acts First Pass

For Bergamo Legal acts, start from:

```bash
python3 tool/scripts/build_anatomy_html.py tool/profiles/acts_discovery_template.json
```

Then replace the placeholder blocks with rules inferred from the 8-12 act examples.
Do not implement `formatters/acts.py` until the client confirms the anatomy and rules.

## Compact Agent Prompt

Use this when handing the task to another agent:

```text
Context: We are building a Python-first legal formatter. AI extracts semantic blocks only; Python owns layout.
Task: Given N approved examples for one client/document family, create a reusable document profile.
Constraints: Preserve reference files. Measure DOCX styles/margins/spacing. Generalize only stable rules. Mark uncertainty as needs_review. Produce a colored HTML anatomy page with legend and a report. Do not implement the formatter until rules are confirmed.
Output: manifest updates, analysis notes, tool/profiles/<profile>.json, generated HTML/report, open questions, and next formatter steps.
```
