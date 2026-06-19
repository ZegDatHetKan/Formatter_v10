# Formatter Report — Delega Mediazione Fiorello

**Script:** `_format_delega_mediazione.py`  
**Input:** `input.docx`  
**Output:** `documento_ricevuto_formattato.docx` / `final.docx`  
**Categoria:** GENERICO  
**Data elaborazione:** 2026-06-09

---

## Documento

Tipo: **Delega a partecipare al procedimento di mediazione**  
Riferimento normativo: art. 8, commi 4 e 4-bis, d.lgs. 4 marzo 2010, n. 28  
Deleganti: Fiorello Gianluca e Fiorello Raffaella  
Delegata: Mocchi Francesca  
Organismo: BeeOrange (n. 1097 registro Ministero della Giustizia)

---

## Interventi di formattazione

| # | Paragrafo | Intervento |
|---|-----------|-----------|
| 1 | Titolo principale | CENTER, 16pt bold, Times New Roman |
| 2 | Rif. normativo `(art. 8...)` | CENTER, 10pt italic |
| 4 | `I sottoscritti` | JUSTIFY, 12pt bold, space_before 12pt |
| 5-6 | Righe parti (Fiorello G. e R.) | JUSTIFY, 12pt, rientro 0.5cm; bold su nomi preservato; en dash `–` → `-` |
| 8 | Corpo qualità/oggetto | JUSTIFY, 12pt; bold runs preservati (`proprietari`, `parti istanti`, `BeeOrange`, materia) |
| 10 | `non potendo partecipare...` | JUSTIFY, 12pt; bold su `giustificati motivi` preservato |
| 12 | `DELEGANO` | CENTER, 16pt bold, space_before 14pt (macro-sezione rituale) |
| 13 | Identità delegata | JUSTIFY, 12pt; bold su nome preservato |
| 14 | Poteri conferiti i)-vi) | JUSTIFY, 12pt; bold su etichette poteri preservato |
| 15 | `dando sin d'ora...` | JUSTIFY, 12pt |
| 17 | `Si allega copia...` | JUSTIFY, 12pt bold (era bold nel sorgente) |
| 19 | `Luogo e data:` | LEFT, 12pt, space_before 18pt |
| 21 | `I deleganti` | LEFT, 12pt bold (label firma) |
| 23, 25 | Righe firma deleganti | LEFT, 12pt |
| 28 | `(eventuale) Per autentica...` | RIGHT, 12pt italic; em dash `—` → `-`; allineato a dx per HARD_005 |
| 30 | `Avv. ___` | RIGHT, 12pt bold |
| 32 | Nota `Bozza -...` | CENTER, 10pt italic (disclaimer); em dash → `-` |

---

## Normalizzazioni

- En dash `–` → `-` in apertura righe parti (para 5, 6)
- Em dash `—` → `-` in para 28 e 32
- Tutti i run: font `Times New Roman`, size esplicita
- Paragrafi vuoti consecutivi (para 26-27) ridotti a uno

---

## Struttura mantenuta

- Nessuna modifica al contenuto giuridico
- Placeholder `[DA INSERIRE: ...]` preservati come da sorgente (non sono artefatti OCR)
- Tutti i dati identificativi preservati (C.F., date, riferimenti normativi, numeri iscrizione)
- Separazione data/firma: `Luogo e data` in proprio paragrafo; firme separate
