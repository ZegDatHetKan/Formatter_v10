# Formatter Report — Esposizione dei Fatti e Riferimenti Normativi

**Data:** 2026-06-09  
**Job:** 20260609T134107_queue_GKkJ831k5go  
**Categoria:** GENERICO  
**Script:** `_format_esposizione_mediazione.py`

---

## Struttura documento

| Para (input) | Tipo | Trattamento |
|---|---|---|
| 0 | Titolo principale | CENTER, bold, 16pt |
| 1 | Sottotitolo descrittivo | CENTER, bold, 16pt (STYLE_005) |
| 2 | Paragrafo vuoto | Saltato (spaziatura tramite space_after) |
| 3, 5, 10 | Intestazioni di sezione (I./II./III.) | LEFT, bold, 14pt, keep_with_next |
| 12 | ACCENNI NORMATIVI E GIURISPRUDENZIALI | LEFT, bold, 14pt, keep_with_next |
| 19 | ALLEGATI | LEFT, bold, 14pt, keep_with_next |
| 4, 6-9, 11, 13-18 | Corpo (paragrafi numerati + argomentativi) | JUSTIFY, 12pt, bold/italic run-level preservati |
| 20-23 | Voci allegato (All. 1-4) | LEFT, 12pt, rientro 0.5cm |

---

## Interventi tipografici

- **En dash/Em dash → `-`:** sostituiti in 5 occorrenze (sottotitolo para 1, para 6 run 6, para 7 run 1, para 20, altri allegati)
- **Italic preservato:** `restitutio in integrum`, `in re ipsa`, `culpa in eligendo`, `diligentia quam in concreto` — tutti correttamente ereditati dai run originali
- **Bold preservato run-level:** numerazioni (1., 2., ..., 9.), label di paragrafo, termini giuridici chiave, riferimenti normativi in grassetto, rimandi ad allegati (All. 1–4)
- **Nessun artefatto OCR** rilevato nel testo sorgente
- **Nessun blocco firma/data** nel documento (allegato a istanza di mediazione, nessun congedo)

---

## Font e size

| Elemento | Font | Size | Bold |
|---|---|---|---|
| Titolo principale | Times New Roman | 16pt | sì |
| Sottotitolo | Times New Roman | 16pt | sì |
| Intestazioni sezione | Times New Roman | 14pt | sì |
| Corpo | Times New Roman | 12pt | per run |
| Voci allegato | Times New Roman | 12pt | no |

---

## Output

- `documento_ricevuto_formattato.docx` ✅
- `final.docx` ✅
- `subject.txt` ✅
- Paragrafi non vuoti: 23/23 preservati
- Contenuto giuridico: intatto (nomi, importi, date, riferimenti normativi, giurisprudenza verificati)
