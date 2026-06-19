# Verification — Esposizione dei Fatti e Riferimenti Normativi

**Data:** 2026-06-09  
**Stato:** NESSUNA AMBIGUITÀ BLOCCANTE

---

## Checklist HARD

| Regola | Stato | Note |
|---|---|---|
| HARD_001 — Contenuto intoccabile | ✅ PASS | Nomi, date, importi, riferimenti normativi preservati |
| HARD_002 — Template | ✅ PASS | Output basato su Template_Vuoto.docx |
| HARD_003 — Font/size espliciti | ✅ PASS | Times New Roman, size su ogni run |
| HARD_004 — Pulizia artefatti | ✅ PASS | Nessun artefatto OCR nel sorgente |
| HARD_004B — Trattino corto | ✅ PASS | En dash e em dash → `-` in tutte le occorrenze |
| HARD_005 — Data/firma | ✅ N/A | Nessun blocco firma/data nel documento |
| HARD_006 — Output verificabile | ✅ PASS | Font, size, align, bold, italic verificati |
| HARD_007 — Titoletti orfani | ✅ PASS | keep_with_next=True su tutte le intestazioni |

---

## Checklist STYLE

| Regola | Stato | Note |
|---|---|---|
| STYLE_003 — Corpo JUSTIFY 12pt | ✅ | Tutti i paragrafi di corpo |
| STYLE_004 — Titolo CENTER bold 16pt | ✅ | Para 0 |
| STYLE_005 — Sottotitolo CENTER bold 16pt | ✅ | Para 1 |
| STYLE_007 — Sottosezioni LEFT bold 14pt | ✅ | Para 3, 5, 10, 12, 19 |
| STYLE_009 — Corsivo per termini latini | ✅ | Preservato da run originali |
| STYLE_010 — Bold semantico | ✅ | Preservato run-level; nessun bold artificiale aggiunto |
| STYLE_011 — Spaziatura | ✅ | corpo 0/6pt; sezioni 14/6pt; allegati 0/4pt |
| STYLE_012 — Rientri | ✅ | Allegati 0.5cm; corpo senza rientro |
| STYLE_014 — Elenchi allegati | ✅ | LEFT, 0.5cm, sequenza All. 1-4 |

---

## Note editoriali

- **Sottotitolo parentetico (para 1):** "(allegato all'istanza di mediazione - cantiere ex Hotel Executive...)" — trattato come sottotitolo CENTER bold 16pt per STYLE_005. Alternativa possibile: 12pt italic come descrittore/nota. Scelta applicata è coerente con le regole.
- **"ACCENNI NORMATIVI E GIURISPRUDENZIALI":** nel sorgente era LEFT; trattato come intestazione di sezione 14pt bold LEFT (non macro-sezione CENTER 16pt). Coerente con le altre sezioni del documento.
- **Paragrafo vuoto (input para 2):** saltato, la spaziatura è garantita da space_after del sottotitolo (14pt).

---

## Verifiche manuali raccomandate

Nessuna: il documento è formalmente semplice, senza ambiguità giuridiche o strutturali.
