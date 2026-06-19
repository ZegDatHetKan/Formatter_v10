# Formatter Report — input.docx

**Data:** 2026-06-12  
**Categoria:** GENERICO  
**Genere rilevato:** Lettera di riscontro/contestazione legale  
**Script:** `_format_input.py`  
**Output:** `documento_ricevuto_formattato.docx`, `final.docx`

---

## Sorgente

- 1 paragrafo Word, 15 `<w:br/>` interni = 16 blocchi logici
- Nessuna formattazione esplicita nei runs (tutto plain)
- En dash × 2, placeholder `[DA INSERIRE: ...]` × 3

## Trasformazioni

| # | Tipo | Dettaglio |
|---|---|---|
| 2 | En dash → `-` | HARD_004B |
| 3 | Placeholder conservati | `[DA INSERIRE: ...]` non sono artefatti |
| 16 | Font esplicitato | `Times New Roman` su ogni run |
| 16 | Size esplicitata | 12pt corpo, 16pt OGGETTO label |

## Layout applicato

```
[RIGHT 12pt]         Bergamo, [DA INSERIRE: data di invio]

[LEFT 12pt ←8.5cm]  Spett.le
[LEFT 12pt ←8.5cm]  Altroconsumo - Servizio Legale
[LEFT 12pt ←8.5cm]  [DA INSERIRE: indirizzo/PEC ...]

[CENTER 16pt BOLD]   OGGETTO:
[JUSTIFY 12pt BOLD]  Vs. comunicazione relativa alla sig.ra Margherita De Luca - ...

[LEFT 12pt]          Spettabile Servizio Legale,

[JUSTIFY 12pt] × 7  Corpo lettera

[RIGHT 12pt]         Distinti saluti.
[RIGHT 12pt BOLD]    Avv. Matteo Bertocchi
[RIGHT 12pt]         Bergamo Legal Società tra Avvocati s.r.l.
```

## Verifiche output

- [x] Font Times New Roman esplicito su tutti i runs
- [x] Size esplicita su tutti i runs
- [x] OGGETTO: 16pt bold CENTER + contenuto 12pt bold JUSTIFY
- [x] Corpo JUSTIFY 12pt
- [x] Blocco finale (saluto + firma + studio) tutto RIGHT
- [x] Data e firma separati (nello stesso blocco, paragrafi distinti)
- [x] En dash rimossi
- [x] Placeholder `[DA INSERIRE: ...]` conservati
- [x] Margini template: top 5.91cm, inf 4.54cm, sx 2cm, dx 2cm
- [x] Nessun artefatto residuo
- [x] Contenuto giuridico intatto

## Anomalie / dubbi

Nessuno.
