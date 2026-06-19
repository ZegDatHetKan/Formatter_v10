# Verification — Lettera Trustpilot / Hormonal Holding OÜ

**Data:** 2026-05-28  
**Documento:** `documento_ricevuto_formattato.docx`

---

## Nessuna verifica manuale richiesta

Il documento non presenta ambiguità giuridiche, corruzioni di testo o incongruenze strutturali che richiedano intervento umano.

---

## Note operative

### 1. Data placeholder `[DATA INVIO]`
Il campo `Bergamo, [DATA INVIO]` è un placeholder non compilato nel sorgente. **Non è un artefatto:** è un campo da riempire prima dell'invio. Conservato invariato.

### 2. URL `[URL PAGINA DUPLICATA]`
Il testo `[URL PAGINA DUPLICATA]` nel corpo (para 19 sorgente) è un placeholder da riempire. Conservato invariato.

### 3. Hyperlink `https://it.trustpilot.com/review/www.oasiormonale.com`
Era codificato come `w:hyperlink` nel docx sorgente (non accessibile via `p.runs`). Estratto tramite parser XML diretto e reso come testo semplice senza sottolineatura. Scelta: testo semplice è preferibile in documenti legali professionali (nessun link attivo). **Verifica umana non richiesta** ma segnalato per trasparenza.

### 4. Grassetto originale su "Egregi Signori,"
Il para 15 sorgente aveva il testo in bold. Conservato: è formula di apertura rituale. Coerente con STYLE_010.

### 5. Parola `reviewer` in italic nel testo dell'OGGETTO
Il run `reviewer` nel para OGGETTO era bold+italic nel sorgente. Conservato come bold+italic anche nel testo dell'oggetto (12pt) — enfasi semantica presente nel documento originale.

### 6. Paragrafi 3.1 e 3.2
Non trattati come titoletti separati ma come corpo con label bold (`3.1.` / `3.2.` in bold), in quanto seguiti immediatamente dal testo continuo nello stesso paragrafo. Scelta conservativa coerente con STYLE_010 ("bold solo titolo, label o formula").

---

## Controllo en-dash

Occorrenze `–` nel sorgente trovate e sostituite con `-`:

- Para 13 (OGGETTO): 2 occorrenze
- Para 18: "creata da terzi – richiesta di accorpamento"
- Para 23: "del medesimo reviewer – richiesta di intervento"
- Para 27: "informazioni commerciali riservate – richiesta di rimozione"
- Para 17/33 (corpo): "lo Studio scrivente –", "delle questioni rappresentate –"
- Para 28 (corpo): "in cui sono stati formulati –"

Nessun em-dash (`—`) rilevato nel sorgente.

---

## Esito

Documento conforme. Nessun intervento umano necessario.
