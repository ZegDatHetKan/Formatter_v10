# Formatter Report – PEC Contestazione Papi Solutions

**Data:** 2026-06-04  
**Script:** `_format_pec_papi.py`  
**Input:** `input.docx` (20 paragrafi)  
**Output:** `documento_ricevuto_formattato.docx` (17 paragrafi), `final.docx`  
**Categoria:** GENERICO – lettera/PEC legale  
**Template:** `Template_Vuoto.docx`

---

## Struttura rilevata

| # input | Contenuto | Trattamento |
|---|---|---|
| 0-2 | Header studio (BERGAMO LEGAL…) | **SALTATI** – già nel template |
| 3 | Paragrafo vuoto | SALTATO |
| 4 | "Trasmessa a mezzo PEC" | Italic, RIGHT, 12pt |
| 5 | "Bergamo, lì [DATA INVIO]" | RIGHT, 12pt, space_after=14 |
| 6-9 | Blocco destinatario (Spett.le, Papi Solutions…) | LEFT, indent=8.5 cm (STYLE_008B) |
| 10 | OGGETTO + contenuto | Diviso in 2 para: label 16pt bold CENTER + contenuto 12pt bold CENTER |
| 11 | "Spett.le Società," | JUSTIFY, 12pt |
| 12-16 | Corpo lettera (5 para) | JUSTIFY, 12pt, bold inline preservato |
| 17 | Congedo "In attesa… distinti saluti" | RIGHT, 12pt (HARD_005) |
| 18 | "Bergamo Legal Società tra Avvocati S.r.l." | RIGHT, 12pt tondo |
| 19 | "Avv. Matteo Bertocchi" | RIGHT, 12pt bold |

---

## Interventi di formattazione

### Dash (HARD_004B)
- Sostituiti tutti gli en dash `–` e em dash `—` con trattino ASCII `-`
- Occorrenze corrette: indirizzo destinatario, oggetto (×2), data range par. contestazione, inciso par. cessazione rapporto
- **Verifica finale:** 0 en/em dash rimasti nel documento

### Header studio
- Para 0-2 dell'input omessi: duplicano l'intestazione già presente nel template

### OGGETTO (STYLE_008)
- Label `OGGETTO:` → para separato, 16pt bold CENTER, keep_with_next=True
- Contenuto oggetto → para separato, 12pt bold CENTER

### Blocco destinatario (STYLE_008B)
- Indent left = 8.5 cm su tutti i para del blocco
- Allineamento LEFT

### Congedo e firma (HARD_005)
- Congedo ("In attesa… distinti saluti") → RIGHT (stesso lato della firma)
- Firma studio + avvocato → RIGHT, separati in paragrafi distinti

### Bold inline
- Preservato integralmente in tutti i paragrafi di corpo (entità, date, importi, formule chiave)

---

## Verifica finale checklist

| Check | Esito |
|---|---|
| Font Times New Roman su ogni run | ✅ |
| Size esplicita su ogni run | ✅ |
| Header studio non duplicato | ✅ |
| Blocco destinatario indent 8.5 cm | ✅ |
| OGGETTO: 16pt label + 12pt contenuto | ✅ |
| Corpo JUSTIFY 12pt | ✅ |
| Bold inline preservato | ✅ |
| En/em dash → trattino ASCII | ✅ (0 rimasti) |
| Data e firma separati | ✅ |
| Congedo a destra | ✅ |
| Firma a destra | ✅ |
| Nessun artefatto OCR rilevato | ✅ |
| Template usato | ✅ |
