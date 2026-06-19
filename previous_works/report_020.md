# Formatter Report

**Job:** 20260528T132855_BERGAMO_LEGAL_Societ_63079cea  
**Data:** 2026-05-28  
**Documento:** Ricorso in opposizione a decreto di revoca della patente di guida - Campos Omar c. Prefettura di Brescia, Giudice di Pace di Brescia  
**Categoria:** GENERICO  

---

## Struttura sorgente

8 paragrafi monoblocco (stile `Normal`, 1 run ciascuno), tutti con newline `\n` interni. Nessuno stile Word dedicato. Testo intero in plain text senza formattazione.

Lo script `_format_ricorso_campos.py` spezza ogni paragrafo per `\n`, classifica ogni riga e costruisce l'output dal template.

---

## Classificazione applicata

| Paragrafo output | Tipo | Font | Align |
|---|---|---|---|
| Giudice di Pace di Brescia | court_header | 16pt bold | CENTER |
| Ricorso in opposizione... | act_title | 16pt bold | CENTER |
| e istanza di sospensione... | act_subtitle | 16pt bold | CENTER |
| Parte ricorrente: / Parti Intimate: / Provvedimento impugnato: | section_label | 14pt bold | LEFT |
| Oggetto del giudizio e sintesi dei motivi: | section_label | 14pt bold | LEFT |
| Corpo parti / decreto / fatti | body | 12pt | JUSTIFY |
| Premesso che: / In fatto: / In diritto: / Conclusioni | ritual_heading | 16pt bold | CENTER |
| tanto premesso / ricorre | transition_formula | 16pt bold | CENTER |
| I - V (motivi in diritto) | argument_heading | 14pt bold | LEFT |
| In via preliminare / Nel merito / In via istruttoria / In ogni caso | claims_section | 14pt bold | LEFT |
| Si producono: / Dichiarazione di valore | section_label/exhibits_heading | 14pt bold | LEFT |
| 1 - 7 (allegati) | exhibit_item | 12pt | LEFT +0.5cm |
| Con osservanza. | closing_formula | 12pt | RIGHT |
| Bergamo, 12 maggio 2026 | place_date | 12pt | RIGHT |
| Avv. Matteo Bertocchi | signature | 12pt bold | RIGHT |

---

## Interventi applicati

- **Para [0] saltato**: intestazione studio già nel Template_Vuoto.docx.
- **En dash `–` → `-`** su tutto il documento (HARD_004B).
- **OCR artifacts riparati**: `proclivit[à]` → `proclività`; `nel[l']infrangere` → `nell'infrangere`.
- **HTML entity `&nbsp;`**: rimossa (HARD_004). Usata come spaziatore nella riga "Bergamo, 12 maggio 2026 &nbsp;... Avv. Matteo Bertocchi" per fondere data e firma.
- **Data+firma separate**: la riga fusa è stata divisa in due paragrafi distinti + vuoto intermedio (HARD_005).
- **Con osservanza.** allineato a destra insieme al blocco firma (HARD_005).
- **Margini pagina**: impostati su top=5.91cm, bottom=4.54cm, sx=2cm, dx=2cm (HARD_002).
- **Font e size espliciti** su ogni run (HARD_003).
- **keep_with_next** applicato su tutti i titoli e titoletti per prevenire orfani (HARD_007).

---

## File prodotti

- `documento_ricevuto_formattato.docx` — output principale
- `final.docx` — copia per webapp
- `formatter_report.md` — questo file
- `verification.md` — note di verifica
- `subject.txt` — slug documento
- `_format_ricorso_campos.py` — script di lavoro temporaneo
