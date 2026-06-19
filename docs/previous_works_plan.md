# Previous Works Corpus Plan

## Source

Historical archive extracted on the remote server:

```text
/home/bgl1/inspect_2026-20260619T124623Z-3-001
```

The archive contains 32 completed or partially completed formatter jobs. Each job usually has:

- `input/original.docx`
- `output/*.docx`
- `reports/*-formatter_report.md`
- `reports/*-verification.md`
- `logs/claude_result.json`
- `workspace/subject.txt`

## Destination

Create:

```text
previous_works/
  input_001.docx
  output_001.docx
  report_001.md
  verification_001.md
  ...
  manifest.json
```

Do not modify the historical output documents after copying them.

## Manifest Fields

Each manifest record must include:

```json
{
  "id": "001",
  "document_type": "letters",
  "subject": "lettera-informativa-consiglieri-mueller-madone",
  "original_job_path": "2026/giugno/04/...",
  "original_input_name": "original.docx",
  "original_output_name": "lettera-informativa-consiglieri-mueller-madone.docx",
  "input_path": "previous_works/input_001.docx",
  "output_path": "previous_works/output_001.docx",
  "report_path": "previous_works/report_001.md",
  "verification_path": "previous_works/verification_001.md",
  "classification_confidence": "high",
  "feedback_notes": [],
  "known_issues": [],
  "desired_rule_change": [],
  "resolved_by_script": false
}
```

## Initial Classification

Use this as the starting point. Re-check with document contents before locking it.

### Letters

- `001` lettera-informativa-consiglieri-mueller-madone
- `002` lettera-consiglieri-comunali-muller-madone
- `003` pec-contestazione-fattura-papi-solutions
- `004` comunicazione-ritiro-marchio-uibm-bergamo-legal
- `005` comunicazione-apple-business-duns-bertocchi
- `007` diffida-rimozione-recensioni-casu
- `010` diffida-pagamento-restituzione-tecnico-bertocchi
- `011` comunicazione-consenso-differimento-mediazione-chebotareva
- `013` lettera-riscontro-contestazione-de-luca
- `015` recesso-gravi-motivi-sublocazione-avantgarde
- `025` lettera-trustpilot-recensioni-hormonal-casula
- `027` lettera-trustpilot-hormonal-holding-recensioni
- `028` diffida-rimozione-recensioni-locafaro
- `029` pec-contestazione-fattura-papi-solutions
- `032` aggiornamento-duns-apple-business-bertocchi

### Acts

- `012` istanza-sospensiva-campos-revoca-patente
- `014` memoria-replica-ads-melocchi-colnaghi
- `016` ricorso-opposizione-revoca-patente-campos
- `017` ricorso-opposizione-revoca-patente-campos
- `018` ricorso-opposizione-revoca-patente-campos
- `019` ricorso-opposizione-revoca-patente-campos
- `020` ricorso-opposizione-revoca-patente-campos
- `021` ricorso-opposizione-revoca-patente-campos
- `022` ricorso-opposizione-revoca-patente-campos
- `023` ricorso-opposizione-revoca-patente-campos
- `024` memoria-replica-giudice-tutelare-colnaghi
- `026` memoria-replica-istanza-ads-colnaghi
- `030` memoria-replica-istanza-ads-colnaghi
- `031` denuncia-querela-vishing-dolazza

### Other Pending Name

- `006` delega-procedimento-mediazione-fiorello
- `008` esposizione-fatti-norme-mediazione-cantiere
- `009` esposizione-fatti-norme-mediazione-immissioni

## Validation

After corpus creation:

- Confirm exactly 32 manifest records.
- Confirm every input has an output.
- Confirm original names are preserved.
- Confirm every copied file opens or can be inspected.
- Mark uncertain classification as `needs_review`.
