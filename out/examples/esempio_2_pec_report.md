# Letters Formatter Report

- mode: letters
- input: examples/esempio_2_pec.docx
- output: out/examples/esempio_2_pec.docx
- needs_review: true

## Rules applied
- normalize: dash->'-', nbsp/zero-width/collapse-spaces
- oggetto: etichetta 16pt bold + contenuto 12pt bold, JUSTIFY, keep_with_next
- template: Template_Vuoto.docx (intestazione preservata)

## Blocks detected (13)
- delivery_method: 'Trasmessa a mezzo PEC'
- date_place: 'Bergamo, lì [DA INSERIRE: data]'
- recipient: 'Spett.le Gamma Servizi S.r.l.'
- recipient: 'Via Europa, 41 - 24035 Curno (BG)'
- recipient: 'PEC: gamma.servizi@pec.it'
- subject_line: 'OGGETTO: Contestazione fattura n. 88/2026'
- opening: 'Spett.le Società,'
- body: 'lo scrivente Studio assiste la Delta S.a.s. in relazion'
- body: 'La pretesa è integralmente contestata in quanto riferit'
- body: 'Si invita pertanto Codesta Società a emettere nota di c'
- closing_signature: 'In attesa di cortese riscontro, si porgono distinti sal'
- closing_signature: 'Bergamo Legal Società tra Avvocati S.r.l.'
- closing_signature: 'Avv. Matteo Bertocchi'

## Warnings
- placeholder [...] presenti: compilazione manuale richiesta
