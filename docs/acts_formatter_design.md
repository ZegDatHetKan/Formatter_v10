# Acts Formatter Design

Status: discovery template only. Do not implement `acts` until examples are reviewed with
the format-definition tool and the client confirms the visual anatomy.

## Goal

Build a deterministic formatter for court-facing or authority-facing acts:

- ricorsi;
- istanze;
- memorie;
- denunce/querele;
- other structured legal acts.

The target architecture is the same as `letters`: semantic extraction first, Python
composition second.

Use the preparation tool first:

```bash
python3 tool/scripts/build_anatomy_html.py tool/profiles/acts_discovery_template.json
```

The confirmed output from `tool/` becomes the input to `formatters/acts.py`.
`formatters/acts.py` is the production component; `tool/` is the client-feedback and
rule-definition component.

## Expected Discovery Blocks

The first visual profile uses these provisional blocks:

| Block | Meaning | Status |
|---|---|---|
| `page_setup` / `template` | page size, margins, header/footer, media | measure from references |
| `authority_header` | court, authority, office | provisional |
| `act_title` | main act title | provisional |
| `party_block` | parties, lawyers, domiciles, PEC, CF/P.IVA | provisional |
| `case_metadata` | case number, object, value, challenged measure | provisional |
| `section_heading` | major sections such as IN FATTO / IN DIRITTO / RICHIESTE | provisional |
| `subsection_heading` | numbered reasons or argument titles | provisional |
| `body_paragraph` | ordinary argument text | provisional |
| `claims_block` | conclusions and requests | provisional |
| `exhibits_block` | exhibits, attachments, produced documents | provisional |
| `signature_block` | place, date, lawyer signature | provisional |
| `needs_review` | ambiguous or one-off material | required safety rule |

## Evidence Required Before Implementation

For every confirmed block, collect:

- document IDs and paragraph numbers;
- detection evidence;
- exact style rule;
- examples where the rule does not apply;
- decision: hardcode, optional, `needs_review`, or fallback.

## Open Questions For The Client

- Which act types belong to one formatter and which need separate formatters?
- Is the title/page setup identical across ricorsi, istanze, memorie, and denunce?
- Are court headers and party blocks always present?
- Which sections are mandatory?
- How should long quotations, citations, footnotes, tables, and exhibits be handled?
- Which variations should be accepted automatically and which require review?
