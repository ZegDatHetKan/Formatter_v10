# Formatter Report — diffida Casu / Hormonal Holding OÜ

**Data elaborazione:** 2026-06-09  
**Script:** `_format_diffida_casu.py`  
**Input:** `input.docx` (47 paragrafi)  
**Output:** `documento_ricevuto_formattato.docx` / `final.docx` (48 paragrafi)  
**Categoria:** GENERICO

---

## Struttura riconosciuta

| Blocco | Paragrafi sorgente | Formato applicato |
|---|---|---|
| Data | 0 | RIGHT, 12pt, bold su [DA INSERIRE] preservato |
| Modalità invio | 1 | JUSTIFY, 12pt |
| Blocco destinatario (Casu) | 2–4 | LEFT, 12pt, left_indent=8.5cm (STYLE_008B) |
| Invio email anticipato | 5–6 | LEFT, 12pt, left_indent=8.5cm |
| OGGETTO: label | 7 (split) | CENTER, 16pt bold (HARD_003) |
| OGGETTO: contenuto | 7 (split) | JUSTIFY, 12pt bold (STYLE_008), italic preservato su nomi piattaforme |
| Saluto iniziale | 8 | JUSTIFY, 12pt bold |
| Apertura studio/assistito | 9 | JUSTIFY, 12pt |
| Sezione "Fatto" | 10 | LEFT, 14pt bold, kwn=True (STYLE_007) |
| Paragrafi 1–2 + sub 1.1–1.3 | 11–15 | JUSTIFY, 12pt, bold/italic preservati |
| Intro lista para 3 | 16 | JUSTIFY, 12pt |
| Lista (i)–(iv) | 17–20 | JUSTIFY, 12pt, indent=0.5cm (STYLE_012) |
| Nota tecnica | 21 | JUSTIFY, 12pt |
| Sezione "Diritto" | 22 | LEFT, 14pt bold, kwn=True (STYLE_007) |
| Paragrafi 4–7 | 23–26 | JUSTIFY, 12pt, bold/italic preservati |
| Formula transizione | 27 | JUSTIFY, 12pt bold, kwn=True |
| DIFFIDA | 28 | CENTER, 16pt bold, kwn=True (STYLE_006) |
| Corpo diffida | 29 | JUSTIFY, 12pt |
| Lista diffida (i)–(iii) | 30–32 | JUSTIFY, 12pt, indent=0.5cm |
| Avvertimento riserva | 33 | JUSTIFY, 12pt |
| Lista azioni (i)–(iv) | 34–37 | JUSTIFY, 12pt, indent=0.5cm |
| Paragrafi chiusura | 38–39 | JUSTIFY, 12pt |
| Congedo/saluto | 40 | RIGHT, 12pt italic (HARD_005: firma a destra → congedo a destra) |
| Firme avvocati | 41–42 | RIGHT, 12pt bold (STYLE_016) |
| Allegati label | 43 | LEFT, 12pt bold |
| Voci allegati | 44–46 | LEFT, 12pt, indent=0.5cm |

---

## Interventi applicati

- **OGGETTO split:** il paragrafo sorgente contenente `OGGETTO: Diffida - ...` è stato separato in due paragrafi: label `OGGETTO:` (16pt bold CENTER) e contenuto (12pt bold JUSTIFY), per rispettare STYLE_008/HARD_003.
- **Congedo spostato a destra:** il saluto "In attesa di un cortese, sollecito riscontro, si porgono distinti saluti." era JUSTIFY nel sorgente; corretto a RIGHT per HARD_005 (firma a destra).
- **Blocco destinatario:** paragrafi 2–6 impostati con `left_indent=8.5cm` per STYLE_008B.
- **En/em dash:** nessun en-dash o em-dash trovato nel sorgente (tutti i `-` erano già ASCII).
- **Artefatti OCR:** nessun artefatto OCR rilevato nel testo.
- **Bold/italic:** preservati fedelmente dai runs sorgente; eccezioni documentate (bold forzato su contenuto OGGETTO per STYLE_008; italic forzato su congedo; bold forzato su firme).
- **Font e size:** espliciti su ogni run (Times New Roman, size dichiarata).
- **keep_with_next:** applicato su "Fatto", "Diritto", "Tutto ciò premesso...", "DIFFIDA".
- **Dato/firma mai fusi:** data a para 0 (RIGHT), firme a paras 41–42 (RIGHT).

---

## Verifica HARD_006

| Check | Esito |
|---|---|
| Font Times New Roman su tutti i run | ✓ |
| Size esplicita su tutti i run | ✓ |
| OGGETTO: 16pt bold CENTER | ✓ |
| Sezioni Fatto/Diritto: 14pt bold LEFT | ✓ |
| DIFFIDA: 16pt bold CENTER | ✓ |
| Corpo: 12pt JUSTIFY | ✓ |
| Congedo a destra | ✓ |
| Firme a destra | ✓ |
| Data separata da firma | ✓ |
| Nessun artefatto en/em dash | ✓ |
| Contenuto giuridico preservato | ✓ |
| Template corretto (Template_Vuoto.docx) | ✓ |
