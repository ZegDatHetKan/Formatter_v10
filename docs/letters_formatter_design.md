# Letters Formatter Design

This document must be completed while building the first deterministic `letters` formatter.

## Purpose

Document the structure Claude deduces from historical letter examples and the deterministic rules implemented in Python.

## Source Examples

Use `previous_works/manifest.json` and filter:

```json
"document_type": "letters"
```

Representative starting examples:

- `001` lettera-informativa-consiglieri-mueller-madone
- `003` pec-contestazione-fattura-papi-solutions
- `007` diffida-rimozione-recensioni-casu
- `011` comunicazione-consenso-differimento-mediazione-chebotareva
- `015` recesso-gravi-motivi-sublocazione-avantgarde
- `025` lettera-trustpilot-recensioni-hormonal-casula
- `032` aggiornamento-duns-apple-business-bertocchi

## Structure To Infer

Record findings for:

- Date and place.
- Delivery channel: PEC, raccomandata, email, platform submission.
- Recipient block.
- Subject/object line.
- Introductory formula.
- Body paragraphs.
- Numbered sections.
- Legal warning or demand block.
- Closing formula.
- Signature block.
- Placeholders such as `[DA INSERIRE: ...]`.

## Rules To Implement

For each implemented rule, document:

- Name.
- Detection logic.
- Formatting output.
- Examples where it applies.
- Examples where it must not apply.
- Open issues.

## First Script Acceptance

The first script is acceptable when it can format at least three representative letters without corrupting text and without duplicating header/footer.

Required report fields:

- Mode used.
- Input path.
- Output path.
- Rules applied.
- Blocks detected.
- Warnings.
- Needs review flag.

## Known Limits

Add limits here as they are discovered. Do not hide uncertain behavior in code.
