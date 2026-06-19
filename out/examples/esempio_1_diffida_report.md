# Letters Formatter Report

- mode: letters
- input: examples/esempio_1_diffida.docx
- output: out/examples/esempio_1_diffida.docx
- needs_review: true

## Rules applied
- normalize: dash->'-', nbsp/zero-width/collapse-spaces
- strip_letterhead (5 righe)
- oggetto: etichetta 16pt bold + contenuto 12pt bold, JUSTIFY, keep_with_next
- template: Template_Vuoto.docx (intestazione preservata)

## Blocks detected (25)
- delivery_method: 'A mezzo Raccomandata A/R, anticipata via email'
- date_place: 'Bergamo, lì [DA INSERIRE: data]'
- recipient: 'Spett.le Beta Costruzioni S.r.l.'
- recipient: 'Via Roma, 12 - 24100 Bergamo (BG)'
- recipient: 'PEC: beta.costruzioni@pec.it'
- subject_line: 'OGGETTO: Diffida ad adempiere - pagamento fatture insol'
- body: 'Egregi Signori,'
- body: 'lo Studio scrivente agisce in nome e per conto della Al'
- section_left: 'Fatto'
- numbered: '1. In data 3 marzo 2026 la Alfa S.p.A. emetteva regolar'
- numbered: '2. Nonostante i solleciti, la S.V. non ha provveduto al'
- enum_item: '(i) fattura n. 14/2026, scaduta il 2 aprile 2026;'
- enum_item: '(ii) fattura n. 21/2026, scaduta il 30 aprile 2026.'
- section_left: 'Diritto'
- numbered: "3. L'inadempimento integra una grave violazione degli a"
- body: 'Tutto ciò premesso e considerato, lo Studio scrivente'
- section_center: 'DIFFIDA'
- body: 'la S.V., come sopra individuata, a voler provvedere ent'
- body: 'In difetto, si procederà nelle competenti sedi giudizia'
- closing_signature: 'In attesa di un cortese e sollecito riscontro, si porgo'
- closing_signature: 'Avv. Matteo Bertocchi'
- closing_signature: 'Avv. Daiana Chiappa'
- attachments: 'Allegati:'
- attachment_item: 'All. 1 - copia fattura n. 14/2026;'
- attachment_item: 'All. 2 - copia fattura n. 21/2026.'

## Warnings
- placeholder [...] presenti: compilazione manuale richiesta
