# Verification — Lettera Consiglieri Madone

**Data verifica:** 2026-06-04  
**Esito generale:** documento accettabile, nessun intervento umano urgente

---

## Verifiche superate

- [x] Contenuto giuridico intatto (nomi, date, importi, riferimenti normativi)
- [x] Template `Template_Vuoto.docx` utilizzato
- [x] Font Times New Roman esplicito su ogni run
- [x] Size esplicita su ogni run (12pt corpo, 16pt titoli)
- [x] Gerarchia visiva: destinatario → data → oggetto → saluto → corpo → sezioni → formule → richieste → chiusura → firma
- [x] Nessun en dash o em dash nel testo (tutti sostituiti con `-`)
- [x] Data (para 27) e firma (para 29-32) separati — HARD_005 rispettato
- [x] Congedo "Con osservanza," a destra insieme alla firma — HARD_005
- [x] Separatori `* * *` rimossi (3 occorrenze)
- [x] Segnaposto `[DA INSERIRE: ...]` preservati intatti
- [x] Bold inline preservato (numeri di punto, nomi, riferimenti normativi)
- [x] Italic preservato ("Con osservanza,", citazione «queste due mani...»)
- [x] Line spacing uniforme 1.05

---

## Note e osservazioni (non bloccanti)

### Doppio congedo (para 23 e 25 output)
Il testo del para 23 output ("Nel rimettere ogni determinazione...") termina con **"porgiamo i più distinti saluti."** integrato nella frase. Il para 25 output contiene **"Con osservanza,"** come formula di congedo autonoma destra. Questa duplicazione è presente nel sorgente e non è stata modificata per rispettare HARD_001. La scelta redazionale (se eliminare uno dei due congedi o unificarli) è rimessa alla revisione umana.

### Doppia data (para 5 e 24 output)
La data placeholder `Bergamo, lì [DA INSERIRE: data]` appare due volte: una nel blocco destinatario/intestazione (para 5, RIGHT) e una nel blocco firma (para 24, RIGHT). Entrambe sono nel sorgente. Il formato a doppia data (intestazione + firma) è prassi nelle lettere italiane formali. Nessun problema strutturale, ma il redattore deve compilare entrambe.

### Saluto di apertura
"Egregio/a Consigliere/a," è reso in bold LEFT, coerente con il sorgente e con il tono formale. Non è un titolo di sezione ma un'intestazione epistolare.

### Segnaposto non compilati
Il documento è una **bozza**: devono essere inseriti:
- Nome e cognome del destinatario (`[DA INSERIRE: NOME E COGNOME]`)
- Canale di recapito (`[DA INSERIRE]` nella riga PEC/recapito)
- Data della lettera (due occorrenze)

---

## Artefatti OCR
Nessun artefatto OCR rilevato nel testo sorgente. Nessuna sequenza `[à]`, `[e]`, `[l']` da integrare.
