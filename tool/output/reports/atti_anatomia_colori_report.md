# Document Anatomy Report

- generated_at: 2026-06-22T13:16:05+00:00
- script: `tool/scripts/build_anatomy_html.py`
- profile: `/tmp/Formatter_v10_push/tool/profiles/acts_discovery_template.json`
- profile_id: `acts_discovery_template`
- client: CLIENTE_DA_CONFERMARE
- document_family: acts
- output: `output/html/atti_anatomia_colori.html`

## Source Of Truth

- `tool/PROCESS.md`
- `docs/acts_formatter_design.md`

## Tool / Formatter Boundary

- This report was produced by the format-definition tool.
- It is a preparation artifact, not a production formatter output.
- Once confirmed, the profile can be handed to `formatters/` for implementation.

## What changed

- Wrote the colored HTML anatomy page.
- Preserved historical input/output files.
- Did not run a production formatter or alter corpus/reference files.

## Blocks rendered

- template: HEADER / carta intestata / eventuale frontespizio - da verificare sugli esempi
- court: TRIBUNALE / CORTE / AUTORITA COMPETENTE
- title: RICORSO / ISTANZA / MEMORIA / DENUNCIA-QUERELA
- party: Per: ricorrente / istante / parte assistita&lt;br&gt;Contro: resistente / intimato / contr
- metadata: Oggetto del giudizio / valore / procedimento / provvedimento impugnato
- section: IN FATTO / IN DIRITTO / RICHIESTE
- subsection: 1. Premessa / 2. Motivo / In via preliminare
- body: Paragrafi argomentativi giustificati, con eventuali citazioni e riferimenti normativi.
- claim: Voglia l&#x27;Ill.mo Tribunale... / In via principale... / In via subordinata...
- exhibit: Si producono: doc. 1, doc. 2, allegati e indice produzioni.
- signature: Luogo, data&lt;br&gt;Avv. Nome Cognome
- needs_review: Blocchi non ricorrenti o ambigui: da discutere prima di automatizzare.

## Client confirmation questions

- Questi blocchi rappresentano tutti i tipi di sezione ricorrenti negli atti?
- Quali blocchi devono essere obbligatori e quali opzionali?
- Quali variazioni devono restare needs_review invece di essere automatizzate?
- Il cliente conferma font, dimensioni, margini, rientri, spaziature e allineamenti?
