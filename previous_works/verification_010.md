# Verification — Diffida tecnico

**Data:** 2026-06-10  

---

## Checklist HARD

| Vincolo | Stato | Note |
|---|---|---|
| HARD_001 - Contenuto intoccabile | ✅ | Nessuna modifica al testo giuridico |
| HARD_002 - Template_Vuoto.docx | ✅ | Usato come base |
| HARD_003 - Font/size espliciti | ✅ | Times New Roman 12pt/16pt su ogni run |
| HARD_004 - Pulizia artefatti | ✅ | Nessun artefatto OCR trovato nel sorgente |
| HARD_004B - Trattino corto | ✅ | Tutti gli em-dash (—) sostituiti con `-` |
| HARD_005 - Data e firma separati | ✅ | Paragrafi distinti; Distinti saluti a destra |
| HARD_006 - Output verificabile | ✅ | Verificato su tutti i criteri |
| HARD_007 - Titoletti orfani | ✅ | keep_with_next su tutti i titoli/sezioni |

---

## Placeholder [DA INSERIRE]

Il documento contiene 8 segnaposto `[DA INSERIRE: ...]` che sono placeholder legali non compilati. Trattamento: preservati intatti. Non sono artefatti da rimuovere.

Lista:
- `[DA INSERIRE: Nome e Cognome del tecnico]` — destinatario (para 2)
- `[DA INSERIRE]` — partita IVA destinatario (para 3)
- `[DA INSERIRE: indirizzo / sede]` — indirizzo (para 4)
- `[DA INSERIRE]` — PEC (para 5)
- `[DA INSERIRE: data]` — data lettera (para 6)
- `[DA INSERIRE: denominazione azienda]` — cliente Società (para 8)
- `[DA INSERIRE: dati cliente / immobile interessato]` — dati intervento (para 10)
- `[DA INSERIRE: estremi fattura]` — estremi fattura (para 10)
- `[DA INSERIRE: data e-mail]` — data comunicazione (para 13)
- `[DA INSERIRE: cognome del tecnico]` — cognome nel corpo (para 20)

**Nota:** il documento è un template a uso interno con campi da compilare. Nessuna verifica manuale richiesta su questi.

---

## Decisioni editoriali

1. **OGGETTO split:** la label `OGGETTO:` è stata separata dal contenuto in due paragrafi distinti (CENTER 16pt bold / CENTER 12pt bold) per conformità a STYLE_008. Il contenuto è reso bold per evidenziare il riassunto.

2. **"tutto ciò premesso e considerato..."** (para 18): trattato come formula di transizione a 12pt bold CENTER (non 16pt) perché è una frase subordinata di collegamento, non una macro-sezione autonoma. L'alternativa 16pt avrebbe appesantito visivamente un elemento che non è un heading.

3. **Spazi rituali DIFFIDA:** la formula "D I F F I D A   E   I N T I M A" mantiene i tripli spazi attorno a "E". La funzione `clean_text` non normalizza spazi multipli proprio per preservare queste lettere spaziate.

---

## Nessuna verifica manuale richiesta

Il documento non presenta ambiguità giuridiche, contenuti corrotti o incongruenze strutturali. Tutti i placeholder sono evidenti e non presentano rischi di interpretazione.
