# Formatter Report

**Job:** 20260606T150101_Oggetto_suo_numero_49e45d07  
**Data:** 2026-06-06  
**Documento:** input.docx → documento_ricevuto_formattato.docx  
**Genere:** GENERICO (comunicazione/risposta lettera ad Apple Support)  
**Script:** _format_bertocchi.py  

---

## Struttura rilevata

Il documento sorgente era composto da **1 unico paragrafo** con 21 segmenti separati da `<w:br/>` interni (line break), tutti in un solo run senza formattazione esplicita.

**Segmenti identificati:**
- [0] Oggetto (label Oggetto: + contenuto)
- [1] Saluto (Gentile Mariachiara,)
- [2-3] Apertura + presentazione del chiarimento
- [4] Riga introduttiva elenco entità coinvolte
- [5-6] 2 bullet: Avv. Bertocchi e Bergamo Legal s.r.l.
- [7-9] 3 paragrafi corpo argomentativo
- [10] Riga introduttiva elenco documentazione caricata
- [11-14] 4 bullet: documentazione allegata
- [15-16] 2 paragrafi conclusivi
- [17] Congedo (Cordiali saluti,)
- [18-20] Blocco firma (Avv. Matteo Bertocchi, qualifica, studio)

---

## Interventi di formattazione

| Intervento | Dettaglio |
|---|---|
| Struttura | Paragrafo unico scomposto in 21 paragrafi distinti |
| Oggetto | Label "Oggetto:" a 16pt bold + contenuto 12pt bold, LEFT |
| Corpo | 12pt Times New Roman, JUSTIFY, space_after=6pt |
| Elenchi | Rientro 0.75cm, bullet "• " esplicito, JUSTIFY |
| Righe introduttive elenchi | keep_with_next=True (para 4 e 10) |
| En dash → trattino | "–" sostituito con "-" in tutti i bullet item |
| Congedo | "Cordiali saluti," → RIGHT, space_before=16pt |
| Firma | "Avv. Matteo Bertocchi" → RIGHT, bold |
| Qualifica/Studio | RIGHT, 12pt, non bold |
| Font espliciti | Times New Roman + size esplicita su ogni run |
| Bold esplicito | False su tutti i run non-bold (nessun None residuo) |

---

## Controlli finali

- ✓ Contenuto giuridico-sostanziale preservato integralmente
- ✓ Tutti i D-U-N-S, nomi, riferimenti di caso conservati
- ✓ Nessun en/em dash residuo
- ✓ Nessun artefatto OCR rilevato
- ✓ Font e size espliciti su ogni run
- ✓ Data e firma: nessuna fusione (non c'è data esplicita nel documento)
- ✓ Congedo e firma allineati a destra
- ✓ keep_with_next sulle righe introduttive degli elenchi
- ✓ Template_Vuoto.docx usato come base
- ✓ Output: documento_ricevuto_formattato.docx + final.docx
