# Format Definition Tool

This folder is the preparation tool used to determine and confirm document
formatting rules before a runtime formatter is implemented.

It is intentionally separate from `formatters/`.

## Purpose

The tool answers this question:

> Given N approved examples of one document type, what are the stable layout and
> styling rules that a deterministic formatter should implement?

The tool does **not** format production documents. It creates analysis and
confirmation artifacts:

- measured DOCX structure;
- semantic block definitions;
- colored anatomy HTML pages;
- reports with stable rules, uncertainty, and client questions;
- profile JSON files that later feed the runtime formatter.

## Boundary

`tool/` is for discovery and confirmation:

- inspect approved examples;
- define block grammar;
- show the client a visual legend;
- integrate client feedback;
- export a confirmed profile.

`formatters/` is for production:

- receive input content or semantic JSON;
- apply confirmed rules deterministically;
- generate final `.docx` and report.

The formatter can consume the tool output, but it must not depend on the tool
being run in production.

## Folder Layout

```text
tool/
  README.md
  PROCESS.md
  requirements.txt
  profiles/
    bergamo_legal_letters.json
    acts_discovery_template.json
  scripts/
    build_anatomy_html.py
    inspect_docx.py
  output/
    html/
    reports/
```

The `tool/` directory is designed so it can later be copied into a separate
repository or package with minimal changes.

## Common Commands

Generate the confirmed letters anatomy:

```bash
python3 tool/scripts/build_letters_anatomy_html.py
```

Generate the initial acts discovery anatomy:

```bash
python3 tool/scripts/build_anatomy_html.py tool/profiles/acts_discovery_template.json
```

Inspect a DOCX reference output:

```bash
python3 tool/scripts/inspect_docx.py path/to/reference_output.docx
```

## Output Contract

Each profile produces:

- one HTML anatomy page in `tool/output/html/`;
- one report in `tool/output/reports/`.

After client confirmation, the profile becomes an input to formatter
implementation. The formatter may copy the confirmed values into code or load a
versioned exported profile, but production formatting remains owned by
`formatters/`.
