# Formatter Report

**Job:** 20260616T181958_Spett_GESTIONI_AMMINISTRATIVE  
**Data:** 2026-06-16  
**Script:** `_format_lettera_recesso.py`  
**Categoria:** GENERICO  
**Regole applicate:** `regole_di_formattazione.md` v4.0  

---

## Documento ricevuto

**Tipo:** Lettera legale - recesso per gravi motivi (sublocazione commerciale)  
**Mittente:** Avv. Matteo Bertocchi per conto di AVANTGARDE S.R.L.  
**Destinatario:** GESTIONI AMMINISTRATIVE S.R.L.  
**Oggetto:** Recesso ex art. 27 c. 8 L. 392/1978 dal contratto di sublocazione del 22/06/2023  
**Struttura sorgente:** 5 paragrafi, con \n interni - testo aggregato da conversione OCR/incolla

---

## Operazioni eseguite

### Struttura e split
- Para[0] (destinatario + data header + trasmissione) → separato in 7 paragrafi distinti
- Para[2] (corpo lettera 5135 char, tutto in un run) → separato in 28 paragrafi logici su `\n`
- Para[4] (nome + campo firma su \n) → separato in 2 paragrafi distinti

### Layout applicato

| Elemento | Allineamento | Size | Bold |
|---|---|---|---|
| Destinatario (Spett.le…) | LEFT + indent 8.5 cm | 12 pt | solo ragione sociale |
| Luogo e data (header) | LEFT | 12 pt | no |
| Trasmessa a mezzo… | LEFT italic | 12 pt | no |
| OGGETTO: (label) | CENTER | 16 pt | sì |
| Oggetto (contenuto) | JUSTIFY | 12 pt | sì |
| Saluto apertura | JUSTIFY | 12 pt | no |
| Corpo testo | JUSTIFY | 12 pt | no |
| PREMESSO CHE / CONSIDERATO CHE / DICHIARA / INVITA | CENTER | 16 pt | sì |
| Items numerati top-level (1. 2. …) | JUSTIFY | 12 pt | no |
| Sub-items (1.1 1.2 …) | JUSTIFY + indent 0.5 cm | 12 pt | no |
| Lista romana i) ii) iii) iv) | JUSTIFY + indent 1.0 cm | 12 pt | no |
| Riserva / Si fa espressa riserva… | JUSTIFY | 12 pt | no |
| Congedo (Nell'auspicio… distinti saluti) | RIGHT | 12 pt | no |
| Luogo e data (firma) | RIGHT | 12 pt | no |
| Avv. Matteo Bertocchi | RIGHT | 12 pt | sì |
| Campo firma (___) | RIGHT | 12 pt | no |

### Pulizia artefatti
- En-dash `–` → `-` in "Via Provinciale n. 67" ✓
- Em-dash `—` → `-` in "[DATA - non anteriore a sei mesi...]" ✓
- Tabs `\t` → spazio singolo negli items i) ii) iii) iv) ✓
- Regex OCR artifacts `[x]` applicata (nessun caso trovato nel testo) ✓

### Vincoli HARD rispettati
- **HARD_001**: Contenuto giuridico intatto; [DA INSERIRE] e valori numerici preservati
- **HARD_002**: Template_Vuoto.docx base; margini top=5.91cm bot=4.54cm sx=2cm dx=2cm ✓
- **HARD_003**: Times New Roman, size esplicito su ogni run ✓
- **HARD_004**: Nessun artefatto HTML/ZWS; dash convertiti ✓
- **HARD_004B**: Tutti en/em-dash convertiti a `-` ✓
- **HARD_005**: Data e firma separate; congedo + firma + data tutti RIGHT ✓
- **HARD_007**: `keep_with_next=True` sulle macro-sezioni (PREMESSO CHE, CONSIDERATO CHE, DICHIARA, INVITA) ✓

---

## File prodotti

- `documento_ricevuto_formattato.docx`
- `final.docx` (copia identica)
- `formatter_report.md`
- `verification.md`
- `subject.txt`
