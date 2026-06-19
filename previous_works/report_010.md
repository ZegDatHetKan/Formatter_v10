# Formatter Report — Diffida tecnico

**Data:** 2026-06-10  
**Input:** input.docx  
**Output:** documento_ricevuto_formattato.docx / final.docx  
**Genere:** GENERICO (diffida professionale)  
**Script:** _format_diffida.py  

---

## Struttura documento

32 paragrafi sorgente → 33 paragrafi output (split OGGETTO in label+contenuto).

| Para | Tipo | Trattamento |
|---|---|---|
| 0 | Metodo invio (Raccomandata a.r.) | LEFT bold 12pt |
| 1-5 | Blocco destinatario | LEFT, left_indent=8.5cm (STYLE_008B) |
| 6 | Data | RIGHT 12pt |
| 7a | OGGETTO: label | CENTER 16pt bold (STYLE_008) |
| 7b | OGGETTO: contenuto | CENTER 12pt bold (STYLE_008) |
| 8 | Introduzione corpo | JUSTIFY 12pt |
| 9 | PREMESSO CHE | CENTER 16pt bold (STYLE_006) |
| 10-14 | Premesse numerate 1-5 | JUSTIFY 12pt, bold/italic preserved |
| 15 | CONSIDERATO CHE | CENTER 16pt bold (STYLE_006) |
| 16-17 | Corpo sotto CONSIDERATO CHE | JUSTIFY 12pt, bold preserved |
| 18 | Transizione "tutto ciò premesso..." | CENTER 12pt bold (formula di transizione) |
| 19 | D I F F I D A   E   I N T I M A | CENTER 16pt bold (STYLE_006) |
| 20 | Intro elenco (la S.V., Sig...) | JUSTIFY 12pt |
| 21-23 | Elenco i) ii) iii) | JUSTIFY 12pt, left_indent=0.5cm |
| 24 | Termine 15 giorni | JUSTIFY 12pt |
| 25 | AVVERTIMENTO | JUSTIFY 12pt, bold preserved |
| 26-27 | Mora / facoltà osservazioni | JUSTIFY 12pt |
| 28 | Distinti saluti | RIGHT 12pt (HARD_005) |
| 29 | Bergamo Legal - Società... | RIGHT 12pt bold |
| 30 | Avv. Matteo Bertocchi | RIGHT 12pt bold |
| 31 | Riga firma ___ | RIGHT 12pt |

---

## Interventi applicati

- **Em dash → trattino:** sostituiti tutti i `—` con `-` (HARD_004B) in: para 7, 8, 14, 21, 23, 29.
- **OGGETTO split:** separata label `OGGETTO:` (16pt bold CENTER) dal contenuto (12pt bold CENTER) per conformità a STYLE_008.
- **Destinatario right-indented:** left_indent=Cm(8.5) su paras 1-5 per STYLE_008B.
- **Formula DIFFIDA spazi preservati:** `D I F F I D A   E   I N T I M A` — spazi tripli attorno a "E" mantenuti (STYLE_011: preservare lettere spaziate rituali). NON applicata normalizzazione spazi multipli.
- **Distinti saluti → RIGHT:** allineato a destra come richiesto da HARD_005 (saluto che introduce firma).
- **keep_with_next:** applicato su PREMESSO CHE, CONSIDERATO CHE, DIFFIDA, transizione, Distinti saluti, firma.
- **Bold/italic preservati:** tutti i runs con bold/italic originali mantenuti (dates, amounts, citazioni, etichette numerate).
- **[DA INSERIRE: ...]:** preservati intatti come placeholder legali.

---

## Verifiche finali

- Font Times New Roman: OK (tutti i run)
- Size valide (12pt/16pt): OK
- Em dash residui: nessuno
- Artefatti OCR: nessuno nel sorgente
- Data e firma separate: OK (paragrafi distinti)
- Congedo (Distinti saluti) a destra: OK
