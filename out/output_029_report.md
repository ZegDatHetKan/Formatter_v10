# Letters Formatter Report

- mode: letters
- input: previous_works/input_029.docx
- output: out/output_029.docx
- needs_review: true

## Rules applied
- normalize: dash->'-', nbsp/zero-width/collapse-spaces
- strip_letterhead (4 righe)
- oggetto: etichetta 16pt bold + contenuto 12pt bold, JUSTIFY, keep_with_next
- template: Template_Vuoto.docx (intestazione preservata)

## Blocks detected (14)
- delivery_method: 'Trasmessa a mezzo PEC'
- date_place: 'Bergamo, lì [DATA INVIO]'
- recipient: 'Spett.le Papi Solutions S.r.l.'
- recipient: 'Via Europa, 41 - 24035 Curno (BG)'
- recipient: 'PEC: [pec destinatario]'
- subject_line: 'OGGETTO: Service Italia S.a.s. di Monzani Ivo Angelo e '
- opening: 'Spett.le Società,'
- body: 'lo scrivente Studio assiste Service Italia S.a.s. di Mo'
- body: 'La pretesa è contestata. Le copie eccedenti addebitate '
- body: 'Ciò nondimeno, al solo fine di definire bonariamente la'
- body: 'La proposta è da intendersi quale offerta finale e non '
- closing_signature: 'In attesa di cortese e sollecito riscontro, si porgono '
- closing_signature: 'Bergamo Legal Società tra Avvocati S.r.l.'
- closing_signature: 'Avv. Matteo Bertocchi'

## Warnings
- placeholder [...] presenti: compilazione manuale richiesta
