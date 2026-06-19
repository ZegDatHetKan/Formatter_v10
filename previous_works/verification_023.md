# Verification Notes

**Documento:** Ricorso in opposizione - Campos Omar vs Prefettura di Brescia  
**Data:** 2026-05-28  

---

## Verifiche automatiche superate

| Check | Esito |
|---|---|
| Font Times New Roman su tutti i run | ✅ |
| Size esplicita su tutti i run | ✅ |
| Nessun en dash / em dash nel testo | ✅ |
| Nessun `&nbsp;` o `\xa0` | ✅ |
| OCR: `proclività` (era `proclivit[à]`) | ✅ |
| OCR: `nell'infrangere` (era `nel[l']infrangere`) | ✅ |
| Data `Bergamo, 12 maggio 2026` → para RIGHT separato | ✅ |
| Firma `Avv. Matteo Bertocchi` → para RIGHT bold separato | ✅ |
| Congedo `Con osservanza.` → para RIGHT | ✅ |
| Letterhead Para 0 saltato (già nel template) | ✅ |
| 79 paragrafi output (da 8 sorgenti con \n embedded) | ✅ |

---

## Note editoriali

### 1. Uppercase formule rituali
Le formule `tanto premesso`, `ricorre`, `conclusioni`, `in fatto`, `in diritto`, `premesso che` sono state rese in maiuscolo secondo la convenzione standard dei ricorsi giudiziari (STYLE_006 regole_di_formattazione.md). Trattamento tipografico, non modifica di contenuto.

### 2. Para 0 (letterhead) saltato
Il paragrafo sorgente 0 conteneva l'intestazione dello studio (BERGAMO LEGAL, Via F.lli Calvi, ecc.) già presente nell'header del Template_Vuoto.docx. Saltato per evitare duplicazione (HARD_002).

### 3. "in via gradata e subordinata"
Paragrafo che inizia con minuscola — classificato correttamente come body (continuazione di "Nel merito"), non come sottosezione.

### 4. Elenchi Art. e incongruenze
Le voci "Art. xxx C.d.S." (sezione III) e le incongruenze (sezione V) sono formattate come list_item con indent 0.5cm e space_after 3pt per segnalare visivamente la struttura enumerativa implicita nel testo.

---

## Nessuna ambiguità residua che richieda intervento umano

Non sono stati rilevati casi di:
- testo giuridicamente sensibile potenzialmente corrotto
- date/firme non separabili con certezza
- contenuti che potrebbero essere codice o artefatti estranei
- incongruenze strutturali che richiedano scelta legale

