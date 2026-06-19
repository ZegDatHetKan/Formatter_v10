# Formatter Report — Istanza sospensiva Campos

**Data job:** 2026-06-11  
**Input:** input.docx  
**Output:** documento_ricevuto_formattato.docx / final.docx  
**Categoria:** GENERICO (atto giudiziario — istanza cautelare)  
**Regole applicate:** regole_di_formattazione.md v4.0  

---

## Struttura riconosciuta

| Tipo | Paragrafi output | Trattamento |
|---|---|---|
| Intestazione tribunale | 0–1 | CENTER, bold, 16 pt |
| Titolo atto + sottotitoli | 2–4 | CENTER, bold, 16 pt |
| Parti processuali | 5–11 | JUSTIFY / CENTER 12 pt, inline bold preservato |
| Sintesi istanza (label) | 12 | LEFT, bold, 14 pt |
| Corpo sintesi | 13 | JUSTIFY 12 pt, inline bold preservato |
| "Premesso che:" | 14 | CENTER, bold, 16 pt |
| Premesse numerate 1–4 | 15–18 | JUSTIFY 12 pt |
| "Considerato in diritto" | 19 | CENTER, bold, 16 pt |
| Intestazioni argomento I–III | 20, 22, 27 | LEFT, bold, 14 pt |
| Corpi argomentativi | 21, 23, 28 | JUSTIFY 12 pt |
| Sub-argomenti II.1–II.3 | 24–26 | JUSTIFY 12 pt, label bold inline preservata |
| Formula rituale conclusiva | 29, 31 | CENTER, bold, 16 pt |
| Corpo conclusioni | 30, 32 | JUSTIFY 12 pt |
| Petitum items (–) | 33–35 | JUSTIFY 12 pt, rientro 0.5 cm |
| "Si producono:" | 36 | LEFT, bold, 12 pt |
| Documenti prodotti | 37–38 | LEFT 12 pt, rientro 0.5 cm |
| "Con osservanza." | 39 | RIGHT 12 pt (HARD_005) |
| Data | 40 | RIGHT 12 pt |
| Firma avvocato | 41 | RIGHT, bold, 12 pt |

---

## Interventi effettuati

1. **En dash → trattino normale:** tutti i `–` sostituiti con `-` (HARD_004B). Interessati: intestazione tribunale, par. parti processuali, par. sintesi, paras argomentativi, claims items, produzioni.

2. **Separazione data/firma (HARD_005):** il paragrafo 42 sorgente conteneva `"Bergamo, [DA INSERIRE: data]\tAvv. Matteo Bertocchi"` fusi da un carattere tab. Separati in due paragrafi distinti: data (para 40) e firma (para 41), entrambi RIGHT.

3. **Congedo "Con osservanza." a destra (HARD_005):** il saluto era allineato a sinistra nel sorgente; portato a RIGHT coerentemente col blocco firma.

4. **Font e size espliciti su ogni run:** Times New Roman 16/14/12 pt assegnati su tutti i run (HARD_003).

5. **keep_with_next su tutti i titoletti e intestazioni** (HARD_007).

6. **keep_together su formule rituali brevi** (Premesso che, Considerato in diritto, Tutto ciò premesso, chiede).

7. **Bold inline preservato** su paragrafi argomentativi e sintesi (runs sorgente copiati senza override).

8. **Italic preservato** su *pro tempore*, *medio tempore*, *sub iudice*, *dictum* (cors. tecnico-giuridico originale).

9. **Placeholder `[DA INSERIRE]`, `[DA RICHIEDERE]`, `[EVENTUALE]` preservati integralmente** — non sono artefatti OCR.

---

## Dimensioni e spaziature applicate

| Elemento | space_before | space_after | align | size |
|---|---:|---:|---|---:|
| Intestazione tribunale | 0 | 0/10 pt | CENTER | 16 pt |
| Titolo atto | 4 / 0 pt | 2/10 pt | CENTER | 16 pt |
| Parti processuali | 0–2 pt | 0 pt | JUSTIFY/CENTER | 12 pt |
| Avverso decreto | 0 | 10 pt | JUSTIFY | 12 pt |
| Label "Sintesi" | 10 pt | 4 pt | LEFT | 14 pt |
| Formule rituali | 14 pt | 4–6 pt | CENTER | 16 pt |
| Intestazioni argomento | 10 pt | 4 pt | LEFT | 14 pt |
| Corpo | 0 pt | 6 pt | JUSTIFY | 12 pt |
| Sub-argomenti II.x | 6 pt | 6 pt | JUSTIFY | 12 pt |
| Claims/petitum | 0 pt | 4 pt | JUSTIFY | 12 pt |
| "Si producono:" | 12 pt | 4 pt | LEFT | 12 pt |
| Blocco firma | 16/10/4 pt | 6 pt | RIGHT | 12 pt |

