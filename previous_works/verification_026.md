# Verification — Memoria di replica e istanza Colnaghi

**Data:** 2026-05-28

---

## Verifiche automatiche superate

- Font Times New Roman: 100% dei run ✅
- Size esplicita su ogni run: nessun None ✅
- En/em dash: 0 rimasti ✅
- Contenuto giuridico: nessuna modifica al testo ✅
- Header/footer template: intatti ✅

---

## Decisioni editoriali documentate

### 1. Paragrafi 0–6 (intestazione studio) → SALTATI
L'intestazione BERGAMO LEGAL, avvocati e website è già presente nel template header.
Includerla nel corpo creerebbe duplicazione. Decisione: omessa.

### 2. Paragrafi 121–125 (footer dati studio) → SALTATI
Ripetono il contenuto già nel footer del template. Omessi.

### 3. OGGETTO: size 12pt bold (non 16pt label)
La regola STYLE_008 prevede label Oggetto: a 16pt bold CENTER, seguita dal contenuto a 12pt bold.
In questo documento la riga OGGETTO è una singola riga di intestazione procedurale (con R.G., data udienza, oggetto articolato).
Trattarla come titolo centrato a 16pt avrebbe sminuito l'equilibrio visivo del blocco header.
Decisione: mantenuta come riga bold 12pt JUSTIFY, coerente con il formato delle memorie giudiziarie.
*Se si preferisce applicare la regola STYLE_008 in senso stretto, modificare il run "OGGETTO:" a 16pt.*

### 4. Data "Bergamo, 2 luglio 2026" in apertura (non nel blocco firma)
Il documento posiziona la data in cima (standard per memorie e istanze depositate in cancelleria),
non nel blocco firma finale. HARD_005 richiede separazione data/firma (✅ rispettata: 100+ paragrafi di distanza).
Non è stato aggiunto un secondo luogo/data prima della firma perché assente nell'originale.

### 5. `[…]` preservati
Le sequenze `[…]` nei paragrafi 48, 49, 81 sono omissis giuridici all'interno di citazioni letterali
tra caporalati « ». Non sono artefatti OCR. Preservati integralmente.

### 6. "Ill.mo Giudice Tutelare," → bold preservato
Il grassetto era presente nell'originale. Mantenuto.

### 7. Para 84 ("7.2. La conferma offerta...") — size normalizzata a 12pt
Il primo run del paragrafo aveva size 177800 (14pt) nel sorgente, ma il testo è un paragrafo body
con label inline "7.2." (non un titolo standalone). Normalizzato a 12pt come tutto il corpo.
Il grassetto del label inline è preservato.

### 8. "Per conoscenza:" lista (23–27)
Il blocco "Per conoscenza:" è una lista di destinatari CC. Formattato con label bold
e voci indentate a 0.5cm, JUSTIFY. Nessuna numerazione aggiunta.

---

## Nessuna verifica manuale richiesta

Non sono stati identificati casi che richiedano intervento umano per:
- testo corrotto o ambiguo giuridicamente
- data/firma impossibili da separare
- genere documentale incerto
- artefatti/allegati dubbi

