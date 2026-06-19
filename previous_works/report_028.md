# Formatter Report — Diffida Locafaro

**Data:** 2026-05-28  
**Input:** input.docx  
**Output:** documento_ricevuto_formattato.docx / final.docx  
**Template:** Template_Vuoto.docx  
**Categoria:** GENERICO (Diffida)  
**Script:** _format_diffida_locafaro.py  

---

## Struttura documento

Diffida formale dello Studio Bergamo Legal (Avv. Bertocchi / Avv. Chiappa) per conto di **HORMONAL HOLDING OÜ** (Alessio Casula) nei confronti di **Sig.ra Simona Locafaro** — rimozione di 4 recensioni Trustpilot reiterate su medesimo rapporto contrattuale + astensione da future pubblicazioni.

---

## Paragrafi sorgente elaborati

| Range sorgente | Contenuto | Trattamento |
|---|---|---|
| 0–4 | Header studio | **SKIP** (già nel template) |
| 5 | Bergamo, [DATA INVIO] | RIGHT, 12pt |
| 6 | A mezzo Raccomandata A/R | LEFT, indent 8.5cm (blocco destinatario) |
| 7–12 | Blocco destinatario (Sig.ra Locafaro) | LEFT, indent 8.5cm (STYLE_008B) |
| 13 | OGGETTO | Splittato: label CENTER 16pt bold + descrizione JUSTIFY 12pt bold |
| 14 | `* * *` | **SKIP** (divisore vietato, STYLE_011) |
| 15 | Egregia Signora, | LEFT, 12pt bold |
| 16 | Intro / identificazione cliente | JUSTIFY, 12pt |
| 17 | "Fatto" | Titoletto LEFT 14pt bold, keep_with_next |
| 18 | Par. 1 (elenca 4 recensioni) | JUSTIFY, 12pt |
| 19–22 | Sub-voci (i)–(iv) recensioni | JUSTIFY, 12pt, indent 0.5cm |
| 23–24 | Par. 2–3 | JUSTIFY, 12pt |
| 25 | Par. 4 (profilo "Rossana Marchesini") | JUSTIFY, 12pt |
| 26 | Intro elementi indiziari | JUSTIFY, 12pt |
| 27–31 | Elementi indiziari (i)–(v) | JUSTIFY, 12pt, indent 0.5cm |
| 32 | Nota verifiche tecniche / DSA | JUSTIFY, 12pt |
| 33 | "Diritto" | Titoletto LEFT 14pt bold, keep_with_next |
| 34–36 | Par. 5–7 (motivi giuridici) | JUSTIFY, 12pt (bold inline preservato) |
| 37 | "Tutto ciò premesso..." | JUSTIFY, 12pt bold (formula passaggio) |
| 38 | "DIFFIDA" | CENTER, 16pt bold, keep_with_next, keep_together |
| 39 | "la S.V., come sopra individuata..." | JUSTIFY, 12pt |
| 40–41 | Richieste diffida (i)–(ii) | JUSTIFY, 12pt, indent 0.5cm |
| 42 | Riserva estensione (Rossana Marchesini) | JUSTIFY, 12pt |
| 43 | Avvertimento inadempimento | JUSTIFY, 12pt |
| 44–46 | Azioni minacciate (i)–(iii) | JUSTIFY, 12pt, indent 0.5cm |
| 47–48 | Riserva generale + formula fiduciosa | JUSTIFY, 12pt |
| 49 | "In attesa… distinti saluti." | RIGHT, 12pt (HARD_005 congedo) |
| 50–51 | Avv. Bertocchi / Avv. Chiappa | RIGHT, 12pt bold (STYLE_016) |
| 52–58 | Footer studio | **SKIP** (già nel template) |

---

## Interventi tipografici

- **En dash → hyphen**: tutti i `–` sostituiti con `-` (HARD_004B). Nessun em dash presente.
- **Divisore `* * *`** (para 14): rimosso (STYLE_011 vieta `***`).
- **OGGETTO**: splitato in due paragrafi (label 16pt CENTER + descrizione 12pt JUSTIFY bold).
- **Bold/italic sui run preservati**: tutte le enfasi originali (nomi, URL, riferimenti normativi, *pro tempore*, *Trustpilot*, *Guidelines*, *account*, *deeplink*, *fingerprint*) mantenute.
- **[DATA INVIO]** e **[DA INSERIRE]**: placeholder intenzionali conservati invariati (non artefatti OCR).
- **Data e firma separate**: para 49 (congedo) → RIGHT; para 50–51 (firme) → RIGHT bold. Nessuna fusione (HARD_005).
- **keep_with_next**: attivo su OGGETTO label, Fatto, Diritto, DIFFIDA (HARD_007).

---

## Verifica output

| Check | Esito |
|---|---|
| Font Times New Roman esplicito su ogni run | ✓ |
| Size esplicita su ogni run | ✓ |
| En/em dash assenti | ✓ |
| Gerarchia visiva (16pt titoli, 14pt sottosezioni, 12pt corpo) | ✓ |
| Blocco destinatario indent Cm(8.5) | ✓ |
| Congedo + firme RIGHT | ✓ |
| Data e firma non fuse | ✓ |
| Template corretto (header/footer intatti) | ✓ |
| Margini A4: top 5.91cm, bot 4.54cm, sx/dx 2cm | ✓ |
| keep_with_next su titoli | ✓ |
| Nessun artefatto OCR residuo | ✓ |
| Contenuto giuridico intatto | ✓ |

