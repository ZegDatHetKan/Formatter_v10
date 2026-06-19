# Feedback Review — Lettere

Analisi dei feedback ricevuti (revisore: *Dolly*) sugli output storici, incrociata con
il comportamento dello **script deterministico attuale** (`formatters/letters.py`) sugli
stessi input.

> Vincolo di questo task: **nessun file è stato modificato** tranne questo documento.
> I fix sono *proposti e localizzati*, non applicati.

Metodo: ogni feedback → mappato a un ID del corpus → verificato sull'output storico
(`previous_works/output_*.docx`) → confrontato con il mio output (`out/output_*.docx`).
Verdetto per ciascuno: **giustificato / problema trovato + fix**, oppure **feedback errato**.

---

## 1. Mappa feedback → corpus

| File feedback | ID | Famiglia | Voto | Nota | In scope |
|---|---|---|---|---|---|
| Lettera_Consiglieri_Madone_BOZZA | 001 | letters | 5/5 | — | ✅ |
| Subject_Procedimento_Mediazione | 011 | letters | 5/5 | — | ✅ |
| PEC_contestazione_Papi_Solutions | 003 / 029 | letters | 5/5 | — | ✅ (ambiguo, vedi §3.5) |
| Lettera_Trustpilot_v2_collaborativa | 025 | letters | 5/5 | "dritto dritto" | ✅ |
| Lettera_Trustpilot_v3_collaborativa | 027 | letters | 4/5 | oggetto centrato a capo + parte alta spezzettata | ✅ |
| Diffida_Locafaro | 028 | letters | 4/5 | "Egr." sotto "Sig.ra" invece di monolinea | ✅ |
| Esposizione_fatti_e_norme_mediazione_1 | 009 | other | 4/5 | "spesso fa Oggetto: a capo" | ➖ corroborante |
| Delega_mediazione_genitori_Fiorello_1 | 006 | other | 5/5 | — | ➖ fuori scope |
| Memorie_preudienza_Colnaghi_Versione finale | 030 | acts | 4/5 | Oggetto a 12 + titoli iniziali a sinistra | ➖ corroborante |
| Memorie_preudienza_Colnaghi_v5 | 026 | acts | 4/5 | — | ➖ fuori scope |
| Memorie_preudienza_Colnaghi_v4 | 024 | acts | 4/5 | nomi/data scriventi non a destra in alto | ➖ corroborante |

**6 feedback su lettere** (la famiglia che stiamo costruendo); 5 su atti/other, tenuti
solo come conferma indiretta. I 4 voti pieni senza nota (001, 011, 003/029) sono la
baseline "corretta" di riferimento.

---

## 2. Sintesi dei problemi reali trovati nello script

Dall'analisi delle due lettere con rilievo (027, 028) emergono **tre difetti reali** del
mio formatter, più uno minore. Tutti azionabili.

