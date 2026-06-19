# Letters Formatter Report

- mode: letters
- input: examples/esempio_4_riscontro.docx
- output: out/examples/esempio_4_riscontro.docx
- needs_review: true

## Rules applied
- normalize: dash->'-', nbsp/zero-width/collapse-spaces
- strip_letterhead (2 righe)
- oggetto: etichetta 16pt bold + contenuto 12pt bold, JUSTIFY, keep_with_next
- template: Template_Vuoto.docx (intestazione preservata)

## Blocks detected (10)
- date_place: 'Bergamo, lì [DA INSERIRE: data]'
- recipient: 'Egr. Sig. Marco De Luca'
- recipient: 'Via Verdi, 9 - 24121 Bergamo (BG)'
- subject_line: 'OGGETTO: Riscontro alla Vostra del 12 maggio 2026'
- opening: 'Egregio Signore,'
- body: 'in riscontro alla Vostra comunicazione in oggetto, si r'
- body: 'La richiesta non può essere accolta nei termini formula'
- body: 'Si resta a disposizione per un incontro chiarificatore.'
- closing_signature: 'Distinti saluti'
- closing_signature: 'Avv. Daiana Chiappa'

## Warnings
- placeholder [...] presenti: compilazione manuale richiesta
