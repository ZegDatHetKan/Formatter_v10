# Verification - Interventi manuali consigliati

**Documento:** recesso per gravi motivi ex art. 27 L. 392/1978 - AVANTGARDE S.R.L. vs GESTIONI AMMINISTRATIVE S.R.L.  
**Data verifica:** 2026-06-16

---

## ⚠ Punti da verificare manualmente

### V-01 — Duplicazione "Luogo e data"
Nel sorgente, "Luogo e data: ____________________" compare **due volte**:
1. In Para[0], dopo il blocco destinatario (header del documento) → reso LEFT nel documento formattato
2. In Para[3], come riga standalone prima della firma → reso RIGHT nel documento formattato

**Azione:** Verificare con il professionista se il campo data in cima al documento è intenzionale (es. data trasmissione da compilare separatamente) oppure è un duplicato da eliminare. Nel dubbio è stato preservato entrambi (vincolo HARD_001).

---

### V-02 — Placeholders [DA INSERIRE] non compilati
Il documento contiene campi da completare:

- `[DA INSERIRE]` → indirizzo studio di Avv. Bertocchi (Para "il sottoscritto Avv. Matteo Bertocchi, del Foro di Bergamo, con studio in [DA INSERIRE]")
- `[DA INSERIRE secondo i dati reali: incremento dell'organico aziendale / del volume di attività / delle linee operative]` → motivazione incremento attività AVANTGARDE
- `[DA INSERIRE: organigramma, contratti di assunzione/comunicazioni UNILAV, dati di attività, eventuale perizia sulla capienza dei locali]` → documentazione allegata
- `[DATA - non anteriore a sei mesi dalla ricezione della presente; si propone il 31 dicembre 2026]` → data di cessazione del rapporto

**Azione:** Completare prima dell'invio.

---

### V-03 — Data trasmissione non compilata
"Luogo e data: ____________________" in header e firma sono entrambi campi vuoti.  
**Azione:** Inserire data e luogo reali prima dell'invio.

---

### V-04 — Congedo integrato nel corpo
La formula di congedo "si porgono distinti saluti" è parte dell'ultima frase del corpo ("Nell'auspicio di una definizione bonaria..."), non un paragrafo autonomo. È stata resa RIGHT come da HARD_005.  
Se si preferisce la formula isolata ("Distinti saluti" su riga separata), occorre intervento manuale.

---

## ✅ Verifiche superate

| Check | Stato |
|---|---|
| Font Times New Roman su ogni run | ✓ |
| Size esplicita su ogni run | ✓ |
| Margini template preservati (5.91/4.54/2/2 cm) | ✓ |
| En-dash e em-dash convertiti a `-` | ✓ |
| Data e firma separate (HARD_005) | ✓ |
| Congedo RIGHT (HARD_005) | ✓ |
| Firma RIGHT e bold | ✓ |
| Blocco destinatario right-shifted (STYLE_008B, 8.5 cm) | ✓ |
| Macro-sezioni 16pt bold CENTER | ✓ |
| OGGETTO: label 16pt bold CENTER + contenuto 12pt bold | ✓ |
| Sub-items 0.5 cm indent | ✓ |
| Lista romana i/ii/iii/iv 1.0 cm indent | ✓ |
| Contenuto giuridico intatto | ✓ |
| Placeholders [DA INSERIRE] preservati | ✓ |
