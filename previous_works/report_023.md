# Formatter Report

**Job:** Ricorso in opposizione a decreto di revoca della patente di guida  
**Cliente:** Campos Omar  
**Categoria:** GENERICO  
**Script:** `_format_ricorso.py`  
**Data elaborazione:** 2026-05-28  

---

## Struttura rilevata

Documento giudiziario (ricorso in opposizione) composto da 8 paragrafi sorgente con `\n` embedded, espansi a 79 paragrafi formattati.

| Blocco | Para output | Tipo | Formato applicato |
|---|---|---|---|
| Giudice di Pace di Brescia | 0 | court_header | CENTER bold 16pt |
| Titolo ricorso (2 righe) | 1–2 | act_title | CENTER bold 16pt |
| Parte ricorrente / Parti Intimate / Provvedimento impugnato | 3–9 | proc_label + body | LEFT bold 14pt / JUSTIFY 12pt |
| Oggetto del giudizio | 10–11 | oggetto_label + content | LEFT bold 14pt / JUSTIFY bold 12pt |
| PREMESSO CHE / IN FATTO | 12–13 | section_center | CENTER bold 16pt |
| Corpo In fatto (7 para) | 14–20 | body | JUSTIFY 12pt |
| IN DIRITTO | 21 | section_center | CENTER bold 16pt |
| Corpo intro In diritto | 22 | body | JUSTIFY 12pt |
| I - Violazione … (+ corpo) | 23–27 | argument + body | LEFT bold 14pt / JUSTIFY 12pt |
| II - Errore … (+ corpo) | 28–31 | argument + body | LEFT bold 14pt / JUSTIFY 12pt |
| III - Sproporzione … (+ lista Art.) | 32–39 | argument + body + list | LEFT bold 14pt / JUSTIFY 0.5cm indent |
| IV - Istruttoria … (+ corpo) | 40–42 | argument + body | LEFT bold 14pt / JUSTIFY 12pt |
| V - Incongruenze … (+ lista + corpo) | 43–50 | argument + body + list | LEFT bold 14pt / JUSTIFY 0.5cm indent |
| TANTO PREMESSO / corpo / RICORRE / corpo | 51–54 | ritual + body | CENTER bold 16pt / JUSTIFY 12pt |
| CONCLUSIONI | 55 | ritual | CENTER bold 16pt |
| Voglia + subsections | 56–65 | body + concl_sub | JUSTIFY 12pt / LEFT bold 14pt |
| Si producono + 7 exhibit | 66–73 | exhibits_hdr + exhibit | LEFT bold 14pt / LEFT 12pt indent 0.5cm |
| Dichiarazione di valore + corpo | 74–75 | dichiarazione_label + body | LEFT bold 14pt / JUSTIFY 12pt |
| Con osservanza | 76 | congedo | RIGHT 12pt |
| Bergamo, 12 maggio 2026 | 77 | place_date | RIGHT 12pt |
| Avv. Matteo Bertocchi | 78 | signature | RIGHT bold 12pt |

---

## Operazioni di pulizia

| Artefatto | Azione | Risultato |
|---|---|---|
| `proclivit[à]` | OCR bracket repair | `proclività` |
| `nel[l']infrangere` | OCR bracket repair | `nell'infrangere` |
| En dash `–` (×19 occorrenze) | Sostituito con `-` (HARD_004B) | ✓ |
| `&nbsp;` tra data e firma | Rimosso | Data e firma separate in para distinti |
| Letterhead Para 0 | Saltato (già nel template) | ✓ |

---

## Formule rituali

Convertite in CAPS (convenzione standard ricorso):
- `tanto premesso` → `TANTO PREMESSO`
- `ricorre` → `RICORRE`
- `Conclusioni` → `CONCLUSIONI`
- `In fatto:` → `IN FATTO`
- `In diritto:` → `IN DIRITTO`
- `Premesso che:` → `PREMESSO CHE:`

---

## Verifica finale

- ✅ Font Times New Roman esplicito su ogni run
- ✅ Size esplicita su ogni run
- ✅ Gerarchia visiva: court_header > act_title > section_center > argument > body
- ✅ Corpo JUSTIFY 12pt
- ✅ Titoli keep_with_next=True (anti-orfano, HARD_007)
- ✅ Data e firma in paragrafi distinti RIGHT (HARD_005)
- ✅ Congedo (Con osservanza) RIGHT nello stesso blocco finale (HARD_005)
- ✅ Nessun en/em dash nel documento output
- ✅ Nessun &nbsp; nel documento output
- ✅ OCR artefatti corretti
- ✅ Template_Vuoto.docx usato come base
- ✅ Contenuto giuridico preservato integralmente
