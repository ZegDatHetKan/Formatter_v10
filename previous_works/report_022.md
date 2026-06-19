# Formatter Report – documento_ricevuto_formattato.docx

**Data:** 2026-05-28  
**Script:** `_format_ricorso.py`  
**Input:** `input.docx`  
**Template:** `Template_Vuoto.docx`  
**Output:** `documento_ricevuto_formattato.docx` / `final.docx`

---

## Documento

**Tipo:** Ricorso in opposizione a decreto di revoca della patente di guida (Giudice di Pace di Brescia)  
**Cliente:** Campos Omar (c.f. CMPMR094H14L400X)  
**Avvocato:** Avv. Matteo Bertocchi – Bergamo Legal Società tra Avvocati s.r.l.  
**Decreto impugnato:** Prefettura di Brescia, n. 2400058609, 02/03/2026

---

## Struttura riconosciuta (80 paragrafi logici)

| Tipo | Count | Descrizione |
|---|---|---|
| court_header | 1 | "Giudice di Pace di Brescia" |
| act_title | 2 | Titolo ricorso su 2 righe |
| section_label | 4 | Parte ricorrente, Parti Intimate, Provvedimento impugnato, (corpo) |
| ritual_heading | 6 | Premesso che / In fatto / In diritto / tanto premesso / ricorre / Conclusioni |
| argument_heading | 5 | Motivi I–V |
| claims_heading | 4 | In via preliminare / Nel merito / In via istruttoria / In ogni caso |
| oggetto_label + body | 2 | Oggetto del giudizio |
| body | 28 | Corpo narrativo e argomentativo |
| list_item | 5 | Violazioni Art. 193/180 (sezione III) |
| list_item_v | 7 | Parti Intimate + Incongruenze V (con `;`) |
| exhibit_item | 7 | Produzioni 1–7 |
| exhibits_heading | 1 | "Si producono:" |
| subsection_label | 1 | Dichiarazione di valore |
| congedo | 1 | "Con osservanza." |
| place_date | 1 | "Bergamo, 12 maggio 2026" |
| signature_name | 1 | "Avv. Matteo Bertocchi" |

---

## Interventi tipografici

1. **Paragrafo 0 (intestazione studio) → saltato**: già presente nell'header del template `Template_Vuoto.docx`.
2. **Paragrafi fusi per `w:br`**: tutti gli 8 paragrafi sorgente suddivisi in 80 logici tramite split `\n`.
3. **Riga fusa data+firma** ("Bergamo, 12 maggio 2026 &nbsp;&nbsp;&nbsp;... Avv. Matteo Bertocchi") → separata in 3 paragrafi distinti (place_date / empty / signature_name). Regola HARD_005 rispettata.
4. **Artefatti OCR riparati**:
   - `proclivit[à]` → `proclività`
   - `nel[l']infrangere` → `nell'infrangere`
5. **En dash** (`–`) → trattino normale `-` in tutto il testo. Regola HARD_004B rispettata.
6. **`&nbsp;`** → spazi normali e separazione paragrafi.
7. **Congedo "Con osservanza." + data + firma** → allineati RIGHT. Regola HARD_005.

---

## Formattazione applicata

| Elemento | Allineamento | Size | Bold | Space before | Space after |
|---|---|---|---|---|---|
| court_header | CENTER | 16pt | sì | 0pt | 4pt |
| act_title | CENTER | 16pt | sì | 2pt | 4pt |
| ritual_heading | CENTER | 16pt | sì | 12pt | 8pt |
| section_label | LEFT | 14pt | sì | 10pt | 4pt |
| oggetto_label | LEFT | 14pt | sì | 10pt | 2pt |
| oggetto_body | JUSTIFY | 12pt | sì | 0pt | 8pt |
| argument_heading | LEFT | 14pt | sì | 10pt | 4pt |
| claims_heading | LEFT | 14pt | sì | 10pt | 4pt |
| subsection_label | LEFT | 14pt | sì | 10pt | 4pt |
| exhibits_heading | LEFT | 12pt | sì | 10pt | 4pt |
| exhibit_item | LEFT | 12pt | no | 0pt | 3pt |
| list_item / list_item_v | JUSTIFY | 12pt | no | 0pt | 3pt |
| body | JUSTIFY | 12pt | no | 0pt | 6pt |
| congedo | RIGHT | 12pt | no | 14pt | 4pt |
| place_date | RIGHT | 12pt | no | 4pt | 4pt |
| signature_name | RIGHT | 12pt | sì | 8pt | 4pt |

Font: `Times New Roman` esplicito su ogni run.

---

## Verifica finale (HARD_006)

- [x] Font Times New Roman su ogni run
- [x] Size esplicita su ogni run
- [x] Gerarchia visiva coerente
- [x] Titoli e titoletti coerenti con regole_di_formattazione.md
- [x] Corpo JUSTIFY 12pt
- [x] Elenchi con rientro 0.5cm
- [x] Data e firma separati (HARD_005)
- [x] Congedo RIGHT (HARD_005)
- [x] keep_with_next su tutti i titoletti (HARD_007)
- [x] Nessun artefatto OCR residuo (HARD_004)
- [x] Nessun en/em dash residuo (HARD_004B)
- [x] Contenuto giuridico preservato (HARD_001): 18/18 check su dati identificativi
- [x] Template corretto usato (HARD_002)

**Parametri di verifica:** 0 errori di struttura, 0 run senza font/size.
