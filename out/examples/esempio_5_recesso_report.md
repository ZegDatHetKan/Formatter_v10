# Letters Formatter Report

- mode: letters
- input: examples/esempio_5_recesso.docx
- output: out/examples/esempio_5_recesso.docx
- needs_review: true

## Rules applied
- normalize: dash->'-', nbsp/zero-width/collapse-spaces
- oggetto: etichetta 16pt bold + contenuto 12pt bold, JUSTIFY, keep_with_next
- template: Template_Vuoto.docx (intestazione preservata)

## Blocks detected (14)
- delivery_method: 'A mezzo Raccomandata A/R'
- date_place: 'Bergamo, lì [DA INSERIRE: data]'
- recipient: 'Spett.le Avantgarde Immobiliare S.r.l.'
- recipient: 'Via Montenapoleone, 8 - 20121 Milano (MI)'
- subject_line: 'OGGETTO: Recesso per gravi motivi dal contratto di subl'
- opening: 'Spett.le Società,'
- body: 'con la presente il sottoscritto comunica formalmente qu'
- numbered: '1. Il contratto di sublocazione in oggetto prevede la f'
- numbered: '2. Sono sopravvenuti gravi motivi che impongono la cess'
- body: 'Tanto premesso, il sottoscritto'
- section_center: 'RECEDE'
- body: 'dal contratto con effetto dal [DA INSERIRE: data], nel '
- closing_signature: 'Con osservanza,'
- closing_signature: '[DA INSERIRE: nome e cognome]'

## Warnings
- placeholder [...] presenti: compilazione manuale richiesta
