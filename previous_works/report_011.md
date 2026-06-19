# Formatter Report — documento_ricevuto_formattato.docx

**Data:** 2026-06-11  
**Script:** `_format_mediazione.py`  
**Categoria:** GENERICO  
**Genere:** Comunicazione breve (lettera di consenso a mediazione)

---

## Documento sorgente

- 6 paragrafi sorgente → 8 paragrafi output (para 5 splittato per `\n` interni)
- Testo pulito, nessun artefatto OCR, un solo en dash `–` rimosso

## Interventi effettuati

| Intervento | Dettaglio |
|---|---|
| En dash rimosso | `–` in "125/2026 – Consenso" → `-` (HARD_004B) |
| Para 5 splittato | `\n` interni: "Cordiali saluti," / "Avv. Matteo Bertocchi" / "Bergamo Legal..." → 3 paragrafi separati |
| Oggetto formattato | "Subject:" 16 pt bold CENTER; contenuto 12 pt bold (STYLE_008) |
| Firma a destra | Congedo + firma + studio → RIGHT (HARD_005, STYLE_016) |
| Font esplicito | Times New Roman 12 pt su ogni run |
| Margini | Preservati dal Template_Vuoto.docx: sup 5.91 cm, inf 4.54 cm, sx/dx 2 cm |

## Layout applicato

| Para | Tipo | Align | Size | Bold |
|---|---|---|---|---|
| 0 | Subject/Oggetto | CENTER | 16/12 pt | Sì (label+contenuto) |
| 1 | Saluto iniziale | LEFT | 12 pt | No |
| 2 | Corpo | JUSTIFY | 12 pt | No |
| 3 | Corpo | JUSTIFY | 12 pt | No |
| 4 | Corpo | JUSTIFY | 12 pt | No |
| 5 | Congedo | RIGHT | 12 pt | No |
| 6 | Firma avvocato | RIGHT | 12 pt | Sì |
| 7 | Studio legale | RIGHT | 12 pt | No |

## Verifiche superate

- [x] Font e size espliciti su ogni run
- [x] Margini A4 corretti
- [x] En/em dash sostituiti
- [x] Bracket artefatti: nessuno presente
- [x] Data e firma separate (nessuna data nel documento, v. verification.md)
- [x] Congedo e firma a destra
- [x] Contenuto giuridico preservato integro
- [x] Nessun artefatto residuo
