# Formatter Report

**Documento:** `input.docx`  
**Output:** `documento_ricevuto_formattato.docx` / `final.docx`  
**Categoria:** GENERICO  
**Tipo rilevato:** lettera professionale / comunicazione email  
**Data elaborazione:** 2026-05-29  
**Regole applicate:** `regole_di_formattazione.md` v4.0

---

## Struttura identificata

| # | Tipo | Contenuto (inizio) |
|---|------|--------------------|
| 0 | `oggetto` | Oggetto: Re: Aggiornamento numeri D-U-N-S - [102902680471] |
| 1 | `saluto` | Gentile Stefania, |
| 2-3 | `body` | Corpo lettera (paragrafi) |
| 4 | `intro_list` | Le due entità coinvolte sono: |
| 5-6 | `list_item` | Voci lista entità (Avv. Bertocchi / Bergamo Legal) |
| 7-10 | `body` | Corpo lettera (paragrafi) |
| 11 | `intro_list` | Come da Sua richiesta... documentazione: |
| 12-15 | `list_item` | Voci lista documentazione |
| 16 | `body` | Resto naturalmente a disposizione... |
| 17 | `congedo` | Cordiali saluti |
| 18 | `firma` | Avv. Matteo Bertocchi |

---

## Operazioni eseguite

### Artefatti rimossi / corretti
- En dash `–` → trattino `-` in 4 occorrenze (paragrafi 0, 5, 6, 9) — HARD_004B
- Punto finale rimosso da "Cordiali saluti." (mantenuto solo "Cordiali saluti") — micro-scelta editoriale coerente col genere lettera

### Layout applicato
| Elemento | Font | Size | Allineamento | Grassetto |
|----------|------|------|--------------|-----------|
| Label `Oggetto:` | Times New Roman | 16pt | CENTER | Sì |
| Contenuto oggetto | Times New Roman | 12pt | CENTER | Sì |
| Saluto | Times New Roman | 12pt | LEFT | No |
| Corpo | Times New Roman | 12pt | JUSTIFY | No |
| Intro lista | Times New Roman | 12pt | JUSTIFY | No |
| Voci lista | Times New Roman | 12pt | JUSTIFY | No |
| Congedo | Times New Roman | 12pt | RIGHT | No |
| Firma | Times New Roman | 12pt | RIGHT | Sì |

### Spaziature
- Oggetto: space_before=2pt, space_after=10pt
- Saluto: space_before=8pt, space_after=8pt
- Corpo: space_before=2pt, space_after=6pt
- Congedo: space_before=18pt, space_after=4pt (separazione adeguata dalla firma)
- Firma: space_before=6pt

### Rientri
- Voci lista: left_indent=0.5cm (conforme STYLE_012)

### Invarianze
- Contenuto giuridico: intatto
- Codici D-U-N-S: preservati (440487417, 442296279)
- Riferimento `[102902680471]`: preservato (codice ticket/ref nel subject email)
- Nomi, denominazioni societarie, titoli: invariati

---

## Vincoli verificati
- [x] HARD_001 Contenuto intoccabile
- [x] HARD_002 Template_Vuoto.docx usato
- [x] HARD_003 Font e size espliciti su ogni run
- [x] HARD_004 Artefatti rimossi (solo certi)
- [x] HARD_004B En dash/em dash → trattino
- [x] HARD_005 Data e firma non fuse (nessuna data presente; congedo separato dalla firma)
- [x] HARD_006 Output verificato
- [x] HARD_007 Nessun titoletto orfano rilevato (documento breve, 1 pagina)
- [x] STYLE_016 Firma a destra, congedo a destra
