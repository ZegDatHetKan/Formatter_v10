# Formatter Report

**Documento:** Ricorso in opposizione a decreto di revoca della patente di guida - Campos Omar
**Giudice:** Giudice di Pace di Brescia
**Script:** `_format_campos.py`
**Output:** `documento_ricevuto_formattato.docx` / `final.docx`
**Paragrafi prodotti:** 79

---

## Struttura riconosciuta e applicata

| Elemento | Formato applicato |
|---|---|
| Court header (`Giudice di Pace di Brescia`) | CENTER, 16pt bold |
| Act title (`Ricorso in opposizione...`, `e istanza di sospensione...`) | CENTER, 16pt bold |
| Label procedurali (`Parte ricorrente:`, `Parti Intimate:`, `Provvedimento impugnato:`) | LEFT, 14pt bold |
| `Oggetto del giudizio e sintesi dei motivi:` | LEFT, 14pt bold |
| Ritual headings (`Premesso che:`, `In fatto:`, `In diritto:`, `tanto premesso`, `ricorre`, `Conclusioni`) | CENTER, 16pt bold |
| Argument headings I-V | LEFT, 14pt bold |
| Sottosezioni conclusioni (`Nel merito`, `In via istruttoria`, `In ogni caso`, `In via preliminare / cautelare`) | LEFT, 14pt bold |
| `Dichiarazione di valore ai fini del contributo unificato` | LEFT, 14pt bold |
| `Si producono:` | LEFT, 14pt bold |
| Elenco Art. 193/180 (Sez. III) | JUSTIFY, 12pt, indent 0.5cm |
| Elenco incongruenze (Sez. V) | JUSTIFY, 12pt, indent 0.5cm |
| Produzioni (1-7) | LEFT, 12pt, indent 0.5cm |
| Corpo testo | JUSTIFY, 12pt, line-spacing 1.05 |
| `Con osservanza.` | RIGHT, 12pt |
| `Bergamo, 12 maggio 2026` | RIGHT, 12pt |
| `Avv. Matteo Bertocchi` | RIGHT, 12pt bold |

## Correzioni applicate

- `proclivit[à]` → `proclività`
- `nel[l']infrangere` → `nell'infrangere`
- Tutti gli en dash `–` → `-` (inclusi argument headings, elenchi produzioni, testi corpo)
- `&nbsp;` multipli nella riga finale → rimossi; data e firma separati in due paragrafi distinti
- Header studio (para 0 del sorgente) saltato: già presente nell'header del template

## Contenuto preservato

Tutti i dati identificativi intoccati: c.f., verbali (49019F24, 50808T, 50809T, 50826T24, 202P24, 203P24), prot. MIT-PRBSSPC-00025143, n. 2400058609, date, indirizzi, PEC, riferimenti normativi, importo contributo unificato (€ 43,00).
