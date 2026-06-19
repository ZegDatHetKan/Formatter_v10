# Formatter Report

**Job:** 20260528T000906_LEGAL_cf9e2f8c  
**Data:** 2026-05-28  
**Documento:** Ricorso in opposizione a decreto di revoca della patente di guida – Campos Omar  
**Script:** `_format_ricorso.py`

---

## Struttura sorgente

8 paragrafi composti da blocchi separati da `<w:br/>` (soft-return). Tutti i run privi di formattazione esplicita (bold/italic/size = None).

| Para | Contenuto |
|---|---|
| 0 | Intestazione studio (saltata: già nel template header) |
| 1 | Court header + titolo atto (2 righe) |
| 2 | Parti processuali (parte ricorrente, parti intimate, provvedimento impugnato) |
| 3 | Oggetto del giudizio e sintesi dei motivi |
| 4 | Premesso che + In fatto (7 blocchi fattuali) |
| 5 | In diritto + motivi I-V |
| 6 | tanto premesso + ricorre + corpo |
| 7 | Conclusioni + claims + produzioni + dichiarazione di valore + congedo + data + firma |

---

## Operazioni eseguite

### Pulizia artefatti
- `proclivit[à]` → `proclività` (artefatto OCR riparato)
- `nel[l']infrangere` → `nell'infrangere` (artefatto OCR riparato)
- Tutti i `–` (en-dash U+2013) → `-` (trattino corto ASCII): circa 25 occorrenze
- `&nbsp;` letterali rimossi/normalizzati a spazio standard

### Separazione data/firma (HARD_005)
- La riga fusa "Bergamo, 12 maggio 2026 &nbsp;×35 Avv. Matteo Bertocchi" è stata separata in tre paragrafi distinti (congedo / data / firma), tutti allineati a destra.

### Gerarchia applicata
| Tipo | Stile | Note |
|---|---|---|
| Intestazione tribunale | CENTER 16pt bold | keep_with_next |
| Titolo atto (2 righe) | CENTER 16pt bold | |
| Label parti (`Parte ricorrente:` ecc.) | LEFT 14pt bold | keep_with_next |
| `Oggetto del giudizio e sintesi dei motivi:` | LEFT 14pt bold | keep_with_next |
| Formule rituali (`Premesso che:`, `In fatto:`, `In diritto:`) | CENTER 16pt bold | keep_with_next + keep_together |
| Argomenti `I - V` | LEFT 14pt bold | keep_with_next |
| Corpo testo | JUSTIFY 12pt | |
| Elenco Art. (sezione III) | JUSTIFY 12pt, indent 0.5cm | |
| Elenco incongruenze (sezione V) | JUSTIFY 12pt, indent 0.5cm | |
| Formule di passaggio (`tanto premesso`, `ricorre`) | CENTER 16pt bold | keep_with_next + keep_together |
| Conclusioni | CENTER 16pt bold | keep_with_next |
| Sub-intestazioni conclusioni (`Nel merito`, ecc.) | LEFT 14pt bold | keep_with_next |
| `Si producono:` | LEFT 14pt bold | keep_with_next |
| Voci produzioni (1-7) | LEFT 12pt, indent 0.5cm | |
| `Dichiarazione di valore...` | LEFT 14pt bold | keep_with_next |
| Congedo (`Con osservanza.`) | RIGHT 12pt | |
| Data (`Bergamo, 12 maggio 2026`) | RIGHT 12pt | |
| Firma (`Avv. Matteo Bertocchi`) | RIGHT 12pt bold | |

---

## Verifica HARD_006

- [x] Font Times New Roman su ogni run
- [x] Size esplicita su ogni run
- [x] Allineamenti conformi alle regole
- [x] Nessun artefatto residuo
- [x] Data e firma separate (HARD_005)
- [x] Congedo a destra nello stesso blocco firma (HARD_005)
- [x] Titoli con keep_with_next (HARD_007)
- [x] Trattino corto su tutti i run (HARD_004B)
- [x] Contenuto giuridico intatto (HARD_001)
- [x] Template corretto (HARD_002)

---

## Output

- `documento_ricevuto_formattato.docx` (79 paragrafi)
- `final.docx` (copia identica)
- `subject.txt`: `ricorso-opposizione-revoca-patente-campos`
