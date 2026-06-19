# Formatter Report — Lettera Consiglieri Madone

**Script:** `_format_lettera_madone.py`  
**Input:** `input.docx` (36 paragrafi)  
**Output:** `documento_ricevuto_formattato.docx` (33 paragrafi), `final.docx`  
**Categoria:** GENERICO  
**Data elaborazione:** 2026-06-04

---

## Struttura identificata

Lettera formale da Ing. Sergio Müller (cittadino di Madone, assistito dagli Avv. Bertocchi e Chiappa – Bergamo Legal) indirizzata individualmente a ciascun Consigliere del Comune di Madone. Documento tipo BOZZA (segnaposto "[DA INSERIRE]" per destinatario e data).

---

## Interventi di formattazione

### Layout

| Blocco | Trattamento |
|---|---|
| Mittente (0-2) | LEFT, 12pt, bold su nome |
| Nota trasmissione (3) | LEFT, 10pt, bold sui nomi avvocati preservato |
| Destinatario (4-8) | STYLE_008B: left_indent=8.5cm, LEFT, 12pt |
| Data intestazione (9) | RIGHT, 12pt |
| OGGETTO (10) | JUSTIFY; label "OGGETTO: " 16pt bold; contenuto 12pt bold |
| Saluto apertura (11) | JUSTIFY, 12pt bold (formula rituale) |
| Corpo (12, 15-18, 21-22, 26-28, 29, 30) | JUSTIFY, 12pt, bold/italic run-level preservati |
| IN FATTO / IN DIRITTO (14, 20) | CENTER, 16pt bold, space_before=14pt, keep_with_next |
| "INVITA LA S.V." (25) | CENTER, 16pt bold (formula rituale) |
| Data firma (31) | RIGHT, 12pt, space_before=18pt (HARD_005) |
| "Con osservanza," (32) | RIGHT, italic, 12pt (HARD_005) |
| Nome firmatario (33) | RIGHT, bold, 12pt |
| Riga firma (34) | RIGHT, 12pt |
| Disclaimer (35) | RIGHT, italic, 10pt |

### Artefatti rimossi

- **"* * *"** (paragrafi 13, 19, 23): rimossi per STYLE_011 ("Vietati `***`"). La gerarchia visiva è garantita da space_before sui titoli di sezione.

### Normalizzazioni

- **En dash "–"** → "-" in tutti i run (HARD_004B). Occorrenze: para 3 (nota mitt.), para 8 (PEC), para 15 (corpo), para 16, para 21, para 26, para 27, para 29, para 35.
- Font `Times New Roman` e size espliciti su ogni run.
- Allineamento `RIGHT` ripristinato su blocco firma/data (para 31: era `None`).

### Non modificato

- Contenuto giuridico integrale preservato (nomi, date, artt., riferimenti normativi, importi, qualifiche).
- Segnaposto "[DA INSERIRE]" lasciati intatti.
- Bold e italic run-level del sorgente preservati dove semanticamente rilevanti.

---

## Verifica checklist (HARD_006)

| Punto | Stato |
|---|---|
| Template usato | ✓ Template_Vuoto.docx |
| Font/size espliciti su ogni run | ✓ |
| Gerarchia visiva chiara | ✓ |
| Corpo 12pt JUSTIFY | ✓ |
| IN FATTO / IN DIRITTO 16pt bold CENTER | ✓ |
| OGGETTO label 16pt bold / contenuto 12pt bold | ✓ |
| Destinatario STYLE_008B (left_indent 8.5cm) | ✓ |
| Data e firma separate in paragrafi distinti | ✓ |
| Con osservanza + firma a destra (HARD_005) | ✓ |
| Nessun artefatto `***` / en dash / em dash | ✓ |
| Contenuto giuridico intatto | ✓ |
| Titoli keep_with_next=True | ✓ |
