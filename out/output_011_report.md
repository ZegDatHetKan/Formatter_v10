# Letters Formatter Report

- mode: letters
- input: previous_works/input_011.docx
- output: out/output_011.docx
- needs_review: true

## Rules applied
- normalize: dash->'-', nbsp/zero-width/collapse-spaces
- template: Template_Vuoto.docx (intestazione preservata)

## Blocks detected (8)
- recipient: 'Subject: Procedimento di Mediazione n. 125/2026 - Conse'
- opening: 'Gentile Dott.ssa Corna,'
- body: 'in riscontro alla Sua comunicazione odierna, relativa a'
- body: 'Il consenso è prestato in spirito di leale collaborazio'
- body: 'Resto in attesa della conferma della nuova convocazione'
- closing_signature: 'Cordiali saluti,'
- closing_signature: 'Avv. Matteo Bertocchi'
- closing_signature: 'Bergamo Legal Società tra Avvocati s.r.l.'

## Warnings
- OGGETTO non trovato: preambolo dedotto euristicamente
