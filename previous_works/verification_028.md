# Verification — Diffida Locafaro

**Data:** 2026-05-28  
**Documento:** Diffida Trustpilot (HORMONAL HOLDING OÜ vs. Simona Locafaro)

---

## Ambiguità risolte autonomamente

| Punto | Decisione |
|---|---|
| Para 14 `* * *` | Rimosso: divisore decorativo vietato (STYLE_011). Nessuna perdita di contenuto. |
| OGGETTO para 13: label + descrizione in unico para | Splittato in 2 para: `OGGETTO:` CENTER 16pt bold + descrizione JUSTIFY 12pt bold (STYLE_008 caso specifico Oggetto). |
| "Egregia Signora," (bold in sorgente) | Mantenuto bold: è l'apertura formale della lettera, enfasi intenzionale. |
| Para 37 "Tutto ciò premesso…" (bold in sorgente) | Mantenuto bold: formula di passaggio — rafforza la transizione verso DIFFIDA. |
| Para 37–38–39: frase spezzata attorno a "DIFFIDA" | Mantenuti come 3 paragrafi distinti (coerente con prassi diffida italiana). |
| "A mezzo Raccomandata A/R" (para 6) | Trattato come prima riga del blocco destinatario: indent Cm(8.5), LEFT. |
| `[DATA INVIO]` e `[DA INSERIRE]` | Conservati: placeholder intenzionali, non artefatti OCR. |
| Para 50–51 firme senza bold in sorgente | Forzato bold=True: nomi firmatari in diffida/lettera devono essere bold (STYLE_016). |

---

## Nessuna verifica manuale richiesta

Non sono stati rilevati:
- testi potenzialmente corrotti ma giuridicamente sensibili;
- separazione data/firma impossibile;
- genere documentale incerto (è una diffida);
- contenuti ambigui tra testo legale e codice/artefatto.

---

## Note operative

- I paragrafi 0–4 (intestazione studio) e 52–58 (footer) del sorgente sono stati esclusi perché già presenti nel template (`Template_Vuoto.docx`).
- Tutti i `–` (U+2013 en dash) sostituiti con `-` ASCII. Nessun em dash presente nel sorgente.
- Bold/italic semantici sui run (riferimenti normativi, nomi commerciali, termini tecnici) preservati fedelmente.

