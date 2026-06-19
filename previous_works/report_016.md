# Formatter Report

**Job:** 20260527T224227_LEGAL_42ea08a2  
**Data:** 2026-05-27  
**Documento:** Ricorso in opposizione a decreto di revoca della patente di guida - Campos Omar  
**Categoria:** GENERICO (regole_di_formattazione.md, no genere specifico)  
**Script:** _format_ricorso_campos.py  

---

## Output prodotti

| File | Stato |
|---|---|
| documento_ricevuto_formattato.docx | ✓ generato |
| final.docx | ✓ copia identica |
| formatter_report.md | ✓ questo file |
| verification.md | ✓ generato |
| subject.txt | ✓ `ricorso-opposizione-revoca-patente-campos` |

---

## Struttura documento (79 paragrafi)

| Tipo | Elementi | Formattazione applicata |
|---|---|---|
| Intestazione giudiziaria | Giudice di Pace di Brescia | CENTER, 16pt bold |
| Titolo atto + sottotitolo | Ricorso in opposizione... + e istanza... | CENTER, 16pt bold |
| Parti processuali | Parte ricorrente / Parti Intimate / Provvedimento impugnato | LEFT, 14pt bold + corpo JUSTIFY 12pt |
| Oggetto | label + contenuto sintetico | CENTER 16pt bold + JUSTIFY 12pt bold |
| Intestazioni rituali | Premesso che, In fatto, In diritto, tanto premesso, ricorre, Conclusioni | CENTER, 16pt bold |
| Motivi I-V | I - Violazione CC 246/2022, II - Errore fatto, III - Sproporzione, IV - Istruttoria, V - Incongruenze | LEFT, 14pt bold |
| Corpo | Narrativa dei fatti, argomentazioni diritto | JUSTIFY, 12pt |
| Elenchi Art. (Motivo III) | Art. 193, Art. 180 (5 voci) | LEFT, 12pt, indent 0.5cm |
| Elenco incongruenze (Motivo V) | 5 voci | LEFT, 12pt, indent 0.5cm |
| Conclusioni / claims | In via preliminare, Nel merito, In via istruttoria, In ogni caso | LEFT, 14pt bold |
| Produzioni (1-7) | Documenti allegati | LEFT, 12pt, indent 0.5cm |
| Dichiarazione di valore | heading + corpo | LEFT 14pt bold + JUSTIFY 12pt |
| Blocco firma | Con osservanza + data + Avv. Matteo Bertocchi | RIGHT, separati (HARD_005) |

---

## Interventi effettuati

### Artefatti OCR riparati (HARD_004)
- `proclivit[à]` → `proclività`
- `nel[l']infrangere` → `nell'infrangere`

### Normalizzazione dash (HARD_004B)
- Tutti i trattini en-dash `–` sostituiti con `-`
- Conteggio residuo en/em-dash nel documento output: **0**

### Separazione data/firma (HARD_005)
- Riga sorgente fusa: `Bergamo, 12 maggio 2026 [&nbsp;×35] Avv. Matteo Bertocchi`
- Output: tre paragrafi distinti → `Con osservanza.` (RIGHT) | `Bergamo, 12 maggio 2026` (RIGHT) | `Avv. Matteo Bertocchi` (RIGHT, bold)

### Para 0 (letterhead) escluso
- Il Para 0 sorgente (BERGAMO LEGAL, Via Calvi, PEC...) è stato omesso perché già presente in Template_Vuoto.docx (HARD_002)

### Regole not applicable
- Nessuna regola di genere specifica (atti/lettere/pareri) applicata: categoria GENERICO
