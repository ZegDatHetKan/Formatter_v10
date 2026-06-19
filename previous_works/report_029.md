# Formatter Report — PEC contestazione Papi Solutions

**Data elaborazione:** 2026-05-28  
**Script:** `_format_pec_papi.py`  
**Input:** `input.docx` (19 paragrafi)  
**Output:** `documento_ricevuto_formattato.docx` → `final.docx` (15 paragrafi)  
**Template:** `Template_Vuoto.docx`  
**Categoria:** GENERICO (comunicazione PEC / lettera legale)

---

## Struttura documento

Contestazione fattura n. 77/25.03.2026 a Papi Solutions S.r.l., per conto di Service Italia S.a.s. di Monzani Ivo Angelo e C. Proposta transattiva a firma Avv. Matteo Bertocchi.

---

## Decisioni di formattazione

### Intestazione studio (paras 0-2 sorgente)
Esclusi dall'output: già presenti nel header del Template_Vuoto.docx (BERGAMO LEGAL, Società tra Avvocati s.r.l., ecc.). Duplicazione evitata.

### "Trasmessa a mezzo PEC" (para 4 sorgente)
Preservato italic del sorgente — funzione semantica: nota di trasmissione.  
Allineamento: RIGHT (conforme al sorgente).

### Data "Bergamo, lì [DATA INVIO]" (para 5 sorgente)
RIGHT, separata dalla firma (HARD_005 rispettato). space_after=18pt per distanziare dal blocco destinatario.

### Blocco destinatario (paras 6-9 sorgente)
Applicato STYLE_008B: `left_indent = Cm(8.5)`. Tutti e 4 i paragrafi (Spett.le, ragione sociale, indirizzo, PEC) condividono lo stesso indent.

### OGGETTO (para 10 sorgente)
- Label `OGGETTO: ` → 16pt bold (titolo centrale, STYLE_008)
- Contenuto → 12pt bold (STYLE_008, caso specifico Oggetto)
- Allineamento JUSTIFY (come sorgente)
- En dash convertiti in trattino semplice (HARD_004B)

### Corpo testo (paras 12-15 sorgente)
- Times New Roman 12pt, JUSTIFY, space_before=0, space_after=6pt
- Bold/italic originali preservati (funzione semantica: enfasi su dati chiave — date, importi, argomenti principali)
- En dash sostituiti con `-` in para 13 (periodo 01.01.2026-25.03.2026)

### Congedo (para 16 sorgente)
Allineato RIGHT per HARD_005 (firma dell'avvocato a destra → saluto/congedo a destra).  
space_before=20pt (apertura blocco firma).

### Firma (paras 17-18 sorgente)
- "Bergamo Legal Società tra Avvocati S.r.l." → RIGHT, 12pt, non bold (preservato dal sorgente)
- "Avv. Matteo Bertocchi" → RIGHT, 12pt, bold (conforme sorgente e STYLE_016)
- Data e firma mai fuse (HARD_005 rispettato)

---

## Pulizia artefatti

- En dash `–` sostituiti con `-` in: indirizzo destinatario, OGGETTO line, para 13 (range date)
- Nessun artefatto OCR rilevato nel testo

---

## Verifiche HARD

| Regola | Stato |
|---|---|
| HARD_001 Contenuto intoccabile | ✓ |
| HARD_002 Template e margini (5.91/4.54/2/2) | ✓ |
| HARD_003 Font Times New Roman, size espliciti | ✓ |
| HARD_004 Nessun artefatto residuo | ✓ |
| HARD_004B En/em dash → trattino semplice | ✓ |
| HARD_005 Data e firma separate; congedo a destra | ✓ |
| HARD_006 Output verificato | ✓ |
| HARD_007 Titoletti orfani | n/a (nessun titoletto interno) |
