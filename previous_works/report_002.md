# Formatter Report — Lettera Consiglieri Madone

**Job:** 20260604T092747 — Lettera Consiglieri Madone FIRMA STUDIO BOZZA  
**Data:** 2026-06-04  
**Categoria:** GENERICO  
**Script:** `_format_lettera_madone.py`  
**Input:** `input.docx` (33 paragrafi sorgente)  
**Output:** `documento_ricevuto_formattato.docx` / `final.docx` (30 paragrafi)  
**Template:** `Template_Vuoto.docx`

---

## Struttura documento

Lettera legale formale a firma doppia (Avv. Bertocchi e Avv. Chiappa) su mandato dell'Ing. Sergio Müller ai Consiglieri Comunali di Madone. Documento in forma di bozza con segnaposto `[DA INSERIRE: ...]`.

---

## Interventi applicati

### Rimozione separatori decorativi
- Paragrafi `* * *` (originali 9, 15, 19) rimossi per conformità a HARD_004 e STYLE_011 (divisori solo tipografici).

### Sostituzione en dash → trattino normale (HARD_004B)
Sostituzioni in:
- Para 4: `– DA INSERIRE` → `- DA INSERIRE`
- Para 11: `ore 20:30 –` e `...locale –` → `-`
- Para 17: `pubblica –` e `rivestita –` → `-`
- Para 22: `assumere – nelle sedi` → `assumere - nelle sedi`
- Para 25: `– ivi compresa` → `- ivi compresa`

### Formattazione applicata

| Blocco | Allineamento | Font | Size | Note |
|---|---|---|---|---|
| Blocco destinatario (0-4) | LEFT, left_indent=8.5cm | TNR | 12pt | STYLE_008B |
| Data intestazione (5) | RIGHT | TNR | 12pt | Top right del foglio |
| OGGETTO (6) | JUSTIFY | TNR | 16pt bold (label) / 12pt bold (contenuto) | STYLE_008 |
| Saluto apertura (7) | LEFT | TNR | 12pt bold | Preservato bold sorgente |
| Corpo intro (8) | JUSTIFY | TNR | 12pt | Bold nomi preservato |
| IN FATTO / IN DIRITTO | CENTER | TNR | 16pt bold | STYLE_006, keep_with_next |
| Punti 1-6 (11-18 out) | JUSTIFY | TNR | 12pt | Bold inline preservato |
| Transizione (20) | JUSTIFY | TNR | 12pt | space_before=12pt |
| INVITA LA S.V. | CENTER | TNR | 16pt bold | Formula rituale |
| Richieste in via X (22-24) | JUSTIFY | TNR | 12pt | left_indent=0.5cm, bold inline |
| Corpo chiusura (25-26) | JUSTIFY | TNR | 12pt | |
| Data firma (27) | RIGHT | TNR | 12pt | space_before=18pt; HARD_005 |
| Con osservanza (28) | RIGHT | TNR | 12pt italic | HARD_005 |
| Avv. Bertocchi / Chiappa | RIGHT | TNR | 12pt bold | STYLE_016 |
| Righe firma | RIGHT | TNR | 12pt | |

### Contenuto preservato
- Tutti i dati identificativi: nomi (Ing. Sergio Müller, Avv. Bertocchi, Avv. Chiappa, Assessore Davide Merisio), date (2 febbraio 2026, 16 marzo 2026, 11 aprile 2026, ecc.), riferimenti normativi (art. 78 D.Lgs. 267/2000, artt. 612 e 612-bis c.p., artt. 1, 2, 38, 97 Costituzione, art. 51 c.p., T.U.E.L.), verbali, esposti ANAC.
- Segnaposto bozza `[DA INSERIRE: ...]` integralmente preservati.
- Bold/italic originali mantenuti su ogni run.

---

## Parametri tecnici

- Font: Times New Roman su tutti i run
- Line spacing: 1.05 su tutti i paragrafi
- Margini: dal template (A4 portrait)
- Tutti i size espliciti: 16pt (titoli centrali), 12pt (corpo)
