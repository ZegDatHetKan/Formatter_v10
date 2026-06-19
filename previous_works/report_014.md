# Formatter Report — Memoria di replica e istanza AdS Melocchi

**Data:** 2026-06-12  
**Script:** `_format_memoria.py`  
**Input:** `input.docx` (124 paragrafi, 0 tabelle)  
**Output:** `documento_ricevuto_formattato.docx` / `final.docx` (104 paragrafi)  
**Template:** `Template_Vuoto.docx` (A4, margini sup 5.91 cm, inf 4.54 cm, sx/dx 2 cm)

---

## Genere documentale

Memoria di replica e istanza depositata dal Amministratore di Sostegno (Prof.ssa Alice Melocchi) al Giudice Tutelare del Tribunale di Bergamo. Procedimento R.G. n. 861/2024 V.G., udienza 3 luglio 2026. Categoria: GENERICO.

---

## Struttura identificata e formattazione applicata

| Blocco | Indici src | Tipo | Formato applicato |
|---|---|---|---|
| Data | [000] | `place_date` | RIGHT, 12pt |
| Mittente | [001] | `sender_bold` | LEFT, 12pt bold |
| Mittente corpo | [002-006] | `sender_body` | LEFT, 12pt |
| Tribunale (bold) | [010-011] | `court_bold` | LEFT, 12pt bold |
| Tribunale (corpo) | [012-014] | `court_body` | LEFT, 12pt |
| Per conoscenza | [016] | `knowledge_label` | LEFT, 12pt bold |
| Destinatari cc | [017-021] | `knowledge_item` | LEFT, 12pt, rientro 0.5cm |
| OGGETTO label | [026] | `oggetto` (label) | CENTER, 16pt bold |
| OGGETTO contenuto | [026] | `oggetto` (content) | JUSTIFY, 12pt bold |
| Saluto | [028] | `salutation` | LEFT, 12pt bold |
| IN FATTO | [036] | `section` | CENTER, 16pt bold |
| IN DIRITTO | [067] | `section` | CENTER, 16pt bold |
| RICHIESTE | [102] | `section` | CENTER, 16pt bold |
| Sezioni numerate 1-10 | vari | `subsection` | LEFT, 14pt bold, keep_with_next |
| Premessa di metodo | [032] | `subsection` | LEFT, 14pt bold, keep_with_next |
| Paragrafi corpo | vari | `body` | JUSTIFY, 12pt, line_spacing 1.08 |
| Richieste a)-e) | [104-108] | `claims_item` | JUSTIFY, 12pt, rientro 0.5cm |
| Allegati label | [110] | `allegati_label` | LEFT, 12pt bold, keep_with_next |
| Allegati voci | [111-114] | `allegati_item` | JUSTIFY, 12pt, rientro 0.5cm |
| Con osservanza, | [116] | `closing` | RIGHT, 12pt, space_before 20pt |
| Firme (bold) | [118, 122] | `sig_bold` | RIGHT, 12pt bold |
| Firme (corpo) | [119-120] | `sig_body` | RIGHT, 12pt |
| Firma digitale | [123] | `sig_italic` | RIGHT, 12pt italic |

---

## Trattamento paragrafi vuoti

- Paragrafi vuoti consecutivi compressi (max 1 tra macro-blocchi).
- Paragrafi vuoti immediatamente dopo section/subsection/salutation/closing: soppressi (sostituti da `space_after` del paragrafo precedente).
- Paragrafi vuoti immediatamente prima di section/subsection: soppressi (space_before del titolo sufficiente).
- Paragrafi vuoti tra allegati e firma (src [115]) e tra i due blocchi firma (src [121]): conservati.

---

## OGGETTO

Trattato con split: label `OGGETTO:` a 16pt bold CENTER (come da STYLE_008 "titolo centrale"); contenuto a 12pt bold JUSTIFY (come da STYLE_008 "caso specifico Oggetto").

---

## Artefatti

- **En/em dash**: assenti nel sorgente. Nessuna sostituzione necessaria.
- **OCR bracket artifacts**: assenti. Le occorrenze `[…]` in [045], [046], [081] sono omissis legali all'interno di citazioni letterali — **preservati correttamente**.
- **Spaziature**: nessun doppio spazio rilevante.

---

## Verifica font/size

- Tutti i runs verificati: font `Times New Roman`, size esplicita su ogni run.
- Section headers: 16pt bold CENTER.
- Subsection headers: 14pt bold LEFT.
- Corpo: 12pt JUSTIFY.
- Firme: 12pt RIGHT.
- Nessun problema rilevato (`NESSUN PROBLEMA FONT/SIZE`).

---

## Integrità contenuto

- Sorgente: 96 paragrafi non-vuoti → Output: 97 paragrafi non-vuoti (+1 per split OGGETTO label/content).
- Nessun contenuto giuridico, dato identificativo, riferimento normativo, nome, importo o data eliminato.
- Date/firma separate: ✓ (data in blocco mittente [000]; firme in blocco finale [116-123]).

---

## Output generati

- `documento_ricevuto_formattato.docx` ✓
- `final.docx` ✓
- `formatter_report.md` ✓
- `verification.md` ✓
- `subject.txt` ✓
