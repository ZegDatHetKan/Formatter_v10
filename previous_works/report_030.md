# Formatter Report — Memoria di replica e istanza (Colnaghi)

**Data:** 2026-05-29  
**Job:** 20260529T091356_queue_5oHKlZBdHqY  
**Documento:** Memoria di replica e istanza dell'Amministratore di Sostegno – R.G. n. 861/2024 V.G.  
**Categoria:** GENERICO

---

## Documento sorgente

- **Tipo:** Memoria di replica e istanza pre-udienza al Giudice Tutelare
- **Mittente:** Prof.ssa Alice Melocchi, Amministratore di Sostegno di Walter Andrea Colnaghi, c/o Studio Legale Bergamo Legal s.r.l. (Avv. Matteo Bertocchi)
- **Destinatario:** Tribunale Ordinario di Bergamo, Ufficio del Giudice Tutelare, Dott.ssa Simona Maria Domenica Cherubini
- **Riferimento:** R.G. n. 861/2024 V.G., udienza 3 luglio 2026 ore 12:15
- **Paragrafi sorgente totali:** 128
- **Paragrafi processati (7–120):** 114 — skip 0–6 (header template) e 121–127 (footer template/decorativo)

---

## Struttura riconosciuta

| Elemento | Paragrafi input | Formato applicato |
|---|---|---|
| Data apertura | 7 | LEFT 12pt |
| Blocco mittente (AdS + contatti) | 9–14 | LEFT 12pt, bold preservato |
| Blocco destinatario (Tribunale) | 16–20 | LEFT 12pt, bold preservato |
| "Per conoscenza:" + lista | 22–27 | LEFT 12pt bold label, JUSTIFY 12pt lista, rientro 0.5cm |
| OGGETTO | 29 | JUSTIFY 12pt bold |
| Saluto apertura | 31 | LEFT 12pt bold |
| Premessa di metodo | 35 | LEFT 14pt bold, keep_with_next |
| Corpo introduttivo | 33, 36, 38 | JUSTIFY 12pt |
| IN FATTO | 40 | CENTER 16pt bold, keep_with_next |
| Sezioni 1–3 (IN FATTO) | 41, 46, 54 | LEFT 14pt bold, keep_with_next |
| Sottoparagrafi 1.1–3.13 | 42–69 | JUSTIFY 12pt, bold/italic run preservati |
| IN DIRITTO | 71 | CENTER 16pt bold, keep_with_next |
| Sezioni 4–10 (IN DIRITTO) | 72, 74, 80, 84, 87, 91, 95 | LEFT 14pt bold, keep_with_next |
| Sottoparagrafi 4.x–10.x | 73, 75–83, 85–86, 88–98 | JUSTIFY 12pt, bold/italic run preservati |
| RICHIESTE | 100 | CENTER 16pt bold, keep_with_next |
| Intro RICHIESTE | 101 | JUSTIFY 12pt |
| Voci a)–e) RICHIESTE | 102–106 | JUSTIFY 12pt, rientro 0.5cm, bold label preservato |
| Allegati: | 108 | LEFT 12pt bold |
| Voci allegati 1–3 | 109–111 | JUSTIFY 12pt, rientro 0.5cm |
| "Con osservanza," | 113 | RIGHT 12pt (HARD_005) |
| Blocco firma | 115–120 | RIGHT 12pt, bold/italic preservati |

---

## Pulizia artefatti

- **En dash (–) → trattino ASCII (-):** sostituiti in tutti i run (blocco mittente, titoli sezione, corpo testo, blocco destinatario)
- **Em dash (—) → trattino ASCII (-):** sostituiti nel corpo testo (es. para 55 originale)
- **Zero-width chars / BOM:** rimossi ove presenti
- **Template header (paras 0–6):** saltati — già presenti nel header del Template_Vuoto.docx
- **Template footer (paras 121–127):** saltati — già presenti nel footer del Template_Vuoto.docx (riga decorativa "___" + dati R.E.A./Ordine/contatti)

---

## Verifiche finali

| Check | Esito |
|---|---|
| Font Times New Roman esplicito su ogni run | ✓ OK |
| Size esplicita su ogni run | ✓ OK |
| Nessun en/em dash residuo | ✓ OK |
| Macro-sezioni CENTER 16pt bold | ✓ OK |
| Section headers LEFT 14pt bold | ✓ OK |
| Corpo testo JUSTIFY 12pt | ✓ OK |
| Congedo + firma RIGHT | ✓ OK |
| Data e firma non fuse (HARD_005) | ✓ OK — data a p. 1, firma in fondo |
| Contenuto giuridico preservato (97/97 righe) | ✓ OK |
| Paragrafi output = paragrafi input (114) | ✓ OK |
| Template_Vuoto.docx come base | ✓ OK |

---

## Output prodotti

- `documento_ricevuto_formattato.docx` ✓
- `final.docx` ✓
- `formatter_report.md` ✓
- `verification.md` ✓
- `subject.txt` ✓
- `_format_memoria_colnaghi.py` (script di lavoro)