> **Aggiornamento — fix APPLICATI** (`formatters/letters.py`). I1–I4 sono stati corretti;
> i test che li codificano sono passati da `xfail` a verdi (`17 passed`). Le rigenerazioni
> di 027/028 e dei 5 esempi confermano le correzioni; le firme in calce restano intatte
> (lo strip I2 rimuove solo l'intestazione duplicata in testa, non la firma).

| # | Problema | Origine feedback | Stato |
|---|---|---|---|
| **I1** | Contenuto dell'OGGETTO reso a **16pt** e allineato **LEFT** | 027 (+ 009, 030) | ✅ risolto: etichetta 16pt + contenuto 12pt, JUSTIFY |
| **I2** | Strip intestazione **incompleto**: le righe soci `Avv. …` che seguono `www.bergamo.legal` non vengono rimosse e diventano un finto destinatario in cima | 027 "top spezzettata" | ✅ risolto: strip estende alle righe soci di testa (firma in calce preservata) |
| **I3** | Riga con **solo titolo onorifico** (`Egr.`, `Spett.le`, `Preg.ma`) non fusa con la riga del nome → niente "monolinea" | 028 | ✅ risolto: onorifico isolato fuso col nome |
| **I4** (minore) | La continuazione del recapito (`e, per anticipazione, a mezzo posta elettronica`) viene intercettata come `delivery_method` e spostata a destra, spezzando il blocco destinatario | 027/028 (parte alta) | ✅ risolto: delivery riconosciuta solo prima del destinatario |

Nota importante: sull'**OGGETTO**, la scelta architetturale del mio script è **corretta**
e già migliore dello storico — l'oggetto è reso su **un solo paragrafo** (`Oggetto: testo`),
quindi il difetto "Oggetto: a capo / centrato" lamentato in 027 e 009 **non si ripresenta
strutturalmente**. Restano da correggere solo size e allineamento (I1).

---

## 3. Lettere — analisi dettagliata

### 3.1 — 027 Lettera_Trustpilot_v3 (4/5) — **giustificato, problema trovato**

Nota revisore: *"la parte in alto l'ha spezzettata… e ha messo l'oggetto con 'oggetto' e
poi sotto il resto e centrale, invece di 'oggetto: testo' giustificato"*.

**Output storico** (`previous_works/output_027.docx`):
- `[08]` `OGGETTO:` da solo, **CENTER 16pt** → `[09]` contenuto su paragrafo separato JUSTIFY.
  Conferma la lamentela: etichetta a capo e centrata invece di inline.
- `[01]` `Via PEC` infilato dentro il blocco destinatario (`left_indent 8.5`), parte alta
  disordinata. Conferma "spezzettata".

**Verdetto:** feedback **giustificato**.

**Mio script** (`out/output_027.docx`):
- `[10]` `OGGETTO: Hormonal Holding…` reso **su un solo paragrafo** → struttura giusta,
  ma a **16pt** e **LEFT** (difetto **I1**).
- `[00]–[01]` `Avv. Matteo Bertocchi` / `Avv. Daiana Chiappa` (soci dello studio,
  intestazione) **non rimossi** e resi come destinatario `left_indent 8.5` (difetto **I2**):
  qui il mio output è perfino più disordinato dello storico in cima.

**Fix proposti (non applicati):**
- *I1*: in `classify()` rendere il `subject_line` come paragrafo unico con **etichetta 16pt
  bold + contenuto 12pt bold**, `alignment = JUSTIFY`. Serve permettere size per-segmento
  (oggi `Block.size` è unico → l'`emit()` applica 16pt anche al contenuto).
- *I2*: estendere `strip_letterhead()` perché, dopo le righe d'intestazione, consumi anche
  le righe-firma soci contigue (`^(avv|dott|ing|prof)\.`), **solo finché si è ancora nel
  blocco di testa** (prima di data / delivery / destinatario / oggetto). Le stesse righe in
  fondo (firma) non vanno toccate.

### 3.2 — 028 Diffida_Locafaro (4/5) — **giustificato, problema trovato**

Nota revisore: *"ha messo Egr. sotto Sig.ra Simona Locafaro invece di usare una monolinea"*.

**Output storico** (`previous_works/output_028.docx`): `[02]` `Egr.` + `[03]`
`Sig.ra Simona Locafaro` su righe distinte. L'input le ha già separate e l'AI le ha
mantenute così.

**Verdetto:** feedback **giustificato**.

**Mio script** (`out/output_028.docx`): `[04]` `Egr.` + `[05]` `Sig.ra Simona Locafaro` →
**identico difetto riprodotto** (I3). In più le solite righe soci in cima (I2) e la riga
`e, per anticipazione…` spostata a destra (I4).

**Fix proposto (non applicato):**
- *I3*: nel ramo `recipient` della preambolo, se una riga è **solo** un onorifico
  (`^(egr|spett|preg|gent|chiar|ill)\.?(\s*m[oa])?\.?$`, ecc.) **fonderla** con la riga
  successiva in un'unica voce `recipient` (`Egr. Sig.ra Simona Locafaro`), preservando il
  testo. È una regola deterministica, sicura, e copre anche `Spett.le` / `Preg.ma`.

### 3.3 — 025 Lettera_Trustpilot_v2 (5/5, "dritto dritto") — **nessun problema**

Output storico pulito (oggetto inline, destinatario a destra, corpo giustificato). È la
prova che la **stessa lettera** (v2 vs v3) può uscire bene: la differenza è proprio lo
split dell'oggetto e la parte alta che hanno fatto scendere v3 a 4/5. Usare 025 come
target di riferimento per l'oggetto.

### 3.4 — 001 e 011 (5/5) — **nessun problema**

Nessun rilievo. Coerenti con il modello (oggetto 16/12, sezioni, firma a destra). Restano
soggetti al difetto trasversale I1 nel mio script (size oggetto), ma il revisore non lo ha
penalizzato sullo storico perché lì l'oggetto era già a 12pt.

### 3.5 — 003 / 029 PEC_contestazione_Papi_Solutions (5/5) — **ambiguità di mapping**

Il nome file del feedback corrisponde a **due** job identici per titolo (003 del 04/06 e
029 del 28/05). Entrambi 5/5, quindi il verdetto non cambia, ma va registrato che il
feedback non distingue le due run. Nessuna azione.

---

## 4. Feedback fuori famiglia (solo conferma)

Non sono lettere, **non li correggiamo ora**, ma confermano che i temi trovati sono
sistemici nel vecchio formatter AI:

- **009** (other) *"spesso fa Oggetto: a capo"* → stesso problema di 027. Conferma che
  l'oggetto inline su paragrafo unico (scelta del nostro script) è la direzione giusta.
- **030** (atto) *"Oggetto lasciato a 12 e titoli iniziali a sinistra"* → qui il revisore
  voleva l'**etichetta** oggetto a 16 (non a 12) e i titoli centrati: coerente con la
  nostra regola 16pt-etichetta / titoli centrali. Conferma I1 al contrario (l'etichetta
  deve restare 16, è il *contenuto* a dover scendere a 12).
- **024** (atto) *"non ha messo a destra i nomi/data scriventi in alto"* → negli atti la
  data/firmatari iniziali vanno a destra. Il nostro script già mette `date_place` a destra;
  per gli atti se ne terrà conto quando implementeremo quella famiglia.

---

## 5. Conclusione operativa

| Feedback lettere | Giustificato? | Problema nel mio script? | Fix |
|---|---|---|---|
| 027 oggetto a capo/centrato | sì | parziale (I1: size+align; struttura già ok) | rendere contenuto 12pt + JUSTIFY |
| 027 top spezzettata | sì | sì (I2) | estendere strip alle righe soci di testa |
| 028 Egr. monolinea | sì | sì (I3) | fondere onorifico isolato con il nome |
| 025 / 001 / 011 / 003 / 029 | n/a (5/5) | solo I1 latente | stesso fix oggetto |

**Nessun feedback sulle lettere risulta errato**: sono tutti giustificati e verificati sui
documenti. Tre difetti reali e localizzati nel mio script (I1, I2, I3) + uno minore (I4),
tutti risolvibili con regole deterministiche, senza reintrodurre l'AI di layout. Da
applicare nel prossimo giro (questo task non modifica il codice).

---

## 6. Come è fatta una lettera e come funziona lo script

### 6.1 Anatomia di una lettera Bergamo Legal

Una lettera è composta da blocchi in sequenza fissa. L'intestazione **non fa parte del
corpo**: vive nell'header/footer del template.

```
┌───────────────────────────────────────────────┐
│ [HEADER del template: logo + BERGAMO LEGAL …]  │  ← non si tocca, viene dal template
├───────────────────────────────────────────────┤
│ A mezzo PEC / Raccomandata…      (delivery)    │
│                         Bergamo, lì <data>     │  ← data/luogo a DESTRA
│                                                │
│                    Spett.le / Egr. <nome>      │  ← destinatario, rientro 8.5 cm
│                    <indirizzo, CAP, PEC>       │     (parte dal centro pagina)
│                                                │
│ OGGETTO: <riassunto>            (subject)      │  ← etichetta 16pt, testo 12pt
│                                                │
│ Egregio/a …,                    (opening)      │
│ <corpo giustificato 12pt>       (body)         │
│                                                │
│ IN FATTO / DIFFIDA / INVITA     (section)      │  ← titoli rituali centrati 16pt
│ 1. … 2. …                       (numbered)     │
│ (i) … (ii) …                    (enum/bullet)  │  ← liste rientrate 0.5 cm
│                                                │
│              Cordiali saluti     (closing)     │  ← chiusura/firma a DESTRA
│              Avv. Nome Cognome   (signature)   │     nome in grassetto
│ Allegati: …                     (attachments)  │
├───────────────────────────────────────────────┤
│ [FOOTER del template: R.E.A., P.IVA, recapiti] │  ← non si tocca
└───────────────────────────────────────────────┘
```

Convenzioni stabili dello studio:
- **Mittente a sinistra** (è il logo nel template); **destinatario a destra**, con rientro
  sinistro `8.5 cm`, così il blocco parte dal centro orizzontale.
- **Data e firma a destra**, mai fuse nello stesso paragrafo.
- **OGGETTO**: etichetta `Oggetto:` grande (16pt, è il "titolo" della lettera) + contenuto
  alla dimensione del corpo (12pt), tutto **sullo stesso paragrafo** (non a capo, non
  centrato — è proprio ciò che il feedback 027/009 chiedeva).
- Testo del corpo **giustificato**, Times New Roman 12pt.
- Trattini sempre ASCII `-`.

### 6.2 Pipeline dello script (`formatters/letters.py`)

```
Template_Vuoto.docx (header/footer/margini)
        │
        ▼
leggi input.docx come testo  ──►  split su paragrafi reali E su '\n'
        │                          (alcuni input sono un unico paragrafo con a-capo)
        ▼
strip_letterhead()           ──►  rimuove l'intestazione studio duplicata in cima
        │
        ▼
normalize()                  ──►  – — → '-', niente nbsp/zero-width, spazi doppi, vuoti
        │
        ▼
classify()                   ──►  ancora sull'OGGETTO: tutto ciò che precede è "preambolo"
        │                          (delivery/data/destinatario), tutto ciò che segue è "corpo"
        │                          ogni riga → un Block (kind + stile)
        ▼
emit() per ogni Block        ──►  crea il paragrafo, applica allineamento/rientro/spazi,
        │                          font Times New Roman + size ESPLICITA su ogni run,
        │                          mette in grassetto etichette, numeri e placeholder [..]
        ▼
out.save() + render_report() ──►  .docx + report (regole applicate, blocchi, warning,
                                   needs_review se ci sono placeholder o oggetto mancante)
```

Punti chiave del funzionamento:
- **L'ancora è la riga `OGGETTO:`**. Divide preambolo e corpo: questo rende il
  riconoscimento robusto (il destinatario sta sempre prima, l'apertura sempre dopo).
- **Stile interamente in Python**: l'AI (in futuro) potrà solo estrarre/mappare contenuto e
  segnalare incertezze; font, size, margini, allineamenti, rientri e spaziature sono
  *hardcoded* e non negoziabili. Questo è ciò che rende ogni run economica e ripetibile.
- **L'incertezza non è nascosta**: i placeholder `[DA INSERIRE: …]` restano nel testo, in
  grassetto, e alzano `needs_review`; un OGGETTO mancante genera warning e `needs_review`.
- **I riferimenti storici non si toccano**: l'output va in `out/`, mai in `previous_works/`.

### 6.3 Dove agiscono i fix proposti

- **I1 (oggetto 12pt + giustificato)** → blocco `subject_line` in `classify()` e gestione
  size per-segmento in `emit()`.
- **I2 (strip soci di testa)** → funzione `strip_letterhead()`.
- **I3 (onorifico monolinea)** → ramo `recipient` del preambolo in `classify()`.
- **I4 (continuazione recapito)** → pattern `DELIVERY`, da restringere così da non
  intercettare le righe di prosecuzione dell'indirizzo destinatario.
