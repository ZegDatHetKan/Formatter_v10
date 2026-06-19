# Formatter Report – Lettera Trustpilot – Hormonal Holding

**Data:** 2026-05-28  
**Categoria:** GENERICO  
**Script:** `_format_trustpilot.py`  
**Template:** `Template_Vuoto.docx`

---

## Struttura documento

| Blocco | Para sorgente | Para output | Trattamento |
|---|---|---|---|
| Header studio (template) | 0-4 | — | SKIP: già nel header template |
| Data lettera | 5 | 0 | RIGHT, 12pt |
| Via PEC | 6 | 1 | LEFT, Cm(8.5), 12pt |
| Blocco destinatario | 7-12 | 2-7 | LEFT, Cm(8.5), 12pt |
| OGGETTO: (label) | 13 | 8 | CENTER, 16pt bold, keep_with_next |
| OGGETTO: (contenuto) | 13 | 9 | JUSTIFY, 12pt bold |
| Separatore `* * *` | 14 | — | RIMOSSO (HARD_004: elemento decorativo) |
| Saluto apertura | 15 | 10 | LEFT, 12pt bold |
| Introduzione | 16-17 | 11-12 | JUSTIFY, 12pt, runs preservati |
| Sezione 1 heading | 18 | 13 | LEFT, 14pt bold, keep_with_next |
| Corpo sezione 1 | 19-22 | 14-17 | JUSTIFY, 12pt |
| Sezione 2 heading | 23 | 18 | LEFT, 14pt bold, keep_with_next |
| Corpo intro sezione 2 | 24 | 19 | JUSTIFY, 12pt |
| Voci (a)(b) | 25-26 | 20-21 | JUSTIFY, 12pt, Cm(0.5) |
| Corpo intermedio | 27 | 22 | JUSTIFY, 12pt |
| Voci (i)-(v) | 28-32 | 23-27 | JUSTIFY, 12pt, Cm(0.5) |
| Corpo dopo (i)-(v) | 33-34 | 28-29 | JUSTIFY, 12pt |
| Voci (α)(β) | 35-36 | 30-31 | JUSTIFY, 12pt, Cm(0.5) |
| Corpo dopo (β) | 37 | 32 | JUSTIFY, 12pt |
| Sezione 3 heading | 38 | 33 | LEFT, 14pt bold, keep_with_next |
| Corpo sezione 3 | 39 | 34 | JUSTIFY, 12pt |
| Sottosezioni 3.1 e 3.2 | 40-41 | 35-36 | JUSTIFY, 12pt, labeled_body (bold label interno) |
| Corpo conclusivo sez. 3 | 42 | 37 | JUSTIFY, 12pt |
| Sezione 4 heading | 43 | 38 | LEFT, 14pt bold, keep_with_next |
| Corpo sezione 4 | 44 | 39 | JUSTIFY, 12pt |
| Voci (i)(ii)(iii) | 45-47 | 40-42 | JUSTIFY, 12pt, Cm(0.5) |
| Corpo chiusura | 48 | 43 | JUSTIFY, 12pt |
| Congedo | 49 | 44 | RIGHT, 12pt bold |
| Firme | 50-51 | 45-46 | RIGHT, 12pt bold |
| Footer studio (template) | 52-58 | — | SKIP: già nel footer template |

---

## Decisioni di formattazione

- **OGGETTO**: splittato in due paragrafi (label 16pt CENTER + contenuto 12pt bold JUSTIFY) per lunghezza del contenuto (>300 caratteri).
- **`* * *`**: rimosso come sequenza decorativa (HARD_004).
- **En-dash `–` e `—`**: sostituiti con `-` ASCII ovunque (HARD_004B) – presenti in 14+ paragrafi sorgente.
- **Blocco destinatario**: Cm(8.5) left_indent per allineamento al centro-destra (STYLE_008B).
- **3.1 e 3.2**: trattati come `labeled_body` (12pt JUSTIFY) con label bold interna preservata; il contenuto argomentativo è incorporato nel paragrafo, non è un titoletto autonomo.
- **Congedo e firme**: RIGHT (HARD_005).
- **Keep_with_next**: sui 4 heading di sezione (1, 2, 3, 4).
- **Font**: Times New Roman esplicito su ogni run.
- **Runs interni**: bold/italic del sorgente preservati su tutti i paragrafi corpo (evidenze, riferimenti normativi, termini tecnici, nomi).

---

## Verifica criteri HARD

| Criterio | Stato |
|---|---|
| HARD_001: Contenuto intoccabile | ✓ Nessuna modifica sostanziale |
| HARD_002: Template_Vuoto.docx | ✓ |
| HARD_003: Font/size espliciti su ogni run | ✓ |
| HARD_004: Artefatti rimossi | ✓ `* * *` rimosso; nessun artefatto OCR trovato |
| HARD_004B: En-dash → hyphen | ✓ |
| HARD_005: Data e firma separate | ✓ Data (para 0), congedo (para 44), firme (para 45-46) |
| HARD_006: Output verificabile | ✓ Verifica completa eseguita |
| HARD_007: Titoletti orfani | ✓ keep_with_next su tutti i heading |
