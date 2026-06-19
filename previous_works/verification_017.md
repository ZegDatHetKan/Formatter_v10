# Verification

**Job:** 20260527T233714_LEGAL_e8a4c59b  
**Data verifica:** 2026-05-27

---

## Checklist HARD_006

| Criterio | Esito |
|---|---|
| Contenuto sostanziale preservato | ✓ |
| Template_Vuoto.docx usato come base | ✓ |
| Font Times New Roman esplicito su ogni run | ✓ |
| Size esplicita su ogni run | ✓ |
| Gerarchia visiva chiara (16pt > 14pt > 12pt) | ✓ |
| Titoli e titoletti coerenti | ✓ |
| Corpo JUSTIFY, leggibile | ✓ |
| Elenchi e rientri coerenti | ✓ |
| Data e firma separate (3 paragrafi distinti) | ✓ |
| Nessun artefatto OCR in output | ✓ |
| En/em dash sostituiti con `-` | ✓ |
| `&nbsp;` rimossi | ✓ |

---

## Segnalazioni di ambiguità

### 1. Incongruenze anagrafiche nel fascicolo sorgente (NON toccate)

La sezione V del ricorso elenca esplicitamente le seguenti incongruenze nel fascicolo della Prefettura:

- Data di nascita di Campos: **14/06/1984** vs **14/06/1994** (anni diversi)
- Residenza: Via della Solidarietà n. 31 vs Via San Benedetto Giuseppe Labre n. 13
- Targa veicolo: **CX548ME** vs **CX549ME**
- Numero verbale sequestro: **49019F** vs **49019T**

Queste incongruenze sono oggetto di contestazione giuridica nel ricorso e sono state **preserve intatte** nel documento formattato. Non si tratta di artefatti di formattazione ma di elementi di prova. **Nessun intervento richiesto**.

### 2. "in via gradata e subordinata" (Para 61, riga iniziale minuscola)

La riga inizia con "in via gradata e subordinata" (minuscolo). Nel sorgente è probabilmente la continuazione della richiesta nel merito, dopo un punto/virgola. Non è un titoletto ma corpo del testo → mantenuto come act_body. Coerente con il contenuto.

### 3. Paragrafo 0 del sorgente (intestazione Bergamo Legal nel body)

Il sorgente contiene l'intestazione dello studio come primo paragrafo nel body Word. Questo è un artefatto di conversione (tipicamente da PDF): il template Word originale ha probabilmente l'intestazione in Word Header, ma la copia convertita l'ha nel body. Il formatter ha saltato questo blocco e si è affidato al Template_Vuoto.docx che contiene la corretta intestazione. **Nessuna verifica manuale richiesta** salvo confronto visivo del PDF finale con il template atteso.
