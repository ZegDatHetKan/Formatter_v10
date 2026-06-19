# Verification — diffida Casu / Hormonal Holding OÜ

**Data:** 2026-06-09

---

## Ambiguità risolte autonomamente

| Elemento | Decisione | Motivazione |
|---|---|---|
| OGGETTO split in 2 paragrafi | Applicato | STYLE_008 distingue label (16pt bold CENTER) da contenuto (12pt bold); contenuto lungo: JUSTIFY più leggibile di CENTER multiplo |
| Paragrafi 5–6 (invio email) nel blocco destinatario | Applicato left_indent=8.5cm | Proseguono la specifica di recapito del destinatario; coerenza visiva con blocco 2–4 |
| Bold su contenuto OGGETTO | Forzato bold=True | STYLE_008 prescrive "12pt bold" per il contenuto dell'oggetto |
| "Tutto ciò premesso..." bold | Preservato dal sorgente | Sorgente bold=True; è formula di transizione che introduce DIFFIDA — semanticamente bold appropriato |
| [VERIFICA: principio pacifico...] in para 23 | Preservato | Non è artefatto: è una nota editoriale del redattore; HARD_001 vieta la modifica del contenuto |
| [DA INSERIRE: ...] preservati | Preservati | Placeholder template intenzionali, non artefatti |

---

## Nessuna verifica manuale richiesta

Nessuna ambiguità giuridica, nessuna fusione data/firma incerta, nessun testo corrotto rilevato.

---

## Note

- I paragrafi numerati (1., 1.1, 1.2, 2., 4., 5., ecc.) nel corpo sono stati trattati come `article_body` (corpo a spaziatura standard), non come titoletti, perché il numero fa parte del testo del paragrafo stesso e il documento non usa articoli separati.
- Le liste (i)–(iv) dentro "Fatto" e "Diritto" e il corpo della diffida sono state indentate di 0.5cm per STYLE_012.
- Il saluto "In attesa... distinti saluti." era italic nel sorgente (JUSTIFY) — corretto a RIGHT italic per HARD_005.
