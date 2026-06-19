# Verification – Lettera Trustpilot – Hormonal Holding

**Data:** 2026-05-28

---

## Verifiche automatiche superate

- Font Times New Roman su ogni run: ✓
- Size 12pt su corpo, 14pt su heading, 16pt su OGGETTO label: ✓
- En-dash sostituiti con hyphen ASCII: ✓
- Paragrafo `* * *` rimosso: ✓
- Blocco destinatario a Cm(8.5): ✓
- Congedo (para 44) RIGHT: ✓
- Firme (para 45-46) RIGHT bold: ✓
- Data (para 0) separata dalla firma: ✓
- Header template non duplicato: ✓
- Footer template non duplicato: ✓
- keep_with_next su heading di sezione: ✓
- Nessun artefatto OCR trovato nel sorgente: ✓

---

## Ambiguità e note editoriali

### Data placeholder `[DATA INVIO]`
Il paragrafo 5 sorgente recita `Bergamo, [DATA INVIO]`. Si tratta di un segnaposto non compilato. Conservato integralmente come da HARD_001. **Nessuna modifica richiesta** a questo formatter; il completamento della data è di competenza del mittente.

### Sottosezioni 3.1 e 3.2
Nel sorgente, `3.1.` e `3.2.` sono label in bold all'inizio di un lungo paragrafo argomentativo (non titoletti standalone). Sono stati trattati come `labeled_body` (12pt, JUSTIFY) con il label `3.1.`/`3.2.` bold preservato. Se si preferisse renderli come titoletti autonomi (14pt LEFT + paragrafo corpo separato), occorrerebbe uno spezzamento manuale del contenuto – scelta legale, non tipografica.

### Segno `ö` in `Hormonal Holding OÜ`
Il testo contiene carattere speciale `Ü` (U con dieresi) nel nome societario estone. Preservato. Nessun intervento OCR.

### Blocco congedo
`Nell'auspicio di un costruttivo riscontro, si porgono distinti saluti.` è nel sorgente in bold. Mantenuto bold e allineato a destra per coerenza con le firme che seguono (HARD_005).

---

## Elementi che richiedono attenzione umana

Nessuno. Il documento è pronto per l'invio previa sostituzione del segnaposto `[DATA INVIO]`.
