# Formatter Report — Bergamo Legal
**Data:** 2026-06-05  
**Input:** input.docx  
**Output:** documento_ricevuto_formattato.docx / final.docx  
**Script:** _format_bergamo_uibm.py  
**Categoria:** GENERICO  
**Regole applicate:** regole_di_formattazione.md v4.0

---

## Struttura del documento

Comunicazione formale di ritiro domanda di registrazione marchio d'impresa n. 302025000112666 indirizzata al Ministero delle Imprese e del Made in Italy / UIBM, ai sensi dell'art. 172, comma 1, D.Lgs. 30/2005 (CPI).

**Paragrafi sorgente:** 11 (molti con `\n` interni che fondevano blocchi distinti)  
**Paragrafi output:** 20 (dopo split logico dei blocchi fusi)

---

## Interventi di formattazione

### 1. Separazione paragrafi fusi (`\n` interni)

| Para sorgente | Contenuto fuso | Azione |
|---|---|---|
| 0 | `Bergamo, 5 giugno 2026\nTramite servizio online UIBM / PEC a:` | Split: data → RIGHT; riga trasmissione → dest block |
| 1 | `dgpi-uibm.div06@pec.mimit.gov.it\nSpett.le` | Split: PEC + Spett.le separati |
| 8 | 7 blocchi fusi (corpo, DICHIARA, dichiarazione, MOTIVA, 2 corpo, CHIEDE ALTRESÌ) | Split in 7 paragrafi distinti |
| 9 | `In fede,\nAvv. Matteo Bertocchi` | Split: congedo → RIGHT; firma → RIGHT bold |

### 2. En/em dash → trattino (HARD_004B)

Sostituiti tutti i `–` (en dash) in:
- "Direzione Generale per la Proprietà Industriale – UIBM" → `-`
- "00184 – Roma" → `-`
- OGGETTO: "n. 302025000112666 – ai sensi" → `-`
- Para 5 (Preso atto): "– obiettivo non perseguibile... –" → `-`

### 3. Artefatto OCR (HARD_004)

- `servizionline` → `servizio online` *(vedere verification.md)*

### 4. Gerarchia tipografica applicata

| Elemento | Allineamento | Size | Bold |
|---|---|---|---|
| Data: "Bergamo, 5 giugno 2026" | RIGHT | 12 pt | No |
| Blocco destinatario (8 righe) | LEFT, indent 8.5 cm | 12 pt | No |
| OGGETTO: (label) | CENTER | 16 pt | Sì |
| Contenuto oggetto | CENTER | 12 pt | Sì |
| Corpo introduttivo (Bergamo Legal, titolare) | JUSTIFY | 12 pt | No |
| DICHIARA | CENTER | 16 pt | Sì |
| Testo dichiarazione | JUSTIFY | 12 pt | No |
| MOTIVA il ritiro come segue. | LEFT | 14 pt | Sì |
| Corpo motivazione (2 paragrafi) | JUSTIFY | 12 pt | No |
| CHIEDE ALTRESÌ (inline label) | — | 12 pt | Sì |
| Corpo CHIEDE ALTRESÌ | JUSTIFY | 12 pt | No |
| "In fede," (congedo) | RIGHT | 12 pt | No |
| "Avv. Matteo Bertocchi" (firma) | RIGHT | 12 pt | Sì |
| "(Firma digitale)" | RIGHT | 12 pt | Italic |

### 5. Regole applicate

- **HARD_002**: Template_Vuoto.docx come base ✓
- **HARD_003**: Times New Roman, size esplicita su ogni run ✓
- **HARD_004**: Artefatto OCR rimosso ✓
- **HARD_004B**: En dash sostituiti ✓
- **HARD_005**: Data e firma separate; congedo + firma a destra ✓
- **STYLE_003**: Corpo JUSTIFY, 12 pt ✓
- **STYLE_006**: DICHIARA → CENTER 16 pt bold ✓
- **STYLE_007**: MOTIVA → LEFT 14 pt bold ✓
- **STYLE_008**: OGGETTO label 16 pt bold, contenuto 12 pt bold ✓
- **STYLE_008B**: Blocco destinatario con left_indent = Cm(8.5) ✓
- **STYLE_016**: Firma RIGHT, bold, separata da data ✓
- **HARD_007**: keep_with_next su OGGETTO, DICHIARA, MOTIVA ✓

---

## Nessuna modifica al contenuto giuridico

- Tutti gli identificatori conservati: n. 302025000112666, Codice IUV V2_UIBM_IUV_20255865325, C.F. e P.IVA 04565220169, date, riferimenti normativi
- Nessuna riscrittura o semplificazione
