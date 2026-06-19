# Formatter Report

**Job:** 20260527T233714_LEGAL_e8a4c59b  
**Data:** 2026-05-27  
**Documento:** Ricorso in opposizione a decreto di revoca patente — Campos Omar vs Prefettura di Brescia  
**Output:** `documento_ricevuto_formattato.docx`, `final.docx`

---

## Struttura rilevata

Il documento sorgente (`input.docx`) contiene 8 paragrafi Word con newline (`\n`) embedded nei run — tipico artefatto da conversione PDF/OCR. La pipeline li ha espansi in 79 paragrafi discreti nel documento di output.

| Blocco | Tipo assegnato | Paragrafi output |
|---|---|---|
| Intestazione studio | SKIP (già nel template) | 0 |
| Giudice di Pace di Brescia | court_header — CENTER 16pt bold | 1 |
| Titolo ricorso (2 righe) | act_title — CENTER 16pt bold | 2 |
| Parte ricorrente / Parti Intimate / Provvedimento impugnato | subsection_header 14pt + act_body | 7 |
| Oggetto del giudizio | subsection_header 14pt + act_body | 2 |
| Premesso che | ritual_heading — CENTER 16pt bold | 1 |
| In fatto | subsection_header 14pt + act_body (7 paragrafi) | 8 |
| In diritto | subsection_header 14pt + act_body | 2 |
| I–V (argomenti) | argument_heading 14pt bold + act_body + liste | 28 |
| tanto premesso / ricorre | ritual_heading — CENTER 16pt bold | 2 |
| Conclusioni | ritual_heading 16pt + subheadings + act_body | 10 |
| Si producono (1–7) | exhibits_heading + exhibit_item (indent 0.5cm) | 8 |
| Dichiarazione di valore | subsection_header 14pt + act_body | 2 |
| Blocco finale (Con osservanza / data / firma) | RIGHT alignment | 3 |

---

## Interventi di pulizia

| Tipo | Dettaglio | Azione |
|---|---|---|
| Artefatti OCR | `proclivit[à]` | → `proclività` |
| Artefatti OCR | `nel[l']infrangere` | → `nell'infrangere` |
| En dash (`–`) | 12+ occorrenze nel testo | → `-` (HARD_004B) |
| `&nbsp;` HTML | Usato come spacer tra data e firma | Rimosso |
| Data+firma fuse | `Bergamo, 12 maggio 2026 &nbsp;...&nbsp; Avv. Matteo Bertocchi` | Separati in 3 paragrafi distinti (saluto / data / firma) |
| Paragrafo 0 | Intestazione Bergamo Legal nel body del sorgente | Saltato (già nel template) |

---

## Formattazione applicata

- Font: Times New Roman esplicito su ogni run ✓  
- Size: 16pt titoli/rituali, 14pt sottosezioni/argument heading, 12pt corpo ✓  
- Liste sezione III (Art. ...): JUSTIFY, indent 0.75cm ✓  
- Liste sezione V (La .../Il numero ...): JUSTIFY, indent 0.75cm ✓  
- Exhibit items (1-7): LEFT, indent 0.50cm ✓  
- keep_with_next su tutti i titoletti ✓  
- Con osservanza / data / firma: tutti RIGHT ✓  
- Firma (Avv. Matteo Bertocchi): RIGHT bold ✓  
- Contenuto giuridico: intatto ✓
