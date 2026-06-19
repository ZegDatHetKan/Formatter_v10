# Formatter Report — Lettera Trustpilot / Hormonal Holding OÜ

**Data:** 2026-05-28  
**Script:** `_format_lettera_trustpilot.py` (v2)  
**Input:** `input.docx`  
**Output:** `documento_ricevuto_formattato.docx` → copiato in `final.docx`  
**Template:** `Template_Vuoto.docx`

---

## Documento identificato

**Tipo:** Lettera legale professionale (GENERICO)  
**Mittente:** Bergamo Legal – Avv. Matteo Bertocchi / Avv. Daiana Chiappa  
**Destinatario:** Trustpilot A/S – Ufficio Legale, Copenhagen  
**Cliente:** HORMONAL HOLDING OÜ (Registry Code 17263175, Tallinn) – Alessio Casula  
**Oggetto:** (i) accorpamento pagina Trustpilot duplicata; (ii) condotte reiterate di un medesimo reviewer; (iii) rimozione recensioni con dati commerciali riservati  

---

## Paragrafi sorgente: classificazione e trattamento

| Para | Contenuto | Trattamento |
|------|-----------|-------------|
| 0-4 | Studio header (BERGAMO LEGAL, avvocati) | **SKIP** – già nel header del Template_Vuoto.docx |
| 5 | `Bergamo, [DATA INVIO]` | `place_date_line` – RIGHT, 12pt |
| 6 | `Via PEC` | Sopra blocco destinatario – LEFT, indent 8.5 cm |
| 7-12 | Blocco destinatario (Spett.le → PEC) | STYLE_008B – LEFT, indent 8.5 cm |
| 13 | OGGETTO (lungo) | Label `OGGETTO:` 16pt bold; contenuto 12pt bold JUSTIFY. En-dash → `-` |
| 14 | `* * *` | **RIMOSSO** – separatore decorativo vietato (STYLE_011) |
| 15 | `Egregi Signori,` | Saluto apertura – LEFT, 12pt bold (formula rituale, bold confermato) |
| 16-17 | Corpo introduttivo | JUSTIFY, 12pt. Iperlink URL estratto come testo semplice |
| 18 | Titoletto sezione 1 | `subsection_header` – LEFT, 14pt bold, keep_with_next. En-dash → `-` |
| 19-22 | Corpo sezione 1 | JUSTIFY, 12pt |
| 23 | Titoletto sezione 2 | `subsection_header` – LEFT, 14pt bold, keep_with_next. En-dash → `-` |
| 24-26 | Corpo sezione 2 | JUSTIFY, 12pt |
| 27 | Titoletto sezione 3 | `subsection_header` – LEFT, 14pt bold, keep_with_next. En-dash → `-` |
| 28 | Corpo sezione 3 | JUSTIFY, 12pt |
| 29-30 | `3.1.` / `3.2.` (label bold + corpo normale) | JUSTIFY, 12pt, run bold preservati dal sorgente |
| 31 | Conclusione sezione 3 | JUSTIFY, 12pt |
| 32 | Titoletto sezione 4 | `subsection_header` – LEFT, 14pt bold, keep_with_next |
| 33 | Intro elenco (chiude con ":") | JUSTIFY, 12pt, space_after 4pt |
| 34-36 | Voci (i) (ii) (iii) | JUSTIFY, 12pt, left_indent 0.5 cm |
| 37 | Corpo finale | JUSTIFY, 12pt |
| 38 | `Nell'auspicio… distinti saluti.` | Congedo – RIGHT, 12pt bold (HARD_005) |
| 39-40 | `Avv. Matteo Bertocchi` / `Avv. Daiana Chiappa` | RIGHT, 12pt bold (HARD_005, STYLE_016) |
| 41 | Paragrafo vuoto | **SKIP** |

---

## Interventi di formattazione

1. **En/em dash sostituiti:** tutti i `–` e `—` convertiti in `-` (HARD_004B). Occorrenze nei titoletti sezione 1, 2, 3 e nei corpi para 11, 15, 22, 27, 31.
2. **Separatore `* * *` rimosso** (para 14): separatore decorativo vietato per STYLE_011.
3. **Header studio rimosso dal corpo:** i para 0-4 (BERGAMO LEGAL, avvocati) sono già nel header di Template_Vuoto.docx; non duplicati nel body.
4. **Hyperlink URL estratto come testo semplice:** `https://it.trustpilot.com/review/www.oasiormonale.com` era in un elemento `w:hyperlink` (non accessibile via `p.runs`); estratto con parser XML diretto. Nessuna sottolineatura/colore blu.
5. **Blocco destinatario a destra:** `left_indent = Cm(8.5)` su `Via PEC` + 6 righe destinatario (STYLE_008B).
6. **OGGETTO:** label `OGGETTO:` a 16pt bold, contenuto a 12pt bold, tutto JUSTIFY. La parola `reviewer` nel testo dell'oggetto preservata in italic bold come da sorgente.
7. **Congedo e firme a destra:** `Nell'auspicio…` (bold), `Avv. Matteo Bertocchi`, `Avv. Daiana Chiappa` tutti RIGHT (HARD_005).
8. **keep_with_next=True** su tutti i titoletti di sezione (para 12, 17, 21, 26 output).

---

## Verifica checklist (HARD_006)

| Check | Esito |
|-------|-------|
| Font Times New Roman su ogni run | ✅ |
| Size esplicita su ogni run | ✅ |
| Contenuto giuridico preservato | ✅ |
| Date/importi/nomi/codici/ref normativi intatti | ✅ |
| En/em dash sostituiti | ✅ |
| Artefatti OCR rimossi | N/A – documento pulito |
| Separatore decorativo rimosso | ✅ |
| Data e firma non fuse | ✅ |
| Congedo + firme a destra | ✅ |
| Template_Vuoto.docx usato | ✅ |
| Paragrafi vuoti: max uno consecutivo | ✅ (nessuno) |
| Titoletti con keep_with_next | ✅ |
