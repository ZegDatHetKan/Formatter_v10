# Verification — PEC contestazione Papi Solutions

**Data:** 2026-05-28

---

## Verifiche automatiche superate

- Font Times New Roman esplicito su ogni run: ✓
- Size esplicita su ogni run (12pt corpo, 16pt label OGGETTO): ✓
- Margini A4 portrait (top 5.91, bot 4.54, sx 2, dx 2): ✓
- Intestazione studio non duplicata (skip paras 0-2 sorgente): ✓
- En dash convertiti in `-`: ✓
- Blocco destinatario: left_indent=Cm(8.5) per STYLE_008B: ✓
- Congedo ("In attesa… distinti saluti.") allineato RIGHT: ✓
- Firma separata dalla data: ✓
- Contenuto giuridico integro (nessuna modifica a date, importi, nomi, riferimenti): ✓

---

## Placeholder nel documento

I seguenti placeholder sono presenti nel sorgente e conservati nell'output — nessuna modifica effettuata:

| Placeholder | Posizione |
|---|---|
| `[DATA INVIO]` | Data lettera (para 1 output) |
| `[pec studio]` | Intestazione template header |
| `[recapito]` | Intestazione template header |
| `[pec destinatario]` | Blocco destinatario (para 5 output) |
| `[IMPORTO]` | Proposta transattiva (para 10 output) |
| `[DATA]` | Scadenza proposta (para 11 output) |

Questi sono placeholder da compilare — non artefatti. Conservati intatti.

---

## Note editoriali

### Italic su "Trasmessa a mezzo PEC"
Preservato: present nel sorgente, ha funzione semantica (nota di trasmissione PEC). Non è artefatto.

### Bold nel corpo testo
Il sorgente usa bold selettivo per evidenziare: nome cliente, date chiave, importi, argomenti principali. Bold preservato integralmente — coerente con la prassi della lettera legale.

### Congedo come frase intera
"In attesa di cortese e sollecito riscontro, si porgono distinti saluti." è congedo + formula in un unico paragrafo. Non separato in due paragrafi (non è necessario per la leggibilità; separarli richiederebbe invenzione di struttura non presente nel sorgente).

---

## Verifica manuale richiesta

Nessun punto critico richiede intervento umano obbligatorio.

Gli unici placeholder `[…]` presenti nel documento sono dati mancanti da inserire prima dell'invio (date, importi, PEC), non ambiguità editoriali.

