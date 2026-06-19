# Verification — input.docx

**Data:** 2026-06-12

## Struttura sorgente

Documento con un unico paragrafo Word, testo suddiviso da 15 `<w:br/>`. Nessuna formattazione runs esplicita (no bold, italic, size). Nessun stile Word applicato.

## Trasformazioni applicate

| Elemento | Azione |
|---|---|
| `–` (en dash) × 2 | Sostituiti con `-` (HARD_004B) |
| Spazi multipli | Nessuno trovato |
| Artefatti OCR `[à]`, `[e]` ecc. | Nessuno trovato |
| `[DA INSERIRE: ...]` × 3 | **Conservati** — sono placeholder intenzionali, non artefatti |
| Caratteri zero-width / BOM | Nessuno trovato |

## Decisioni di layout

- **Luogo/data** (`[0]`): RIGHT — linea di intestazione della lettera.
- **Blocco destinatario** (`[1-3]`): LEFT con `left_indent=8.5cm` (STYLE_008B) — Spett.le + nome + indirizzo/PEC.
- **OGGETTO:** (`[4]`): CENTER 16pt bold (titolo centrale) + contenuto (`[5]`) JUSTIFY 12pt bold.
- **Saluto apertura** (`[6]`): LEFT 12pt — formula non heading.
- **Corpo** (`[7-13]`): JUSTIFY 12pt, space_after=6pt.
- **Blocco finale** (`[14-16]`): RIGHT — "Distinti saluti." + "Avv. Matteo Bertocchi" (bold) + studio (HARD_005).
- Margini da Template_Vuoto.docx: top 5.91cm, inf 4.54cm, sx 2cm, dx 2cm ✓

## Contenuto giuridico

Preservato integralmente. Nessuna frase modificata, nessun dato eliminato.

## Verifiche manuali richieste

Nessuna. Il documento è strutturalmente semplice e privo di ambiguità legali o strutturali.
