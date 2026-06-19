# Verification — Memoria di replica Colnaghi

**Data:** 2026-05-28  
**Output verificato:** documento_ricevuto_formattato.docx

---

## Checklist HARD vincoli

| Regola | Stato | Note |
|---|---|---|
| HARD_001 Contenuto intoccabile | ✅ OK | Tutti i dati giuridici preservati |
| HARD_002 Template | ✅ OK | Base: Template_Vuoto.docx |
| HARD_003 Font espliciti | ✅ OK | Tutti i run: TNR + size esplicita |
| HARD_004 Artefatti OCR | ✅ OK | Nessun artefatto trovato |
| HARD_004B Trattini | ✅ OK | 0 en-dash/em-dash nel testo finale |
| HARD_005 Data/firma | ✅ OK | Data a par. 0 (top), firma in fondo separata |
| HARD_006 Output verificabile | ✅ OK | Verifica completata |
| HARD_007 Titoletti orfani | ✅ OK | keep_with_next=True su tutti i titoletti |

---

## Scelte editoriali

| Elemento | Scelta | Motivazione |
|---|---|---|
| Paragrafi 0-5 (studio header) | Eliminati | Duplicati del template header |
| Paragrafi 116-122 (footer) | Eliminati | Duplicati del template footer |
| Paragrafi vuoti sorgente | Eliminati | Spaziatura gestita via space_before/space_after |
| "Ill.mo Giudice Tutelare," | 12pt bold JUSTIFY | Saluto apertura, non titolo gerarchico |
| Sezioni 2.1-10.3 | 12pt JUSTIFY (body) | Paragrafi misti label+corpo: preservato bold sul prefisso |
| CC items "— Comune..." | "-  Comune..." LEFT 0.5cm | Sostituzione dash + rientro lista |
| OGGETTO | 16pt bold label + 12pt bold desc | Per STYLE_008 specifico Oggetto |
| "Con osservanza," | 12pt RIGHT | HARD_005: congedo con firma a destra |

---

## Ambiguità risolte

**Nessuna ambiguità strutturale rilevata.** Il documento ha struttura chiara e uniforme.

---

## Verifiche manuali suggerite

| # | Elemento | Tipo |
|---|---|---|
| 1 | Impaginazione fisica (salti pagina, titoletti vicini a fine pagina) | Solo visivo — non verificabile senza renderer |
| 2 | Blocco AdS (par. 1-6): struttura "from/to" della memoria | Conforme al genere memoria giudiziaria: filing party + court info |

---

## Output files

| File | Stato |
|---|---|
| documento_ricevuto_formattato.docx | ✅ Generato (122 KB) |
| final.docx | ✅ Copia identica |
| formatter_report.md | ✅ |
| verification.md | ✅ |
| subject.txt | ✅ `memoria-replica-giudice-tutelare-colnaghi` |

