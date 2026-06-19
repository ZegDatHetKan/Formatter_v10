# Formatter Report — Memoria di replica Colnaghi

**Data:** 2026-05-28  
**Input:** input.docx  
**Output:** documento_ricevuto_formattato.docx / final.docx  
**Script:** _format_colnaghi.py  
**Categoria:** GENERICO  
**Genere riconosciuto:** Memoria giudiziaria per il Giudice Tutelare (Tribunale di Bergamo)

---

## Documento

**Oggetto:** Memoria di replica e istanza dell'Amministratore di Sostegno – R.G. n. 861/2024 V.G.  
**Firmataria:** Prof.ssa Alice Melocchi (Amministratore di Sostegno di Walter Andrea Colnaghi)  
**Difensore:** Avv. Matteo Bertocchi – Studio Bergamo Legal  
**Udienza:** 3 luglio 2026, ore 12:15  

---

## Operazioni eseguite

### Struttura gerarchica applicata

| Tipo | Font | Size | Align | Esempi |
|---|---|---|---|---|
| Macro-sezione | TNR bold | 16 pt | CENTER | IN FATTO, IN DIRITTO, RICHIESTE |
| Sottosezione numerata | TNR bold | 14 pt | LEFT | 1. Lo stato del procedimento... |
| Titoletto testuale | TNR bold | 14 pt | LEFT | Premessa di metodo, Allegati: |
| OGGETTO label | TNR bold | 16 pt | - | "OGGETTO:" |
| OGGETTO contenuto | TNR bold | 12 pt | JUSTIFY | descrizione completa |
| Corpo atto | TNR | 12 pt | JUSTIFY | tutto il corpo narrativo |
| Saluto apertura | TNR bold | 12 pt | JUSTIFY | "Ill.mo Giudice Tutelare," |
| Voci richieste a)-e) | TNR | 12 pt | JUSTIFY | rientro 0.5 cm |
| Voci allegati 1-3 | TNR | 12 pt | LEFT | rientro 0.5 cm |
| Congedo | TNR | 12 pt | RIGHT | "Con osservanza," |
| Blocco firma | TNR bold/regular | 12 pt | RIGHT | Prof.ssa Melocchi, Avv. Bertocchi |

### Contenuto eliminato (duplicato dal template)
- Paragrafi 0–5: intestazione studio (BERGAMO LEGAL, Società tra Avvocati, www.bergamo.legal, Avv. Bertocchi, Avv. Chiappa) → già nel header del Template_Vuoto.docx
- Paragrafi 116–122: footer studio (R.E.A., P.IVA, indirizzi) → già nel footer del Template_Vuoto.docx
- Tutti i paragrafi vuoti → rimossi; spaziatura gestita via space_before/space_after

### Normalizzazioni applicate
- **HARD_004B:** tutti gli en-dash (–) e em-dash (—) sostituiti con trattino semplice (-) — verificato: 0 dash unicode nel testo output
- **Spazi:** nessun artefatto di spaziatura multipla trovato
- **OCR artefatti:** nessuno trovato nel testo (pattern `[à]`, `[e]` ecc. non presenti)
- **keep_with_next=True** su tutti i titoletti e macro-sezioni per evitare titoli orfani

### Preservato integralmente
- Tutti i riferimenti normativi: artt. c.c., L. 328/2000, d.P.C.M., art. 413, artt. 374-375
- Tutti i dati identificativi: R.G. n. 861/2024 V.G., Prot. n. 7011, date, importi
- Tutti i nomi propri: Colnaghi, Melocchi, Bertocchi, Assanelli, Domanico, Mapelli, ecc.
- Bold originale su citazioni giuridiche (Cass. civ., All. 1, art. 6 d.P.C.M., ecc.)
- Italic originale su citazioni letterali e termini latini (contra se, ex officio, inerzia, tabulas, ecc.)
- Caporalati «» e virgolette testuali invariati

### Paragrafi output: 95
### Verifica font/size: OK — tutti i run hanno Times New Roman con size esplicita

---

## Qualità documento finale

- Gerarchia visiva chiara: macro → sezione → sub-sezione → corpo
- Corpo interamente giustificato, 12pt
- Firme e congedo allineati a destra in blocco coerente
- Nessuna data/firma fusa
- Nessun titoletto senza contenuto (keep_with_next attivo)
- Nessun artefatto residuo

