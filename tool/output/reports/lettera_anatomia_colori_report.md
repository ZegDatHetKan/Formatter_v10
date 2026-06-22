# Document Anatomy Report

- generated_at: 2026-06-22T13:16:05+00:00
- script: `tool/scripts/build_anatomy_html.py`
- profile: `/tmp/Formatter_v10_push/tool/profiles/bergamo_legal_letters.json`
- profile_id: `bergamo_legal_letters`
- client: Bergamo Legal
- document_family: letters
- output: `output/html/lettera_anatomia_colori.html`

## Source Of Truth

- `docs/letters_formatter_design.md`
- `formatters/letters.py`

## Tool / Formatter Boundary

- This report was produced by the format-definition tool.
- It is a preparation artifact, not a production formatter output.
- Once confirmed, the profile can be handed to `formatters/` for implementation.

## What changed

- Wrote the colored HTML anatomy page.
- Preserved historical input/output files.
- Did not run a production formatter or alter corpus/reference files.

## Blocks rendered

- template: HEADER TEMPLATE: logo, BERGAMO LEGAL, soci e recapiti alti
- delivery: A mezzo PEC / Raccomandata / anticipata via email
- date: Bergamo, li [DA INSERIRE: data]
- recipient: &lt;strong&gt;Spett.le / Egr. Sig.&lt;/strong&gt;&lt;br&gt;Nome destinatario&lt;br&gt;Indi
- subject: &lt;strong class=&quot;subject-label&quot;&gt;Oggetto:&lt;/strong&gt; riepilogo sintetico 
- opening: Egregio Signore, / Spett.le Societa,
- body: Corpo della lettera: paragrafi giustificati, Times New Roman 12 pt, contenuto preservato e
- section: IN FATTO / DIFFIDA / INVITA
- body: Paragrafi argomentativi ordinari dopo il titolo rituale.
- list: 1. Punto numerato con prefisso in grassetto.&lt;br&gt;(i) Sotto-punto o elenco rientrato.
- closing: Cordiali saluti&lt;br&gt;&lt;strong&gt;Avv. Nome Cognome&lt;/strong&gt;
- attachments: &lt;strong&gt;Allegati:&lt;/strong&gt;&lt;br&gt;All. 1 - Documento&lt;br&gt;All. 2 - Docum
- template: FOOTER TEMPLATE: R.E.A., C.F./P.IVA, indirizzi, contatti

## Client confirmation questions

- Il cliente conferma che header/footer e margini vengono dal template?
- Il cliente conferma posizione e stile di destinatario, oggetto, corpo e firma?
- Il cliente conferma quando un caso va in needs_review invece che in fallback generico?
