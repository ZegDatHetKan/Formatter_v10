# Letters Formatter Report

- mode: letters
- input: examples/esempio_3_comunicazione.docx
- output: out/examples/esempio_3_comunicazione.docx
- needs_review: false

## Rules applied
- normalize: dash->'-', nbsp/zero-width/collapse-spaces
- oggetto: etichetta 16pt bold + contenuto 12pt bold, JUSTIFY, keep_with_next
- template: Template_Vuoto.docx (intestazione preservata)

## Blocks detected (10)
- subject_line: 'Oggetto: Aggiornamento pratica e documenti richiesti'
- opening: 'Gentile Stefania,'
- body: 'la ringrazio per il riscontro fornito nei giorni scorsi'
- body: 'Le confermo che ho provveduto a trasmettere la seguente'
- bullet_item: '• visura camerale aggiornata;'
- bullet_item: "• certificato di iscrizione all'Albo;"
- bullet_item: '• copia di un documento di identità.'
- closing_signature: 'Resto a disposizione per ogni ulteriore chiarimento.'
- closing_signature: 'Cordiali saluti'
- closing_signature: 'Avv. Matteo Bertocchi'

## Warnings
- none
